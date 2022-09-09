from django.db import models

# Create your models here.
import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.

class UserManager(BaseUserManager):
	def _create_user(self, username, email, password, is_staff,is_superuser,**extra_fields):
		if is_staff and is_superuser :
			extra_fields['tipo_usuario'] = "Administrador"
		print(extra_fields)
		if not email:
			raise ValueError('El email debe ser obligatorio')
		if not extra_fields['tipo_usuario']:
			raise ValueError("Debe especificar tipo de usuario")
		email= self.normalize_email(email)
		user = self.model(username=username, email=email, is_active=True,
				is_staff=is_staff, is_superuser=is_superuser, **extra_fields)
		user.set_password(password)
		user.save(using = self._db)
		return user
	def create_user(self, username, email,  password=None,**extra_fields):
		return self._create_user(username, email, password, False,False, **extra_fields)
	def create_superuser(self, username, email, password, **extra_fields ):
		return self._create_user(username, email, password, True,True, **extra_fields)

class usuarios(AbstractBaseUser, PermissionsMixin):
	id_user = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
	#id_usuario = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True) 
	#id_user = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
	username = models.CharField('Nombre de usuario',max_length=50, unique = True)
	email = models.EmailField('Correo electronico', max_length=254, unique = True)
	first_name = models.CharField('Primer nombre',max_length=100,blank=True)
	last_name = models.CharField('Apellido',max_length=100,blank=True)
	rut = models.CharField("RUT", max_length=11,blank=True)
	address = models.CharField('Direccion', max_length=50,blank=True)
	phone = models.CharField("Telefono", max_length=20, blank= True)
	objects = UserManager()
	is_active = models.BooleanField('Esta activo',default=True)
	is_staff = models.BooleanField('Es administrador',default=False)
	tipos = (('0','Productor'),('1','Interno'),('2','Externo'),('3','Consultor'),('4','Transportista'),('5', "Administrador"))
	tipo_usuario = models.CharField("Tipo de usuario",max_length=50,choices=tipos,default='interno')
	country = models.CharField('Pais',max_length=20, default='Chile',blank=True)
	doc_num = models.CharField("Numero de documento", max_length=9, blank=True)
	business_name = models.CharField("Razón Social", max_length=100, blank= True)
	capacity = models.IntegerField("Capacidad de Carga", blank=True, default=0)
	prod_type = models.CharField("Tipo de productos", max_length=150, blank=True)
	size = models.DecimalField("Tamaño Transporte", max_digits=10, decimal_places=2, blank=True, default=0)
	cooling = models.BooleanField("Refrigeración", blank=True, default=False)


	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username','tipo_usuario','phone']
	#REQUIRED_FIELDS = ['tipo_usuario']

	def get_short_name(self):
		return self.username
