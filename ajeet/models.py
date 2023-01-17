from distutils.command.upload import upload
import email
from django.db import models
from sqlalchemy import desc
from django.db import models
#compress image
from io import BytesIO
from PIL import Image
from django.core.files import File
# Create your models here.

#image compression method
def compress(image):
    im=Image.open(image)
    im_io=BytesIO()
    try:
        
       im.save(im_io,'JPEG',quality=60)
    except:
        im.save(im_io,'png',quality=60)
    new_image=File(im_io,name=image.name)
    return new_image
    
class Destination(models.Model):
    name = models.CharField(max_length=100)
    image  =models.ImageField(upload_to='gallery')
    #call image compression function before saving the data
    def save(self,*args,**kwargs):
        new_image=compress(self.image)
        self.image=new_image
        super().save(*args,**kwargs)
    def __str__(self):
        return self.name
    