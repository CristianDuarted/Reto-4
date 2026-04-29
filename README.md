# Ejercicios de Programación Orientada a Objetos

Este repositorio contiene dos ejercicios desarrollados en Python para practicar conceptos básicos de programación orientada a objetos.

## Ejercicio 1: Figuras geométricas

Se implementa un sistema de figuras usando herencia y composición.

### Clases principales

- Shape (clase base)
- Rectangle
- Square
- Triangle
- Tipos de triángulo:
  - Equilateral
  - Isosceles
  - Scalene
  - Right triangle

También se usan clases auxiliares:

- Point
- Line

### Funcionalidades

- Calcular área
- Calcular perímetro
- Obtener vértices
- Determinar si una figura es regular

## Ejercicio 2: Sistema de restaurante

Se implementa un sistema simple de pedidos de restaurante.

### Clases

- MenuItem (base)
- Drink
- Appetizer
- MainCourse
- Order
- Payment

### Funcionalidades

- Agregar productos a una orden
- Calcular total
- Aplicar descuento a bebidas si hay un plato principal
- Mostrar el pedido
- Uso de getters y setters

### Lógica de descuento

Si el pedido contiene al menos un MainCourse, se aplica un 10% de descuento a las bebidas.

