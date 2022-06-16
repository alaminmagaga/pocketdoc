from django.shortcuts import render
from django.contrib.auth import get_user_model
from chats.models import ChatModel



User = get_user_model()

#homepage
def homepage(request):
    return render(request, 'home.html')

#chat Homepage
def index(request):
    users = User.objects.exclude(username=request.user.username)
    return render(request, 'index.html', context={'users': users})




def options(request):
    return render(request,'options.html')

def appointment(request):
    return render(request,'appointment.html')

def chatPage(request, username):
    user_obj = User.objects.get(username=username)
    print(user_obj)
    users = User.objects.exclude(username=request.user.username)

    if request.user.id > user_obj.id:
        thread_name = f'chat_{request.user.id}-{user_obj.id}'
    else:
        thread_name = f'chat_{user_obj.id}-{request.user.id}'
    message_objs = ChatModel.objects.filter(thread_name=thread_name)
    return render(request, 'main_chat.html', context={'user': user_obj, 'users': users, 'messages': message_objs})
