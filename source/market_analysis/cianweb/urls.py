from django.urls import path, reverse_lazy
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',            views.HomeView.as_view(),   name='home'),
    path('parser/',     views.ParserView.as_view(), name='parser'),
    path('train/',      views.VisualizeView.as_view(), name='visualize'),
    path('visualize/',  views.TrainView.as_view(), name='train'),

    path('parser/get_metro/', views.getMetro,name='metro')

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)