from django.urls import path
from .views.articles import ArticleCreateView, ArticleDetail,ArticleUpdateView,ArticleDeleteView
from .views.base import IndexView
from .views.cart import add_to_cart
from .views.cart_list import CartView, CartLineDeleteView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('articles/add/', ArticleCreateView.as_view(), name='article_add'),
    path('articles/<int:pk>/update/', ArticleUpdateView.as_view(), name='article_update'),
    path('articles/<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('articles/<int:pk>/confirm-delete/', ArticleDeleteView.as_view(), name='confirm_delete'),
    path('articles/<int:pk>', ArticleDetail.as_view(), name='article_detail'),
    path('cart/', CartView.as_view(), name='cart'),
    path('cart/<int:pk>/create/', add_to_cart, name='add_to_cart'),
    # path('cart/<int:pk>/delete/', CartLineDeleteView, name='delete_from_cart'),

]