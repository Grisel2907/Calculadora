# Calculadora
primer avance de calculadora en Flet
# Calculadora básica en Flet

## Descripción
Este proyecto es el primer avance de una calculadora básica desarrollada en Python utilizando la librería Flet.  
El objetivo de este trabajo es aprender a crear una interfaz gráfica y manejar eventos al presionar botones.

## Interfaz
La interfaz cuenta con un display en la parte superior donde se muestran los números y resultados.  
Debajo del display se encuentran los botones organizados en forma de calculadora, incluyendo los números del 0 al 9 y las operaciones básicas.

Para el diseño se utilizaron contenedores (`Container`) y una cuadrícula (`GridView`), además de colores para diferenciar los botones.

## Funcionamiento
Cada botón tiene un evento `on_click` que se activa cuando el usuario lo presiona.  
Cuando se presiona un número, este se muestra en el display.  
Cuando se selecciona una operación y se presiona el botón igual, la calculadora realiza la operación correspondiente.

Las operaciones implementadas son:
- Suma
- Resta
- Multiplicación
- División

También se incluye un botón para limpiar el display.

## Observaciones
Este proyecto corresponde a un avance inicial, por lo que la calculadora tiene funciones básicas.  
El propósito principal es practicar el uso de eventos y el desarrollo de interfaces gráficas con Flet.
