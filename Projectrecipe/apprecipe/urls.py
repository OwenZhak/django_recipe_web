from django.urls import path
from .views import HomeView,CategoryListView, RecipeDetailView, RecipeCreateView, RecipeUpdateView, RecipeDeleteView, CategoryCreateView, search_feature, SearchListView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('recipe/<int:pk>', RecipeDetailView.as_view(), name='recipe-detail'),
    path('create_recipe/', RecipeCreateView.as_view(), name='create-recipe'),
    path('recipe/edit/<int:pk>', RecipeUpdateView.as_view(), name='edit-recipe'),
    path('recipe/<int:pk>/delete', RecipeDeleteView.as_view(), name='delete-recipe'),
    path('category/create', CategoryCreateView.as_view(), name='create-category'),
    path('category/<str:categ>/', CategoryListView.as_view(), name='category'),
    path('search/', SearchListView.as_view(), name='search'),
]