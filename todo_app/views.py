from django.shortcuts import render,redirect
from .models import Note
# Create your views here.

def todo(request):
    notes = Note.objects.all()
    return render(request,'todo.html',{'notes' : notes})
def addnote(request):
    title = request.POST['title']
    content = request.POST['content']

    note = Note()
    note.Title = title
    note.Content = content
    note.save()

    return redirect('todo')

def delete(request,noteid):
    note = Note.objects.get(id = noteid)
    note.delete()
    return redirect('todo')




