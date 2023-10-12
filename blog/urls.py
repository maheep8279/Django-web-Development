from django.urls import path
from . import views
from .views import StartingPageView


urlpatterns = [
    path("", views.StartingPageView.as_view(), name="starting-page"),
    path("posts", views.AllPostsView.as_view(), name="post-page"),
    path("posts/<slug:slug>", views.SinglePostView.as_view(), name="post-detail-page")
]
