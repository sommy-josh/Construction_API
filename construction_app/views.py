from django.shortcuts import render
from .models import Contact, GetQUote,Home
from rest_framework import generics
from rest_framework.response import Response
from .serializers import HomeSerializer
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import CanViewProductOnly
from rest_framework.decorators import api_view
import resend
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAdminUser
# class HomeView(generics.ListCreateAPIView):
#     authentication_classes=[BasicAuthentication]
#     permission_classes=[IsAuthenticated & CanViewProductOnly]
#     # queryset=Home.objects.all()
#     # serializer_class=HomeViewSerializer
#     def get_products(self,request):
#         products=Home.objects.all()
#         serializer=HomeViewSerializer(products, many=True)
#         return Response(serializer.data)

class ListProductView(generics.ListAPIView):
    permission_classes=[CanViewProductOnly]
    queryset=Home.objects.all().order_by('id')
    pagination_class = PageNumberPagination
    serializer_class=HomeSerializer
    
    filter_backends=[filters.SearchFilter]
    search_fields=['image','text']

    # def get_product_list(self, request):
    #     queryset=Home.objects.all()
    #     product=self.get_queryset()
    #     serializer=HomeSerializer(queryset, many=True)
    #     return Response(serializer.data)
    
    
class CreateProductView(generics.CreateAPIView):
    permission_classes=[IsAdminUser]
    serializer_class=HomeSerializer
    def create(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers=self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED,headers=headers)

class UpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[IsAdminUser]
    queryset=Home.objects.all()
    serializer_class=HomeSerializer
    

@api_view(['POST'])
def send_email(request):
    if request.method == 'POST':
        resend.api_key = "re_cjwn4MRX_5JxsSEjjMtCDY4DegWqgPyky"
        r = resend.Emails.send({
            "from": "onboarding@resend.dev",
            "to": "chisomzzy1@gmail.com",  # Ensure this follows the correct format
            "subject": "Hello World",
            "html": "<p>Congrats on sending your <strong>first email</strong>!</p>"
        })
        # Process the response from ReSend if needed
        return Response({'message': 'Email sent successfully'})

