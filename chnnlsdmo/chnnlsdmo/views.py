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
    f = get_object_or_404(Flag, pk=flag_id)
    current_user = request.user
    v = get_object_or_404(Voter, pk=current_user.id)
    print(f.name)
    v = Vote(flag=f, voter=v);
    v.save()
    return HttpResponseRedirect(reverse('index'))
    '''
    try:
        v = Vote(flag=f);
        v.save()
    except ():
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
        return HttpResponseRedirect(reverse('index',))
    '''
