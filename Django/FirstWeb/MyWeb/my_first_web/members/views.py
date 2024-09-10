from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Member
from .forms import MemberForm

def members_old(request):
    return HttpResponse("Hello world!")

def members(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def all_members(request):
  mymembers = Member.objects.all().values()
  context = {
    'mymem': mymembers,
  }
  return render(request,"all_members.html",context)

def details(request, id):
  mymember = Member.objects.get(id=id)
  return render(request,"details.html", {"mymember":mymember})

def add_member(request):
    if request.method == 'POST':
      form = MemberForm(request.POST)
      if form.is_valid():
        # first_name = form.cleaned_data['firstname']
        # last_name = form.cleaned_data['lastname']
        # print(f"Hi, {first_name} {last_name}!")
        form.save()
        return redirect("all")

    return render(request, 'add_member.html', {'form': MemberForm()})