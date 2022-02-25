from django.contrib import messages
from django.shortcuts import render , redirect
from jazzmin.templatetags.jazzmin import User

from .forms import RegistrationForm , ClientRegistrationModel
from .models import ClientRegistration , RegistrationData , Clientprofile , Post


# Create your views here.
def basehome (request) :
    return render( request , 'home.html' )


def page (request) :
    return render( request , 'page.html' )


def contact (request) :
    context = {
        'form' : RegistrationForm ,

    }
    return render( request , 'contact.html' , context )


def adduser (request) :
    form = RegistrationForm( request.POST )

    if form.is_valid( ) :
        register = RegistrationData( name=form.cleaned_data[ 'name' ] ,
                                     email=form.cleaned_data[ 'email' ] ,
                                     subject=form.cleaned_data[ 'subject' ] ,
                                     message=form.cleaned_data[ 'message' ] ,
                                     )

        register.save( )
        messages.add_message( request , messages.SUCCESS , "Your message has been sent successfully" )

    return redirect( 'contact' )


#
# # Here is the client form submission
# def form(request):
#     print("---------------------")
#     print( "---------------------" )
#     print(request.method)
#     print( "---------------------" )
#     print( "---------------------" )
#     if request.method == "POST":
#         print("------------------------")
#         print("------------------------")
#         print(request.POST.get("email"))
#         fm = RegistrationForm( request.POST )
#         if fm.is_valid( ) :
#             Em = fm.cleaned_data[ 'email' ]
#             JO = fm.cleaned_data[ 'text' ]
#             Lo = fm.cleaned_data[ 'toxt' ]
#             pi = fm.cleaned_data[ 'file' ]
#             Desc = fm.cleaned_data[ 'tuxt' ]
#         reg = ClientRegistration( email=Em , text=JO , toxt=Lo , file=pi , tuxt=Desc )
#         reg.save( )
#         fm = RegistrationForm( )
#     else :
#         fm = RegistrationForm( )
#
#     return render( request , 'form.html' , {'form' : fm , } )


# def form (request) :
#     form = FormRegistration( )
#     context = {'form' : form}
#
#     if request.method == 'POST' :
#         form = FormRegistration( request.POST , request.FILES )
#         if form.is_valid( ) :
#             form.save( )
#         else :
#             return render( request , 'form.html' )
#
#     return render( request , 'form.html' , context )


# def addform (request) :
#     form = FormRegistration( request.POST )
#     if form.is_valid( ) :
#         register = ClientRegistration( Email=form.cleaned_data[ 'Email' ] ,
#                                        JOB=form.cleaned_data[ 'JOB' ] ,
#                                        Location=form.cleaned_data[ 'Location' ] ,
#                                        Type=form.cleaned_data[ 'Type' ] ,
#                                        pics=form.cleaned_data[ 'pics' ] ,
#                                        Description=form.cleaned_data[ 'Description' ] ,
#                                        )
#         register.save( )
#         messages.add_message( request , messages.SUCCESS , "congratulations you have a account" )
#     return redirect( '/' )


def aanmelden (request) :
    return render( request , 'aanmelden.html' )


def overons (request) :
    return render( request , 'overons.html' )


def login (request) :
    return render( request , 'login.html' )


def business (request) :
    if request.method == 'POST' :
        if request.POST.get( 'email' ) :
            fm = ClientRegistration( )
            fm.Email = request.POST.get( 'email' )
            fm.save( )
        if request.POST.get( 'text' ) :
            fm = ClientRegistration( )
            fm.JOB = request.POST.get( 'text' )
            fm.save( )
        if request.POST.get( 'toxt' ) :
            fm = ClientRegistration( )
            fm.Location = request.POST.get( 'toxt' )
            fm.save( )
        if request.POST.get( 'file' ) :
            fm = ClientRegistration( )

            fm.pics = request.POST.get( 'file' )
            fm.save( )
        if request.POST.get( 'tuxt' ) :
            fm = ClientRegistration( )
            fm.Description = request.POST.get( 'tuxt' )
            fm.save( )
        return render( request , '/' )
    else :
        return render( request , 'business.html' )


def index (request) :
    return render( request , 'index.html' )


#
# def profile (request):
#     ft=ClientRegistrationModel()
#     context = {'fom' : ft}
#
#     if request.method == 'POST':
#         ft = ClientRegistrationModel(request.POST)
#         if ft.is_valid():
#             fm = ft.cleaned_data['text']
#             lm = ft.cleaned_data['tixt']
#             Bm = ft.cleaned_data['Company_Name']
#             Cn = ft.cleaned_data['Chamber_of_Commerce_number']
#             regt = Clientprofile( text=fm , tixt=lm , Company_Name=Bm , Chamber_of_Commerce_number=Cn )
#             regt.save( )
#             ft = ClientRegistrationModel( )
#         else :
#             ft = ClientRegistrationModel( )
#
#     return render( request , 'profile.html' , context )
def create (request) :
    if request.method == 'POST' :
        if request.POST.get( 'user' ) and request.POST.get( 'pass' ) :
            post = Post( )
            post.username = request.POST.get( 'user' )
            post.Password = request.POST.get( 'pass' )
            post.save( )
            return render( request , 'create.html' )
    else :
        return render( request , 'create.html' )
    return render( request , 'create.html' )


def form (request) :
    if request.method == 'POST' :
        if request.POST.get( 'email' ) :
            fm = ClientRegistration( )
            fm.Email = request.POST.get( 'email' )
            fm.save( )
        if request.POST.get( 'text' ) :
            fm = ClientRegistration( )
            fm.JOB = request.POST.get( 'text' )
            fm.save( )
        if request.POST.get( 'toxt' ) :
            fm = ClientRegistration( )
            fm.Location = request.POST.get( 'toxt' )
            fm.save( )
        if request.POST.get( 'file' ) :
            fm = ClientRegistration( )

            fm.pics = request.POST.get( 'file' )
            fm.save( )
        if request.POST.get( 'tuxt' ) :
            fm = ClientRegistration( )
            fm.Description = request.POST.get( 'tuxt' )
            fm.save( )
        return render( request , 'profile.html' )
    else :
        return render( request , 'form.html' )


def profile (request) :
    if request.method == 'POST' :
        if request.POST.get( 'Voornaam' ) and request.POST.get('Achternaam') and request.POST.get('Bedrijfsnaam') and \
                request.POST.get('KVK_nummer') and request.POST.get('text') and request.POST.get('tixt') and request.POST.get('toxt') and request.POST.get('tuxt'):
            fm = Clientprofile( )
            fm.First_name = request.POST.get( 'Voornaam' )
            fm.Last_name = request.POST.get( 'Achternaam' )
            fm.Company_Name = request.POST.get( 'Bedrijfsnaam' )
            fm.Chamber_of_Commerce_number = request.POST.get( 'KVK_nummer' )
            fm.number = request.POST.get( 'text' )
            fm.mail = request.POST.get( 'tixt' )
            fm.link = request.POST.get( 'toxt' )
            fm.lonk = request.POST.get( 'tuxt' )
            fm.save( )
        if request.POST.get('intro'):
            fm = Clientprofile()
            fm.Intriduction=request.POST.get('intro')
            fm.save()
        if request.POST.get('Summary'):
            fm = Clientprofile()
            fm.Summary=request.POST.get('Summary')
            fm.save()
        # if request.POST.get('Summary'):
        #     fm = Clientprofile()
        #     fm.Work_experience=request.POST.get('Summary')
        #     fm.save()

        return render( request , 'profile.html' )
    else :
        return render( request , 'profile.html' )
