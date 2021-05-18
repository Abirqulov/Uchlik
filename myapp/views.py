from django.shortcuts import render
from .models import *
from django.db.models import Q
from django.views.generic import TemplateView, ListView
from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate, gettext
# Create your views here.
def Index(request):
    uch = Uchlik.objects.all()


    from django.utils import translation
    # user_language = 'fr'
    # translation.activate(user_language)
    # request.session[translati
    # on.LANGUAGE_SESSION_KEY] = user_language

    # if translation.LANGUAGE_SESSION_KEY in request.session:
    #     del request.session[translation.LANGUAGE_SESSION_KEY]

    if request.method=="POST":
        name = request.POST["name"]
        email = request.POST["email"]
        password = request.POST["password"]
        # print(name, email)
        ins = Register(name=name, email=email, password=password)
        ins.save()
    return render(request, 'index.html', {'uch': uch})


def gallery(request):
    return render(request, 'gallery.html')

def full_width(request):

    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        url = request.POST["url"]
        comment = request.POST["comment"]

        full = FullWidth(name=name, email=email, url=url, comment=comment)
        full.save()

    return render(request, 'full-width.html')

def basic_grid(request):
    return render(request, 'basic-grid.html')

def font_icons(request):
    return render(request, 'font-icons.html')

def sidebar_left(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        url = request.POST["url"]
        comment = request.POST["comment"]

        left = SidebarLeft(name=name, email=email, url=url, comment=comment)
        left.save()

    return render(request, 'sidebar-left.html')

def sidebar_right(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        url = request.POST["url"]
        comment = request.POST["comment"]

        right = SidebarRight(name=name, email=email, url=url, comment=comment)
        right.save()

    return render(request, 'sidebar-right.html')


class HomePageView(TemplateView):
    template_name = 'home.html'

class SearchResultsView(ListView):
    model = Uchlik
    template_name = 'search_results.html'
    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Uchlik.objects.filter(
            Q(name_uz__contains=query) | Q(description_uz__contains=query) |
            Q(name_ru__contains=query) | Q(description_ru__contains=query) |
            Q(name_en__contains=query) | Q(description_en__contains=query)
        )
        return object_list
    # queryset = City.objects.filter(name='Toshkent City')