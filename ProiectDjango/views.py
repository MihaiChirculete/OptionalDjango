from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.views.generic import TemplateView, ListView
from .models import Article
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# def article_list(request):
#     object_list = Article.published.all()
#     paginator = Paginator(object_list, 3)  # 3 posts in each page
#     page = request.GET.get('page')
#     try:
#         posts = paginator.page(page)
#     except PageNotAnInteger:
#         # If page is not an integer deliver the first page
#         posts = paginator.page(1)
#     except EmptyPage:
#         # If page is out of range deliver last page of results
#         posts = paginator.page(paginator.num_pages)
#     return render(request,
#                   'ProiectDjango/article/list.html',
#                   {'page': page,
#                    'posts': posts})


def article_detail(request, year, month, day, post):
    post = get_object_or_404(Article, slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request,
                  'ProiectDjango/article/detail.html',
                  {'post': post})


class ArticleListView(ListView):
    queryset = Article.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'ProiectDjango/article/list.html'
