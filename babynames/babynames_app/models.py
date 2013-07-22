from django.db import models

# Create your models here.



class LastName(models.Model):
	lastName = models.CharField(max_length = 20)

	def _unicode_(self):
		return self.lastName


class Gender(models.Model):
	genderAccronym = models.CharField(max_length = 1)
	genderLabel = models.CharField(max_length = 13)

	def _unicode_(self):
		return self.genderAccronym


class Country(models.Model):
	countryName = models.CharField(max_length = 35)

	def _unicode_(self):
		return self.countryName



class FirstName (models.Model):
	firstName = models.CharField(max_length = 20)
	country = models.ForeignKey('Country')
	rank = models.IntegerField(default = 0)
	gender = models.ForeignKey('Gender')
	meaning = models.CharField(max_length = 100)

	def _unicode_(self):
		return self.firstName


class FullName(models.Model):
	first = models.ForeignKey('FirstName')
	last = models.ForeignKey('LastName')

	def _unicode_(self):
		return self.first + ' ' + self.last