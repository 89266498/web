from django.db import models


# Create your models here.

class Contactor(models.Model):
    # id      = models.AutoField()
    name = models.CharField(max_length=20, blank=False, null=False)
    phone = models.CharField(max_length=15)
    orgid = models.ForeignKey("Org", on_delete=models.SET_DEFAULT, default='3333')

    def __str__(self):
        return "%s:%s" % (self.name, self.phone)


class Org(models.Model):
    # id      = models.AutoField()
    orgname = models.CharField(max_length=200, blank=False, null=False)
    orgaddr = models.CharField(max_length=2000)
    orgpra = models.CharField(max_length=200)

    def __str__(self):
        return "%s" % (self.orgname)


class Elog(models.Model):
    logtime = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True,default="This is slug")
    logcontent = models.TextField(max_length=2000)

    def __str__(self):
        return "%s--%s" % (self.logtime, self.logcontent)
