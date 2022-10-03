from django.contrib import admin
from django.urls import path
# from app.views import demo
from app.views import DemoView,WeapomView
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('demo/', demo),
    path('demo/', DemoView.as_view()),
    path('weapon/<pk>/', WeapomView.as_view()),
]
