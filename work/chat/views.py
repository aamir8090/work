from django.shortcuts import render , redirect
from chat.models import Room , Message
from django.http import HttpResponse , JsonResponse


# Create your views here.


def homed (request) :
    return render( request , 'homed.html' )


def room (request) :
    print( ".............kjnondem..........." )
    username = request.GET.get( 'username' )
    room_details = Room.objects.get( name="room" )
    return render( request , 'room.html' , {
        'username' : username ,
        'room' : room ,
        'room_details' : room_details
    } )


def checkview (request) :
    fm = Room( )
    room = request.POST.get( name='room_name' )
    fm.room = room
    name = request.POST.get( name='username' )
    fm.username = name

    if Room.objects.filter( name=room ).exists( ) :
        return redirect( '/' + room + '/?username=' + name )
    else :
        new_room = Room.objects.create( name=room )
        new_room.save( )
        return redirect( '/' + room + '/?username=' + name )


def send (request) :
    message = request.POST[ 'message' ]
    username = request.POST[ 'username' ]
    room_id = request.POST[ 'room_id' ]

    new_message = Message.objects.create( value=message , user=username , room=room_id )
    new_message.save( )
    return HttpResponse( 'Message sent successfully' )


def getMessages (request , room) :
    room_details = Room.objects.get( name=room )

    messages = Message.objects.filter( room=room_details.id )
    return JsonResponse( {"messages" : list( messages.values( ) )} )
