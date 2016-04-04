from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Voter, Flag, Vote


class IndexView(generic.ListView):
    template_name = 'chnnlsdmo/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Flag.objects.order_by('name')


class DetailView(generic.DetailView):
    model = Flag 
    template_name = 'chnnlsdmo/detail.html'


class ResultsView(generic.DetailView):
    model = Flag 
    template_name = 'chnnlsdmo/results.html'


def vote(request, question_id):
    ... # same as above, no changes needed.
