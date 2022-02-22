from django.shortcuts import render
def index(request):
    print('>>>>>>>>> aiWEB index')
    return render(request,'index.html')