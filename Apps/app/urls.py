from django.urls import path
from Apps.app.views import *

urlpatterns = [
    path('job-types/', JobTypeView.as_view(), name='jobtype-list-create'),
    path('job-types/<int:pk>/', JobTypeDetailView.as_view(), name='jobtype-detail'),
    path('job-descriptions/', JobDescriptionView.as_view(), name='jobdescription-list-create'),
    path('job-descriptions/<int:pk>/', JobDescriptionDetailView.as_view(), name='jobdescription-detail'),
]