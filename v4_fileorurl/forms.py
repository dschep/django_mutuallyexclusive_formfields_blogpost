from django import forms
from mutuallyexclusive_formfields.forms import FileOrURLField

class TestForm(forms.Form):
    test_field = FileOrURLField(to='file')
