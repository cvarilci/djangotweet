from django.shortcuts import render,redirect
from . import models
from django.urls import reverse,reverse_lazy
from tweety_app.forms import AddTweetForm,AddTweetModelForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView


# Create your views here.
def listtweet(request):
    all_tweets=models.Tweet.objects.all()
    tweet_dictionary={"tweets":all_tweets}
    return render(request,"tweety_app/listtweet.html",context=tweet_dictionary)

@login_required(login_url="/login")
def addtweet(request):
    if request.POST:
        
        message = request.POST["message"]
        models.Tweet.objects.create(username=request.user,message=message)
        """tweet=models.Tweet(nickname,message)
        tweet.save()"""
        return redirect(reverse('tweety_app:listtweet'))
    else:
        return render(request,"tweety_app/addtweet.html")
    
def addtweetbyform(request):
    if request.method == 'POST':
        form = AddTweetForm(request.POST)
        if form.is_valid():
           nickname=form.cleaned_data["nickname_input"]
           message=form.cleaned_data["message_input"]
           models.Tweet.objects.create(nickname=nickname,message=message)
           return redirect(reverse('tweety_app:listtweet'))
        else:
           print("error in form!")
           return render(request,'tweety_app/addtweetbyform.html',context={"form":form})
    else:
        form = AddTweetForm()
        return render(request,'tweety_app/addtweetbyform.html',context={"form":form})

def addtweetbymodelform(request):
    if request.method == 'POST':
        form = AddTweetModelForm(request.POST)
        if form.is_valid():
           nickname=form.cleaned_data["nickname"]
           message=form.cleaned_data["message"]
           models.Tweet.objects.create(nickname=nickname,message=message)
           return redirect(reverse('tweety_app:listtweet'))
        else:
           print("error in form!")
           return render(request,'tweety_app/addtweetbymodelform.html',context={"form":form})
    else:
        form = AddTweetModelForm()
        return render(request,'tweety_app/addtweetbymodelform.html',context={"form":form})
    
@login_required
def deletetweet(request,id):
    tweet = models.Tweet.objects.get(pk=id)
    if request.user == tweet.username:
        models.Tweet.objects.filter(id=id).delete()
        return redirect('tweety_app:listtweet')
    
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
    

