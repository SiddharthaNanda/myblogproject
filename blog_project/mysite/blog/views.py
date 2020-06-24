from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import (TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from blog.forms import PostForm, CommentForm
from django.urls import reverse_lazy
from blog.models import Post,Comment

class AboutView(TemplateView):
    template_name="about.html"

class TrymeView(TemplateView):
    template_name="practice2.html"

class PostListView(ListView):
    model = Post
    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    form_class = PostForm
    login_url = '/login/'
    redirect_field_name='blog/post_detail.html'

class PostUpdateView(UpdateView,LoginRequiredMixin):
    model = Post
    login_url='/login/'
    form_class = PostForm
    redirect_field_name='blog/post_detail.html'

class PostDeleteView(DeleteView,LoginRequiredMixin):
    model = Post
    success_url = reverse_lazy('post_list')

class DraftListView(ListView,LoginRequiredMixin):
    model = Post
    login_url = '/login/'
    redirect_field_name = 'blog/post_draft_list.html'

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')



def add_comment_to_post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method=='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form = CommentForm()

    return render(request,'blog/comment_form.html',{'form':form})

@login_required
def approve_comment(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    comment.approve()
    return redirect('post_detail',pk=comment.post.pk)

@login_required
def remove_comment(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    post_pk=comment.post.pk
    comment.delete()
    return redirect('post_detail',pk=post_pk)

@login_required
def post_publish(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('post_detail',pk=pk)
