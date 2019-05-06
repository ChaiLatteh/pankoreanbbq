from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'homepage/home.html')

def promotion(request):
    return render(request, 'homepage/promotion.html')
