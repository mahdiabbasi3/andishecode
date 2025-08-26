from django.shortcuts import render,redirect
from .forms import ContactUsForm
from .models import ContactInfo
from django.contrib import messages

def contactus(request):
    contact_info=ContactInfo.objects.first()
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'پیام شما با موفقیت ارسال شد')
            return redirect('contactus')
    else:
        form = ContactUsForm()
    return render(request,'contact_module/contact_us.html',{
        'form':form,
        'contact':contact_info
    })
