from django.shortcuts import render, redirect
from .models import Post, Contact, Comment, Category
import requests
from django.core.paginator import Paginator


def index_view(request):
    posts = Post.objects.filter(is_published=True).order_by("-created_at")
    return render(request, 'index.html', context={'posts': posts})


def about_view(request):
    return render(request, 'about.html')


def contact_view(request):
    print("=" * 50)
    print(request.method)
    print("=" * 50)

    if request.method == "POST":
        # frontan kelgan
        data = request.POST

        # datani database ga save qilamiz
        obj = Contact.objects.create(name=data.get("name"), email=data.get("email"),
                                     message=data.get("message"), subject=data.get("subject"), phone=data.get("phone"))
        obj.save()

        # telegram notify
        token = '6780110729:AAF71LYp2nEcgNAyQDIwFLmVer-8P2cImDU'
        requests.get(
            f"""https://api.telegram.org/bot{token}/sendMessage?chat_id=5467422443&text=SHAKHRUZ\nid: {obj.id}\nname: {obj.name}\nphone: {obj.phone}\nemail: {obj.email}\nmessage: {obj.message}""")

        return redirect("/contact")
    return render(request, 'contact.html')


def blog_view(request):
    data = request.GET
    cat = data.get("cat")
    page = data.get("page", 1)

    if cat:
        posts = Post.objects.filter(is_published=True, category_id=cat).order_by("-created_at")
    else:
        posts = Post.objects.filter(is_published=True).order_by("-created_at")

    page_obj = Paginator(posts, 6)

    return render(request, 'blog.html', context={'posts': page_obj.page(page)})


def blog_single_view(request, pk):
    if request.method == "POST":
        data = request.POST
        obj = Comment.objects.create(post_id=pk, name=data.get("name"), email=data.get("email"),
                                     website=data.get("website"), message=data.get("message"))
        obj.save()
        return redirect(f'/blog/{pk}')
    post = Post.objects.get(id=pk)
    comments = Comment.objects.filter(post_id=pk)

    return render(request, 'blog-single.html', context={'post': post, "comments": comments})
