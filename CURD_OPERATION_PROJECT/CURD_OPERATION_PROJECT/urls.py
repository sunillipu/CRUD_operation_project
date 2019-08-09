from django.conf.urls import include, url
from django.contrib import admin
from CURD_OPERATION_APPLICATION import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'CURD_OPERATION_PROJECT.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',views.home_view),
    url(r'^create/',views.create_view),
    url(r'^update/',views.update_view),
    url(r'^retrive/',views.retrive_view),
    url(r'^delete/',views.delete_view)
]
