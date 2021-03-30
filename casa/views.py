from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .forms import contact_form
from django.contrib import messages
from .models import CakeCategory, CakeProduct

# Create your views here.

def index (request):
    return render(request, 'casa/index.html')


def about (request):
    return render(request, 'casa/about.html')


def cake_list(request, category_slug=None):
    category = None
    categories = CakeCategory.objects.all()
    products = CakeProduct.objects.filter(available=True)
    # cart_product_form = CartAddForm
    if category_slug:
        category = get_object_or_404(CakeCategory, slug=category_slug)
        products = products.filter(cake_category=category)

    context = {
        'category': category,
        'products': products,
        'categories': categories,
        'title': 'standard cakes',
        # 'cart_product_form': cart_product_form
    }
    return render(request, 'casa/cakes/item_list.html', context)


def cake_detail (request, id, slug):
    product = get_object_or_404(CakeProduct, id=id, slug=slug, available=True)
    context = {
        'product': product
    }
    return render(request, 'casa/cakes/item_detail.html', context)


def contact_view (request):
    if request.method == 'POST':
        form = contact_form(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            try:
                send_mail(subject, message, email, ['ukejemicheal@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

            messages.success (request, f'message {subject} successfully sent')
            return redirect("casa:casa-contact")
    form = contact_form ()
    return render(request, "casa/contact.html", {'form': form})