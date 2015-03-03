from django.shortcuts import render
from django.shortcuts import render_to_response,RequestContext
from CarSharing_app.models import clientMessages, route, driver
from CarSharing_app.forms import details_driverForm, routeForm, messagesForm
from django.contrib.auth.decorators import login_required

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect




# Create your views here.
#############################################################################
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


##welcome
#############################################################################
def logout(request):

  return render(request, "registration/logout.html")


##welcome
#############################################################################
def welcome(request):
    text = request.user.username
    return render(request,'welcome.html', {'text':text})




##profile code
#############################################################################
@login_required
def profile(request):
  term = request.user.username
  if not term:
    return render_to_response('profile.html',{'error':True})
  data = driver.objects.filter(driver_id=term)
  data_route = route.objects.filter(driver_id = term)

  if not data:
    return render(request,'profile.html',{'error':True,'msg':'No match found for...'+term})
    
  return render(request,'profile.html',{'term':term,'wdata':data, 'rdata':data_route})
  






#########################################################################################
@login_required
def update_details(request):
  return render(request, 'update_details.html')

####################################################################################################################################
@login_required
def searchUserForm(request):
  print request.session
  return render(request,'searchUserForm.html')

@login_required
def searchUser(request):
    if 'u' in request.GET:
        term = request.GET['u']
        data = driver.objects.filter(driver_id=term)
        data2 = route.objects.filter(driver_id= term)
    if not term:
        return render_to_response('searchUserForm.html',{'error':True})
    
    if not data:
        return render(request,'searchUserForm.html',{'error':True,'msg':'No match found for...'+term})

    return render(request,'searchUserResults.html',{'term':term, 'wdata':data , 'rdata':data2 })


# Displays the search form
####################################################################################################################################
#@login_required
def search_form(request):
    print request.session
    return render(request,'search.html')

# Processes the search request and displays the records
#@login_required
def search(request):
    if 'q' in request.GET:
        term = request.GET['q']
        data = route.objects.filter(from_place=term)
    if 't' in request.GET:
        term = request.GET['t']
        data = route.objects.filter(to_place=term)
    if not term:
        return render_to_response('search.html',{'error':True})
    
    if not data:
        return render(request,'search.html',{'error':True,'msg':'No match found for...'+term})

    return render(request,'search_results.html',{'term':term,'wdata':data})
    




# Processes the search request and displays the records
#@login_required
def search_to(request):
    if 'q' in request.GET:
        term = request.GET['q']
        data = route.objects.filter(from_place=term)
    if 't' in request.GET:
        term = request.GET['t']
        data = route.objects.filter(to_place=term)
    if not term:
        return render_to_response('search.html',{'error':True})
    
    if not data:
        return render(request,'search.html',{'error':True,'msg':'No match found for...'+term})

    return render(request,'search_results_to.html',{'term':term,'wdata':data})
    


#add route data
###############################################################################################################################
# Displays the CarSharing data form
@login_required
def addCarSharingData(request):
    form = routeForm()
    return render(request,
                  'wdata_form.html',
                  {'form':form})

# Stores the CarSharing data record
@login_required
def storeCarSharingData(request):
    if request.method == 'POST':
        form = routeForm(request.POST)
        name = request.user.username

        if(form.is_valid()):
            cd = form.cleaned_data

            wd = route(driver_id = name,
                          journey_name=cd['journey_name'],
                          from_place=cd['from_place'],
                          to_place=cd['to_place'],
                          time=cd['time'],
                          price=cd['price'],
                          seats_free = cd['seats_free'],
                          car_desc= cd['car_desc'],
                          deviate= cd['deviate'])
            wd.save()
            print("Saved CarSharing record...")
        else:
            return render(request,
                          'wdata_form.html',{'form':form})

    print("should be calling status...")
    return render(request, 'status.html',{'term':"Saved data to d/base..."})
    


#add driver data 
##############################################################################################
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
        name = request.user.username
        
        if(form.is_valid()):
            cd = form.cleaned_data
            wd = driver(driver_id= name,
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
    return render(request, 'status.html',{'term':"Profile Updated"})
    



#add message 
##############################################################################################
@login_required
def create_message(request):
    form = messagesForm()
    
    term = request.user.username
    if not term:
      return render_to_response('store_message.html',{'error':True})
    data = clientMessages.objects.filter(messageTo=term).order_by('-time')
    
    return render(request, 'store_message.html', {'form':form, 'term':term, 'mdata':data})
                  
                  
@login_required
def store_message(request):
    if request.method == 'POST':
        form = messagesForm(request.POST)
        name = request.user.username
        
        if(form.is_valid()):
            cd = form.cleaned_data
            wd = clientMessages(messageFrom = name,
                          messageTo = cd['messageTo'],
                          driverMessage = cd['driverMessage'])
            wd.save()
            print(name, "Sent message.")
        else:
            return render(request, 'store_message.html', {'form':form})
    return render(request, 'profile.html')
    


##############################################################################################






