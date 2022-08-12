from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from app.models import Post
from app.forms import PostForm


@login_required
def index(request: HttpRequest) -> HttpResponse:

    # if not request.user.is_authenticated:
    #     return redirect("/accounts/login/")

    qs = Post.objects.all()

    return render(request, "app/index.html",
                  {"post_list": qs, }
                  )


def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
    post = get_object_or_404(Post, pk=pk)

    return render(request, "app/post_detail.html", {
        "post": post
    },
    )


post_new = CreateView.as_view(
    model=Post,
    form_class=PostForm,
    success_url="/app/",
)
