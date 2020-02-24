from django import forms

from .models import Contactor,Elog


class ContactorFrom(forms.ModelForm):
    class Meta:
        modal = Contactor
        fields = [
            'name', 'phone', 'orgid',
        ]

class ElogFrom(forms.Form):
    slug = forms.SlugField()
    content = forms.CharField(widget=forms.Textarea)


class ElogModelFrom(forms.ModelForm):
    class Meta:
        modal = Elog
        fields = [
            'slug', 'content',
        ]