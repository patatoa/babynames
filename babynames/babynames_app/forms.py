__author__ = 'pthomas'

from django import forms
from models import FullName

class UpdateNameForm(forms.ModelForm):

    class Meta:
        model = FullName
        fields = ('pros', 'cons')
