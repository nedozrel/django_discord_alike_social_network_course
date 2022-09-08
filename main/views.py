from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Room, Topic
from .forms import RoomForm


def login_page(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		try:
			user = User.objects.get(username=username)
		except:
			messages.error(request, 'User does not exist')

	context = {}
	return render(request, 'main/login_register.html', context)


def root(request):
	is_searching = False
	if request.GET.get('q'):
		q = request.GET.get('q')
		is_searching = True
	else:
		q = ''
	rooms = Room.objects.filter(
		Q(topic__name__icontains=q) |
		Q(name__icontains=q) |
		Q(description__icontains=q)
	)
	topics = Topic.objects.all()
	rooms_count = rooms.count()
	context = {
		'rooms': rooms,
		'topics': topics,
		'room_count': rooms_count,
		'is_searching': is_searching
	}
	return render(request, 'main/index.html', context)


def room(request, pk):
	room = Room.objects.get(id=pk)
	context = {'room': room}
	return render(request, 'main/room.html', context)


def create_room(request):
	form = RoomForm()
	if request.method == 'POST':
		form = RoomForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	context = {"form": form}
	return render(request, 'main/room_form.html', context)


def update_room(request, pk):
	room = Room.objects.get(id=pk)
	form = RoomForm(instance=room)
	if request.method == 'POST':
		form = RoomForm(request.POST, instance=room)
		if form.is_valid():
			form.save()
			return redirect('home')
	context = {'form': form}
	return render(request, 'main/room_form.html', context)


def delete_room(request, pk):
	room = Room.objects.get(id=pk)
	if request.method == 'POST':
		room.delete()
		return redirect('home')
	return render(request, 'main/delete.html', {'obj': room})
