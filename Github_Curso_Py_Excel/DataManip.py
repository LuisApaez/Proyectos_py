""" Script para generar información de ventas de papelerias.
En este caso genera la información de un rango de fecha, de modo
que pueden generarse archivos para un mes completo, incluso año.
También con este script se puede consolidar la información de un mes.
"""

#####################################################################
#####################################################################
#####################################################################
   
class GIC_BASE():
    
    # Atributos de la clase
    year = 2023
    base_holidays = ['2023-04-06', '2023-04-07', '2023-05-05', '2023-10-12',
                     '2023-11-02', '2023-12-12']
    meses_lista = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio',
                'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
    
    @classmethod
    def holidays_mx(cls):
        """ Metodo para obtener los dias festivos en Mexico. """
        
        import holidays as hd
        dias_festivos_mx = []
        aux = list(hd.Mexico(years=cls.year).items())
        
        for _ in range(len(aux)):
            dias_festivos_mx.append(cls.convert_to_str(aux[_][0]))
            
        dias_festivos_mx += cls.base_holidays
        return dias_festivos_mx 
    
    # Metodos estaticos
    @staticmethod
    def convert_to_str(fecha):
        """ Metodo para convertir un objeto de tipo datetime a string. """
        
        import datetime as dt
        return dt.datetime.strftime(fecha, '%Y-%m-%d')
    
    @staticmethod
    def convert_to_dt(fecha):
        """ Metodo para convertir un objeto de tipo string a datetime. """
        
        import datetime as dt
        return dt.datetime.strptime(fecha, '%Y-%m-%d')
    
    @staticmethod
    def consolidar_info_mens(m, 
                             r = "C:\\Users\\usuario\\OneDrive\\Documentos\\Programación\\Python\\Py-Excel\\Exceles\\ConsolMensual",
                             k = "Consolidado"):
        """ Función para realizar la consolidación mensual de la información

        Args:
            m (str, optional): Mes en formato ddaaaa. Defaults to '012023'.
            n (str, optional): Mes en formato NombreMesaaaa. Defaults to 'Enero2023'.
            r (str, optional): Ruta de guardado. Defaults to "C:\\Users\\usuario\\OneDrive\\Documentos\\Programación\\Python\\Py-Excel\\Exceles\\ConsolMensual".
        """
    
        # Importacion de las librerias necesarias
        import pandas as pd 
        import time as t
        import os
        
        # Mediremos el tiempo de ejecución
        init = t.time()
        mes = m

        # ruta inicial
        ruta_base = "C:\\Users\\usuario\\OneDrive\\Documentos\\Programación\\Python\\Py-Excel\\Exceles"
        # ruta de guardado
        ruta_base_save = r
        
        meses = os.listdir(ruta_base)

        # accedemos al mes de interes
        mes_interes = meses[meses.index(mes)]
        ruta_base_interes = ruta_base + "\\" + mes_interes

        # accedemos a los dias
        archivos_dia = os.listdir(ruta_base_interes)
        consol = []
        for dia in archivos_dia:
            ruta_auxiliar = ruta_base_interes + "\\" + dia
            
            # accedemos a los 10 archivos del día referentes cada uno a una zona
            try: 
                zonas_lista = os.listdir(ruta_auxiliar)
                zonas_lista = list(filter(lambda x: not x.endswith('.csv'), zonas_lista))
            except:
                continue
            
            # consolidado del dia
            consolidado = []
            for zona_ruta in zonas_lista:
                df_aux = pd.read_excel(ruta_auxiliar + "\\" + zona_ruta)
                df_aux_base = zona_ruta.split('.')[0].split('_')
                df_aux['ZONA'] = df_aux_base[0]
                df_aux['DIA'] = df_aux_base[1][4:] + '-' + df_aux_base[1][2:4] + '-' + df_aux_base[1][:2] 
                consolidado.append(df_aux)
                
            consol.append(pd.concat(consolidado))
            
        consolidado_df = pd.concat(consol)
        
        # Exportamos el dataframe
        consolidado_df.to_csv(ruta_base_save + "\\" + k + ".csv", index=False)
        fin = t.time()
        
        print("Tiempo de ejecución:", round((fin - init)/60, 2), "minutos")
        print("Consolidado generado")
    
    @staticmethod
    def consolidar_info_trim(n):
        """ Función para realizar la consolidación trimestral de la información

        Args:
            n (int): Número de trimestre en cuestión.
        """
        
        ruta_save = "C:\\Users\\usuario\\OneDrive\\Documentos\\Programación\\Python\\Py-Excel\\Exceles\\ConsolTrimestre"
        
        # [01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11 ,12]
        meses_num = ['0'+str(i) for i in range(1, 13) if i < 10] + [str(i) for i in range(10, 13)]
        
        # Accedemos a los meses del trimestre
        meses_num_interes = meses_num[(n*3)-3 : (n*3)]
        
        # Generamos los consolidados de los meses respectivos del trimestre
        for i in range(3):
            f1 = meses_num_interes[i] + str(GIC_BASE.year)
            k =  "Consolidado" + str(i+1)
            GIC_BASE.consolidar_info_mens(f1, ruta_save, k)
        
    #####################################################################
    #####################################################################
    
    # Constructor
    def __init__(self, f_init, f_fin):
        self.f_init = f_init
        self.f_fin = f_fin
    
    def crear_info(self):

        from GeneraInfoClase import GIC
        import pandas as pd
        import datetime as dt
        import time 

        rango_fechas = list(pd.date_range(start=self.f_init, end=self.f_fin, freq='D'))
        rango_fechas = list(map(GIC_BASE.convert_to_str, rango_fechas))

        # Filtros:
        # - Sin dias festivos
        dias_festivos_mx = GIC_BASE.holidays_mx()
        rango_fechas_filtro1 = list(filter(lambda x: x not in dias_festivos_mx, 
                                        rango_fechas))
        # - Sin domingos
        rango_fechas_filtro2 = list(filter(lambda x: GIC_BASE.convert_to_dt(x).weekday() != 6,
                                        rango_fechas_filtro1))

        inicio = time.time()

        # Generamos la informacion mensual
        for fecha in rango_fechas_filtro2:
            GIC_INTERN = GIC(fecha)
            GIC_INTERN.crear_info()

        fin = time.time()
        print(f"Tiempo de ejecución: {round((fin - inicio) / 60, 2)} minutos.")