from django import forms
from django.core.validators import EMPTY_VALUES
from mutuallyexclusive_formfields.forms import (
        MutuallyExclusiveValueField, MutuallyExclusiveRadioWidget,
        FileOrURLField)

class V1TestForm(forms.Form):
    test_field1 = forms.ChoiceField(
            required=False,
            choices=[('', 'Custom (below)'), ('1','1'), ('2','2'), ('3','3')],
            help_text="fill in either test_field1 or test_field2")
    test_field2 = forms.CharField(
            required=False,
            help_text="fill in either test_field1 or test_field2")

    def clean(self):
        cleaned_data = super(V1TestForm, self).clean()

        if not (bool(self.cleaned_data['test_field1']) !=
                bool(self.cleaned_data['test_field2'])):
            raise forms.ValidationError, 'Fill in only one of the two fields'

        return cleaned_data


class V2TestForm(forms.Form):
    test_field1 = forms.ChoiceField(
            required=False,
            choices=[('', 'Custom (below)'), ('1','1'), ('2','2'), ('3','3')])
    test_field2 = forms.CharField(required=False)

    def clean(self):
        cleaned_data = super(V2TestForm, self).clean()

        if not (bool(self.cleaned_data['test_field1']) !=
                bool(self.cleaned_data['test_field2'])):
            raise forms.ValidationError, 'Fill in only one of the two fields'

        return cleaned_data

    class Media:
        js = ('v2_djangoandjs.js',)


class V3TestForm(forms.Form):
    test_field = MutuallyExclusiveValueField(
            fields=(forms.IntegerField(), forms.IntegerField()),
            widget=MutuallyExclusiveRadioWidget(widgets=(
                forms.Select(choices=[(1,1), (2,2), (3,3)]),
                forms.TextInput(),
            )))


class V4TestForm(forms.Form):
    test_field1 = FileOrURLField(
            to=None, help_text='This normalized to what the user submitted.')
    test_field2 = FileOrURLField(
            to='file', help_text='This normalized to a file.')
    test_field3 = FileOrURLField(
            upload_to='TEST', to='url', help_text='This normalized to an url.')
