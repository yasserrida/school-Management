from django.db import models


class student(models.Model):
    gender_types = (
        ('H', 'Homme'),
        ('F', 'Femme')
    )

    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    gender = models.CharField(max_length=6, choices=gender_types)
    birthday = models.DateTimeField()
    note = models.IntegerField()

    def store(self, firstName, lastName, gender, birthday, note):
        return self.objects.create(firstName=firstName, lastName=lastName,
                                      gender=gender, birthday=birthday, note=note)

    def all(self):
        return self.objects.all()

    def filterById(self, id):
        return self.objects.filter(_id=id)

    def filterByFirstName(self, term):
        return self.objects.filter(firstName__startswith=str(term))

    def filterByLastName(self, term):
        return self.objects.filter(lastName__startswith=str(term))

    def getById(self, id):
        return self.objects.get(_id=id)

    def delete(self, id):
        item = self.getById(self, id)
        item.delete()
