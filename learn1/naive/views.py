from django.shortcuts import render
from django.shortcuts import HttpResponse

import os
import pickle
import math
import re

# from naive.naivesen import *

# from naive.md import *
# from naive.naivesen import *
# from naive.testing import *

# failed to it by loading files
# so doing it here itself

tot_pos, pos = pickle.load(open('naive\\pos_file','rb'))
tot_neg, neg = pickle.load(open('naive\\neg_file','rb'))

# updating paths
# importing naive classifier

# Create your views here.

def get_features(text):
    features = []
    negated = False
    clean_text = re.sub(r'[^a-zA-Z0-9\']', ' ', text)
    for feature in clean_text.split():
        if not feature in stopwords:
            if feature in ['not','n\'t','no']:
                negated = True
            else:
                if negated == True:
                    feature = 'not_'+feature
                    negated = False
                features.append(feature)
    return features

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
        pos_sent = 0
        neg_sent = 0
        features = set(get_features(text))
        for w in features:
            pos_sent += math.log((pos[w]+1.0)/(2.0*tot_pos))
            neg_sent += math.log((neg[w]+1.0)/(2.0*tot_neg))

        sentiment = str((pos_sent,neg_sent))
        # sentiment = cur
        # t = NaiveBayes()
        # sentiment = str(t.pos)
        # sentiment = t.classify('good')
        # f = open('naivesen.py')
        # sentiment = f.read()
        # f.close()
        # sentiment = os.listdir('.')
        html = "<h1>Output sentiment : %s</h1>" %(sentiment)
        return HttpResponse(html)
    
