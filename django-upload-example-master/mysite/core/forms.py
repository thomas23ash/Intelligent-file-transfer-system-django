from django import forms


from .models import Book

from django_clamd.validators import validate_file_infection


class BookForm(forms.ModelForm):
    class Meta:
        model = Book

        fields = ('title', 'author','From','file') #'cover')
        upload_file = forms.FileField(validators=[validate_file_infection])

