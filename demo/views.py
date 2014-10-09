from django.views.generic.edit import FormView
from django.shortcuts import render_to_response
from .forms import V1TestForm, V2TestForm, V3TestForm, V4TestForm

class TestView(FormView):
    template_name = 'test_form.html'

    def form_valid(self, form):
        return render_to_response('success.html', {'form': form})

class V1TestView(TestView):
    form_class = V1TestForm

class V2TestView(TestView):
    form_class = V2TestForm

class V3TestView(TestView):
    form_class = V3TestForm

class V4TestView(TestView):
    form_class = V4TestForm
