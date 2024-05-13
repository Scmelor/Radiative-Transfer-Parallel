# Radiative-Transfer-Parallel
## Descripción del Proyecto
Este proyecto tiene como objetivo simular la transferencia radiativa en discos protoplanetarios mediante el Método Monte Carlo (MC) utilizando Python en un entorno de cómputo en paralelo. La transferencia radiativa es un proceso crucial en la formación planetaria, donde la interacción de la radiación con el material del disco protoplanetario influye en su temperatura, densidad y composición.

## Objetivos:

Simular la transferencia radiativa estelar en discos protoplanetarios para comprender la propagación de la radiación.
Estudiar los tiempos de cómputo del modelo de transferencia radiativa en serie y en paralelo.

## Instalación

1. Clona este repositorio en tu máquina local.
2. Asegúrate de tener Python y las siguientes bibliotecas instaladas: matplotlib, numpy, mpi4py.
3. Ejecuta el script principal llamado parallel.py desde terminal  /usr/bin/mpiexec -n 4 python3 parallel.py
4. Grafica los resultados del modelo en paralelo y en serie con el repositorio de GraphicResults.ipynb en un jupyter notebook


## Conclusiones sobre las Ventajas del Modelado en Paralelo de Transferencia Radiativa

Eficiencia Computacional: El modelado en paralelo permite distribuir la carga computacional entre múltiples procesadores, lo que acelera significativamente el tiempo de ejecución de las simulaciones de transferencia radiativa en discos protoplanetarios. Esto permite abordar problemas más grandes y complejos en menos tiempo.

Escalabilidad: El uso de paralelo facilita la escalabilidad del modelo, lo que significa que se puede aumentar el tamaño y la resolución de las simulaciones sin comprometer la eficiencia computacional. Esto es especialmente importante en el estudio de sistemas astrofísicos complejos como los discos protoplanetarios, donde se requiere un alto nivel de detalle.

## Contribuir
Las contribuciones son bienvenidas. Si tienes sugerencias o encuentras algún error, por favor crea un "issue" o envía un "pull request".
