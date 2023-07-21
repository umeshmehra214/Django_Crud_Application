from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from .models import Teacher

# Create your views here.

def HomePage(request):
    return render(request, "insert.html")

def InsertData(request):
    # Data come from HTML to Server
    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    contact = request.POST['contact']

    # creating object of Model Class
    # Inserting data into table(Teacher)
    newuser = Teacher.objects.create(Firstname=fname,Lastname=lname,Email=email,Contact=contact)

    # After Insert render on show.html
    # return render(request, "show.html")   #now it will be change becouse we want redirect our showpage
    return redirect('showpage')


#show Page View
def ShowPage(request):
    # show all the data from table on the ShowPage View
    # select * from tableName
    # we are using all() beacouse we want to fetch all the data of Teacher table
    all_data = Teacher.objects.all()
    return render(request, "show.html", {'key1':all_data})

# Edit Page View
def EditPage(request,pk):
    # Fetching the data of particular ID
    get_data = Teacher.objects.get(id=pk)
    return render(request, "edit.html", {'key2':get_data})

#update Data View 
def UpdateData(request,pk):
    udata = Teacher.objects.get(id=pk)
    udata.Firstname = request.POST['fname']
    udata.Lastname = request.POST['lname']
    udata.Email = request.POST['email']
    udata.Contact = request.POST['contact']
    # Query for update 
    udata.save()
    # render to show Show Page
    return redirect('showpage')

# Delete data view
def DeleteData(request,pk):
    ddata = Teacher.objects.get(id=pk)
    # Query For Delete
    ddata.delete()
    return redirect('showpage')





