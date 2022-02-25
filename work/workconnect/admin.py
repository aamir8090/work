from django.contrib import admin
from .models import RegistrationData , ClientRegistration , Clientprofile , Post , businessclient


@admin.register( RegistrationData )
class RegistAdmin( admin.ModelAdmin ) :
    list_display = ('id' , 'name' , 'email' , 'subject' , 'message')


@admin.register( ClientRegistration )
class ClientAdmin( admin.ModelAdmin ) :
    list_display = ('id' , 'Email' , 'JOB' , 'Location' , 'Type' , 'pics' , 'Description')


@admin.register( Clientprofile )
class ClientAdmin( admin.ModelAdmin ) :
    list_display = ('First_name' , 'Last_name' , 'Company_Name' ,
                    'Chamber_of_Commerce_number' , ' number' , ' mail' , ' link' , ' lonk' , 'Intriduction' ,
                    'Work_experience' ,
                    'Summary' , 'Education' , 'pics')


@admin.register( Post )
class PostAdmin( admin.ModelAdmin ) :
    list_display = ('id' , 'username' , 'Password')


@admin.register( businessclient )
class ClientAdmin( admin.ModelAdmin ) :
    list_display = ('email' , 'name' , 'contect' ,
                    'tellphone' , 'stad' , 'straat' ,
                    'postcode' , 'website' , 'KVK')
