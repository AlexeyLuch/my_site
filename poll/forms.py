from django import forms

class ChatForm(forms.Form):
    your_name = forms.CharField()
