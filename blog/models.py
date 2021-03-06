from django.db import models
from django.core.urlresolvers import reverse
from django import forms
from django.forms import ModelForm
from django.http import HttpResponse
from django.utils import simplejson
import random, string
 
GRADE = (
    ('Incredible', 'Incredible'),
    ('Great', 'Great'),
    ('Good', 'Good'),
    ('Average', 'Average'),
    ('Poor', 'Poor'),
)

class word(models.Model):
    word = models.CharField(max_length=255)
    count = models.IntegerField()    
    definition = models.CharField(max_length=255) 
    synonyms = models.CharField(max_length=255)
    connotation = models.CharField(max_length=255)

class essayData(models.Model):
    # essayId = models.IntegerField(default= lambda: random.randint(10000000,19999999))
    text = models.CharField(max_length=255555)
    paragraph_text = models.CharField(max_length=255555)    
    word_list = models.CharField(max_length=255)  
    words_count = models.CharField(max_length=255)
    top_words = models.CharField(max_length=255)
    top_words_count = models.CharField(max_length=255)

class sentenceComplexityData(models.Model):
    # essayId = models.IntegerField(default= lambda: random.randint(10000000,19999999))
    avg_len = models.IntegerField()
    complexity_variance = models.IntegerField()
    max_length = models.IntegerField()
    min_length = models.IntegerField()
    complexity_grade = models.CharField(max_length=10, choices=GRADE)
    # class Meta:
    #     top_words_array = topWords

#     class Meta:
#         ordering = ['-text']

# class textForm(ModelForm):
#     class Meta:
#         model = essayData

# class textForm(models.Model):
#     text = models.CharField(max_length=25500, blank=True, null=True)
#     words = models.CharField(max_length=25500, blank=True, null=True)

