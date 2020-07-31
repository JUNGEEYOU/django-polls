"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include

"""
    path(route, view, kwargs, name) 형태 
    - route: 주소를 의미 
    - view: route 주소로 접근했을 때 호출할 뷰 
    - krwargs: 뷰에 전달되는 값들 
    - name: route의 이름. 이 이름으로 원하는 곳에서 호출 가능. 
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls'))   # include는 다른 urls 파일 참조 가능
]
