from django import forms

from p_library.models import Author, Book, Friend, Publisher


class AuthorForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput)
    class Meta:
        model = Author
        fields = '__all__'