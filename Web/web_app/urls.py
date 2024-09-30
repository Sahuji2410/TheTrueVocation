# urls.py
from django.urls import path
from .views import (
    JobTypeListView, JobTypeDetailView, JobTypeCreateView, JobTypeUpdateView, JobTypeDeleteView,
    JobDescriptionListView, JobDescriptionDetailView, JobDescriptionCreateView, JobDescriptionUpdateView, JobDescriptionDeleteView
)
from .views import *

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

Add_data_to_db_urlpatterns = [
    path('add-user/', add_user, name='add_user'),
    path('add-job-type/', add_job_type, name='add_job_type'),
    path('add-job-description/', add_job_description, name='add_job_description'),
    path('add-job-announcement/', add_job_announcement, name='add_job_announcement'),
    path('add-dynamic-image/', add_dynamic_image, name='add_dynamic_image'),
    path('dynamic-images/', dynamic_image_list, name='dynamic_image_list'),
    path('delete-dynamic-image/<int:image_id>/', delete_dynamic_image, name='delete_dynamic_image'),
    path('logo-images/', logo_image_list, name='logo_image_list'),
    path('delete-logo-image/<int:image_id>/', delete_logo_image, name='delete_logo_image'),
]
urlpatterns += Add_data_to_db_urlpatterns