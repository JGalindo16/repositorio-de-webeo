"""
Encapsulamiento:

Se refiere a la protección de atributos y métodos dentro de una clase, por ejemplo si mi clase
tiene el atributo edad, no quiero que sea negativa. 
Por ende puedo encapsular el atributo para que no pueda ser accedido.
Creo dos métodos un getter y un setter que me permitan trabajar con el atribut. El getter me permite obtener el valor
y el setter modificarlo. En este último se puede agregar la validación.

ES LITERALMENTE PONERLE TRABAS A ALGO, POR EJEMPLO PROTEGER LAS CLAVES EN LOS USUARIOS 
"""
"""
si le pongo en los self un __ (doble guíon bajo)se protege la variable para la lectura pero no para cambiarla 
Por ejemplo:
self.__password

lo de @property y el setter es por convención y fácil llamado 
"""
class User:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password
    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, value):
        if (self.__username == None):
            self.__username = value



usr= User("admin", "1234")
print(usr.username)
usr.username= "admin2"
print(usr.username)


