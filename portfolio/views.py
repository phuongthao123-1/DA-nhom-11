from django.shortcuts import render, get_object_or_404
from .models import PortfolioItem

def portfolio(request):
    items = PortfolioItem.objects.all()
    return render(request, 'portfolio/portfolio.html', {
        'title': 'Elon Musk - Portfolio',
        'items': items
    })

def portfolio_detail(request, item_id):
    item = get_object_or_404(PortfolioItem, pk=item_id)
    return render(request, 'portfolio/portfolio_detail.html', {
        'title': f'Elon Musk - {item.title}',
        'item': item
    })
