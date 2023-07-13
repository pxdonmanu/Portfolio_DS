from django.shortcuts import render, redirect
from .models import Projects
from .models import Post
from .models import Projects_en
from .models import Post_en
from .models import TecSkills
from .models import ContactData
from .models import ProSkills
from .models import ProSkills_en
from django.contrib import messages

def index(request):
    if request.method == 'POST':
        
        name = request.POST.get('name')
        email = request.POST.get('email')
        position = request.POST.get('position')
        company = request.POST.get('company')
        message = request.POST.get('message')

        contact_data = ContactData(
            name=name,
            email=email,
            position=position,
            company=company,
            message=message
        )

        contact_data.save()

        messages.success(request, 'Envío de datos exitoso')

        return redirect('index')

    projects = Projects.objects.all()
    posts = Post.objects.all()
    tecskills = TecSkills.objects.all()
    proskills= ProSkills.objects.all()
    return render(request, 'spanish/index.html', {'projects': projects, 'posts': posts, 'tecskills': tecskills, 'proskills': proskills})

def index_en(request):
    if request.method == 'POST':
        
        name = request.POST.get('name')
        email = request.POST.get('email')
        position = request.POST.get('position')
        company = request.POST.get('company')
        message = request.POST.get('message')

        contact_data = ContactData(
            name=name,
            email=email,
            position=position,
            company=company,
            message=message
        )

        contact_data.save()

        messages.success(request, 'Successful data submission')

        return redirect('index')
    
    projects = Projects_en.objects.all()
    posts = Post_en.objects.all()
    tecskills = TecSkills.objects.all()
    proskills= ProSkills_en.objects.all()
    return render(request, 'english/en_index.html', {'projects': projects, 'posts': posts, 'tecskills': tecskills, 'proskills': proskills})