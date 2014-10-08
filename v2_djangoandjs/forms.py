from django import forms
from django.core.validators import EMPTY_VALUES

class TestForm(forms.Form):
    test_field1 = forms.ChoiceField(
            required=False,
            choices=[('', 'Custom (below)'), ('1','1'), ('2','2'), ('3','3')])
    test_field2 = forms.CharField(required=False)

    def clean(self):
        cleaned_data = super(TestForm, self).clean()

        if not (bool(self.cleaned_data['test_field1']) !=
                bool(self.cleaned_data['test_field2'])):
            raise forms.ValidationError, 'Fill in only one of the two fields'

        return cleaned_data

    class Media:
        js = ('v2_djangoandjs.js',)
