from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.



#post_list
def index(request):

	return render(request, 'blog/post_list.html', {})
	#return HttpResponse("Blog hey")