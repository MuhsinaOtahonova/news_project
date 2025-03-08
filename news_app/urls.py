from django.urls import path
from .views import news_list, news_detail, homePgaeView, ContactPageView, errorPageView, HomePgaeView
from .views import DefenseInventoryView, NationalProductionView, HumanitarianEffortsView, \
    DefenseAviationTechnologiesView, AiTechView, NewsUpdateView, NewsDeleteView, NewsCreateView

urlpatterns = [
    path('', HomePgaeView.as_view(), name = 'home_page'),
    path('news/', news_list, name = "all_news_list"),
    path('news/create/', NewsCreateView.as_view(), name = 'news_create'),
    path('news/<slug:news>/', news_detail, name = "news_detail_page"),
    path('contact-us/', ContactPageView.as_view(), name = "contact_page"),
    path('404/', errorPageView, name = "404_page"),
    path('news/<slug>/edit/', NewsUpdateView.as_view(), name = 'news_update'),
    path('news/<slug>/delete/', NewsDeleteView.as_view(), name = 'news_delete'),

    path('defense-inventory/', DefenseInventoryView.as_view(), name = "defense_inventory_page"),
    path('national-production/', NationalProductionView.as_view(), name = "national_production_page"),
    path('humani-efforts/', HumanitarianEffortsView.as_view(), name = "humani_efforts_page"),
    path('defense-aviation/', DefenseAviationTechnologiesView.as_view(), name = "defense_aviation_page"),
    path('ai-technology/', AiTechView.as_view(), name = "ai_technology_page")
]
