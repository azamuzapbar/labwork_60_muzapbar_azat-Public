from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from webapp.forms import ProductForm
from webapp.models import Product


class ArticleCreateView(CreateView):
    template_name = 'article_create.html'
    model = Product
    form_class = ProductForm
    print('article_create.html')

    def get_success_url(self):
        return reverse('article_detail', kwargs={'pk': self.object.pk})




class ArticleDetail(DetailView):
    template_name = 'article.html'
    model = Product



class ArticleUpdateView(UpdateView):
    template_name = 'article_update.html'
    form_class = ProductForm
    model = Product

    def get_success_url(self):
        return reverse('article_detail', kwargs={'pk':self.object.pk})


class ArticleDeleteView(DeleteView):
    template_name = 'article_confirm_delete.html'
    model = Product
    success_url = reverse_lazy('index')