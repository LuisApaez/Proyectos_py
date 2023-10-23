""" Script para generar información de ventas de papelerias.
* Supondremos que día con día nos hacen llegar un Excel por
papelería con las ventas totales de ese día.
* La estructura del código ahora es mediante clases para 
su posterior uso en otros scripts.
"""

#####################################################################
#####################################################################
#####################################################################
   
class GIC:                                                               
    # ATRIBUTOS DE LA CLASE
    abcdario = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
                'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 
                'U', 'V', 'W', 'X', 'Y', 'Z']

    papelerias = ['Xochimilco', 'Cuemanco', 'Coapa', 'Milpa Alta', 'CU', 'Zócalo', 
                'Narvarte', 'Santa Fé', 'Polanco', 'Centro']

    lineas = ['Cuadernos', 'Libretas', 'Lápices', 'Plumones', 'Borradores', 'Sacapuntas',
              'Laptops', 'Tablets', 'Mochilas', 'Bolsas', 'Cajas', 'Pegamento', 'Tijeras',
              'Monitores', 'Teclados', 'Mouse', 'Audífonos', 'Cables', 'Cargadores', 'Baterías',
              'Pc', 'Uniformes', 'Pinturas', 'Pinceles', 'Papel', 'Cartulinas']
    
    ruta = "C:\\Users\\usuario\\OneDrive\\Documentos\\Programación\\Python\\Py-Excel\\Exceles"
    ruta_base = "C:\\Users\\usuario\\OneDrive\\Documentos\\Programación\\Python\\Py-Excel"

    # CONSTRUCTOR
    def __init__(self, dia):
        self.dia = dia
        
    # METODOS DE INSTANCIA
    def crear_info(self):
        """ Método para generar el dataframe con la información de ventas
            de las papelerias para el día dado. """
        
        # Importacion de las librerias necesarias
        import seaborn as sns
        import matplotlib.pyplot as plt
        import pandas as pd
        import random as r
        import string
        import os
        import datetime as dt
        import time
        
        claves_precio = {}
        claves_lineas = {}
        
        for _ in range(100):
            r1 = r.randint(0, len(GIC.abcdario)-1)
            r2 = r.randint(0, len(GIC.abcdario)-1)
            r3 = r.randint(0, len(GIC.abcdario)-1)
            
            val_clave = GIC.abcdario[r1] + GIC.abcdario[r2] + GIC.abcdario[r3] + str(r.randint(0, 10)) + str(r.randint(0, 10)) + str(r.randint(0, 10)) 
            val_precio = r.random() * r.randint(1, 50000)
            val_linea = r.choice(GIC.lineas)
            
            claves_precio[val_clave] = val_precio
            claves_lineas[val_clave] = val_linea
            
        dia_str = self.dia[-2:] + self.dia[5:7] + self.dia[:4]
        carpeta_mes = GIC.ruta + "\\" + self.dia[5:7] + self.dia[:4]
        carpeta_dia = GIC.ruta + "\\" + self.dia[5:7] + self.dia[:4] + "\\" + dia_str 
        
        try:
            os.mkdir(carpeta_mes)
            os.mkdir(carpeta_dia)
            os.chdir(carpeta_dia)
        except:
            os.mkdir(carpeta_dia)
            os.chdir(carpeta_dia)
        
        for _ in range(0, len(GIC.papelerias)):
            productos_diferentes = r.randint(100, 10000)
            info = {'CLAVE': [r.choice(list(claves_precio.keys())) for _ in range(productos_diferentes)],
                    'CANTIDAD': [r.randint(1, 50) for _ in range(productos_diferentes)]}
            df = pd.DataFrame(info)
            df['PRECIO'] = df['CLAVE'].apply(lambda x: claves_precio[x])
            df['CANTIDAD'] = df['CANTIDAD'].astype(str)
            df['LINEA'] = df['CLAVE'].apply(lambda x: claves_lineas[x])
            df = df[['CLAVE', 'PRECIO', 'CANTIDAD', 'LINEA']]
            nombre_archivo = GIC.papelerias[_] + '_' + dia_str + '.xlsx'
            df.to_excel(nombre_archivo, index=False)
            
        os.chdir(GIC.ruta_base)
        
        print(f"Información al día {self.dia} generada con éxito.")