from django.views.generic import ListView, DetailView
from django.views.generic.edit import  UpdateView, DeleteView
from  django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from . import models

class ArticleListView(ListView):
    model = models.Article
    template_name = 'article_list.html'

class ArticleDetailView(DetailView):
    model = models.Article
    template_name = 'article_detail.html'

class ArticleDeleteView(DeleteView):
    model = models.Article
    success_url = reverse_lazy('article_list')
    template_name = 'article_delete.html'

class ArticleUpdateView(UpdateView):
    model = models.Article
    fields = ['title', 'body']
    template_name = 'article_edit.html'

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = models.Article
    template_name =  'article_new.html'
    fields = ['title', 'body', 'author']
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
