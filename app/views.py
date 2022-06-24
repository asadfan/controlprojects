from django.shortcuts import render

# Create your views here.
d={'name':'ASAD','fullname':'MD ASAD AHMED','nick':4,'full':13}
def conditional(request):
    #d={'name':'ASAD','fullname':'MD ASAD AHMED','nick':4,'full':13}
    return render(request,'conditional.html',context=d)
def looping(request):
    return render(request,'looping.html',d)