class SiguienteDia():

    def comprobarFecha31(self, dia, mes, anio):
        meses_31 = [1, 3, 5, 7, 8, 10]
        for meses in meses_31:
            if meses == mes:
                if 1 <= dia <= 31:
                    if 1812 <= anio <= 2014:
                        return "Fecha valida"
            
                
            
                
    def comprobarFecha30(self,dia,mes,anio):
        meses_30=[4,6,9,11]
        for meses in meses_30:
            if meses == mes :
                if 1 <= dia <= 30:
                    if 1812 <= anio <= 2014:
                        return "Fecha valida"

    def comprobarFecha_febrero(self,dia,mes,anio):
            if mes== 2 :
                if dia == 29:
                    if anio % 4 == 0:
                        return "Fecha valida bisiesto"
                if dia ==28:
                    if anio % 4 != 0:
                          return "Fecha valida normal"  
                      
                        
                  
    
