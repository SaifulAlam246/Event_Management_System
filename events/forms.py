from django import forms
from events.models import *
from django.contrib.auth.models import User

class EventForm(forms.ModelForm):
    class Meta:
        model=Event
        fields=['name','description','date','time','location','category','event_image']

        widgets={
            'name':forms.TextInput(attrs={
                'class': 'border rounded black-500 shadow-md p-2 mt-5'
            }),
             'description': forms.Textarea(attrs={
                'class': 'border shadow-md p-2 rounded w-full h-32'
            }),
            'date':forms.DateInput(attrs={'type':'date'}),
            'time':forms.DateInput(attrs={'type':'time'})
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=['name','description']  

        widgets={
            'name':forms.TextInput(attrs={'type':'text'}),
            'description': forms.Textarea(attrs={
                    'class': 'border shadow-md p-2 rounded w-full h-32'
            }),
        }      

