from django import forms
from .models import RegistrationData , ClientRegistration , Clientprofile
from django.forms import ModelForm , Textarea


class RegistrationForm( forms.Form ) :
    name = forms.CharField( max_length=100 ,
                            widget=forms.TextInput( attrs={
                                'class' : 'form-control' ,
                                'placeholder' : 'Enter Name'
                            } ) )
    email = forms.EmailField(
        widget=forms.TextInput( attrs={
            'class' : 'form-control' ,
            'placeholder' : 'Enter Email'
        } )
    )
    subject = forms.CharField( max_length=100 ,
                               widget=forms.TextInput( attrs={
                                   'class' : 'form-control' ,
                                   'placeholder' : 'Enter Subject'
                               } ) )

    message = forms.CharField(
        widget=forms.Textarea( attrs={
            'class' : 'form-control' ,
            'placeholder' : 'Enter Message' ,
            'rows' : 1 ,
            'cols' : 40 ,
            'style' : 'height: 8em;'

        } ) )


class RegistrationModel( forms.ModelForm ) :
    class Meta :
        model = RegistrationData

        fields = [
            'id' ,
            'name' ,
            'email' ,
            'subject' ,
            'message'
        ]

        widgets = {
            'name' : forms.TextInput( attrs={
                'class' : 'form-control' ,
                'placeholder' : 'Enter Name'
            } ) ,
            'email' : forms.TextInput( attrs={
                'class' : 'form-control' ,
                'placeholder' : 'Enter Email'
            } ) ,
            'subject' : forms.TextInput( attrs={
                'class' : 'form-control' ,
                'placeholder' : 'Enter Subject'
            } ) ,
            'message' : forms.Textarea( attrs={
                'class' : 'form-control' ,
                'placeholder' : 'Enter Message' ,

            } ) ,

        }


class ClientRegistrationModel( forms.ModelForm ) :
    class Meta :
        model = Clientprofile

        fields = [ 'First_name' , 'Last_name' , 'Company_Name' ,
                   'Chamber_of_Commerce_number' , 'Intriduction' , 'Work_experience' ,
                   'Summary' , 'Education' , 'pics' ]
