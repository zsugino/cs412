from django.shortcuts import render
from .models import Article
from django.views.generic import ListView, DetailView, CreateView, DeleteView
import random
from .forms import CreateCommentForm, CreateArticleForm
from django.urls import reverse
from typing import Any, Dict
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm ## NEW
from django.contrib.auth.models import User ## NEW
from django.contrib.auth import login # NEW
from django.shortcuts import redirect, reverse


# class-based views
class ShowAllView(ListView):
  '''Create a subclass of ListView to display all blog articles'''
  model = Article
  template_name = "blog/show_all.html"
  context_object_name = "articles"

  def dispatch(self, *args, **kwargs):

    print("self.request.user={self.request.user}")
    return super().dispatch(*args, **kwargs)


class RandomArticleView(DetailView):
  '''Show the details for one article'''
  model = Article
  template_name = 'blog/article.html'
  context_object_name = 'article'

  # pick one article at random:
  def get_object(self):
    '''Return one Article object chosen at random.'''

    all_articles = Article.objects.all()
    return random.choice(all_articles)

class ArticleView(DetailView):
    '''Show one article by its primary key.'''

    model = Article
    template_name = 'blog/article.html'
    context_object_name = "article" # note the singular name

class CreateCommentView(CreateView):
    '''A view to create a new comment and save it to the database.'''
    form_class = CreateCommentForm
    template_name = "blog/create_comment_form.html"
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        '''
        Build the dict of context data for this view.
        '''
        # superclass context data
        context = super().get_context_data(**kwargs)
        # find the pk from the URL
        pk = self.kwargs['pk']
        # find the corresponding article
        article = Article.objects.get(pk=pk)
        # add article to context data
        context['article'] = article
        return context

    def form_valid(self, form):
        '''
        Handle the form submission. We need to set the foreign key by 
        attaching the Article to the Comment object.
        We can find the article PK in the URL (self.kwargs).
        '''
        print(form.cleaned_data)
        article = Article.objects.get(pk=self.kwargs['pk'])
        # print(article)
        form.instance.article = article
        return super().form_valid(form)
    
    ## show how the reverse function uses the urls.py to find the URL pattern
    def get_success_url(self) -> str:
        '''Return the URL to redirect to after successfully submitting form.'''
        #return reverse('show_all')
        return reverse('article', kwargs={'pk': self.kwargs['pk']})

class CreateArticleView(LoginRequiredMixin, CreateView):
    '''A view to create a new Article and save it to the database.'''
    form_class = CreateArticleForm
    template_name = "blog/create_article_form.html"

    def get_login_url(self) -> str:
        '''Return the URL to the login page.'''
        return reverse('login')

    def form_valid(self, form):
        '''
        Handle the form submission to create a new Article object.
        '''
        print(f'CreateArticleView: form.cleaned_data={form.cleaned_data}')


        # FIND WHICH USER IS LOGGED IN
        user = self.request.user
        print("CreateArticleViewform_valid() user={user}")
        form.instance.user = user
        # delegate work to the superclass version of this method
        return super().form_valid(form)


class RegistrationView(CreateView):
    '''
    show/process form for account registration
    '''
    template_name = 'blog/register.html'
    form_class = UserCreationForm
    def dispatch(self, *args, **kwargs):
        '''
        Handle the User creation part of the form submission, 
        '''
        # handle the POST:
        if self.request.POST:
            # reconstruct the UserCreationForm from the POST data
            user_form = UserCreationForm(self.request.POST)
            # create the user and login
            user = user_form.save()     
            print(f"RegistrationView.form_valid(): Created user= {user}")   
            login(self.request, user)
            print(f"RegistrationView.form_valid(): User is logged in")   
            
            # for mini_fb: attach the user to the Profile instance object so that it 
            # can be saved to the database in super().form_valid()
            return redirect(reverse('show_all'))
        
        # GET: handled by super class
        return super().dispatch(*args, **kwargs)




    








  


