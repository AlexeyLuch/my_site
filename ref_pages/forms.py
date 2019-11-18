from django import forms

from my_site.ref_pages.models import Referer


class TopicForm(forms.ModelForm):
    class Meta:
        model = Referer
        fields = ["text", "public"]
        labels = {"text": "label", "public": "label for public"}