from django.shortcuts import render,redirect
from .models import todomodel
# Create your views here.
def todo(request):
  todos = todomodel.objects.all()
  if request.method == "POST":
    title = request.POST.get('title')
    datetime = request.POST.get('datetime')
    datetime = f'{datetime[0:10:1]} {datetime[11:]}'
    if not todomodel.objects.filter(title = title ).exists():
      print(f'{title} -- {datetime}')
      task = todomodel.objects.create(title=title,datetime=datetime)
      print(task)
      task.save()
  return render(request,'page.html',{'todos':todos})
def removetask(request,todo_id):
  print(todo_id)
  getelem = todomodel.objects.filter(id=todo_id)
  print(getelem)
  getelem.delete()
  print('remove perfome')
  return redirect('todo')