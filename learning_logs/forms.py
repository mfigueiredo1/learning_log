from django import forms

from .models import Topic, Entry

# Added comment on 1/10/2025 to practice git 

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = {'text'}
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols':80})}

