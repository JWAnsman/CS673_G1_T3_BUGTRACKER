"""Container for the various views supported."""

from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import FormView
from issue_tracker.app import forms
from issue_tracker.app import models as it_models


class ExampleView(TemplateView):
    template_name = 'example.html'

    def get(self, request, *args, **kwargs):
        context = {
            'example_value': 'Hello World!',
        }
        return self.render_to_response(context)

class CreateIssue(CreateView):
    model = it_models.Issue
    fields = ['title', 'description', 'issue_type', 'priority', 'project',
              'assignee']
    template_name = 'create_issue.html'

    def get_initial(self):
        return {"user": self.request.user}

class ViewIssue(DetailView):
    model = it_models.Issue
    template_name = 'issue_detail.html'

# TODO(jdarrieu): Not done with this work yet.
class SearchIssues(FormView):
    form_class = forms.SearchForm
    template_name = 'search.html'

    def form_valid(self, form):
        results = search(form.cleaned_data)
        if results:
            return self.render_to_response({'form': form,
                                            'issues': results})
