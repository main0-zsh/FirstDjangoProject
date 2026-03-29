from django.urls import path, re_path, include
from .views import *

article_patterns=[
    re_path('(?P<id>8)/', article_8),
    re_path('(?P<id>2)/', article_2),
    re_path('(?P<id>5)/', article_5),
    path('', article_page),
    path('sorted_article/', sorted_article_page)
]

urlpatterns=[
    re_path(r'^id/(?P<id>55555)/',aiphone_17pm),
    re_path(r'^user/adill/password/12345',account),
    path('',welcome),
    path('id/fake', fake_prank),
    path('info_abt_me/',info_abt_me),
    path('info_abt_me_67/', error_info),
    path('attributes',get_attributes),
    path('user/<str:username>/',user_page),
    path('article/', include(article_patterns)),
    path('list/',Json_Response),
    path('cookies/',set_cookies)
]

handler404=fourzerofour_error