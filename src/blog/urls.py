from django.urls import path

from blog.view import all_blogs, create_blog

urlpatterns = [
    path("create/", create_blog, name="create_blog"),
    path("", all_blogs, name="all_blogs"),
]
