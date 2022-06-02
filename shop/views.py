from django.db.models import query
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
#from django import http
#from django.http import HttpResponse
from .models import Contact, Product,Orders,orderUpdate
from math import ceil, prod
import json
from django.views.decorators.csrf import csrf_exempt
from .PayTm import checksum
MERCHANT_KEY = 'VMLsKh33374131769871' #'Your-Merchant-Key-Here'

# Create your views here.
def index(request):
   #Products = Product.objects.all()
   #print(Products)
   #n = len(Products)
   #nslide = n//4 + ceil((n/4)-(n//4))
    #params = {'product':Products,'no.of Slide': nslide,'range':range(nslide)}
    #allProd = [[Products,range(1,nslide),nslide],[Products,range(1,nslide),nslide]]
    allProd = []
    catProds = Product.objects.values('category','id')
    cats = {item['category'] for item in catProds}
    for cat in cats :
        prod = Product.objects.filter(category =cat)
        n = len(prod)
        nslide = n//4 + ceil((n/4)-(n//4))
        allProd.append([prod,range(1,nslide),nslide])
    params = {'allProds':allProd}
    return render(request,'shop/index.html',params)

def searchMatch(query,item):
    if query in item.desc.lower() or query in item.product_name.lower() or query in item.category.lower() or query in item.subcategory.lower() :
        return True
    else : 
        return False

def search(request):
    query = request.GET.get('search')
    allProd = []
    catProds = Product.objects.values('category','id')
    cats = {item['category'] for item in catProds}
    for cat in cats :
        prodtemp = Product.objects.filter(category =cat)
        prod = [item for item in prodtemp if searchMatch(query, item)]
        n = len(prod)
        nslide = n//4 + ceil((n/4)-(n//4))
        if len(prod) != 0 :
            allProd.append([prod,range(1,nslide),nslide])
    params = {'allProds':allProd}
   # if len(allProd) ==0 or len(allProd)<3 :
   #         params = {'msg':"Please make sure that you enter relavent search query"}
    return render(request,'shop/index.html',params)

def aboutus(request):
    return render(request,'shop/about.html')
def contact(request):
    thank = False
    if request.method == "POST" :
        print(request)
        Firstname = request.POST.get('Fname',"")
        lastname = request.POST.get('Lname',"")
        Email = request.POST.get('email',"")
        phonenumber = request.POST.get('phone',"")
        Address = request.POST.get('address',"")
        City = request.POST.get('city',"")
        State = request.POST.get('state',"")
        Query = request.POST.get('query',"")
        contact = Contact(Firstname=Firstname,Lastname=lastname,Email=Email,phonenumber=phonenumber,Address=Address,City=City,
                State=State,Query= Query)
        contact.save()
        thank = True
    return render(request,'shop/contact.html',{"thank": thank})
def tracker(request):
    if request.method == "POST":
        orderId =  request.POST.get('orderId',"")
        email =  request.POST.get('email',"")
        #return HttpResponse(f"{orderId} and {email}")
        try:
            order = Orders.objects.filter(order_id = orderId,email= email)
            if len(order)>0 :
                update = orderUpdate.objects.filter(order_id = orderId)
                updates = []
                for items in update:
                    updates.append({'text':items.update_desc,'time': items.timestamps})
                    responce = json.dumps({"status":"successed","updates":updates,"itemsjson": order[0].items_json},default=str)
                return HttpResponse(responce)
            else :
                return HttpResponse('{"status":"successed"}')
        except Exception as e:
            return HttpResponse('{"status":"error"}')

    return render(request,'shop/tracker.html')



def prodview(request,myid):
    # Fetch the Product using ID
    product = Product.objects.filter(id=myid)
    return render(request,'shop/Prodview.html',{'product':product[0]})

def checkout(request):
    if request.method == "POST" :
       print(request)
       item_json = request.POST.get('itemsJson',"")
       Name = request.POST.get('name',"")
       amount = request.POST.get('amount',"")
       Email = request.POST.get('email',"")
       phonenumber = request.POST.get('phone',"")
       Address1 = request.POST.get('address1',"")
       Address2 = request.POST.get('address2',"")
       City = request.POST.get('city',"")
       State = request.POST.get('state',"")
       Zip_code = request.POST.get('zipcode','')
       order = Orders(name= Name,email=Email,phonenumber=phonenumber,address1=Address1,address2=Address2, city=City,amount= amount,
               state=State,zip_code = Zip_code,items_json=item_json)
       order.save()
       update = orderUpdate(order_id = order.order_id,update_desc = 'The order has been placed')
       update.save()
       #thank = True
       #id = order.order_id
       param_dict={

            'MID': 'WorldP64425807474247',
            'ORDER_ID': 'order.order_id',
            'TXN_AMOUNT': '1',
            'CUST_ID': 'email',
            'INDUSTRY_TYPE_ID': 'Retail',
            'WEBSITE': 'WEBSTAGING',
            'CHANNEL_ID': 'WEB',
            'CALLBACK_URL':'http://127.0.0.1:8000/shop/handlerequest/',
        }
       param_dict['CHECKSUMHASH'] = checksum.generate_checksum(param_dict, MERCHANT_KEY)   
       return render(request,'shop/paytm.html',{'param_dict':param_dict})

    
    return render(request,'shop/checkout.html')
    
    # Request paytm to transfer the amount in your account after payment


@csrf_exempt
def handlerequest():
    # payem will send you post request here
    return HttpResponse("Done")
    pass

