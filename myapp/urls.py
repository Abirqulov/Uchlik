from django.urls import path
from myapp.views import *


urlpatterns = [
    path('', Index, name='index'),
    path('gallery/', gallery, name='gallery'),
    path('full_width/', full_width, name='full_width'),
    path('basic_grid/', basic_grid, name='basic_grid'),
    path('font_icons/', font_icons, name='font_icons'),
    path('sidebar_left/', sidebar_left, name='sidebar_left'),
    path('sidebar_right/', sidebar_right, name='sidebar_right'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('search_home/', HomePageView.as_view(), name='home'),

]