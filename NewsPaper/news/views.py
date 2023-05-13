
from django.views.generic import ListView, DetailView
from .models import Author, Category, Post, PostCategory, Comment
from datetime import datetime


class PostList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'posts'
    gueryset = Post.objects.order_by('-id')

    def get_queryset(self):
        return Post.objects.all()


    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['value'] = None
        context['news_count'] = self.get_queryset().count()
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'id.news.html'
    context_object_name = 'post'

    def get_queryset(self):
        return Post.objects.filter(categoryType='AR')





