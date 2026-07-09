from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Trip
from decimal import Decimal
from django.contrib.auth.decorators import login_required
from .models import Trip
from django.shortcuts import get_object_or_404



def home(request):
    return render(request, 'home.html')


def login_page(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request,
                            username=username,
                            password=password)

        if user is not None:

            login(request, user)

            return redirect('home')

        else:

            messages.error(request,
                           "Invalid Username or Password")

    return render(request, 'login.html')


def register_page(request):

    if request.method == "POST":

        fullname = request.POST.get("fullname")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:

            messages.error(request,
                           "Passwords do not match")

            return redirect('register')

        if User.objects.filter(username=username).exists():

            messages.error(request,
                           "Username already exists")

            return redirect('register')

        if User.objects.filter(email=email).exists():

            messages.error(request,
                           "Email already exists")

            return redirect('register')

        User.objects.create_user(
            username=username,
            first_name=fullname,
            email=email,
            password=password1
        )

        messages.success(request,
                         "Account Created Successfully")

        return redirect('login')

    return render(request, 'register.html')


from decimal import Decimal

from decimal import Decimal

@login_required
def add_trip(request):

    if request.method == "POST":

        print("========== FORM SUBMITTED ==========")
        print(request.POST)

        try:

            trip = Trip(
                user=request.user,
                title=request.POST.get("title"),
                destination=request.POST.get("destination"),
                description=request.POST.get("description"),
                hotel_name=request.POST.get("hotel_name"),
                places_visited=request.POST.get("places_visited"),
                travel_cost=Decimal(request.POST.get("travel_cost") or 0),
                hotel_cost=Decimal(request.POST.get("hotel_cost") or 0),
                food_cost=Decimal(request.POST.get("food_cost") or 0),
                other_cost=Decimal(request.POST.get("other_cost") or 0),
                image=request.FILES.get("image")
            )

            trip.save()

            print("Trip Saved Successfully")
            print("Trip ID:", trip.id)

            messages.success(request, "Trip Saved Successfully!")

            return redirect("home")

        except Exception as e:

            print("ERROR OCCURRED")
            print(e)

    return render(request, "add_trip.html")


def logout_page(request):

    logout(request)

    return redirect('home')
def explore(request):

    trips = Trip.objects.all().order_by('-created_at')

    return render(request,
                  'explore.html',
                  {'trips': trips})

@login_required
def my_trips(request):

    trips = Trip.objects.filter(user=request.user).order_by('-created_at')

    return render(request, 'my_trips.html', {
        'trips': trips
    })
@login_required
def trip_details(request, id):

    trip = Trip.objects.get(id=id)

    return render(request, 'trip_details.html', {
        'trip': trip
    })

@login_required
def delete_trip(request, id):

    Trip.objects.get(id=id).delete()

    messages.success(request, "Trip Deleted Successfully.")

    return redirect('my_trips')

from decimal import Decimal
from django.shortcuts import get_object_or_404

@login_required
def edit_trip(request, id):

    trip = get_object_or_404(
        Trip,
        id=id,
        user=request.user
    )

    if request.method == "POST":

        trip.title = request.POST.get("title")

        trip.destination = request.POST.get("destination")

        trip.hotel_name = request.POST.get("hotel_name")

        trip.description = request.POST.get("description")

        trip.places_visited = request.POST.get("places_visited")

        trip.travel_cost = Decimal(
            request.POST.get("travel_cost") or 0
        )

        trip.hotel_cost = Decimal(
            request.POST.get("hotel_cost") or 0
        )

        trip.food_cost = Decimal(
            request.POST.get("food_cost") or 0
        )

        trip.other_cost = Decimal(
            request.POST.get("other_cost") or 0
        )

        if request.FILES.get("image"):

            trip.image = request.FILES.get("image")

        trip.save()

        messages.success(
            request,
            "Trip Updated Successfully!"
        )

        return redirect("my_trips")

    return render(
        request,
        "edit_trip.html",
        {
            "trip": trip
        }
    )


@login_required
def trip_details(request, id):

    trip = get_object_or_404(Trip, id=id)

    return render(request, 'trip_details.html', {
        'trip': trip
    })

from django.shortcuts import get_object_or_404

def view_trip(request, id):

    trip = get_object_or_404(Trip, id=id)

    return render(request, "trip_view.html", {
        "trip": trip
    })
from django.db.models import Q

from django.db.models import Q
from .models import Trip

def home(request):

    search = request.GET.get("search", "").strip()

    print(request.GET)
    print("Search =", search)

    trips = Trip.objects.all().order_by("-created_at")

    if search:

        trips = trips.filter(
            Q(title__icontains=search) |
            Q(destination__icontains=search) |
            Q(hotel_name__icontains=search) |
            Q(description__icontains=search) |
            Q(places_visited__icontains=search)
        )

    print("Trips Found =", trips.count())

    return render(request, "home.html", {
        "trips": trips,
        "search": search,
    })