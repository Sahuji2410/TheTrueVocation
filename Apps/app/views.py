# views.py
from rest_framework import generics
from rest_framework.views import APIView
from Apps.apps_models.models import JobType, JobDescription
from .serializers import JobTypeSerializer, JobDescriptionSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework import serializers, status

from rest_framework.response import Response

class JobTypeView(APIView):
    @swagger_auto_schema(
        responses={
            200: JobTypeSerializer(many=True),
            500: "Internal Server Error"
        }
    )
    def get(self, request):
        try:
            job_type = JobType.objects.all()
            serializer = JobTypeSerializer(job_type, many=True)
            return Response(
                {
                    "status": "success",
                    'responseMessage': 'Job Types retrieved successfully',
                    "responseData": serializer.data
                },
                status=status.HTTP_200_OK
            )
        except Exception as e:
            print(f"JobTypeView get error ----{e}")
            return Response(
                {
                    'responseCode': status.HTTP_500_INTERNAL_SERVER_ERROR,
                    'responseMessage': "Something went wrong",
                    'responseData': None,
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    @swagger_auto_schema(
        request_body=JobTypeSerializer,
        responses={
            201: JobTypeSerializer,
            400: "Bad Request",
            500: "Internal Server Error"
        }
    )
    def post(self, request):
        try:
            serializer = JobTypeSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        "status": "success",
                        'responseMessage': 'Job Type created successfully',
                        "responseData": serializer.data
                    },
                    status=status.HTTP_201_CREATED
                )
            return Response(
                {
                    'responseCode': status.HTTP_400_BAD_REQUEST,
                    'responseMessage': "Bad Request",
                    'responseData': serializer.errors,
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            print(f"JobTypeView post error ----{e}")
            return Response(
                {
                    'responseCode': status.HTTP_500_INTERNAL_SERVER_ERROR,
                    'responseMessage': "Something went wrong",
                    'responseData': None,
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        

# views.py (continued)
class JobTypeDetailView(APIView):
    @swagger_auto_schema(
        responses={
            200: JobTypeSerializer,
            404: "Not Found",
            500: "Internal Server Error"
        }
    )
    def get(self, request, pk):
        try:
            job_type = JobType.objects.get(pk=pk)
            serializer = JobTypeSerializer(job_type)
            return Response(
                {
                    "status": "success",
                    'responseMessage': 'Job Type retrieved successfully',
                    "responseData": serializer.data
                },
                status=status.HTTP_200_OK
            )
        except JobType.DoesNotExist:
            return Response(
                {
                    'responseCode': status.HTTP_404_NOT_FOUND,
                    'responseMessage': "Job Type not found",
                    'responseData': None,
                },
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            print(f"JobTypeDetailView get error ----{e}")
            return Response(
                {
                    'responseCode': status.HTTP_500_INTERNAL_SERVER_ERROR,
                    'responseMessage': "Something went wrong",
                    'responseData': None,
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    @swagger_auto_schema(
        request_body=JobTypeSerializer,
        responses={
            200: JobTypeSerializer,
            400: "Bad Request",
            404: "Not Found",
            500: "Internal Server Error"
        }
    )
    def put(self, request, pk):
        try:
            job_type = JobType.objects.get(pk=pk)
            serializer = JobTypeSerializer(job_type, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        "status": "success",
                        'responseMessage': 'Job Type updated successfully',
                        "responseData": serializer.data
                    },
                    status=status.HTTP_200_OK
                )
            return Response(
                {
                    'responseCode': status.HTTP_400_BAD_REQUEST,
                    'responseMessage': "Bad Request",
                    'responseData': serializer.errors,
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        except JobType.DoesNotExist:
            return Response(
                {
                    'responseCode': status.HTTP_404_NOT_FOUND,
                    'responseMessage': "Job Type not found",
                    'responseData': None,
                },
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            print(f"JobTypeDetailView put error ----{e}")
            return Response(
                {
                    'responseCode': status.HTTP_500_INTERNAL_SERVER_ERROR,
                    'responseMessage': "Something went wrong",
                    'responseData': None,
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    @swagger_auto_schema(
        responses={
            204: "No Content",
            404: "Not Found",
            500: "Internal Server Error"
        }
    )
    def delete(self, request, pk):
        try:
            job_type = JobType.objects.get(pk=pk)
            job_type.delete()
            return Response(
                {
                    "status": "success",
                    'responseMessage': 'Job Type deleted successfully',
                    "responseData": None
                },
                status=status.HTTP_204_NO_CONTENT
            )
        except JobType.DoesNotExist:
            return Response(
                {
                    'responseCode': status.HTTP_404_NOT_FOUND,
                    'responseMessage': "Job Type not found",
                    'responseData': None,
                },
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            print(f"JobTypeDetailView delete error ----{e}")
            return Response(
                {
                    'responseCode': status.HTTP_500_INTERNAL_SERVER_ERROR,
                    'responseMessage': "Something went wrong",
                    'responseData': None,
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        

class JobDescriptionView(APIView):
    @swagger_auto_schema(
        responses={
            200: JobDescriptionSerializer(many=True),
            500: "Internal Server Error"
        }
    )
    def get(self, request):
        try:
            job_descriptions = JobDescription.objects.all()
            serializer = JobDescriptionSerializer(job_descriptions, many=True)
            return Response(
                {
                    "status": "success",
                    'responseMessage': 'Job Descriptions retrieved successfully',
                    "responseData": serializer.data
                },
                status=status.HTTP_200_OK
            )
        except Exception as e:
            print(f"JobDescriptionView get error ----{e}")
            return Response(
                {
                    'responseCode': status.HTTP_500_INTERNAL_SERVER_ERROR,
                    'responseMessage': "Something went wrong",
                    'responseData': None,
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    @swagger_auto_schema(
        request_body=JobDescriptionSerializer,
        responses={
            201: JobDescriptionSerializer,
            400: "Bad Request",
            500: "Internal Server Error"
        }
    )
    def post(self, request):
        try:
            serializer = JobDescriptionSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        "status": "success",
                        'responseMessage': 'Job Description created successfully',
                        "responseData": serializer.data
                    },
                    status=status.HTTP_201_CREATED
                )
            return Response(
                {
                    'responseCode': status.HTTP_400_BAD_REQUEST,
                    'responseMessage': "Bad Request",
                    'responseData': serializer.errors,
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            print(f"JobDescriptionView post error ----{e}")
            return Response(
                {
                    'responseCode': status.HTTP_500_INTERNAL_SERVER_ERROR,
                    'responseMessage': "Something went wrong",
                    'responseData': None,
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        
# views.py (continued)
class JobDescriptionDetailView(APIView):
    @swagger_auto_schema(
        responses={
            200: JobDescriptionSerializer,
            404: "Not Found",
            500: "Internal Server Error"
        }
    )
    def get(self, request, pk):
        try:
            job_description = JobDescription.objects.get(pk=pk)
            serializer = JobDescriptionSerializer(job_description)
            return Response(
                {
                    "status": "success",
                    'responseMessage': 'Job Description retrieved successfully',
                    "responseData": serializer.data
                },
                status=status.HTTP_200_OK
            )
        except JobDescription.DoesNotExist:
            return Response(
                {
                    'responseCode': status.HTTP_404_NOT_FOUND,
                    'responseMessage': "Job Description not found",
                    'responseData': None,
                },
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            print(f"JobDescriptionDetailView get error ----{e}")
            return Response(
                {
                    'responseCode': status.HTTP_500_INTERNAL_SERVER_ERROR,
                    'responseMessage': "Something went wrong",
                    'responseData': None,
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    @swagger_auto_schema(
        request_body=JobDescriptionSerializer,
        responses={
            200: JobDescriptionSerializer,
            400: "Bad Request",
            404: "Not Found",
            500: "Internal Server Error"
        }
    )
    def put(self, request, pk):
        try:
            job_description = JobDescription.objects.get(pk=pk)
            serializer = JobDescriptionSerializer(job_description, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        "status": "success",
                        'responseMessage': 'Job Description updated successfully',
                        "responseData": serializer.data
                    },
                    status=status.HTTP_200_OK
                )
            return Response(
                {
                    'responseCode': status.HTTP_400_BAD_REQUEST,
                    'responseMessage': "Bad Request",
                    'responseData': serializer.errors,
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        except JobDescription.DoesNotExist:
            return Response(
                {
                    'responseCode': status.HTTP_404_NOT_FOUND,
                    'responseMessage': "Job Description not found",
                    'responseData': None,
                },
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            print(f"JobDescriptionDetailView put error ----{e}")
            return Response(
                {
                    'responseCode': status.HTTP_500_INTERNAL_SERVER_ERROR,
                    'responseMessage': "Something went wrong",
                    'responseData': None,
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    @swagger_auto_schema(
        responses={
            204: "No Content",
            404: "Not Found",
            500: "Internal Server Error"
        }
    )
    def delete(self, request, pk):
        try:
            job_description = JobDescription.objects.get(pk=pk)
            job_description.delete()
            return Response(
                {
                    "status": "success",
                    'responseMessage': 'Job Description deleted successfully',
                    "responseData": None
                },
                status=status.HTTP_204_NO_CONTENT
            )
        except JobDescription.DoesNotExist:
            return Response(
                {
                    'responseCode': status.HTTP_404_NOT_FOUND,
                    'responseMessage': "Job Description not found",
                    'responseData': None,
                },
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            print(f"JobDescriptionDetailView delete error ----{e}")
            return Response(
                {
                    'responseCode': status.HTTP_500_INTERNAL_SERVER_ERROR,
                    'responseMessage': "Something went wrong",
                    'responseData': None,
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )   
