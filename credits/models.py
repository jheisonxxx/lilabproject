from django.db import models


class Client(models.Model):
    dni = models.IntegerField(unique=True, blank = False)
    name = models.CharField(max_length=200, blank = False)
    GOOD = 2
    AVERAGE = 1
    BAD = 0
    PUNCTUATION_CHOICES = [
        (GOOD, 'Good'),
        (AVERAGE, 'Average'),
        (BAD, 'Bad'),
    ]
    punctuation= models.CharField(
        max_length=2,
        choices=PUNCTUATION_CHOICES,
        default=GOOD,
    )
    debt_sbs = models.DecimalField(decimal_places=3, max_digits=10, blank = False)

    def __str__(self):
        return str(self.dni) + " - " + self.name 


class Solicitude(models.Model):
    PENDING = 0
    APPROVED = 1
    DISAPPROVED = 2
    STATE_CHOICES = [
        (PENDING, 'Approved'),
        (APPROVED, 'Disapproved'),
        (DISAPPROVED, 'Pending'),
    ]
    state = models.CharField(
        max_length=2,
        choices=STATE_CHOICES,
        default=PENDING,
    )
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    credit_indicator = models.IntegerField(blank = False)
    amount = models.DecimalField(decimal_places=3, max_digits=10, blank = False)


    def __str__(self):
        return self.state