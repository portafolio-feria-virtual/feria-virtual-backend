from django.db import models
from django.contrib.auth.models import AbstractBaseUser,AbstractUser, PermissionsMixin, BaseUserManager
from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail

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
        user.is_active = True
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
    is_active = models.BooleanField(default = False)
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
    businessName = models.CharField( max_length=50)
    country = models.CharField(max_length=255)


    def save(self , *args , **kwargs):
        
        self.type = UserAccount.Types.COMERCIANTE_EXTRANJERO
        self.esComercianteExtranjero = True
        self.is_staff = False
        return super().save(*args , **kwargs)
    

    def __str__(self):
        return f"{self.businessName} representado por {self.firstName} {self.lastName}"

class ComercianteLocal(UserAccount):

    documentNumber = models.CharField(max_length=255, blank=True)
    businessName = models.CharField( max_length=50)
    rut = models.CharField(max_length=255, blank=True)
    

    def __str__(self):
        return str(self.firstName)

    def save(self , *args , **kwargs):

        self.type = UserAccount.Types.COMERCIANTE_LOCAL
        self.esComercianteLocal = True
        self.is_staff = False
        return super().save(*args , **kwargs)


class Productor(UserAccount):
    
    documentNumber = models.CharField(max_length=255, blank=True)
    businessName = models.CharField( max_length=50)
    rut = models.CharField(max_length=255, blank=True)
    productType = models.CharField(max_length=255, blank=True)
    #mercancia = models.ForeignKey("app.Model", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.firstName)

    def save(self , *args , **kwargs):

        self.type = UserAccount.Types.PRODUCTOR
        self.esProductor = True
        self.is_staff = False 
        return super().save(*args , **kwargs)



class Transportista(UserAccount):
    businessName = models.CharField( max_length=50)
    documentNumber = models.CharField(max_length=255, blank=True)
    rut = models.CharField(max_length=255, blank=True)
    



    def __str__(self):
        return str(self.firstName)

    def save(self , *args , **kwargs):

        self.type = UserAccount.Types.TRANSPORTISTA
        self.esTransportista = True
        self.is_staff = False
        return super().save(*args , **kwargs)


class Consultor(UserAccount):

    
    

    def __str__(self):
        return str(self.firstName)

    def save(self , *args , **kwargs):

        self.type = UserAccount.Types.CONSULTOR
        self.is_active= True
        self.esConsultor = True
        self.is_staff = True
        self.has_perm('cuentas.view_consultor')
        return super().save(*args , **kwargs)

class Administrador(UserAccount):

    

    def __str__(self):
        return str(self.firstName)

    def save(self , *args , **kwargs):

        self.type = UserAccount.Types.ADMINISTRADOR
        self.is_staff = True
        self.is_active = True
        self.is_admin = True
        self.es_clienteInterno = True
        return super().save(*args , **kwargs)






class Sistema(models.Model):

    usuario = models.ForeignKey(UserAccount, on_delete=models.DO_NOTHING)

    def actualizarEstadoProcesoLicitacionVenta():
        """ Metodo para actualizar estado proceso de la venta internacional """

        pass

    def enviarReporteResumenVentaEmail():
        """ Metodo para enviar reporte de resumen de la venta internacional al correo de los involucrados """
        
        pass

    def crearSubastaTransporte():
        """ Metodo para crear subasta de transporte """

        pass

    def adjudicarSubasta():
        """ Metodo para adjudicar subasta """

        pass

    def determinarCantidadProductoresMercancia():
        """ Metodo para determinar cantidad productores de mercancia que abasteceran una venta"""

        pass

    def evaluarRendimiento():
        """ Metodo para evaluar rendimiento """

        pass
    
    def evaluarPerdidaFruta():
        """ Metodo para evaluar perdida de fruta """

        pass

    def crearReporteRol():
        """ Metodo para crear reporte por rol """

        pass

@receiver(post_save)
def afterCreateMail(sender, instance=None, created= False, **kwargs):
    if sender.__name__ in ("ComercianteExtranjero","ComercianteLocal","Productor","Transportista"):
        if created:
            print(instance.email)

            subject = f"Bienvenido {instance.firstName} {instance.lastName} a Maipo Grande"
            message = f"Estimado {instance.firstName} {instance.lastName}:\nEn Maipo Grande estamos muy contentos de contar con tu apoyo.\nEn las proximas horas uno de nuestros ejecutivos se contactará contigo "
            lista = []
            lista.append(instance.email)
            send_mail(subject=subject, message=message, from_email=settings.EMAIL_HOST_USER, recipient_list=lista)


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        "noreply@somehost.local",
        # to:
        [reset_password_token.user.email]
    )