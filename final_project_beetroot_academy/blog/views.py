from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from users.models import Profile
from django.views import View
from .forms import ChatGptForm
import openai
import os

cwd = os.path.dirname(__file__)

PATH = f'{cwd}\\token'
def start(request):
    if request.method == 'POST':
        form = ChatGptForm(request.POST)
        if form.is_valid():
            choice = form.cleaned_data['meal_choice']

            if choice == '1':
                API_KEY = open(PATH,'r').read()
                openai.api_key = API_KEY

                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages = [
                        {"role":"system", "content": "You are a system that suggests meals for muscle building"},
                        {"role":"user", "content": "Suggest one breakfast which would be good for muscle building and ingredients and directions for that"}]
                )
                assistant_response = response['choices'][0]['message']['content'].replace('\n','<br>')

                return render(request, 'blog/start_page.html', {'form': ChatGptForm(), 'meal': assistant_response})
            elif choice == '2':
                API_KEY = open(PATH,'r').read()
                openai.api_key = API_KEY

                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages = [
                        {"role":"system", "content": "You are a system that suggests meals for muscle building"},
                        {"role":"user", "content": "Suggest one lunch which would be good for muscle building and ingredients and directions for that"}]
                )
                assistant_response = response['choices'][0]['message']['content'].replace('\n','<br>')

                return render(request, 'blog/start_page.html', {'form': ChatGptForm(), 'meal': assistant_response})
            elif choice == '3':
                API_KEY = open(PATH,'r').read()
                openai.api_key = API_KEY

                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages = [
                        {"role":"system", "content": "You are a system that suggests meals for muscle building"},
                        {"role":"user", "content": "Suggest one dinner which would be good for muscle building and ingredients and directions for that"}]
                )
                assistant_response = response['choices'][0]['message']['content'].replace('\n','<br>')

                return render(request, 'blog/start_page.html', {'form': ChatGptForm(), 'meal': assistant_response})

            return render(request, 'blog/start_page.html', {'form': ChatGptForm()})
    else:
        return render(request, 'blog/start_page.html', {'form': ChatGptForm()})


class BlogPostsView(LoginRequiredMixin,ListView):
    model = Post
    template_name = 'blog/blog_page.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class BlogPostsDetailsView(LoginRequiredMixin,DetailView):
    model= Post

class PostProfileDetailsView(LoginRequiredMixin,DetailView):
    model = Profile
    template_name = 'blog/post_profile_details.html'


class CreateBlogPost(LoginRequiredMixin,CreateView):
        model = Post
        fields = ['title', 'content']
        template_name = 'blog/blog_create.html'

        def form_valid(self, form):
            form.instance.author = self.request.user
            return super().form_valid(form)


class UpdateBlogPost(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/blog_update.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()

        if post.author == self.request.user:
            return True
        return False

class DeleteBlogPost(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = '/'
    def test_func(self):
        post = self.get_object()

        if post.author == self.request.user:
            return True
        return False


class BreakfastPageView(View):
    def get(self,request, *args, **kwargs):
        return render(request,'blog/breakfasts.html')

class LunchPageView(View):
    def get(self,request, *args, **kwargs):
        return render(request,'blog/lunches.html')

class DinnerPageView(View):
    def get(self,request, *args, **kwargs):
        return render(request,'blog/dinners.html')

class SupplementPageView(View):
    def get(self,request, *args, **kwargs):
        return render(request,'blog/supplements.html')

class ProteinPageView(View):
    def get(self,request, *args, **kwargs):
        return render(request,'blog/protein.html')

class ContactsPageView(View):
    def get(self,request, *args, **kwargs):
        return render(request,'blog/contacts.html')
