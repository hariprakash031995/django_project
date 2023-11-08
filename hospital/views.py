from django.shortcuts import render
from django.http.response import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,reverse, loader
from .models import Hospital_Doctors_info

# Create your views here.


def test_helloworld(request):
    print("****************0")
    print(request)
    print(dir(request))
    return HttpResponse("<h1>Hello World This is Django sample endpoint functionality</h1>")


def doctors_info(request):
    doc_info = list(Hospital_Doctors_info.objects.all().values())
    # return HttpResponse(doc_info)
    return render(request, 'doctors_information.html', {'doctors': doc_info})


def doctors_individual_info(request, id) -> render:
    """
    This functionality is used to extract the individual doctors information.
    Params:
        id: Int value
    Return:
        returning the filtered data to the UI
    """
    information = Hospital_Doctors_info.objects.filter(id=id)
    return render(request, 'doctors_information.html', {'doctors': information})


def add_doctors(request):
    if request.method == 'GET':
        template_data = loader.get_template('doctors_add.html')
        return HttpResponse(template_data.render({}, request))
    elif request.method == 'POST':
        data_exists = Hospital_Doctors_info.objects.filter(email = request.POST['email'])
        if not data_exists:
            Hospital_Doctors_info(name=request.POST['name'],
                                  age=request.POST['age'],
                                  department=request.POST['department'],
                                  specialization=request.POST['specialization'],
                                  email=request.POST['email'],
                                  phone_number=request.POST['phone']
                                  ).save()
            return HttpResponseRedirect(reverse('Doctors information'))
        else:
            return HttpResponse(f"{request.POST['name']} doctor is already the existing member")

def delete_doctor(request, email):
    data = Hospital_Doctors_info.objects.filter(email=email)
    if data:
        data.delete()
        # Hospital_Doctors_info.objects.get(email=email).delete()
        return HttpResponse(f'{email} got Deleted Successfully....!')
    return HttpResponse(f'{email} doctor is not exists')
