"""hospital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from testapp import views

from rest_framework_simplejwt import views as v
# from rest_framework_jwt.views import obtain_jwt_token


from rest_framework import routers
router = routers.DefaultRouter()
# # router.register(r'addcart',PhotoViewSet)
# router.register(r'photo/', PhotoViewSet)


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),



    path('api/token/', v.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', v.TokenRefreshView.as_view(), name='token_refresh'),

    # path('api/token/auth/',obtain_jwt_token),

    path('hospital', views.hospital_list),
    path('hospital/<int:pk>/', views.hospital_list_detail),

    # Sales view
    path('sales', views.sales_view),

    #for register
    path('reg', views.register),



    path('img',views.image_upload),
    path('img/<int:pk>/', views.image_upload_detail),




    path('registration/', views.RegistrationView.as_view(), name='registration'),

    #uploading multiple images at once
    path('multi',views.myFiles),
    path('m',views.mv),




    # custom images(restricted) Task
    path('restricted',views.Custom_images),

    # pagination   Task
    path('pagination',views.Pagination_view),
    path('myview/',views.vio),







    # Testing purpose
    path('temp',views.temp_view),


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
