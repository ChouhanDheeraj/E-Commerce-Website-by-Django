
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="Shop home"),
    
    path("about/",views.aboutus,name="AboutUs"),
    path("contact/",views.contact,name="ContactUs"),
    path("tracker/",views.tracker,name="TrackingStatus"),
    path("search/",views.search,name="Search"),
    path("products/<int:myid>",views.prodview,name="ProductView"),
    path("checkout/",views.checkout,name="CheckOut"),
    path("handlerequest/",views.handlerequest,name="handlerequest"),
    
]
