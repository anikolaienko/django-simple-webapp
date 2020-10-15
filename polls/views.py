from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from .models import Poll, Question, Choice
from .forms import RegisterForm, PollForm

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_polls_list'

    def __is_my__(self):
        return self.request.user.is_authenticated and self.request.GET.get('my')

    def get_queryset(self):
        """Return the last five published questions."""
        filters = {}
        
        if self.__is_my__():
            filters['author_id'] = self.request.user.id

        return Poll.objects.filter(**filters).order_by('-created_at')[:15]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        isMy = self.__is_my__()
        context['list_title'] = 'List of my polls' if isMy else 'List of all polls'
        context['my_polls'] = isMy
        return context

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(created_at__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('polls:index')
    else:
	    form = RegisterForm()

    return render(request, 'polls/register.html', {"form":form})

class FormActionMixin(object):

    def post(self, request, *args, **kwargs):
        """Add 'Cancel' button redirect."""
        if 'cancel' not in request.POST:
            form = PollForm(request.POST)
            poll = form.save(commit = False)
            poll.author_id = request.user.id
            poll.save()
        url = reverse('polls:index')
        return HttpResponseRedirect(url)

class PollCreateView(FormActionMixin, generic.CreateView):
    model = Poll
    form_class = PollForm
    template_name = 'polls/create_poll.html'
