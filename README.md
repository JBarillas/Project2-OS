  # Thread Pool 🧜‍♀️
  ## Problema: 
  
1. Multiplicar 2 matrices haciendo uso de thread-pool, el programa recibirá como entrada 2 archivos csv
que deben de ser leídos y cargados a memoria
2. El tamaño del pool de hilos a utilizar.
3. Cada matriz es de enteros, los archivos no tienen encabezados y el separador de columnas es el
carácter “,” cada línea indica una nueva fila
4. El producto de matrices debe grabarse en otro archivo
  
Para realizar de manera mas eficiente y que su tiempo de ejecucion sea el menor posible, se utilizaran tecnicas de threads. Para comprender mejor  nuestro algoritmo es importante comprender que es un thread. 

## Threads

Un hilo es un flujo de ejecución a través del código de proceso, con su propio contador de programa que realiza un seguimiento de qué instrucción ejecutar a continuación, registros del sistema que contienen sus variables de trabajo actuales y una pila que contiene el historial de ejecución. Debido a que los hilos tienen algunas de las propiedades de los procesos, a veces se denominan procesos ligeros.

Un sistema operativo (SO) que tiene capacidad de hilos, la unidad básica de utilización de la CPU es un hilo. Un hilo se compone o consta de un contador de programa (PC), un registro y un espacio de pila. Los hilos no son independientes entre sí, como los procesos, como resultado, los hilos comparten con otros hilos su sección de código, sección de datos, recursos del sistema operativo también denominados tareas, como archivos abiertos y señales.

![Threads](https://github.com/lsophiagr/plop/blob/main/sistemas/Process-And-Thread-In-Lixus-2.jpeg)


## Paralelismo

El término paralelismo significa que una aplicación divide sus tareas en subtareas más pequeñas que se pueden procesar en paralelo, por ejemplo, en varias CPU al mismo tiempo. 

Para lograr un verdadero paralelismo, su aplicación debe tener más de un subproceso en ejecución, y cada subproceso debe ejecutarse en CPU / núcleos de CPU / núcleos de GPU de tarjeta gráfica separados o similar.

El siguiente diagrama ilustra una tarea más grande que se divide en 4 subtareas. Estas 4 subtareas están siendo ejecutadas por 4 subprocesos diferentes, que se ejecutan en 2 CPU diferentes. Esto significa que partes de estas subtareas se ejecutan simultáneamente (las que se ejecutan en la misma CPU) y las partes se ejecutan en paralelo (las que se ejecutan en diferentes CPU).

![Threads](https://github.com/lsophiagr/plop/blob/main/sistemas/concurrency-vs-parallelism-4.png)

## Concurrencia

Concurrencia significa que una aplicación está progresando en más de una tarea, al mismo tiempo o al menos aparentemente al mismo tiempo (al mismo tiempo).

Si la computadora solo tiene un CPU, es posible que la aplicación no avance en más de una tarea al mismo tiempo, pero hay más de una tarea en progreso a la vez dentro de la aplicación. Para progresar en más de una tarea al mismo tiempo, la CPU cambia entre las diferentes tareas durante la ejecución. Esto se ilustra en el diagrama siguiente:

![Threads](https://github.com/lsophiagr/plop/blob/main/sistemas/concurrency-vs-parallelism-1.png)

## Thread Pools

Supongamos que tuviéramos que crear una gran cantidad de hilos para nuestras tareas multithread. Computacionalmente sería más costoso ya que puede haber muchos problemas de rendimiento debido a demasiados hilos. Un problema importante podría ser que el rendimiento se limite. Podemos resolver este problema creando un 'thread pool'. Un 'thread pool' puede definirse como el grupo de 'threads' previamente instanciados e inactivos, que están listos para recibir trabajo. Se prefiere crear un 'thread pool' a crear instancias de nuevos hilos para cada tarea cuando necesitamos realizar una gran cantidad de tareas. Un 'thread pool' puede gestionar la ejecución simultánea de una gran cantidad de hilos de la siguiente manera:

Si un 'thread pool' en un 'thread pool' completa su ejecución, ese hilo se puede reutilizar.

Si se termina un hilo, se creará otro hilo para reemplazar ese hilo.


![Threads](https://github.com/lsophiagr/plop/blob/main/sistemas/ThreadPool.png)


## ¿Cómo funciona una multiplicación de matrices? 👀🧑🏻‍💻

Solo puede multiplicar dos matrices si sus dimensiones son compatibles, lo que significa que el número de columnas en la primera matriz es el mismo que el número de filas en la segunda matriz.

La forma habitual de definir la multiplicación de matrices es como una suma o, de forma más compacta, un 'dot product' de las filas de A y las columnas de B. El 'dot product' de la fila 1 de A y la columna 1 de B dará la primera entrada de C.

![Threads](https://github.com/lsophiagr/plop/blob/main/Screen%20Shot%202021-04-17%20at%208.05.05%20AM.png)


En general, la ij-ésima entrada de C es la i-ésima fila de A punteada con la j-ésima columna de B.

![Threads](https://github.com/lsophiagr/plop/blob/main/sistemas/Screen%20Shot%202021-04-17%20at%207.58.05%20AM.png)


### Ejemplo 🧠

Encuentre la tercera fila y la segunda columna del producto C. 🤖

![Threads](https://github.com/lsophiagr/plop/blob/main/sistemas/ThreadPool.png)

La respuesta es (1) (1) + (2) (2) + (3) (1) = 8. Intente usar la definición para encontrar el resto de las entradas de C.

### Interpretación: Una entrada de C es el producto escalar de una fila de A y una columna de B. Las entradas cero en C corresponden a una fila de A y una columna de B que son ortogonales (en ángulos rectos entre sí).










