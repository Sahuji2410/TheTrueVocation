# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from Apps.apps_models.models import JobType, JobDescription,jobAnnouncments
from django.conf import settings
from django.views.generic import DetailView
import re


# JobType Views
class JobTypeListView(View):
    def get(self, request):
        job_types = JobType.objects.all()
        job_descriptions = JobDescription.objects.all()
        other_context = jobAnnouncments.objects.first() # Fetch the single instance
        images = DynamicImage.objects.all()
        first_image = images.first()
        # Extract video ID from youtube_link
        youtube_link = other_context.youtube_link
        match = re.search(r"\bv=([^&]+)", youtube_link)  # Regular expression to extract video ID
        if match:
            video_id = match.group(1)
            embed_url = f"https://www.youtube.com/embed/{video_id}"  # Construct embed URL
            print(f"embed url is-------->{embed_url}")

            other_context.youtube_link = embed_url  # Update context with embed URL
        else:
            print("Error: Could not extract video ID from YouTube link.")

        print("other_context.youtube_link",other_context.youtube_link)
        print("other_context",other_context)
        return render(request, 'hero.html', {'job_types': job_types, 'job_descriptions': job_descriptions , 'other_context':other_context,'first_image':first_image})

class JobTypeDetailView(View):
    def get(self, request, pk):
        job_types = JobType.objects.all()
        job_type = get_object_or_404(JobType, pk=pk)
        job_descriptions = JobDescription.objects.filter(job_type=job_type)
        other_context = jobAnnouncments.objects.first()  # Fetch the single instance
        images = DynamicImage.objects.all()
        first_image = images.first()
        # Extract video ID from youtube_link
        youtube_link = other_context.youtube_link
        match = re.search(r"\bv=([^&]+)", youtube_link)  # Regular expression to extract video ID
        if match:
            video_id = match.group(1)
            embed_url = f"https://www.youtube.com/embed/{video_id}"  # Construct embed URL
            print(f"embed url is-------->{embed_url}")
            other_context.youtube_link = embed_url  # Update context with embed URL
        else:
            print("Error: Could not extract video ID from YouTube link.")

        print("other_context.youtube_link",other_context.youtube_link)

        print("other_context",other_context)


        return render(request, 'hero.html', {'job_types': job_types,'job_type': job_type, 'job_descriptions': job_descriptions,'other_context':other_context,'first_image':first_image})
    
class JobDescriptionDetailView(DetailView):
    model = JobDescription
    template_name = 'partials/jobdescription_detail_partial.html'

    def render_to_response(self, context, **response_kwargs):
        if self.request.is_ajax():
            return render(self.request, self.template_name, context)
        return super().render_to_response(context, **response_kwargs)
    


    

class JobTypeCreateView(View):
    def get(self, request):
        return render(request, 'jobtype_form.html')

    def post(self, request):
        name = request.POST.get('name')
        if name:
            JobType.objects.create(name=name)
            return redirect('jobtype_list')
        return render(request, 'jobtype_form.html', {'error': 'Name is required'})

class JobTypeUpdateView(View):
    def get(self, request, pk):
        job_type = get_object_or_404(JobType, pk=pk)
        return render(request, 'jobtype_form.html', {'job_type': job_type})

    def post(self, request, pk):
        job_type = get_object_or_404(JobType, pk=pk)
        name = request.POST.get('name')
        if name:
            job_type.name = name
            job_type.save()
            return redirect('jobtype_list')
        return render(request, 'jobtype_form.html', {'job_type': job_type, 'error': 'Name is required'})

class JobTypeDeleteView(View):
    def get(self, request, pk):
        job_type = get_object_or_404(JobType, pk=pk)
        return render(request, 'jobtype_confirm_delete.html', {'job_type': job_type})

    def post(self, request, pk):
        job_type = get_object_or_404(JobType, pk=pk)
        job_type.delete()
        return redirect('jobtype_list')


# JobDescription Views
class JobDescriptionListView(View):
    def get(self, request):
        job_descriptions = JobDescription.objects.all()
        return render(request, 'jobdescription_list.html', {'job_descriptions': job_descriptions})



class JobDescriptionCreateView(View):
    def get(self, request):
        return render(request, 'jobdescription_form.html')

    def post(self, request):
        title = request.POST.get('title')
        company_name = request.POST.get('company_name')
        location = request.POST.get('location')
        job_type_id = request.POST.get('job_type')
        description = request.POST.get('description')
        requirements = request.POST.get('requirements')
        salary = request.POST.get('salary')
        posted_by_id = request.POST.get('posted_by')
        url = request.POST.get('url')

        if all([title, company_name, location, job_type_id, description, requirements, posted_by_id]):
            job_type = get_object_or_404(JobType, pk=job_type_id)
            posted_by = get_object_or_404(settings.AUTH_USER_MODEL, pk=posted_by_id)
            JobDescription.objects.create(
                title=title,
                company_name=company_name,
                location=location,
                job_type=job_type,
                description=description,
                requirements=requirements,
                salary=salary,
                posted_by=posted_by,
                url=url
            )
            return redirect('jobdescription_list')
        return render(request, 'jobdescription_form.html', {'error': 'All fields except salary and url are required'})

