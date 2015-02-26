from django.shortcuts import render
from django.shortcuts import render_to_response,RequestContext
from CarSharing_app.models import CarSharingData, driver
from CarSharing_app.forms import CarSharingDataForm, details_driverForm
from django.contrib.auth.decorators import login_required

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect




# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/search-form/")
    else:
        form=UserCreationForm()

    return render(request,
                  "registration/register.html",
                  {'form':form})





def welcome(request):
    return render(request,'welcome.html')






@login_required
def profile(request):
  return render(request, 'search_PersonalDetails.html')
  
  
  
  
  
  
@login_required
def information(request):
  return render(request, 'information.html')



@login_required
def update_details(request):
  return render(request, 'update_details.html')





# Displays the search form
#@login_required
def search_form(request):
    print request.session
    return render(request,'search.html')

# Processes the search request and displays the records
#@login_required
def search(request):
    if 'q' in request.GET:
        term = request.GET['q']
    if not term:
        return render_to_response('search.html',{'error':True})
    data = CarSharingData.objects.filter(fromPlace=term)
    if not data:
        return render(request,'search.html',{'error':True,'msg':'No match found for...'+term})

    return render(request,'search_results.html',{'term':term,'wdata':data})

# Displays the CarSharing data form
@login_required
def addCarSharingData(request):
    form = CarSharingDataForm()
    return render(request,
                  'wdata_form.html',
                  {'form':form})

# Stores the CarSharing data record
@login_required
def storeCarSharingData(request):
    if request.method == 'POST':
        form = CarSharingDataForm(request.POST)

        if(form.is_valid()):
            cd = form.cleaned_data

            wd = CarSharingData(fromPlace=cd['fromPlace'],
                             toPlace=cd['toPlace'],
                             time=cd['time'],
                             reg=cd['reg'],
                             seats_free = cd['seats_free'])
            wd.save()
            print("Saved CarSharing record...")
        else:
            return render(request,
                          'wdata_form.html',{'form':form})

    print("should be calling status...")
    return render(request, 'status.html',{'term':"Saved data to d/base..."})
    
    
    ##############################################################################################
      ##############################################################################################
@login_required
def searchPersonal_form(request):
  print request.session
  return render(request,'search_PersonalDetails.html')
  
  
@login_required
def searchPersonal(request):
  if 'q' in request.GET:
    term = request.GET['q']
  if not term:
      return render_to_response('profile.html',{'error':True})
  data = driver.objects.filter(driver_id=term)
 
  if not data:
      return render(request,'profile.html',{'error':True,'msg':'No match found for...'+term})
      
  #return render(request,'search_resultsPersonalDetails.html',{'term':term,'wdata':data})
  return render(request,'profile.html',{'term':term,'wdata':data})



@login_required
def addDriverData(request):
    form = details_driverForm()
    return render(request,
                  'add_PersonalDetails.html',
                  {'form':form})
    
# Stores the info of driver
@login_required
def storeDriverData(request):
    if request.method == 'POST':
        form = details_driverForm(request.POST)

        if(form.is_valid()):
            cd = form.cleaned_data

            wd = driver(driver_id=cd['driver_id'],
                                firstname=cd['firstname'],
                                lastname=cd['lastname'],
                                email = cd['email'],
                                age=cd['age'],
                                phone =cd['phone'],
                                gender = cd['gender'],
                                home =cd['home'],
                                car_reg =cd['car_reg'],
                                car_desc =cd['car_desc'],
                                seats_free = cd['seats_free'])
            wd.save()
            print("Saved CarSharing record...")
        else:
            return render(request,
                          'add_PersonalDetails.html',{'form':form})

    print("should be calling status...")
    return render(request, 'status.html',{'term':"Saved data to d/base..."})
    
