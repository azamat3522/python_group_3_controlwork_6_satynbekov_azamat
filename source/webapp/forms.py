from django import forms
from django.forms import widgets



class QuestBookForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label='Name')
    mail = forms.EmailField(label='Mail')
    text = forms.CharField(max_length=2000, required=True, label='Text',
                           widget=widgets.Textarea)

