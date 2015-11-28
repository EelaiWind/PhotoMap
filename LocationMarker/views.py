from django.shortcuts import render,  HttpResponseRedirect
from .models import Marker
from django.core.urlresolvers import reverse

# Create your views here.
def index (request):
	context = { 'markerList':Marker.objects.all()};
	return render(request,'LocationMarker/index.html', context);

def post (request):
	Marker.objects.all().delete();
	titleList = request.POST.getlist('title');
	latList = request.POST.getlist('lat');
	lngList = request.POST.getlist('lng');
	for i in range(len(titleList)):
		Marker.objects.create(title=titleList[i], latitude=latList[i], longitude=lngList[i]);

	context = {'pack':Marker.objects.all()};
	return  HttpResponseRedirect(reverse('LocationMarker:index'));