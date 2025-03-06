from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import News, Category 
from .forms import ContactForm
from django.views.generic import TemplateView
# Create your views here.

def news_list(request):
    news_list = News.published.all()
    context = {
        "news_list" : news_list
    }
    return render(request, "news/news_list.html", context)

def news_detail(request, id):
    news = get_object_or_404(News, id=id, status = News.Status.Published)
    context = {
        "news" : news
    }
    return render(request, 'news/news_detail.html', context)

def homePgaeView(request):
    news_list = News.published.all().order_by('-publish_time')[:10]
    categories = Category.objects.all()
    defense_aviation_technologies = News.published.all().filter(category__name = "Defense and Aviation Technologies")
    context = {
        'news_list' : news_list,
        'categories' : categories,
        "defense_aviation_technologies" : defense_aviation_technologies
    }
    return render(request, 'news/home.html', context)


def errorPageView(request):
    context = {
        
    }
    return render(request, 'news/404.html', context)

# def contactPageView(request):
#     # print(request.POST)
#     form = ContactForm(request.POST or None)
#     if request.method == "POST" and form.is_valid():
#         form.save()
#         return HttpResponse("<h2> Thank you for contact us ")

#     context = {
#         "form":form
#     }
    # return render(request, 'news/contact.html', context)

class ContactPageView(TemplateView):
    template_name = 'news/contact.html'

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {
            "form":form
        }
        return render(request, 'news/contact.html', context)
    
    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if request.method == 'POST' and form.is_valid():
            form.save()
            return HttpResponse("<h2> Thank you for contact us <h2>")
        
        context = {
            "form":form
        }
        return render(request, 'news/contact.html', context)