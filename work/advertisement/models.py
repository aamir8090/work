from django.db import models


# Create your models here.
class advrt(models.Model):
    CATEGORY = {
        ('3KM', '3KM'),
        ('4KM', '4KM'),
        ('5KM', '5KM'),
        ('6KM', '6KM'),
        ('7KM', '7KM'),
        ('8KM', '8KM'),
        ('9KM', '9KM'),

    }
    OPTIONS = {
        ('Agricultural & Environmental', 'Agricultural & Environmental'),
        ('General', 'General'),
        ('Architecture & Design', 'Architecture & Design'),
        ('Automotive', 'Automotive'),
        ('Banks', 'Banks'),
        ('Betting & Gaming', 'Betting & Gaming'),
        ('Security', 'Security'),
        ('Build', 'Build'),
        ('Chemistry, Oil & Energy', 'Chemistry, Oil & Energy'),
        ('Defence', 'Defence'),
        ('Animals & Care', 'Animals & Care'),
        ('Engineering', 'Engineering'),
        ('Facility management', 'Facility management'),
        ('Fashion & Styling', 'Fashion & Styling'),
        ('Finance', 'Finance'),
        ('9KM', 'Township'),
        ('Healthcare & Pharmaceuticals', 'Healthcare & Pharmaceuticals'),
        ('Trade, Wholesale and Retail', 'Trade, Wholesale and Retail'),
        ('Catering industry', 'Catering industry'),
        ('IT', 'IT'),
        ('Industry and Production', 'Industry and Production'),
        ('Legal', 'Legal'),
        ('Art and Culture and Entrainment', 'Art and Culture and Entrainment'),
        ('Life sciences', 'Life sciences'),
        ('Aviation and Maritime', 'Aviation and Maritime'),
        ('Marketing and Communication', 'Marketing and Communication'),
        ('Media and Journalism', 'Media and Journalism'),
        ('Education', 'Education'),
        ('Research', 'Research'),
        ('Government and Semi-Government', 'Government and Semi-Government'),
        ('Law enforcement', 'Law enforcement'),
        ('Travel and Recreation', 'Travel and Recreation'),
        ('Travel and Recreation', 'Travel and Recreation'),
        ('Technic', 'Technic'),
        ('Transport and Logistics', 'Transport and Logistics'),
        ('Employment agencies and Recruitment and Selection', 'Employment agencies and Recruitment and Selection'),
        ('Real Estate and Brokerage', 'Real Estate and Brokerage'),
        ('Nutrition and Exercise', 'Nutrition and Exercise'),
        ('Business services', 'Business services'),

    }

    description = models.TextField(max_length=1000)
    distance = models.TextField(max_length=40, choices=CATEGORY, blank=True, null=True)
    Categories = models.TextField(max_length=4000, choices=OPTIONS)
    till_date = models.DateTimeField()
    remark = models.CharField(max_length=50000)
    address = models.TextField(max_length=500, null=True)

