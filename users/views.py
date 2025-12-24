from django.shortcuts import render,redirect
from django.contrib import messages
from users.forms import LoginForm,RegisterForm
from django.contrib.auth.models import User, Group
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Prefetch,Count
from users.forms import AssignRoleForm,CreateGroupForm
from events.models import Event
from django.contrib.auth.tokens import default_token_generator
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.

def is_admin(user):
    return user.groups.filter(name='admin').exists()

def is_manager(user):
    return user.groups.filter(name='organizer').exists()


def activate_user(request, user_id, token):
    try:
        user = User.objects.get(id=user_id)
        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return redirect('sign-in')
        else:
            return HttpResponse('Invalid Id or token')

    except User.DoesNotExist:
        return HttpResponse('User not found')



@login_required
def add_rsvp(request,event_id):
    event=Event.objects.get(id=event_id)
    if request.method=='POST':
        if event.participants.filter(id=request.user.id).exists():
           messages.error(request,'You have already rsvp!')
           return redirect('role-dashboard')
        else:
            event.participants.add(request.user)
            subject=f'RSVP Confirmed: {event.name}'
            message=f'Hello {request.user.username},\n\n You have successfully Rsvped for {event.name}'
            recipient_list=[request.user.email]
            send_mail(subject,message,settings.EMAIL_HOST_USER,recipient_list)

            messages.success(request,'RSVP Successfull!! Confirmation Email Sent.')
            return redirect('role-dashboard')
    return render(request,'admin/dashboard.html')    


@login_required
def view_rsvp_events(request):
    events=Event.objects.filter(participants=request.user)
    return render(request,'rsvp_events.html',{'events':events})
    


@login_required
def admin_dashboard(request):
    # events = Event.objects.select_related('category').annotate(participant_count=Count('participants'))
    total_events=Event.objects.count()
    total_participants=User.objects.count()
    all_events=Event.objects.all()
    context={
        'total_events':total_events,
        'total_participants':total_participants,
        'events':all_events
    }

    return render(request,'admin/admin_dashboard.html',context)

@login_required
def organizer_dashboard(request):
    # events = Event.objects.select_related('category').annotate(participant_count=Count('participants'))
    # total_events=Event.objects.count()
    # total_participants=User.objects.count()
    all_events=Event.objects.all()
    context={
        # 'total_events':total_events,
        # 'total_participants':total_participants,
        'events':all_events
    }

    return render(request,'organizer/organizer_dashboard.html',context)

@login_required
def participant_dashboard(request):
    # events = Event.objects.select_related('category').annotate(participant_count=Count('participants'))
    # total_events=Event.objects.count()
    # total_participants=User.objects.count()
    all_events=Event.objects.all()
    context={
        # 'total_events':total_events,
        # 'total_participants':total_participants,
        'events':all_events
    }

    return render(request,'participant/participant_dashboard.html',context)

def sign_up(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get('password1'))
            user.is_active = False
            user.save()
            messages.success(
                request, 'A Confirmation mail sent. Please check your email')
            return redirect('sign-in')

        else:
            print("Form is not valid")
    return render(request, 'registration/sign_up.html', {"form": form})

def sign_in(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    return render(request, 'registration/sign_in.html', {'form': form})

@login_required
def sign_out(request):
    if request.method == 'POST':
        logout(request)
        return redirect('sign-in')
    return HttpResponse("Something went wrong!")


                # Admin er views.


# @user_passes_test(is_admin,login_url='no-permission')
# def admin_dashboard(request):
#     users=User.objects.prefetch_related(
#         Prefetch('groups',queryset=Group.objects.all(),to_attr='all_groups')
#     ).all()

#     for user in users:
#         if user.all_groups:
#             user.group_name=user.all_groups[0].name
#         else:
#             user.group_name='No group Assigned'  

#     return render(request,'admin/admin_dashboard.html',{"users":users})  

@user_passes_test(is_admin,login_url='no-permission')
def assign_role(request,user_id):
    user=User.objects.get(id=user_id)
    form = AssignRoleForm()

    if request.method=='POST':
        form = AssignRoleForm(request.POST)
        if form.is_valid():
            role=form.cleaned_data.get('role')
            user.groups.clear()
            user.groups.add(role)
            messages.success(request,f"User {user.username} has been assigned to the {role.name} role.")
            return redirect('admin-dashboard')
    return render(request,'admin/assign_role.html',{"form":form})      


@user_passes_test(is_admin,login_url='no-permission')
def  create_group(request):
    form=CreateGroupForm()
    if request.method=='POST':
        form=CreateGroupForm(request.POST)
        if form.is_valid():
            group=form.save()
            messages.success(request,f"Group {group.name} has been created successfullly!")
            return redirect('group-list')
        
    return render(request,'admin/create_group.html',{"form":form})

@user_passes_test(is_admin,login_url='no-permission')
def group_list(request):
    groups=Group.objects.prefetch_related('permissions').all()
    return render(request,'admin/group_list.html',{'groups':groups})

@login_required
def dashboard(request):
    if is_admin(request.user):
        return redirect('admin-dashboard')
    elif is_manager(request.user):
        return redirect('organizer-dashboard')
    else:
        return redirect('participant-dashboard')