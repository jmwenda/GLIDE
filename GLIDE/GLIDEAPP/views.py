from django.shortcuts import render_to_response, get_object_or_404
from GLIDEAPP.models import GLIDE
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def index(request):
	glide_list = GLIDE.objects.all()
        paginator = Paginator(glide_list, 20)
        page = int(request.GET.get('page', '1')) 
	try:
		glides  = paginator.page(page)
        except PageNotAnInteger:
		glides = paginator.page(1)
        except EmptyPage:
                glides = paginator.page(paginator.num_pages)
	return render_to_response("index.html",{"glides": glides})

