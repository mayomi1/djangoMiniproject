from django.shortcuts import render
from .models import Addbook, Add_lecture_note
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def index(request):

	return render(request, 'index.html', {})

def hardware_view(request):

	hardware_list = Addbook.objects.filter(category__iexact = 'hardware')
	allbook = Addbook.objects.all().order_by('-id')


	paginator = Paginator(hardware_list, 12) # Show 25 contacts per page

	page = request.GET.get('page')
	try:
		hardware = paginator.page(page)
	except PageNotAnInteger:
	# If page is not an integer, deliver first page.
		hardware = paginator.page(1)
	except EmptyPage:
	# If page is out of range (e.g. 9999), deliver last page of results.
		hardware = paginator.page(paginator.num_pages)



	context = {
		'hardware':hardware,
		'allbook': allbook,



		}
	return render(request, 'hardware.html', context)

def programming_view(request):
	programming_list = Addbook.objects.filter(category__iexact = 'programming')
	allbook = Addbook.objects.all().order_by('-id')

	paginator = Paginator(programming_list, 12) # Show 25 contacts per page

	page = request.GET.get('page')
	try:
		programming = paginator.page(page)
	except PageNotAnInteger:
	# If page is not an integer, deliver first page.
		programming = paginator.page(1)
	except EmptyPage:
	# If page is out of range (e.g. 9999), deliver last page of results.
		programming = paginator.page(paginator.num_pages)

	context = {
		'programming':programming,
		'allbook': allbook,

	}
	return render(request, 'programming.html', context)





def networking_view(request):
	network_list = Addbook.objects.filter(category__iexact = 'networking')
	allbook = Addbook.objects.all().order_by('-id')

	paginator = Paginator(network_list, 12) # Show  contacts per page

	page = request.GET.get('page')
	try:
		network = paginator.page(page)
	except PageNotAnInteger:
	# If page is not an integer, deliver first page.
		network = paginator.page(1)
	except EmptyPage:
	# If page is out of range (e.g. 9999), deliver last page of results.
		network = paginator.page(paginator.num_pages)

	context = {
		'network':network,
		'allbook': allbook,

	}
	return render(request, 'networking.html', context)


		


def software_view(request):
	software_list = Addbook.objects.filter(category__iexact = 'software')
	allbook = Addbook.objects.all().order_by('-id')

	paginator = Paginator(software_list, 12) # Show  contacts per page

	page = request.GET.get('page')
	try:
		software = paginator.page(page)
	except PageNotAnInteger:
	# If page is not an integer, deliver first page.
		software = paginator.page(1)
	except EmptyPage:
	# If page is out of range (e.g. 9999), deliver last page of results.
		software = paginator.page(paginator.num_pages)

	context = {
		'software':software,
		'allbook': allbook,

	}
	return render(request, 'software.html', context)

def other_view(request):
	others_list = Addbook.objects.filter(category__iexact = 'others')
	allbook = Addbook.objects.all().order_by('-id')

	paginator = Paginator(others_list, 12) # Show 25 contacts per page

	page = request.GET.get('page')
	try:
		others = paginator.page(page)
	except PageNotAnInteger:
	# If page is not an integer, deliver first page.
		others = paginator.page(1)
	except EmptyPage:
	# If page is out of range (e.g. 9999), deliver last page of results.
		others = paginator.page(paginator.num_pages)

	context = {
		'others':others,
		'allbook': allbook,

	}
	return render(request, 'others.html', context)


def lecture_note_view(request):
	lecture_list = Addbook.objects.filter(category__iexact = 'lecture_notes')
	allbook = Addbook.objects.all().order_by('-id')

	paginator = Paginator(lecture_list, 12) # Show 25 contacts per page

	page = request.GET.get('page')
	try:
		lecture = paginator.page(page)
	except PageNotAnInteger:
	# If page is not an integer, deliver first page.
		lecture = paginator.page(1)
	except EmptyPage:
	# If page is out of range (e.g. 9999), deliver last page of results.
		lecture = paginator.page(paginator.num_pages)

	context = {
		'lecture':lecture,
		'allbook': allbook,

	}
	return render(request, 'lecture_note.html', context)

def software_view_detail(request, softslug):
	#software = Addbook.objects.get(id  = Id )
	software = Addbook.objects.get(slug = softslug)
	allbook = Addbook.objects.all().order_by('-id')
	context = {
		'software': software,
		'allbook': allbook,
		#'image': image,
	}

	return render(request, 'software_detail.html', context )

def hardware_view_detail(request, hardslug ):
	hardware = Addbook.objects.get(slug  = hardslug )
	context = {
		'hardware': hardware
	}

	return render(request, 'hardware_detail.html', context )

def network_view_detail(request, networkslug):
	network = Addbook.objects.get(slug  = networkslug )
	context = {
		'network': network
	}

	return render(request, 'network_detail.html', context )


def programming_view_detail(request, programslug ):
	programming = Addbook.objects.get(slug  = programslug)
	context = {
		'programming': programming
	}

	return render(request, 'program_detail.html', context )

def lectures_view_detail(request, lectureslug ):
	lecture = Addbook.objects.get(slug  = lectureslug )
	context = {
		'lecture': lecture
	}

	return render(request, 'lecture_detail.html', context )

def others_view_detail(request, otherslug):
	others = Addbook.objects.get(slug  = otherslug)
	context = {
		'others': others
	}

	return render(request, 'others_detail.html', context )


