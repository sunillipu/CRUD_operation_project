from django.shortcuts import render
from .models import ProductData
from django.http.response import HttpResponse

def home_view(request):
    return render(request,'home.html')


def create_view(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id', '')
        product_name = request.POST.get('product_name', '')
        product_color = request.POST.get('product_color', '')
        product_class= request.POST.get('product_class', '')
        product_price = request.POST.get('product_price', '')
        customer_name = request.POST.get('customer_name', '')
        customer_mobile = request.POST.get('customer_mobile', '')
        customer_email = request.POST.get('customer_email', '')
        data = ProductData(
            product_id=product_id,
            product_name=product_name,
            product_color=product_color,
            product_class=product_class,
            product_price=product_price,
            customer_name=customer_name,
            customer_mobile=customer_mobile,
            customer_email=customer_email
        )
        data.save()
        return render(request, 'create.html')
    return render(request,'create.html')


def update_view(request):
    if request.method == 'POST':
        product_id = request.POST.get('productid', '')
        product_price = request.POST.get('productprice', '')
        pid = ProductData.objects.filter(product_id=product_id)

        if not pid:
            return HttpResponse("Product Id is not available")
        else:
            pid.update(product_price=product_price)
            return render(request, 'update.html')
    else:
        return render(request, 'update.html')



def retrive_view(request):
    pdata=ProductData.objects.all()
    return render(request,'retrive.html',{'pdata':pdata})


def delete_view(request):
    if request.method=='POST':
        product_id = request.POST.get('ppid', '')

        pid = ProductData.objects.filter(product_id=product_id)

        if not pid:
            return HttpResponse("Product Id Is Not Available")
        else:
            pid.delete()
    return render(request,'delete.html')