from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Forum, Post
from .forms import PostForm

@login_required
def post_create(request, forum_id):
    forum = get_object_or_404(Forum, id=forum_id)

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.forum = forum
            post.save()
            return redirect('forum_detail', forum_id=forum.id)
    else:
        form = PostForm()

    return render(request, 'forums/post_create.html', {'form': form, 'forum': forum})
