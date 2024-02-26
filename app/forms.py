from django import forms
from . models import ChatMessage

class ChatMessageForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id':'id_body', 'rows':2, 'cols':20, 'placeholder': 'Enter your message here...'}))
    class Meta:
        model = ChatMessage
        fields = ['message',]