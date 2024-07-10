from django.contrib import admin
from django.urls import path,include
from . import views

# for viewset -->
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'', views.TaskViewSet, basename = 'task')


urlpatterns = [
    path('', include(router.urls))
]


# for other views --->
# urlpatterns = [
#     path('',views.index.as_view(), name='index'),
#     path('create/',views.create.as_view(), name='create'),
#     path('<int:pk>/',views.del_update.as_view(), name='del_update'),
# ]