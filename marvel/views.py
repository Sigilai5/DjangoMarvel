from django.shortcuts import render,redirect
from .models import Image
from .forms import NewImageForm

# Create your views here.
def home(request):

    images = Image.objects.all()

    return render(request,'home.html',{'images':images})

def hero(request,id):

    images = Image.objects.filter(category_id=id)


    return render(request, 'hero.html', locals())

def upload(request):

    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.save()
            return redirect('hom')

    else:
        form = NewImageForm()

    return render(request, 'upload.html', locals())