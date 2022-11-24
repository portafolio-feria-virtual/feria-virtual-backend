from django.db import models
from django.contrib.auth.models import AbstractBaseUser,AbstractUser, PermissionsMixin, BaseUserManager
from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.conf import settings
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
    
    country = models.CharField(max_length=255)


    def save(self , *args , **kwargs):
        
        self.type = UserAccount.Types.COMERCIANTE_EXTRANJERO
        self.esComercianteExtranjero = True
        self.is_staff = False
        return super().save(*args , **kwargs)
    

    def __str__(self):
        return str(self.firstName)

    def crearLicitacionInternacional():
        """
        por hacer
        
        Metodo donde el comerciante Extranjero crear una solicitud de compra en la que pueden participa diferentes productores y transportistas
        """
        pass


    def verProcesoVenta():
        """

        Metodo que retorna el estado actual de la licitación(iniciado, recibido, en trasporte, etc)
        
        """
        
        pass
    
    def actualizarProceo():

        """ Metodo que permite al comerciante extranjero editar el proceso, creando avisos o modificando el estado de este mismo """




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
        self.esComercianteLocal = True
        self.is_staff = False
        return super().save(*args , **kwargs)


    def actualizarProceso():
        """ Metodo que permite al comerciante local actualizar el proceso de venta, permitiendole recepcionar el pedido """
        pass

    def comprarSaldos():
        """ Metodo que permite al comerciante local comprar saldos( resultantes de una venta internacional donde no se compró todo lo puesto a disposición por el productor ) """
        pass

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

    def  ingresarInformacionMercancia():
    
        """ Metodo que permite a los productores ingresar informacion respecto a la mercancia que poseen   """
        
        pass

    def participarProcesoVenta():
    
        """ Metodo que permite a los productores ingresar a los procesos de venta creados por los comerciantes extranjeros """
        
        pass

    def crearVentaNacional():
    
        """ Metodo que permite a los productores crear una publicacion de venta para que los comerciantes locales se contacten o decidan comprar el stock que poseen """

        pass





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
        self.esTransportista = True
        self.is_staff = False
        return super().save(*args , **kwargs)

    def  ingresarSubastaVentaInternacional():
        
        """ Metodo que permite a los Transportista ingresar a las subastas de transporte de ventas internacionales  """

        pass

class Consultor(UserAccount):

    is_staff = True

    def __str__(self):
        return str(self.firstName)

    def save(self , *args , **kwargs):

        self.type = UserAccount.Types.CONSULTOR
        self.esConsultor = True
        self.is_staff = True
        return super().save(*args , **kwargs)


class MetodoTransporte(models.Model):
    
    tipo =  models.CharField(max_length=255, blank=True)
    description =  models.CharField(max_length=255, blank=True)
    transportista = models.ForeignKey(Transportista, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.description)

    


class Mercancia(models.Model):

    title =  models.CharField(max_length=255, blank=True)
    price = models.IntegerField()
    image = models.CharField(max_length=255, blank=True)
    stockDec = models.DecimalField( max_digits=10, decimal_places=2)
    stockInt = models.IntegerField()
    productor = models.ForeignKey(Productor, on_delete=models.DO_NOTHING)

class VentaNacional(models.Model):

    description = models.CharField(max_length=255, blank=True)
    productor = models.ForeignKey(Productor, on_delete=models.DO_NOTHING)
    mercancia = models.ForeignKey(Mercancia, on_delete = models.DO_NOTHING)
    geoLocation = models.CharField(max_length=255, blank=True)

class LicitacionInternacional(models.Model):
    description = models.CharField(max_length=255, blank=True)
    extranjero = models.ForeignKey(ComercianteExtranjero, on_delete=models.DO_NOTHING)
    productor = models.ForeignKey(Productor, on_delete=models.DO_NOTHING)
    mercancia = models.ForeignKey(Mercancia, on_delete=models.DO_NOTHING)
    geoLocation = models.CharField(max_length=255, blank=True)


class SubastaTransporte(models.Model):

    description = models.CharField(max_length=255, blank=True)
    productor = models.ForeignKey(Productor, on_delete=models.DO_NOTHING)
    transportista = models.ForeignKey(Transportista, on_delete=models.DO_NOTHING)
    comprador = models.ForeignKey(ComercianteExtranjero, on_delete=models.DO_NOTHING)
    
    def calculoGanador():
        
        """ Metodo que determina que transportista ha sido el ganador del contrato por el transporte de la venta internacional """

        pass

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
