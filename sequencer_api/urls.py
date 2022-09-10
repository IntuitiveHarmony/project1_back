from django.urls import path
from . import views

urlpatterns = [
    path('api/sequencer', views.SequenceList.as_view(), name='sequence_list'), 
    path('api/sequencer/<int:pk>', views.SequenceDetail.as_view(), name='sequence_detail'),
]
