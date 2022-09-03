# Feria Virtual Maipo Grande


## Rutas

### 1. Login

Para ejecutar la acción **_Login_**,en el sistema se debe realizar una petición a través del metodo **_POST_** a la dirección:
    
    /api/auth/login/

Para que la acción de **_Login_** se efectue de manera correcta, se debe entregar un parametro en formato **_JSON_** con la siguiente estructura:
```json
    {
        "email": "email@email.com",
        "password": "password"
    }
```
### 2. Logout

Para ejecutar la acción **_Logout_**, en el sistema se debe realizar una petición a través del metodo **_POST_** a la dirección:

    /api/auth/logout/

Para que la acción de **_Logout_** se efectue de manera correcta, se debe enviar una **_petición POST vacia_**


### 3. Signup

Para que la acción de **_Signup_** se efectue de manera correcta, se debe se debe entregar un parametro en formato **_JSON_** con la siguiente estructura:

```json
    {
        "email": "correo@correo.com",
        "username": "Nombre de usuario", 
        "password": "12345678"
    }
```
### 4. Password Reset 

Para que la acción de **_Password Reset_** se inicie se debe ir a la dirección :

    /api/auth/reset/

Para que la acción de **_Password Reset_** se efectue de manera correcta se debe entregar un parametro en formato **_JSON_** con el siguiente formato:

```json
{
    "email": "email@email.com"
}
```






