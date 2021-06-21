from django.db.models import Count, Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import *
from .forms import CommentForm, PostForm
# Create your views here.

# for creating a post we need the author
def get_author(user):
    qs = Author.objects.filter(user=user)
    if qs.exists():
        return qs[0]
    return None


def search_results(request):
    queryset = Post.objects.all()
    query = request.GET.get('query')
    # query = request.GET.get('q')
    # if query == None:
    #     query = ''

      
        
    if query:
        queryset = queryset.filter(             
            Q(title__icontains=query) |
            Q(overview__icontains=query)

        ).distinct()

        context = {

            "queryset": queryset
        }
        return render(request, "myblog/search_results.html", context)

  

def home(request):
    posts = Post.objects.order_by("timestamp")[:3]
    categories = Category.objects.all()
    tags = Tag.objects.all()
    latest = Post.objects.order_by("-timestamp")[:3]

    if request.method == 'POST':
        email = request.POST['email']
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()
    context = {
        'posts': posts,
        'latest': latest,
        'tags': tags,
        'categories': categories
    }

    return render(request, "myblog/home.html", context)


def posts(request):
    most_recent = Post.objects.order_by("-timestamp")[:3]
    post_list = Post.objects.all()
    post = Post.objects.all()
    categories = Category.objects.all()
    tags = Tag.objects.all()
    paginator = Paginator(post, 3)  # order_by order_by('name')
    page_request_var = 'page'
    page = request.GET.get(page_request_var)  # gives us a page_number
    try:
        paginated_queryset = paginator.page(page)

    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)

    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    context = {
        "post_list": post_list,
        "categories": categories,
        "most_recent": most_recent,
        "post": post,
        "tags": tags,
        "queryset": paginated_queryset,
        "page_request_var": page_request_var
    }
    return render(request, "myblog/posts.html", context)


def post_detail(request, pk):
    post = get_object_or_404(Post,  pk=pk)
    post_list = Post.objects.all()
    latest = Post.objects.order_by('-timestamp')[0:3]
    categories = Category.objects.all()
    tags = Tag.objects.all()
    thumbnail = Post.objects.all()
    lists = Post.objects.all()
    share = Post.objects.all()
    # quote = Quotes.objects.all()
    # quote_by = Quotes.objects.all()
    form = CommentForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.instance.user = request.user
            form.instance.post = post
            form.save()
            return redirect(reverse('post_detail', kwargs={'pk': post.pk}))
    context = {"post": post,
               "post_list": post_list,
               "latest": latest, "tags"
               "categories":  categories,
               "tags": tags,
               "form": form,
               "lists": lists,
               "thumbnail": thumbnail,
               #    "quote": quote,
               #    "quote_by": quote_by,
               "share": share
               }
    return render(request, "myblog/post_detail.html", context)


def post_create(request):
    title = "Create"
    # for tinymce we need request.files or none
    form = PostForm(request.POST or None, request.FILES or None)
    author = get_author(request.user)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.author = author
            form.save()
            return redirect(reverse('post_detail', kwargs={'pk': form.instance.pk}))

    context = {

        "form": form,
        "title": title,
        
        # "author": author
    }

    return render(request, "myblog/post_create.html", context)


def post_update(request, pk):
    title = 'Update'
    post = get_object_or_404(Post, pk=pk)
    form = PostForm(
        request.POST or None,
        request.FILES or None,
        instance=post)
    author = get_author(request.user)
    if request.method == "POST":
        if form.is_valid():
            form.instance.author = author
            form.save()
            return redirect(reverse('post_detail', kwargs={'pk': form.instance.pk}))
    context = {
        'title': title,
        'form': form
    }
    return render(request, "myblog/post_create.html", context)


def post_delete(request, pk):
    post = get_object_or_404(Post,  pk=pk)
    post.delete()
    return redirect(reverse('posts'))
