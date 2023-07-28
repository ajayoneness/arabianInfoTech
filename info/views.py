from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Enrollment


def main(request):

    # if request.method == "POST":
    #     name = request.POST['fname']
    #     email = request.POST['email']
    #     phone = request.POST['mobno']
    #
    #     try:
    #         Enrollment(name=name,email=email,phone=phone).save()
    #         print("Data Saved Successfully")
    #     except:
    #         print("You are already registered")

    return render(request,'index.html')





@csrf_exempt
def enrollment_create(request):
    if request.method == 'POST':
        data = request.POST

        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')

        if not name or not email or not phone:
            return JsonResponse({"error": "Incomplete data. 'name', 'email', and 'phone' fields are required."},
                                status=400)

        # Check if the email or phone already exists in the database
        if Enrollment.objects.filter(email=email).exists():
            return JsonResponse({"error": "Already Enrolled."},
                                status=400)
        if Enrollment.objects.filter(phone=phone).exists():
            return JsonResponse({"error": "Already Enrolled"},
                                status=400)

        enrollment = Enrollment(name=name, email=email, phone=phone)
        enrollment.save()

        return JsonResponse({"message": "Enrolled successfully."},
                            status=201)