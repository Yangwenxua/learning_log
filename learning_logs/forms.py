from django import forms
from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        fields = ['text']
        labels = {'text': ''}
=======
=======
        fields = ['text', 'public']
        labels = {'text': '', 'public': 'Public topic'}
>>>>>>> temp-lzy
=======
        fields = ['text']
        labels = {'text': ''}
=======
        fields = ['text', 'public']
        labels = {'text': '', 'public': 'Public topic'}
>>>>>>> main
>>>>>>> 692d21f307d04745ca70f09977f7c5aaa7a6f475

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}