from django.shortcuts import render

# Create your views here.
def operations(request):
    d={'a':200,'b':300,'c':438}
    return render(request,'operations.html',d)