class JobDescriptionUpdateView(View):
    def get(self, request, pk):
        job_description = get_object_or_404(JobDescription, pk=pk)
        return render(request, 'jobdescription_form.html', {'job_description': job_description})

    def post(self, request, pk):
        job_description = get_object_or_404(JobDescription, pk=pk)
        title = request.POST.get('title')
        company_name = request.POST.get('company_name')
        location = request.POST.get('location')
        job_type_id = request.POST.get('job_type')
        description = request.POST.get('description')
        requirements = request.POST.get('requirements')
        salary = request.POST.get('salary')
        posted_by_id = request.POST.get('posted_by')
        url = request.POST.get('url')

        if all([title, company_name, location, job_type_id, description, requirements, posted_by_id]):
            job_description.title = title
            job_description.company_name = company_name
            job_description.location = location
            job_description.job_type = get_object_or_404(JobType, pk=job_type_id)
            job_description.description = description
            job_description.requirements = requirements
            job_description.salary = salary
            job_description.posted_by = get_object_or_404(settings.AUTH_USER_MODEL, pk=posted_by_id)
            job_description.url = url
            job_description.save()
            return redirect('jobdescription_list')
        return render(request, 'jobdescription_form.html', {'job_description': job_description, 'error': 'All fields except salary and url are required'})

class JobDescriptionDeleteView(View):
    def get(self, request, pk):
        job_description = get_object_or_404(JobDescription, pk=pk)
        return render(request, 'jobdescription_confirm_delete.html', {'job_description': job_description})

    def post(self, request, pk):
        job_description = get_object_or_404(JobDescription, pk=pk)
        job_description.delete()
        return redirect('jobdescription_list')




####################-------------------------TO add data in db-------------------##########################################
# views.py
from django.shortcuts import render, redirect
from Apps.apps_models.models import CareersBucketBaseUser, JobType, JobDescription, jobAnnouncments,DynamicImage
from django.contrib.auth import get_user_model

User = get_user_model()

def add_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        full_name = request.POST['full_name']
        profile_picture = request.FILES.get('profile_picture')
        phone_number = request.POST['phone_number']
        
        user = User(email=email, full_name=full_name, profile_picture=profile_picture, phone_number=phone_number)
        user.set_password('defaultpassword')  # Set a default password or handle it as needed
        user.save()
        
        return redirect('user_list')  # Assume you have a user list view
    return render(request, 'add_user.html')

def add_job_type(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        
        job_type = JobType(name=name, description=description)
        job_type.save()
        
        return redirect('job_type_list')  # Assume you have a job type list view
    return render(request, 'add_job_type.html')

def add_job_description(request):
    if request.method == 'POST':
        title = request.POST['title']
        company_name = request.POST['company_name']
        location = request.POST['location']
        job_type_id = request.POST['job_type']
        experience_level = request.POST['experience_level']
        description = request.POST['description']
        requirements = request.POST['requirements']
        salary = request.POST['salary']
        posted_by_id = request.POST['posted_by']
        url = request.POST['url']
        company_picture = request.FILES.get('company_picture')
        
        job_type = JobType.objects.get(id=job_type_id)
        posted_by = User.objects.get(id=posted_by_id)
        
        job_description = JobDescription(
            title=title, company_name=company_name, location=location,
            job_type=job_type, experience_level=experience_level,
            description=description, requirements=requirements, salary=salary,
            posted_by=posted_by, url=url, company_picture=company_picture
        )
        job_description.save()
        
        return redirect('job_description_list')  # Assume you have a job description list view
    return render(request, 'add_job_description.html')

def add_job_announcement(request):
    if request.method == 'POST':
        announment_title = request.POST['announment_title']
        description = request.POST['description']
        youtube_link = request.POST['youtube_link']
        
        job_announcement = jobAnnouncments(announment_title=announment_title, description=description, youtube_link=youtube_link)
        job_announcement.save()
        
        return redirect('job_announcement_list')  # Assume you have a job announcement list view
    return render(request, 'add_job_announcement.html')


def add_dynamic_image(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        
        dynamic_image = DynamicImage(image=image)
        dynamic_image.save()
        
        return redirect('dynamic_image_list')
    return render(request, 'add_dynamic_image.html')

def dynamic_image_list(request):
    images = DynamicImage.objects.all()
    return render(request, 'dynamic_image_list.html', {'images': images})

def delete_dynamic_image(request, image_id):
    image = get_object_or_404(DynamicImage, id=image_id)
    image.delete()
    return redirect('dynamic_image_list')