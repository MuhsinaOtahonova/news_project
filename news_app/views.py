from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import News, Category 
from .forms import ContactForm
from django.views.generic import TemplateView, ListView
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
    news_list = News.published.all().order_by('-publish_time')[:4]
    categories = Category.objects.all()
    defense_aviation_technologies = News.published.all().filter(category__name = "Defense and Aviation Technologies").order_by("-publish_time")[:4]
    defense_aviation_technologies_one = News.published.all().filter(category__name = "Defense and Aviation Technologies").order_by("-publish_time")[:1]
    context = {
        'news_list' : news_list,
        'categories' : categories,
        "defense_aviation_technologies" : defense_aviation_technologies,
        "defense_aviation_technologies_one" : defense_aviation_technologies_one
    }
    return render(request, 'news/home.html', context)




class HomePgaeView(ListView):
    model = News
    template_name = 'news/home.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['news_list'] = News.published.all().order_by('-publish_time')[:3]
        context['defense_aviation_technologies'] = News.published.all().filter(category__name = "Defense and Aviation Technologies").order_by("-publish_time")[:5]
        context['ai_tech'] = News.published.all().filter(category__name = "AI and Advanced Technologies").order_by("-publish_time")[:5]
        context['defense_inventory'] = News.published.all().filter(category__name = "Defense Power and Inventory Updates").order_by("-publish_time")[:5]
        context['national_production'] = News.published.all().filter(category__name = "National and Indigenous Production Achievements").order_by("-publish_time")
        context['humanitarian_efforts'] = News.published.all().filter(category__name = "Humanitarian Aid and Social Responsibility").order_by("-publish_time")
        return context




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