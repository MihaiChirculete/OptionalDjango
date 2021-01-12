from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.views.generic import TemplateView, ListView
from .models import Article
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import EmailArticleForm
from django.core.mail import send_mail


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


def article_share(request, article_id):
    # Retrieve article by id
    article = get_object_or_404(Article, id=article_id, status='published')
    sent = False

    if request.method == 'POST':
        # Form was submitted
        form = EmailArticleForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            clean_data = form.cleaned_data
            article_url = request.build_absolute_uri(
                article.get_absolute_url())
            subject = f"{clean_data['name']} recommends you read " \
                      f"{article.title}"
            message = f"Read {article.title} at {article_url}\n\n" \
                      f"{clean_data['name']}\'s comments: {clean_data['comments']}"
            send_mail(subject, message, 'admin@proiectdjango.com',
                      [clean_data['to']])
            sent = True
        else:
            form = EmailArticleForm()
            return render(request, 'ProiectDjango/article/share.html', {'post': article,
                                                            'form': form})
