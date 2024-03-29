"""
En un banco tienen clientes que pueden hacer depósitos y extracciones de dinero. 
El banco requiere también al final del día calcular la cantidad de dinero que se ha depositado.
/*/Se deberán crear dos clases, la clase cliente y la clase banco. 
La clase cliente tendrá los atributos nombre y cantidad y los métodos __init__, depositar, extraer, mostrar_total.
La clase banco tendrá como atributos 3 objetos de la clase cliente y los métodos __init__, operar y deposito_total.
"""
 
class Banco:
	def __init__(self):
		self.cliente1 = Cliente("Ivan")
		self.cliente2 = Cliente("Marcos")
		self.cliente3 = Cliente("Juan")

	def operacion(self):
		self.cliente1.depositar(1000)
		self.cliente2.depositar(300)
		self.cliente3.depositar(43)
		self.cliente1.extraer(400)
 
	def depositos(self):
		total = self.cliente1.devolver_cantidad() + self.cliente2.devolver_cantidad() + self.cliente3.devolver_cantidad()
		print("El total de dinero del banco es: ",total)
		self.cliente1.imprimir()
		self.cliente2.imprimir()
		self.cliente3.imprimir()
 
class Cliente:
	def __init__(self, nombre):
		self.nombre = nombre
		self.cantidad = 0
        
	def depositar(self, cantidad):
		self.cantidad += cantidad
 
	def extraer(self, cantidad):
		self.cantidad -= cantidad

	def devolver_cantidad(self):
		return self.cantidad

	def imprimir(self):
		print(self.nombre, " tiene depositada una cantidad de ", self.cantidad)
 
banco=Banco()
banco.operacion()
banco.depositos()