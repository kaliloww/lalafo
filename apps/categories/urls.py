from django.urls import path

from apps.categories.views import CategoryAPIView, CategoryRetriveApiView, CategoryCreateAPIView, CategoryUpdateAPIView, CategoryDestroyAPIView

urlpatterns = [
    path('', CategoryAPIView.as_view(), name="api_category"),
    path('<int:pk>/', CategoryRetriveApiView.as_view(), name="api_category_retrive"),
    path('create/<int:pk>/', CategoryCreateAPIView.as_view(), name="api_category_create"),
    path('update/<int:pk>/', CategoryUpdateAPIView.as_view(), name='api_category_update'),
    path('destroy/<int:pk>/', CategoryDestroyAPIView.as_view(), name='api_category_destroy'),

]