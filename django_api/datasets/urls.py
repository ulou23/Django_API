from django.urls import include,path
from django.conf.urls import url

#alternatywnie urls.py

from rest_framework.routers import SimpleRouter

from .viewset import UserViewSet, PostViewSet

router=SimpleRouter()
router.register('users',UserViewSet,basename='users')
router.register('posts',PostViewSet,basename='posts')

from .views import DataPackList,DataList,DataDetail,DataCatDetail,DataCatList,DataPackDetail,ResearcherDetail,ResearcherList,ApiRoot ,HomeLabView

urlpatterns=[
    path('datacat/',DataCatList.as_view(),name=DataCatList.name),
    path('datacat/<int:pk>',DataCatDetail.as_view(),name=DataCatDetail.name),
    path('data/',DataList.as_view(),name=DataList.name),
    path('data/<int:pk>',DataDetail.as_view(),name=DataDetail.name),
    path('researcher/',ResearcherList.as_view(),name=ResearcherList.name) ,
    path('researcher/<int:pk>',ResearcherDetail.as_view(),name=ResearcherDetail.name) ,
    path('pack/',DataPackList.as_view(),name=DataPackList.name) ,
    path('pack/<int:pk>',DataPackDetail.as_view(),name=DataPackDetail.name),
    path('',ApiRoot.as_view(),name=ApiRoot.name) ,
    path('homelab',HomeLabView.as_view()),

]
urlpatterns=router.urls

