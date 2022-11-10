from django.db import models
from django.contrib.auth.models import AbstractBaseUser,AbstractUser, PermissionsMixin, BaseUserManager
from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
# Create your models here.

class UserAccountManager(BaseUserManager):
    def create_user(self , email , password = None):
        if not email or len(email) <= 0 : 
            raise  ValueError("Email field is required !")
        if not password :
            raise ValueError("Password is must !")
          
        user = self.model(
            email = self.normalize_email(email) , 
        )
        user.set_password(password)
        user.save(using = self._db)
        return user
      
    def create_superuser(self , email , password):
        user = self.create_user(
            email = self.normalize_email(email) , 
            password = password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.es_clienteInterno = True
        user.save(using = self._db)
        return user
      
class UserAccount(AbstractBaseUser, PermissionsMixin):
    class Types(models.TextChoices):
        COMERCIANTE_LOCAL = "COMERCIANTE LOCAL" , "comerciante local"
        COMERCIANTE_EXTRANJERO = "COMERCIANTE EXTRANJERO" , "comerciante extranjero"
        CONSULTOR = "CONSULTOR","consultor"
        PRODUCTOR = "PRODUCTOR", "productor"
        TRANSPORTISTA = "TRANSPORTISTA","transportista"
        ADMINISTRADOR = "ADMINISTRADOR", "administrador"


        
          
    type = models.CharField(max_length = 30 , choices = Types.choices , 
                            # Default is user is teacher
                            default = Types.COMERCIANTE_LOCAL)
    email = models.EmailField(max_length = 200 , unique = True)

    """
    Las siguientes variables pertenecen a django, por eso utilizan snake_case 
    
    """
    is_active = models.BooleanField(default = True)
    is_admin = models.BooleanField(default = False)
    is_staff = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default = False)
    last_login = models.DateTimeField(null= True, blank = True)
    date_joined = models.DateTimeField(auto_now_add=True)

     
      
    esClienteInterno = models.BooleanField(default = False)

    esComercianteExtranjero = models.BooleanField(default = False)
    esComercianteLocal = models.BooleanField(default = False)
    esConsultor = models.BooleanField(default = False)
    esProductor = models.BooleanField(default = False)
    esTransportista = models.BooleanField(default = False)

    firstName = models.CharField(max_length= 100)
    lastName = models.CharField(max_length= 100)
    address = models.CharField(max_length= 100)
    phone = models.CharField(max_length= 100)
       
    USERNAME_FIELD = "email"
      
    # defining the manager for the UserAccount model
    objects = UserAccountManager()
      
    def __str__(self):
        return str(self.email)
      
    def has_perm(self , perm, obj = None):
        return self.is_admin
      
    def has_module_perms(self , app_label):
        return True
      
    def save(self , *args , **kwargs):
        if not self.type or self.type == None : 
            self.type = UserAccount.Types.EXTERNO
        return super().save(*args , **kwargs)

class ComercianteExtranjero(UserAccount):
    #user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    
    country = models.CharField(max_length=255)


    def save(self , *args , **kwargs):

        self.type = UserAccount.Types.COMERCIANTE_EXTRANJERO
        self.es_comercianteExtranjero = True
        return super().save(*args , **kwargs)
    

    def __str__(self):
        return str(self.firstName)




# @receiver(post_save, sender= UserAccount)
# def create_profile(sender, instance, created, **kwargs):

#     if created:
#         if sender.

class ComercianteLocal(UserAccount):
    documentNumber = models.CharField(max_length=255, blank=True)
    businessName = models.CharField( max_length=50)
    rut = models.CharField(max_length=255, blank=True)
    

    def __str__(self):
        return str(self.firstName)

    def save(self , *args , **kwargs):

        self.type = UserAccount.Types.COMERCIANTE_LOCAL
        self.es_comercianteLocal = True
        return super().save(*args , **kwargs)

class Productor(UserAccount):
    
    documentNumber = models.CharField(max_length=255, blank=True)
    businessName = models.CharField( max_length=50)
    rut = models.CharField(max_length=255, blank=True)
    productType = models.CharField(max_length=255, blank=True)
    

    def __str__(self):
        return str(self.firstName)

    def save(self , *args , **kwargs):

        self.type = UserAccount.Types.PRODUCTOR
        self.es_productor = True
        return super().save(*args , **kwargs)


class Transportista(UserAccount):
    
    documentNumber = models.CharField(max_length=255, blank=True)
    rut = models.CharField(max_length=255, blank=True)
    capacity = models.CharField(max_length=255, blank=True)
    size=models.IntegerField(null=True)
    cooling = models.BooleanField(default=False)


    def __str__(self):
        return str(self.firstName)

    def save(self , *args , **kwargs):

        self.type = UserAccount.Types.TRANSPORTISTA
        self.es_transportista = True
        return super().save(*args , **kwargs)



    
