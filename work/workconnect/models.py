from django.db import models
from django.conf import settings


class RegistrationData( models.Model ) :
    name = models.CharField( max_length=100 )
    email = models.EmailField( )
    subject = models.CharField( max_length=100 )
    message = models.TextField( )

    def __str__ (self) :
        return self.name


class ClientRegistration( models.Model ) :
    Email = models.EmailField( max_length=20, null=True )
    JOB = models.TextField( max_length=200 ,null=True )
    Location = models.TextField( max_length=100 ,null=True)
    Type = models.TextField( max_length=70 ,null=True )
    pics = models.ImageField( upload_to='images/' , blank=False,null=True  )
    Description = models.TextField( max_length=100,null=True  )

    def __str__ (self) :
        return self.Email


class Clientprofile( models.Model ) :
    First_name = models.TextField( max_length=20 )
    Last_name = models.TextField( max_length=200 )
    Company_Name = models.TextField( max_length=100 )
    Chamber_of_Commerce_number = models.TextField( max_length=70 )
    number = models.IntegerField( null=True)
    mail = models.EmailField( max_length=70 ,null=True)
    link = models.URLField( max_length=70, null=True )
    lonk = models.URLField( max_length=70 ,null=True )
    Intriduction = models.TextField( max_length=70 )
    Work_experience = models.TextField( max_length=70 )
    Summary = models.TextField( max_length=70 )
    Education = models.TextField( max_length=70 )
    pics = models.ImageField( upload_to='images/' , blank=False )

    def __str__ (self) :
        return self.First_name


class Post( models.Model ) :
    username = models.TextField( max_length=200 )
    Password = models.EmailField( max_length=20 )

    def __str__ (self) :
        return self.username



class businessclient( models.Model ) :
    email = models.EmailField( max_length=20 ,null=True)
    name = models.TextField( max_length=200 )
    contect = models.TextField( max_length=100 )
    tellphone = models.IntegerField(  )
    stad = models.TextField( max_length=70 )
    straat = models.TextField( max_length=70 )
    postcode = models.TextField( max_length=70 )
    website = models.URLField( max_length=70 )
    KVK = models.TextField( max_length=200 , blank=False )

    def __str__ (self) :
        return self.email