from django import forms
from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
<<<<<<< HEAD
<<<<<<< HEAD
        fields = ['text']
        labels = {'text': ''}
=======
=======
        fields = ['text', 'public']
        labels = {'text': '', 'public': 'Public topic'}
>>>>>>> temp-lzy

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}