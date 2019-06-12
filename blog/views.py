from django.shortcuts import render,get_object_or_404
from .models import posts
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,DetailView, CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin



# print(posts.objects.first().pk)
@login_required
def home(request):
    return render(request,'blog/home.html',{'title':'Home','posts':posts.objects.all()})
@login_required
def about(request):
    return render(request,'blog/about.html',{'title':'About'})


class PostListView(LoginRequiredMixin,ListView):
	model =posts
	template_name = 'blog/home.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']
	paginate_by =4
	#<app>/<model>_<viewtype>.html 




class PostDetailView(LoginRequiredMixin,DetailView):
	context_object_name = 'object'
	model =posts
	template_name = 'blog/posts_detail.html'



class PostCreateView(LoginRequiredMixin,CreateView):
	model = posts
	fields=['title','content']
	template_name = 'blog/posts_form.html'
	#query_set = posts.objects.all()
	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)



class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
	model =posts
	fields = ['title','content']

	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)
	def test_func(self):
		post = self.get_object()
		if self.request.user== post.author:
			return True
		return False



class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
	model =posts
	success_url = '/blog/blog-home/'
	def test_func(self):
		post = self.get_object()
		if self.request.user== post.author:
			return True
		return False
	
class UserPostListView(LoginRequiredMixin,ListView):
	model =posts
	template_name = 'blog/user_posts.html'
	context_object_name = 'posts'
	
	paginate_by =4
	def get_queryset(self):
		user = get_object_or_404(User,username = self.kwargs.get('username'))
		return posts.objects.filter(author=  user).order_by('-date_posted')