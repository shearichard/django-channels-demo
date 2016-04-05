from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Voter, Flag, Vote


class IndexView(generic.ListView):
    template_name = 'chnnlsdmo/index.html'
    context_object_name = 'flag_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Flag.objects.order_by('name')


class DetailView(generic.DetailView):
    model = Flag 
    template_name = 'chnnlsdmo/detail.html'


class ResultsView(generic.DetailView):
    model = Flag 
    template_name = 'chnnlsdmo/results.html'


def vote(request, flag_id):
    flag = get_object_or_404(Flag, pk=flag_id)
    print(flag.name)
    '''
    try:
        selected_choice = flag.choice_set.get(pk=flag_id)
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the flag voting form.
        return render(request, 'polls/detail.html', {
            'flag': flag,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(flag.id,)))
    '''
    return HttpResponseRedirect(reverse('index'))
