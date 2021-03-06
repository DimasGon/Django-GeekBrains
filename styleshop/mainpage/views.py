from django.shortcuts import render
from django.views.generic import View
from . import models
from cartapp.models import Cart

class Index(View):

    def get(self, request):

        sections = models.Section.objects.all()
        brands = models.Brand.objects.all()
        categories = models.Category.objects.all()

        return render(
            request, 'mainpage/index.html', 
            {
                'sections': sections, 
                'brands': brands,
                'categories': categories,
                'amount': Cart.total_amount(request)
            }
        )
