"""
    This is the url pattern for the snippets.
"""
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views
# from snippets import views_class

urlpatterns = [
    url(r'^snippets/$', views.snippet_list),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail)
]

# if you use the class-style's view
# urlpatterns = [
#     url(r'^snippets/', views_class.SnippetList.as_view()),
#     url(r'^snippets/(?P<pk>[0-9]+)/$', views_class.SnippetDetail.as_view())
# ]

urlpatterns = format_suffix_patterns(urlpatterns)
