from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from .models import Post

# Create your views here.



#post_list
def index(request):

	posts = Post.objects.order_by('-published_date')

	return render(request, 'blog/post_list.html', {'posts': posts})


	

	return render(request, 'blog/post_list.html', {})
	#return HttpResponse("Blog hey")