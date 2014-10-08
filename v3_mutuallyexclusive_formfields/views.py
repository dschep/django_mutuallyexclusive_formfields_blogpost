from django.views.generic.edit import FormView
from .forms import TestForm

class TestView(FormView):
    template_name = 'test_form.html'
    form_class = TestForm
    success_url = '/static/success.html'
