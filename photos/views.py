from django.shortcuts import render,redirect
from .models import Category , Photo
# Create your views here.

def gallery(request):
    cat = request.GET.get('category')
    if cat == None :
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name__contains = cat )
    
    category = Category.objects.all()
    context = {'category':category,'photos':photos}
    return render(request,'gallery.html',context)


def viewPhoto(request , pk):
    photos = Photo.objects.get(id=pk)
    context = {'photos':photos}
    return render(request,'photo.html',context)

def addPhoto(request):
    category = Category.objects.all()
    if request.method == "POST":
        data = request.POST
        image = request.FILES.get('image')
        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['new_category'] != '':
            category , created = Category.objects.get_or_create(name = data['new_category'])
        else:
            category = None
        photo = Photo.objects.create(
            category = category,
            description = data['description'],
            image = image,
        )
        return redirect('/')
    context = {'category':category}
    return render(request,'add.html',context)