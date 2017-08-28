from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from app.views import *





urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^first_view/(?P<starts_with>\w+)/$', 'app.views.first_view'),
    url(r'^get_post', 'app.views.get_post'),
    url(r'^template_view', 'app.views.template_view'),
    url(r'^state_list_view/', StateListView.as_view()),
    url(r'states/(?P<pk>[0-9]+)/$', 'app.views.state_detail'),
    url(r'cities/(?P<pk>[0-9]+)/$', CityDetailView.as_view()),
    url(r'city_search/$', 'app.views.city_search'),
    url(r'^city_create/', 'app.views.city_create'),
    url(r'city_delete/$', 'app.views.city_delete'),
    url(r'user_signup/$', 'app.views.user_signup'),













]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
