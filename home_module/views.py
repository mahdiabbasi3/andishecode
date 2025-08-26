from django.shortcuts import render
from django.views.generic import TemplateView
from .models import site_setting,License,SocialMedia
from article_module.models import Article
from product_module.models import Product,Plan,feature

class HomeView(TemplateView):
    template_name = 'home_module/home_page.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['site_set']=site_setting.objects.first()
        context['product']=Product.objects.filter(is_active=True)
        context['plan']=Plan.objects.filter(is_active=True)
        context['feature']=feature.objects.select_related('plane')
        context['lasted_article']=Article.objects.all()[:3]
        return context

# def index_page(request):
#     site_set=site_setting.objects.first()
#     return render(request,'home_module/home_page.html',context={'site_set':site_set})



def headersite(request):
    site_set = site_setting.objects.first()
    return render(request,'shared/header_site.html',context={'site_set':site_set})

def footersite(request):

    site_set = site_setting.objects.first()
    licens=License.objects.filter(is_active=True)
    social=SocialMedia.objects.filter(is_active=True)
    return render(request,'shared/footer_site.html',context={'site_set':site_set,'license':licens,
                                                             'social':social})

def about_site(request):
    return render(request,'home_module/about.html')


