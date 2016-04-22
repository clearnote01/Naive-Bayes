from django.shortcuts import render
from django.shortcuts import HttpResponse
from naivesen import *

# Create your views here.

def home(request):
    html = "naive_home.html"
    return render(request, html)

def about(request):
    html = "about.html"
    return render(request, html)
    
def demo(request):
    html = "demo.html"
    return render(request, html)
    
def compute(request):
    if request.method == 'POST':
        text = request.POST.get('textbox')
        t = NaiveBayes()
        sentiment = t.classify(text)
        html = "<h1>Output sentiment : %s</h1>" %(sentiment)
        return HttpResponse(html)
    
