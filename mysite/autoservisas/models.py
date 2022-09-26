from django.db import models
from django.urls import reverse


# Create your models here.

class AutomobilioModelis(models.Model):
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=80)

    class Meta:
        verbose_name = "Automobilio modelis"
        verbose_name_plural = "Automobilio modeliai"

    def __str__(self):
        return f"{self.brand} {self.model}"

    def get_absolute_urls(self):
        return reverse("model-detail", args=[str(self.id)])


class Automobilis(models.Model):
    plate = models.CharField(max_length=8)
    vehicle_id = models.ForeignKey(AutomobilioModelis, on_delete=models.SET_NULL, null=True, related_name="auto")
    vin = models.CharField(max_length=30)
    client = models.CharField(max_length=30)
    image = models.ImageField(upload_to="covers", null=True)

    class Meta:
        verbose_name = "Automobilis"
        verbose_name_plural = "Automobiliai"

    def __str__(self):
        return f"{self.vehicle_id} {self.plate}"

    def get_absolute_urls(self):
        return reverse("car-detail", args=[str(self.id)])

    def display_owner(self):
        return f"{self.client}"

    def display_plate(self):
        return f"{self.plate}"

    def display_vin(self):
        return f"{self.vin}"

    def display_model(self):
        return f"{self.vehicle_id.brand} {self.vehicle_id.model}"


class Uzsakymas(models.Model):
    order_date = models.DateField("Data")
    vehicle_id = models.ForeignKey("Automobilis", on_delete=models.SET_NULL, null=True, related_name="orders")
    amount = models.FloatField("Viso")

    ORDER_STATUS = (("s", "Sukurtas"),
                    ("p", "Priimtas"),
                    ("v", "Vykdomas"),
                    ("i", "Ivykdytas"))

    status = models.CharField(max_length=1, choices=ORDER_STATUS, blank=True, default="s")

    class Meta:
        verbose_name = "Užsakymas"
        verbose_name_plural = "Užsakymai"

    def __str__(self):
        return f"{self.id} {self.order_date} {self.vehicle_id} {self.status}"

    def display_model(self):
        return f"{self.vehicle_id.vehicle_id.brand} {self.vehicle_id.vehicle_id.model} {self.vehicle_id.plate}"

    # {self.amount} {self.get_status(self.status)}
    @staticmethod
    def get_status(status_name):
        for or_status in Uzsakymas.ORDER_STATUS:
            if or_status[0] == status_name:
                return or_status[1]

    def get_absolute_urls(self):
        return reverse("order-detail", args=[str(self.id)])


class Paslauga(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField(default=0)

    class Meta:
        verbose_name = "Paslaug"
        verbose_name_plural = "Paslaugos"

    def __str__(self):
        return f"{self.id} {self.name}"

    def get_absolute_urls(self):
        return reverse("service-detail", args=[str(self.id)])


class UzsakymoEilutes(models.Model):
    order_id = models.ForeignKey(Uzsakymas, on_delete=models.SET_NULL, null=True, related_name="lines")
    service_id = models.ForeignKey(Paslauga, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()
    # price = models.FloatField()

    class Meta:
        verbose_name = "Užsakymo eilutė"
        verbose_name_plural = "Užsakymo eilutės"

    def __str__(self):
        return f"{self.id} {self.order_id.id} {self.service_id.name} {self.service_id.price}"

    # def get_absolute_urls(self):
    #     return reverse("order_line-detail", args=[str(self.id)])


