from blogging.views import BlogDetailView, BlogListView
from django.urls import path, include

# from blogging.views import stub_view, list_view, detail_view

urlpatterns = [
    # path('', stub_view, name="blog_index"),
    path("", BlogListView.as_view(), name="blog_index"),
    path("posts/<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
]
