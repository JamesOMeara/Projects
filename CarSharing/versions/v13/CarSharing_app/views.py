from django.shortcuts import render
from django.shortcuts import render_to_response,RequestContext
from CarSharing_app.models import clientMessages, route, driver, drivers_car
from CarSharing_app.forms import details_ClientForm, routeForm, messagesForm, drivers_carForm
from django.contrib.auth.decorators import login_required

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User



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
    data = route.objects.all()
    return render(request,'welcome.html', {'text':text, 'wdata':data})




##profile code
#############################################################################
@login_required
def profile(request):
  term = request.user.username
  if not term:
    return render_to_response('profile.html',{'error':True})
  data = driver.objects.filter(client_id=term)
  data_route = route.objects.filter(driver_id = term)
  car_det = drivers_car.objects.filter(id_client = term)

  if not data:
    return render(request,'profile.html',{'error':True,'msg':'No match found for...'+term})
    
  return render(request,'profile.html',{'term':term,'wdata':data, 'rdata':data_route, 'cdata':car_det})
  






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
        data = driver.objects.filter(client_id=term)
        data2 = route.objects.filter(driver_id= term)
        data3 = drivers_car.objects.filter(id_client= term)
    if not term:
        return render_to_response('searchUserForm.html',{'error':True})
    
    if not data:
        return render(request,'searchUserForm.html',{'error':True,'msg':'No match found for...'+term})

    return render(request,'searchUserResults.html',{'term':term, 'wdata':data , 'rdata':data2 , 'cdata':data3})


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
    if 'n' in request.GET:
        term = request.GET['n']
        data = route.objects.filter(journey_name=term)
        
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
            return HttpResponseRedirect('/profile/') # Redirect after POST
        else:
            return render(request,
                          'wdata_form.html',{'form':form})
    else:
      print("should be calling status...")
      return render(request, 'status.html',{'term':"Saved data to d/base..."})
    


#add driver data 
##############################################################################################
@login_required
def addDriverData(request):
    form = details_ClientForm()
    return render(request,
                  'add_PersonalDetails.html',
                  {'form':form})
    

# Stores the info of driver
@login_required
def storeDriverData(request):
    if request.method == 'POST':
        form = details_ClientForm(request.POST)
        name = request.user.username
        
        if(form.is_valid()):
            cd = form.cleaned_data
            wd = driver(client_id= name,
                                firstname=cd['firstname'],
                                lastname=cd['lastname'],
                                email = cd['email'],
                                age=cd['age'],
                                phone =cd['phone'],
                                gender = cd['gender'],
                                client_is = cd['client_is'],
                                home =cd['home'])
            wd.save()
            print("Saved CarSharing record...")
            return HttpResponseRedirect('/profile/') # Redirect after POST
        else:
            return render(request,
                          'add_PersonalDetails.html',{'form':form})

    print("should be calling status...")
    return render(request, 'status.html',{'term':"Profile Updated"})



@login_required
def addDriverCarData(request):
    form = drivers_carForm()
    return render(request,
                  'update_car_details.html',
                  {'form':form})    

# Stores the info of driver
@login_required
def storeDriverCarData(request):
    if request.method == 'POST':
        form = drivers_carForm(request.POST)
        name = request.user.username
        
        if(form.is_valid()):
            cd = form.cleaned_data
            wd = drivers_car(id_client= name,
                                car_reg=cd['car_reg'],
                                car_desc=cd['car_desc'],
                                seats_free=cd['seats_free'])
            wd.save()
            print("Saved Car record...")
            return HttpResponseRedirect('/profile/') # Redirect after POST
        else:
            return render(request,
                          'update_car_details.html',{'form':form})

    print("should be calling status...")
    return render(request, 'status.html',{'term':"Profile Updated"})
    
    
    
    
    
#methods dealing with 
          #######   messaging
##############################################################################################
@login_required
def create_message(request):
    form = messagesForm()
    
    term = request.user.username
    if not term:
      return render(request, 'store_message.html', {'form':form, 'term':term, 'mdata':data,'error':True,'msg':'No match found for...'})
      
    data = clientMessages.objects.filter(messageTo=term).order_by('-time')

    return render(request, 'store_message.html', {'form':form, 'term':term, 'mdata':data})
                  
                  
@login_required
def store_message(request):
    if request.method == 'POST':
        form = messagesForm(request.POST)
        name = request.user.username
        
        
        if(form.is_valid()):
          cd = form.cleaned_data
          if User.objects.filter(username= cd['messageTo'] ).count():
            wd = clientMessages(messageFrom = name,
                          messageTo = cd['messageTo'],
                          driverMessage = cd['driverMessage'])
            wd.save()
            print(name, "Sent message.")
            return HttpResponseRedirect('/messanger/') # Redirect after POST
          else:
            print(name + "attempted to send message but no user exists...")
            return HttpResponseRedirect('/message_error/') # Redirect after POST if no user exists to send message to
        else:
          print(name + " form not filled...")
          return HttpResponseRedirect('/messanger/') # Redirect after POST, if form isnt valid
    print ("failed to save message render profile") 
    return render(request, 'profile.html')
    

@login_required
def message_error(request):
    form = messagesForm()
    
    term = request.user.username
    if not term:
      return render_to_response('store_message.html', {'form':form, 'term':term, 'mdata':data},{'error':True})
      
    data = clientMessages.objects.filter(messageTo=term).order_by('-time')

    return render(request, 'store_message.html', {'form':form, 'term':term, 'mdata':data, 'error':True})
##############################################################################################





def About(request):
  return render(request, "about.html")



################################################################################################


@login_required
def info_journey(request):

  if 'q' in request.GET:
    term = request.GET['q']
    data = route.objects.filter(id=term)
    
    
    term2 = route.objects.values_list("driver_id")
    print ( term2 )

    
    data2 = driver.objects.filter(client_id=term2)
    print(data2)
    
    return render(request, 'route_info.html', {'term':term, 'wdata':data, 'cdata':data2})
  else:
    return render(request, 'search.html')














