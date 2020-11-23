from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import authentication_classes, permission_classes
from .serializers import *


@api_view(['GET'])
def api_main(request):
    api_urls = {
        'All users': 'users/all',
        'All notes': 'notes/all',
        'User register': 'user/register',
        'User login': 'user/login',
        'User delete': 'user/delete',
        'Note create': 'create/note',
        'Note delete': 'delete/note',
        'Get all notes by a specific user': 'user/<str:fk>/notes'
    }

    return Response(api_urls)


@api_view(['GET'])
def get_all_users(request):
    users = User.objects.filter(is_staff=False, is_superuser=False)
    user_serializer = UserSerializer(users, many=True)

    return Response(user_serializer.data)


@api_view(['GET'])
def get_all_notes(request):
    notes = Note.objects.all()
    note_serializer = NoteSerializer(notes, many=True)

    return Response(note_serializer.data)


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def register_user(request):
    user = User.objects.create_user(username=request.data['username'], password=request.data['password'])

    user.save()

    return Response(200)


@api_view(['GET'])
def get_notes_for_user(request):
    notes = Note.objects.filter(created_by=request.user.id)

    note_serializer = NoteSerializer(notes, many=True)

    return Response(note_serializer.data)


@api_view(['DELETE'])
def delete_user(request):
    try:
        user = User.objects.get(id=request.user.id)
    except:
        return Response(400)

    user.delete()

    return Response(200)


@api_view(['POST'])
def create_note(request):
    note = Note(created_by=request.user, content=request.data['content'])

    note.save()
    serialized = NoteSerializer(note, many=False)

    return Response(serialized.data)


@api_view(['DELETE'])
def delete_note(request, note_id):
    try:
        note = Note.objects.get(id=note_id)
    except:
        return Response(400)

    note.delete()

    return Response(200)


@api_view(['PUT'])
def update_note(request, note_id):
    try:
        note = Note.objects.get(id=note_id)
    except:
        return Response(400)

    note.content = request.data['content']

    note.save()

    return Response(200)
