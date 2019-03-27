
from django.contrib import admin
from django.urls import path, include
from users import views as user_vievs







urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_vievs.register, name='register'),
    path('', include("blog.urls")),



]
