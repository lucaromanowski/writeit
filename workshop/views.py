from django.shortcuts import render


def list_of_projects(request):
	return render(request, 'workshop/list_of_projects.html', {})