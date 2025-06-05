from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

def get_dummy_contact_info():
    """Trả về thông tin liên hệ mẫu"""
    return {
        'address': 'Thung lũng Silicon, California, Hoa Kỳ',
        'email': 'info@elonmusk.com',
        'phone': '+1 (123) 456-7890',
        'website': 'www.elonmusk.com',
        'social_media': {
            'twitter': 'https://twitter.com/elonmusk',
            'linkedin': 'https://www.linkedin.com',
            'instagram': 'https://www.instagram.com/elonmusk',
            'facebook': 'https://www.facebook.com',
        }
    }

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        try:
            contact = Contact(name=name, email=email, subject=subject, message=message)
            contact.save()
            messages.success(request, 'Tin nhắn của bạn đã được gửi thành công!')
        except Exception as e:
            messages.error(request, f'Có lỗi xảy ra: {str(e)}')
        
        return redirect('contact:contact')
    
    contact_info = get_dummy_contact_info()
    
    return render(request, 'contact/contact.html', {
        'title': 'Elon Musk - Liên hệ',
        'contact_info': contact_info,
    })
