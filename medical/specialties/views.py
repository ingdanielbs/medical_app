from django.shortcuts import render

# Create your views here.
def specialties(request):
    return render(request, "specialties/index.html")