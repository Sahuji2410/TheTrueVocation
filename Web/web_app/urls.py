# urls.py
from django.urls import path
from .views import (
    JobTypeListView, JobTypeDetailView, JobTypeCreateView, JobTypeUpdateView, JobTypeDeleteView,
    JobDescriptionListView, JobDescriptionDetailView, JobDescriptionCreateView, JobDescriptionUpdateView, JobDescriptionDeleteView
)

urlpatterns = [
    # JobType URLs
    path('', JobTypeListView.as_view(), name='jobtype_list'),
    path('jobtypes/<int:pk>/', JobTypeDetailView.as_view(), name='jobtype_detail'),


    
    path('jobtypes/create/', JobTypeCreateView.as_view(), name='jobtype_create'),
    path('jobtypes/<int:pk>/update/', JobTypeUpdateView.as_view(), name='jobtype_update'),
    path('jobtypes/<int:pk>/delete/', JobTypeDeleteView.as_view(), name='jobtype_delete'),

    # JobDescription URLs
    path('jobdescriptions/', JobDescriptionListView.as_view(), name='jobdescription_list'),
    path('jobdescriptions/<int:pk>/', JobDescriptionDetailView.as_view(), name='jobdescription_detail'),
    path('jobdescriptions/create/', JobDescriptionCreateView.as_view(), name='jobdescription_create'),
    path('jobdescriptions/<int:pk>/update/', JobDescriptionUpdateView.as_view(), name='jobdescription_update'),
    path('jobdescriptions/<int:pk>/delete/', JobDescriptionDeleteView.as_view(), name='jobdescription_delete'),
]
