"""
    This is the apidemo module's urlpatterns.
"""
from django.conf.urls import url
from apidemo import views

api_urls = [
    url(r'^api/', views.GameRecordView.as_view())
]
