# Radiative-Transfer-Parallel
## Descripción del Proyecto
Este proyecto tiene como objetivo simular la transferencia radiativa en discos protoplanetarios mediante el Método Monte Carlo (MC) utilizando Python en un entorno de cómputo en paralelo. Se busca visualizar las posiciones finales de los fotones en un espacio tridimensional y analizar su distribución acumulativa y densidad de probabilidad.

La transferencia radiativa es un proceso crucial en la formación planetaria, donde la interacción de la radiación con el material del disco protoplanetario influye en su temperatura, densidad y composición.

## Objetivos:

Simular la transferencia radiativa en discos protoplanetarios para comprender la propagación de la radiación.
Visualizar las posiciones finales de los fotones en un espacio tridimensional para analizar la distribución espacial de la radiación.
Estudiar la influencia de parámetros físicos como la densidad del disco y su opacidad en la transferencia radiativa.
Implementación:

La simulación se realiza mediante el Método Monte Carlo en paralelo, una técnica que utiliza muestreo aleatorio para resolver problemas complejos de transferencia radiativa. Se generan fotones con posiciones y direcciones aleatorias dentro del disco protoplanetario y se simula su movimiento a través del medio. La absorción, dispersión y emisión de la radiación se modelan de acuerdo con las características físicas del disco.

## Componentes del Proyecto:

Generación de Fotones: Se generan fotones con posiciones y direcciones aleatorias dentro del disco protoplanetario.
Simulación de Movimiento: Se simula el movimiento de los fotones a través del medio utilizando el Método Monte Carlo en un entorno de cómputo en paralelo.
Visualización 3D: Se visualizan las posiciones finales de los fotones en un espacio tridimensional para comprender su distribución espacial.
Análisis de Resultados: Se analizan los datos obtenidos para comprender la transferencia radiativa en el disco protoplanetario y su relación con los parámetros físicos del sistema.

## Instalación

Clona este repositorio en tu máquina local.
Asegúrate de tener Python y las siguientes bibliotecas instaladas: matplotlib, numpy.
Ejecuta el script principal para generar las posiciones finales de los fotones.

## Uso
Una vez que hayas instalado las dependencias y clonado el repositorio, simplemente ejecuta el script. Esto generará las posiciones finales de los fotones y mostrará una visualización en 3D de las mismas.

Contribuir
Las contribuciones son bienvenidas. Si tienes sugerencias o encuentras algún error, por favor crea un "issue" o envía un "pull request".

## Conclusiones sobre las Ventajas del Modelado en Paralelo de Transferencia Radiativa

Eficiencia Computacional: El modelado en paralelo permite distribuir la carga computacional entre múltiples procesadores, lo que acelera significativamente el tiempo de ejecución de las simulaciones de transferencia radiativa en discos protoplanetarios. Esto permite abordar problemas más grandes y complejos en menos tiempo.

Escalabilidad: El uso de paralelismo facilita la escalabilidad del modelo, lo que significa que se puede aumentar el tamaño y la resolución de las simulaciones sin comprometer la eficiencia computacional. Esto es especialmente importante en el estudio de sistemas astrofísicos complejos como los discos protoplanetarios, donde se requiere un alto nivel de detalle.

En resumen, el modelado en paralelo de la transferencia radiativa en discos protoplanetarios ofrece ventajas significativas en términos de eficiencia computacional y escalabilidad, lo que permite realizar simulaciones más precisas y detalladas de estos sistemas astrofísicos fundamentales.
