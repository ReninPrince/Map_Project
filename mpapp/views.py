from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.template import Context, Template
from mpapp.models import maps
from . import forms
from mpapp.forms import NFormName,MFormName
from pymongo import MongoClient
# from mpapp.spark import *
from mpapp.rates import *
# Create your views here.

client = MongoClient()
db = client.Maps

sch = []
tofind = ['null']
portal = 'http://127.0.0.1:8000'

def Home(request):
    form = NFormName()
    if request.method == 'POST':
        Username=''
        Password=''
        form = NFormName(data=request.POST)
        if form.is_valid():
            print("Validation success!")
            username = form.cleaned_data['Username']
            password = form.cleaned_data['Password']
            #print(username)
            det = db.mpapp_maps.find_one({"Username":username})

            if det == None:
                form = NFormName()
                return render(request, 'mpap/Home.html',{'form':form})
            elif det['Password'] != password:
                form = NFormName()
                return render(request, 'mpap/Home.html',{'form':form})
            elif (det['Username']).isalpha() == True:
                u = ''
                for i in range(len(det['Username'])):
                    u = u + str(ord(det['Username'][i]))
                j = int(u)
                if j > 980:
                    process1 = j
                    predictor1(process1)
                    name = ''
                    place = ''
                    name = op[-2]
                    place = op[-1]


                    return render(request, 'mpap/show.html',{'name':name,'place':place})
            else:
                #print(det['Username'])
                process = det['Username']
                predictor(process)
                name = ''
                place = ''
                name = op[-2]
                place = op[-1]

                form = forms.MFormName(initial={'search': ',' + place})
                # name = ''

                # name = op[-2]

                if request.method == 'GET':
                    form = forms.MFormName(data=request.GET)
                    if form.is_valid():
                        print(form.cleaned_data['search'])
                        sc = (form.cleaned_data['search'])
                        sch.append(sc)
                return render(request, 'mpap/map.html',{'form':form,'place':place})
                # return render(request, 'mpap/show.html',{'name':name,'place':place})


    return render(request, 'mpap/Home.html',{'form':form})




def create(request):
    form = NFormName()
    if request.method == 'POST':
        Username=''
        Password=''
        form = NFormName(data=request.POST)
        if form.is_valid():
            print("Validation success!")
            username = form.cleaned_data['Username']
            password = form.cleaned_data['Password']
            print(username)
            det = db.mpapp_maps.find_one({"Username":username})
            #print(int(username))
            if det == None and (username).isdigit() == False:
                tofind.append(username)
                form.save(commit=True)

                return redirect(portal + '/mpapp/questions')
            elif det == None and (username).isdigit() == True:
                tofind.append(username)
                form.save(commit=True)
                sparktest()
                return redirect(portal + '/mpapp')
            else:
                form = NFormName()

                print(det)

        else:
            print("Not successful")
            form = NFormName()



    return render(request, 'mpap/create.html',{'form':form})


def questions(request):
    form2 = forms.DFormName()
    val = db.mpapp_maps.find_one({"Username":tofind[-1]})
    #det = db.Mapsapp_user.find_one({"first":tofind[-1]})

    un = (val['Username'])
    pw = (val['Password'])
    if request.method == 'POST':
        form2 = forms.DFormName(data=request.POST)
        if form2.is_valid():
            print("Validation success!")
            Holiday = int(form2.cleaned_data['holiday'])
            Languages = int(form2.cleaned_data['languages'])
            Nathis = int(form2.cleaned_data['nathis'])
            Time = int(form2.cleaned_data['time'])
            Soqu = int(form2.cleaned_data['soqu'])
            relationship = int(form2.cleaned_data['Relationship'])
            Preference = int(form2.cleaned_data['preference'])
            Foodie = int(form2.cleaned_data['foodie'])
            Stress = int(form2.cleaned_data['stress'])
            #print(Holiday,Languages,Nathis,Time,Soqu,relationship,Preference,Foodie,Stress)

            rating(Holiday,Languages,Nathis,Time,Soqu,relationship,Preference,Foodie,Stress,un)
            sort_list(Ratings,us,pl)
            return redirect(portal + '/mpapp/')

    return render(request, 'mpap/questions.html',{'un':un,'pw':pw,'form2':form2})

def show(request):
    name = ''
    place = ''
    name = op[-2]
    place = op[-1]


    return render(request, 'mpap/show.html',{'name':name,'place':place})



def map(request):
    place = 'hi'

    # place = op[-1]

    form = forms.MFormName(initial={'search': ',' + place})
    # name = ''

    # name = op[-2]

    if request.method == 'GET':
        form = forms.MFormName(data=request.GET)
        if form.is_valid():
            print(form.cleaned_data['search'])
            sc = (form.cleaned_data['search'])
            sch.append(sc)
    return render(request, 'mpap/map.html',{'form':form,'place':place})
