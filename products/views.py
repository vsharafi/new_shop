
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import Product, Comment
from .forms import CommentForm
from django.contrib import messages
from django.utils.translation import gettext as _
from cart.forms import AddProductToCartForm


class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'products/product_list.html'
    queryset = Product.objects.filter(active=True)


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'products/product_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.active_posts.filter(product=get_object_or_404(Product, pk=self.kwargs['pk']))
        context['form'] = CommentForm()
        context['cart_form'] = AddProductToCartForm()
        return context
    
    # def post(self, request, *args, **kwargs):
    #     form = CommentForm()
    #     form = CommentForm(request.POST)
    #     obj = form.save(commit=False)
    #     obj.product = get_object_or_404(Product, pk=self.kwargs['pk'])
    #     obj.author = request.user
    #     obj.save()
    #     form = CommentForm()
    #     return render(request, 'products/product_detail.html', {'form': form, 'product': obj.product})
    
class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'products/product_detail.html'
    context_object_name = 'form'
    
    def form_valid(self, form):
        product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        comment_obj = form.save(commit=False)
        comment_obj.product = product
        comment_obj.author = self.request.user
        messages.success(self.request, _('Your comment has sent successfully.'))
        return super().form_valid(form)
