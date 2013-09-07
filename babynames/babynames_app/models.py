from django.db import models


class LastName(models.Model):
    lastName = models.CharField(max_length=20)

    def __unicode__(self):
        return self.lastName


class FirstName(models.Model):
    name = models.CharField(max_length=25)
    nicknames = models.ManyToManyField('self', symmetrical=False,
                                       null=True)

    def __unicode__(self):
        return self.name


#class Nickname(models.Model):
#    longname = models.ForeignKey(FirstName)
#    nickname = models.ForeignKey(FirstName)
#
#    def __unicode__(self):
#        return "%s" % (self.nickname)


class Gender(models.Model):
    genderAccronym = models.CharField(max_length=1)
    genderLabel = models.CharField(max_length=13)

    def __unicode__(self):
        return self.genderAccronym


class Country(models.Model):
    countryName = models.CharField(max_length=35)

    def __unicode__(self):
        return self.countryName


class NameInfo (models.Model):
    firstName = models.ForeignKey(FirstName)
    country = models.ForeignKey('Country', null=True)
    gender = models.ForeignKey('Gender')
    meaning = models.CharField(max_length=100, null=True)

    def __unicode__(self):
        return "%s" % (self.firstName)


class FullName(models.Model):
    first = models.ForeignKey(NameInfo)
    last = models.ForeignKey(LastName)
    rank = models.IntegerField(default=0)
    pros = models.CharField(max_length=100, null=True)
    cons = models.CharField(max_length=100, null=True)

    def __unicode__(self):
        return '%s %s' % (self.first.firstName, self.last.lastName)
