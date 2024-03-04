
from django.db.models import  Count, Avg
from django.shortcuts import render, redirect
from django.db.models import Count
from django.db.models import Q
import datetime


# Create your views here.
from Remote_User.models import ClientRegister_Model,search_ratio_model,adSherlock_model,clickfraud_model


def serviceproviderlogin(request):
    if request.method  == "POST":
        admin = request.POST.get('username')
        password = request.POST.get('password')
        if admin == "SProvider" and password =="SProvider":
            adSherlock_model.objects.all().delete()
            search_ratio_model.objects.all().delete()
            clickfraud_model.objects.all().delete()

            return redirect('View_Remote_Users')

    return render(request,'SProvider/serviceproviderlogin.html')


def viewtreandingquestions(request,chart_type):
    dd = {}
    pos,neu,neg =0,0,0
    poss=None
    topic = adSherlock_model.objects.values('ratings').annotate(dcount=Count('ratings')).order_by('-dcount')
    for t in topic:
        topics=t['ratings']
        pos_count=adSherlock_model.objects.filter(topics=topics).values('names').annotate(topiccount=Count('ratings'))
        poss=pos_count
        for pp in pos_count:
            senti= pp['names']
            if senti == 'positive':
                pos= pp['topiccount']
            elif senti == 'negative':
                neg = pp['topiccount']
            elif senti == 'nutral':
                neu = pp['topiccount']
        dd[topics]=[pos,neg,neu]
    return render(request,'SProvider/viewtreandingquestions.html',{'object':topic,'dd':dd,'chart_type':chart_type})

def Search_App_Details(request): # Search
   ratio=""
   if request.method == "POST":
        kword = request.POST.get('keyword')
        print(kword)
        obj = adSherlock_model.objects.all().filter(Q(names=kword))
        obj1 = adSherlock_model.objects.all()
        count =obj.count();
        count1 = obj1.count();

        ratio=(count/count1)*100
        if ratio != 0:
            search_ratio_model.objects.create(names=kword, ratio=ratio)
        return render(request, 'SProvider/Search_App_Details.html', {'list_objects': obj,'ratio': ratio})
   return render(request, 'SProvider/Search_App_Details.html')

def View_Mesured_MobileApps_Details(request):
    sname = ''
    Eno = ''
    gender = ''
    cname = ''
    dname = ''
    collegename =''
    obj1 = adSherlock_model.objects.values('names',
                                           'App_Desc',
                                           'Mobile_OS',
                                           'App_Developer',
                                           'App_Developed_Country',
                                           'App_Uses',
                                           'Allowed_Clicks',
                                           'User_Name',
                                           'System_IP_Address',
                                           'Clicked_DT',
                                           'No_Of_Time_Clicked',
                                           'Like1',
                                           'Rate'
                                                    )

    clickfraud_model.objects.all().delete()
    for t in obj1:
        names = t['names']
        App_Desc= t['App_Desc']
        Mobile_OS= t['Mobile_OS']
        App_Developer= t['App_Developer']
        App_Developed_Country= t['App_Developed_Country']
        App_Uses= t['App_Uses']
        Allowed_Clicks= t['Allowed_Clicks']
        User_Name= t['User_Name']
        System_IP_Address= t['System_IP_Address']
        Clicked_DT= t['Clicked_DT']
        No_Of_Time_Clicked= t['No_Of_Time_Clicked']
        Like1= t['Like1']
        Rate= t['Rate']


        allowedclick =int( t['Allowed_Clicks'])
        NoOfTimeClicked =int( t['No_Of_Time_Clicked'])


        if(allowedclick<NoOfTimeClicked):

         clickfraud_model.objects.create(names=names,App_Desc=App_Desc,Mobile_OS=Mobile_OS,App_Developer=App_Developer,App_Developed_Country=App_Developed_Country,App_Uses=App_Uses,
            Allowed_Clicks=Allowed_Clicks,
            User_Name=User_Name,
            System_IP_Address=System_IP_Address,
            Clicked_DT=Clicked_DT,
            No_Of_Time_Clicked=No_Of_Time_Clicked)

    obj = clickfraud_model.objects.all()

    return render(request, 'SProvider/View_Mesured_MobileApps_Details.html', {'objs': obj})

def View_Remote_Users(request):
    obj=ClientRegister_Model.objects.all()
    return render(request,'SProvider/View_Remote_Users.html',{'objects':obj})

def ViewTrendings(request):
    topic = adSherlock_model.objects.values('topics').annotate(dcount=Count('topics')).order_by('-dcount')
    return  render(request,'SProvider/ViewTrendings.html',{'objects':topic})

def negativechart(request,chart_type):
    dd = {}
    pos, neu, neg = 0, 0, 0
    poss = None
    topic =adSherlock_model.objects.values('ratings').annotate(dcount=Count('ratings')).order_by('-dcount')
    for t in topic:
        topics = t['ratings']
        pos_count = adSherlock_model.objects.filter(topics=topics).values('names').annotate(topiccount=Count('ratings'))
        poss = pos_count
        for pp in pos_count:
            senti = pp['names']
            if senti == 'positive':
                pos = pp['topiccount']
            elif senti == 'negative':
                neg = pp['topiccount']
            elif senti == 'nutral':
                neu = pp['topiccount']
        dd[topics] = [pos, neg, neu]
    return render(request,'SProvider/negativechart.html',{'object':topic,'dd':dd,'chart_type':chart_type})


def charts(request,chart_type):
    chart1 = search_ratio_model.objects.values('names').annotate(dcount=Avg('ratio'))
    return render(request,"SProvider/charts.html", {'form':chart1, 'chart_type':chart_type})

def charts1(request,chart_type):
    chart1 = clickfraud_model.objects.values('names').annotate(dcount=Avg('No_Of_Time_Clicked'))
    return render(request,"SProvider/charts1.html", {'form':chart1, 'chart_type':chart_type})

def View_Online_Mobile_Apps_Details(request):
    obj =adSherlock_model.objects.all()
    return render(request, 'SProvider/View_Online_Mobile_Apps_Details.html', {'list_objects': obj})

def likeschart(request,like_chart):
    charts =adSherlock_model.objects.values('names').annotate(dcount=Avg('Like1'))
    return render(request,"SProvider/likeschart.html", {'form':charts, 'like_chart':like_chart})

def View_Click_Frauds(request):
    obj = clickfraud_model.objects.all()
    return render(request, 'SProvider/View_Click_Frauds.html', {'list_objects': obj})

def View_Search_Ratio(request):
    obj = search_ratio_model.objects.all()
    return render(request, 'SProvider/View_Search_Ratio.html', {'list_objects': obj})







