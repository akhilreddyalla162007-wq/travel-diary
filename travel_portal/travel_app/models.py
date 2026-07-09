from django.db import models
from django.contrib.auth.models import User


class Trip(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=100)

    destination = models.CharField(max_length=100)

    description = models.TextField()

    hotel_name = models.CharField(max_length=100)

    places_visited = models.TextField(
        help_text="Enter places separated by commas."
    )

    travel_cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    hotel_cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    food_cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    other_cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    total_cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        editable=False,
        default=0
    )

    image = models.ImageField(
        upload_to='trip_images/',
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):

        self.total_cost = (
            self.travel_cost +
            self.hotel_cost +
            self.food_cost +
            self.other_cost
        )

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title