from django.shortcuts import render, get_object_or_404
from .models import Uzsakymas, Paslauga, Automobilis, AutomobilioModelis, UzsakymoEilutes
from django.http import HttpResponse
from django.views import generic
from django.core.paginator import Paginator
from django.db.models import Q


# Create your views here.

def index(request):
    num_of_services = Paslauga.objects.count()
    done_orders = Uzsakymas.objects.filter(status="i").count()
    total_vehicles = Automobilis.objects.count()
    context = {"data": [num_of_services, done_orders, total_vehicles]}
    return render(request, "index.html", context=context)


def allcars(request):
    paginator = Paginator(Automobilis.objects.all(), 2)
    page_number = request.GET.get("page")
    paged_cars = paginator.get_page(page_number)
    context = {"cars": paged_cars}
    return render(request, "allcars.html", context=context)


def car_orders(request, id):
    order_status = {"s": "Sukurtas",
                    "p": "Priimtas",
                    "v": "Vykdomas",
                    "i": "Ivykdytas"}
    vehicle = get_object_or_404(Automobilis, pk=id)

    context = {"order_status": order_status,
               "vehicle": vehicle}
    return render(request, "orders.html", context=context)


def order_lines(request, id):
    order = get_object_or_404(Uzsakymas, pk=id)
    return render(request, "order_lines.html", {"order": order})


def search(request):
    find_data = request.GET.get("query")
    data = Automobilis.objects.filter(
        Q(plate__icontains=find_data) | Q(vin__icontains=find_data) | Q(vehicle_id__model__icontains=find_data) | Q(
            client__icontains=find_data) | Q(vehicle_id__brand__icontains=find_data))
    return render(request, "search.html", {"searchtxt": find_data, "vehicle_data": data})


class OrdersListView(generic.ListView):
    model = Uzsakymas
    template_name = "allorders.html"
    paginate_by = 2


class OrderDetailView(generic.DetailView):
    model = Uzsakymas
    template_name = "order_details.html"
