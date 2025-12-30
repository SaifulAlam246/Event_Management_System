from django.http import HttpResponse
from django.shortcuts import render,redirect
from events.models import *
from django.db.models import *
from datetime import date
from events.forms import *
from django.contrib import messages
from django.views.generic import ListView,TemplateView,View,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model

User = get_user_model()

# def view_dashboard(request):
#     total_events=Event.objects.count()
#     total_participants=User.objects.count()
#     all_events=Event.objects.all()
#     context={
#         'total_events':total_events,
#         'total_participants':total_participants,
#         'all_events':all_events
#     }
#     return render(request,'dashboard/dashboard.html',context)

# def event_list(request):
#     events = Event.objects.select_related('category').annotate(participant_count=Count('participants'))
    

#     category = request.GET.get('category')
#     start_date=request.GET.get('start_date')
#     end_date=request.GET.get('end_date')
    
#     if category:
#         events=events.filter(category__name__icontains=category)
#     if start_date and end_date:
#         events=events.filter(date__range=[start_date,end_date])

#     context={
#         'events':events,
#     }
#     return render(request,'event_list.html',context)

class EventList(ListView):
    model=Event
    template_name='event_list.html'
    context_object_name='events'

    def get_queryset(self):
        events = Event.objects.select_related('category').annotate(participant_count=Count('participants'))
        category = self.request.GET.get('category')
        start_date=self.request.GET.get('start_date')
        end_date=self.request.GET.get('end_date')
        
        if category:
            events=events.filter(category__name__icontains=category)
        if start_date and end_date:
            events=events.filter(date__range=[start_date,end_date])

        return events
    
# def search_events(request):
#     search = request.GET.get('search')
#     events=Event.objects.select_related('category').prefetch_related('User').all()
   
#     if search:
#         events = events.filter(
#             Q(name__icontains=search) |
#             Q(location__icontains=search)
#         )


#     return render(request,'event_list.html',{'events':events})

class SearchEvents(ListView):
    model=Event
    template_name='event_list.html' 
    context_object_name='events'

    def get_queryset(self):
        search = self.request.GET.get('search')
        events=Event.objects.select_related('category').prefetch_related('User').all()
    
        if search:
            events = events.filter(
                Q(name__icontains=search) |
                Q(location__icontains=search)
            )

        return events    
            


# def event_detail(request,id):
#     event=Event.objects.select_related('category').prefetch_related('User').get(id=id)
#     participants=event.participants.all()
#     context={
#         'event':event,
#         'participants':participants
#     }
#     return render(request,'event_detail.html',context)

class EventDetail(DetailView):
    model=Event
    template_name='event_detail.html'
    context_object_name='event'
    pk_url_kwarg='id'
    
    def get_queryset(self):
        event=Event.objects.select_related('category').prefetch_related('User')
        return event
    
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['participants']=self.object.participants.all()
        return context

# def event_create(request):
#     form=EventForm()
    
#     if request.method=='POST':
#         form=EventForm(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.success(request,'Event created successfully')
#             return redirect('event_list')
#     return render(request,'event_form.html',{'form':form})  

class EventCreate(CreateView):
    model=Event
    form_class=EventForm
    template_name='event_form.html'
    success_url=reverse_lazy('event_list')
    
    def form_valid(self,form):
        messages.success(self.request,'Event created successfully')
        return super().form_valid(form)
  
# def event_update(request,id):
#     event=Event.objects.get(id=id)
#     form=EventForm(instance=event)
#     if request.method=='POST':
#         form=EventForm(request.POST,request.FILES, instance=event)
#         if form.is_valid():
#             form.save()
#             messages.success(request,'Event Updated successfully')
#             return redirect('event_list')
#     return render(request,'event_form.html',{'form':form}) 

class EventUpdate(UpdateView):
    model=Event
    form_class=EventForm
    template_name= 'event_form.html'
    pk_url_kwarg='id'
    success_url=reverse_lazy('event_list')

    def form_valid(self,form):
        messages.success(self.request,'Event Updated successfully')
        return super().form_valid(form)

  
# def event_delete(request,id):
#     if request.method=='POST':
#             event=Event.objects.get(id=id)
#             event.delete()
#             messages.success(request,'Event Deleted successfully')
#             return redirect('event_list')

#     else:
#         messages.error(request,'Something went Wrong!')
#         return redirect('event_list')
    

class EventDelete(DeleteView):
    model=Event
    pk_url_kwarg='id'
    success_url=reverse_lazy('event_list')
    template_name='event_list.html'
 
    def delete(self,request,*args,**kwargs):
        messages.success(self.request,'Event Deleted successfully')
        return super().delete(request,*args,**kwargs)
   

# CRUD for participants 

def participant_list(request):
    Participants=User.objects.prefetch_related('events').all()
    context={
       'participants':Participants
    }
    return render(request,'participant_list.html',context)        
              

# def participant_create(request):
#     form=ParticipantForm()
#     if request.method=='POST':
#         form=ParticipantForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request,'Participant Created Successfully')
#             return redirect('participant_list')
#     return render(request,'dashboard/participant_form.html',{'form':form})    

# def participant_update(request,id):
#     participant=User.objects.get(id=id)
#     form=ParticipantForm(instance=participant)
#     if request.method=='POST':
#         form=ParticipantForm(request.POST,instance=participant)
#         if form.is_valid():
#             form.save()
#             messages.success(request,'Participant Updated Suceesfully')
#             return redirect('participant_list')
#     return render (request,'dashboard/participant_form.html',{'form':form})

def participant_delete(request,id):

    if request.method=='POST':
        participant=User.objects.get(id=id)
        participant.delete()
        messages.success(request,'Participant Deleted Successfully')
        return redirect('participant_list')
    else:
        messages.success(request,'Something Went Wrong')
        return redirect('participant_list')


   # CRUD for Category 

def category_create(request):
    form=CategoryForm()
    if request.method=='POST':
        form=CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Category Added!!')
            return redirect('category_list')
    return render(request,'category_form.html',{'form':form}) 


def category_list(request):
    categorys=Category.objects.prefetch_related('event_set').all() 
    context={
        'categorys':categorys,
    }  
    return render(request,'category_list.html',context)

def category_update(request,id):
    category=Category.objects.get(id=id)
    form=CategoryForm(instance=category)
    if request.method=='POST':
        form=CategoryForm(request.POST,instance=category)
        if form.is_valid():
            form.save()
            messages.success(request,'category Updated Suceesfully')
            return redirect('category_list')
    return render (request,'category_form.html',{'form':form}) 

def category_delete(request,id):
    category=Category.objects.get(id=id)
    if request.method=='POST':
        category.delete()
        messages.success(request,'Category Deleted!')
        return redirect('category_list')
    else:
        messages.success(request,'Something went wrong!')
        return redirect('category_list')


