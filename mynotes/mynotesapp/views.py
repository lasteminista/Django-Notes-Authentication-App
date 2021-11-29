from django.shortcuts import render
from mynotesapp.models import Note
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
	context ={
	'notes': Note.objects.filter(author=request.user)
	}
	return render(request, 'home.html',context)
