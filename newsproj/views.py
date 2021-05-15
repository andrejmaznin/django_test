from django.shortcuts import render
from .models import News
from django.http import HttpResponseNotFound
from .forms import AddForm
from datetime import datetime
from django.shortcuts import redirect


def news_list(request):
    news = News.objects.all()
    return render(request, 'news_list.html', {"news": news})


def news_id(request, id):
    news = News.objects.get(id=id)
    if not news:
        return HttpResponseNotFound()
    return render(request, 'news.html', {"news": news, "tags": news.tags.split(",")})


def add(request):
    if request.method == "POST":
        form = AddForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
            post.save()
            news = News.objects.order_by('id')
            news = news[len(news) - 1]
            return redirect(f"/{news.id}")
    else:
        form = AddForm()
    return render(request, 'add_form.html', {'form': form})


def stats(request):
    news = News.objects.all()
    news = list(sorted(news, key=lambda a: a.views, reverse=True))

    return render(request, 'stats.html', {"news": news})
