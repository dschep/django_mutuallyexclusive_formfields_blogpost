from django import forms
from mutuallyexclusive_formfields.forms import (
        MutuallyExclusiveValueField, MutuallyExclusiveRadioWidget)

class TestForm(forms.Form):
    test_field = MutuallyExclusiveValueField(
            fields=(forms.CharField(), forms.ChoiceField(
                choices=[('1','1'), ('2','2'), ('3','3')])),
            widget=MutuallyExclusiveRadioWidget(widgets=(
                forms.TextInput(),
                forms.Select(choices=[('1','1'), ('2','2'), ('3','3')]),
            )))
    #test_fileurl_field = FileOrURLField(to='file')

