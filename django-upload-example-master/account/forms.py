from django import forms

from account.models import registermodel


class AccountForm(forms.ModelForm):
    class Meta:
        model=registermodel
        fields={'first_name','last_name','username' ,'email' ,'password1' ,'password2' }