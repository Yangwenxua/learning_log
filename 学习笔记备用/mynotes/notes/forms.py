# notes/forms.py
from django import forms
from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['title']

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['content']  # 添加 'owner' 到 fields 列表