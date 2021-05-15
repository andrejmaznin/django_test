from django import forms

from .models import News


class AddForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ('title', 'text', 'tags')
