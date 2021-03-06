from django.conf import settings
from django.conf.urls import include
from django.conf.urls import patterns
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.contrib.staticfiles.views import serve
from django.contrib import admin
from issue_tracker.app import views as it_views

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^search/$', login_required(it_views.SearchIssues.as_view()),
        name='search'),
    url(r'^issue/add/$', login_required(it_views.CreateIssue.as_view()),
        name='create_issue'),
    # For the uninitiated, pk is the primary key, which in our case is the 
    # bug id.
    url(r'^issue/view/(?P<pk>\d+)/$',
        login_required(it_views.ViewIssue.as_view()),
        name='view_issue'),
    # Examples:
    url(r'^$', it_views.ExampleView.as_view(), name='example'),
    # static files path
    url(r'^%s(?P<path>.*)$' % settings.STATIC_URL.lstrip('/'), serve,
        {'show_indexes': True, 'insecure': False}),
    # Admin site setup.
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
