from django.shortcuts import render, redirect, get_object_or_404
from .forms import UrlForm
from .models import URL
import random
import string

def generate_short_url(length=6):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

def redirect_url(request, short_url):
    url = get_object_or_404(URL, short_url=short_url)
    return redirect(url.original_url)

def home(request):
    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            original_url = form.cleaned_data['original_url']
            short_url = generate_short_url()  # 生成短网址
            url = URL(original_url=original_url, short_url=short_url)
            url.save()
            return render(request, 'shortener/success.html', {'short_code': short_url})  # 确保使用 short_code
    else:
        form = UrlForm()
    return render(request, 'shortener/home.html', {'form': form})
            
# Create your views here.
