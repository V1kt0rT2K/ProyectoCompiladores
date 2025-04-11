from config import Config

class Conversor:

    def conversionLempiras(self,cantidad,origen):
        if origen == "Lempiras":
            return cantidad
        
        tasa = self.tasas[origen+"Lempiras"]
        return cantidad * tasa
    
    def conversion(self,cantidad,origen,destino):
        if destino == "Lempiras":
            return self.conversionLempiras(cantidad,origen)
        
        tasa = self.tasas["Lempiras"+destino]

        cantidadLempiras = self.conversionLempiras(cantidad,origen)

        return cantidadLempiras * tasa

    

    def __init__(self):
        self.tasas = Config.tasas
    

