from django.conf import settings

from .import views
from django.urls import path
from django.conf.urls.static import static

urlpatterns = [

    path('',views.demo,name='demo'),
    # path('details',views.details,name='details')
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('cbvhome/',views.listview.as_view(),name='cbvhome'),
    path('cbvdetaild/<int:pk>/',views.detailview.as_view(),name='cbvdetaild'),
    path('cbvupdate/<int:pk>/',views.updateview.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.deleteview.as_view(),name='cbvdelete'),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                        document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)