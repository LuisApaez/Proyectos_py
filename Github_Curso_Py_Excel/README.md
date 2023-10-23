# Proyecto de automatización del curso de _Python-Excel-Power BI_.

Para este proyecto requerimos definir primero el código del archivo `GenerarInfoClase.py` en el cual tenemos el código para generar 
la información simulada de las ventas diarias de las diferentes papelerías, donde podremos generar la información de un día
en particular hasta la información de todo un mes (o más). 

Luego, con el archivo `DataManip.py` podremos generar particularmente la información de un mes o un trimestre
y asimismo consolidarla para obtener los insumos que pasaremos a Power BI. En este archivo ocupamos las funcionalidades
del archivo anterior, por lo cual no es necesario utilizar `GenerarInfoClase.py` directamente.

Finalmente, con la notebook `automatización.ipynb` tenemos el proceso automatizado para generar la información mensual correspondiente
al mes en curso y para generar los consolidados para los tableros, en dado caso que nos encontremos en un mes donde
querramos y podamos analizar la información trimestral.

### Tableros de Power BI

Una vez que tenemos los insumos listos, actualizaremos los siguientes tableros:

* [Tablero mensual]()
* [Tablero trimestral](https://app.powerbi.com/view?r=eyJrIjoiYWE3ODk5YmEtNzI2Zi00NGU5LTg4MjMtODllNWRjZjA4YTcxIiwidCI6IjVmMjgyOTEwLTE3NmYtNDU5ZC1hYjdkLWI3NDRhYTZlZmMwNyIsImMiOjR9)

### Creación paso a paso del Proyecto

En este mismo repositorio encontrarás las notebooks guía para ir programando el proyecto, dichas notebooks se encuentran en la carpeta `ProyectoGuiado`.

Además, encontrarás una carpeta con Exceles de ejemplo (carpeta  `02012023`) generados con Python para un día de ventas en las 10 sucursales.
