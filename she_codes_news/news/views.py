from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .models import NewsStory
from .forms import StoryForm, CommentForm


class IndexView(generic.ListView):
    template_name = 'news/index.html'
    context_object_name = 'all_stories'

    def get_queryset(self):
        '''Return all news stories.'''
        qs = NewsStory.objects.all()
        sort = self.request.GET.get("sort")
        print (f"{sort=}")
        if sort == "OldestFirst":
            qs = qs.order_by('pub_date')
        else:
            qs = qs.order_by('-pub_date')
        return qs
        
        

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'
 

class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class AddCommentView(generic.CreateView):
    form_class = CommentForm
    template_name = "news/createComment.html"
    success_url = reverse_lazy("news:newsStory")

    def form_valid(self, form):
        form.instance.author = self.request.user
        pk = self.kwargs.get("pk")
        story = get_object_or_404(NewsStory, pk=pk)
        form.instance.story = story
        return super().form_valid(form)

    def get_success_url(self) -> str:
        pk = self.kwargs.get("pk")
        return reverse_lazy("news:story", kwargs={"pk":pk})