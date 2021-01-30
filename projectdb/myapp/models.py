from django.db import models

# Create your models here.
class Staff(models.Model):
    fullname = models.CharField(max_length=40)
    sex = models.CharField(max_length=10)
    age = models.IntegerField(default=0)
    address = models.CharField(max_length=100)
    image = models.ImageField(null=True)
    workplace = models

    def __str__(self):
        s = "Tên nhân viên: " + str(self.fullname) + ", giới tính: " + str(self.sex) + ", tuổi: " + str(self.age) + ", địa chỉ: " + str(self.address)
        return s


class Store(models.Model):
    storename = models.CharField(max_length=40)
    phone = models.IntegerField(max_length=20)
    storeaddress = models.CharField(max_length=100)

    def __str__(self):
        x = "Tên của hàng: " + str(self.storename) + ", điện thoại liên lạc: " + str(self.phone) + ", địa chỉ của hàng" + str(self.storeaddress)
        return x
