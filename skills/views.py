from django.shortcuts import render

# Create your views here.

def skills(request):
    return render(request, 'skills/skills.html', {
        'title': 'Elon Musk - Kỹ năng',
    })
