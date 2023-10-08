class CuentaCorriente:
    
    def __init__(self, dni, saldo):
        self.dni = dni
        self.nombre = ""
        self.saldo = saldo

    def __init__(self, dni, nombre, saldo):
        self.dni = dni
        self.nombre = nombre
        self.saldo = saldo

    def sacarDinero(self, saldo)