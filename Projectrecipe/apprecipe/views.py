from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy

#def home(request):
#   return render(request, 'home.html', {})


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-id']

    def get_context_data(self, *args, **kwargs):
        categ_menu = Category.objects.all()
        context = super().get_context_data(*args, **kwargs)
        context['categ_menu'] = categ_menu
        return context


class RecipeDetailView(DetailView):
    model = Post
    template_name = 'recipedetail.html'

    def get_context_data(self, *args, **kwargs):
        categ_menu = Category.objects.all()
        context = super(DetailView, self).get_context_data(*args, **kwargs)
        context['categ_menu'] = categ_menu
        return context

class RecipeCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_recipe.html'
    #fields = '__all__'


class CategoryCreateView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'
    success_url = reverse_lazy('home')


class RecipeUpdateView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'edit_recipe.html'


class RecipeDeleteView(DeleteView):
    model = Post
    template_name = 'delete_recipe.html'
    success_url = reverse_lazy('home')


def CategoryView(request, categ):
    category_posts = Post.objects.filter(category=categ)
    return render(request, 'categories.html', {'categ': categ.title(), 'category_post': category_posts})

class CategoryListView(ListView):
    model = Post
    template_name = 'categories.html'
    context_object_name = 'category_post'

    def get_queryset(self):
        categ = self.kwargs['categ']
        return Post.objects.filter(category=categ)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categ_menu = Category.objects.all()
        categ = self.kwargs['categ']
        context['categ_menu'] = categ_menu
        context['categ'] = categ.title()
        return context

def search_feature(request):
    # Check if the request is a post request.
    if request.method == 'POST':
        # Retrieve the search query entered by the user
        search_query = request.POST['search_query']
        search_query = search_query.lower()
        # Filter your model by the search query
        posts = Post.objects.filter(recipe_tittle__contains=search_query)
        return render(request, 'search_recipes.html', {'query':search_query, 'posts':posts})
    else:
        return render(request, 'search_recipes.html',{})

class SearchListView(ListView):
    model = Post
    template_name = 'your_template.html'  # Update with your actual template name
    context_object_name = 'posts'


    def get_queryset(self):
        search_query = self.request.GET.get('search_query', '').lower()
        if search_query:
            return Post.objects.filter(recipe_tittle__contains=search_query)
        else:
            return Post.objects.all()

    def post(self, request, *args, **kwargs):
        search_query = request.POST.get('search_query', '').lower()
        posts = Post.objects.filter(recipe_tittle__contains=search_query)
        categ_menu = Category.objects.all()
        return render(request, 'search_recipes.html', {'query': search_query, 'posts': posts, 'categ_menu': categ_menu})


    def get_context_data(self, *args, **kwargs):
        categ_menu = Category.objects.all()
        context = super().get_context_data(*args, **kwargs)
        context['categ_menu'] = categ_menu
        return context


