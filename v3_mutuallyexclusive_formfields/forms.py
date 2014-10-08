from django import forms
from mutuallyexclusive_formfields.forms import (
        MutuallyExclusiveValueField, MutuallyExclusiveRadioWidget)

class TestForm(forms.Form):
    test_field = MutuallyExclusiveValueField(
            fields=(forms.IntegerField(), forms.IntegerField()),
            widget=MutuallyExclusiveRadioWidget(widgets=(
                forms.Select(choices=[(1,1), (2,2), (3,3)]),
                forms.TextInput(),
            )))
    #test_fileurl_field = FileOrURLField(to='file')

