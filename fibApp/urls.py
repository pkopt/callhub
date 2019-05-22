
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import calFib,index

urlpatterns = [

    url(r'^callhub/fib/$', calFib.as_view()),
      url(r'^callhub/latest.html', index.as_view())
    ]