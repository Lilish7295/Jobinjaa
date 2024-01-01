from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Transaction
from .serializers import TransictionSerializer
from rest_framework import generics 


class TractionView(generics.ListCreateAPIView):
    queryset = Transaction.objects.order_by("transaction_date")
    serializer_class = TransictionSerializer

