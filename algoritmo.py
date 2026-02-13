#1. Cálculo de suma y promedio: Solicitar al usuario tres números enteros. Calcular y mostrar la suma total y el promedio de los números ingresados.

# Entradas
def a1():
    try:
        x = int(input("Ingrese el primer número entero: "))
        y = int(input("Ingrese el segundo número entero: "))
        z = int(input("Ingrese el tercer número entero: "))

        # Proceso
        sum = x + y + z
        average = sum / 3

        # Salidas
        print("La suma total es:", sum)
        print("El promedio es:", average)
        print("El promedio es:", int(average))

    except ValueError:
        print("debes ingresar un numero valido")
        
if __name__ == "__main__":
    a1()















#2. Área de un rectángulo: Solicitar la base y la altura de un rectángulo. Calcular y mostrar el área correspondiente.
"""
2. Área de un rectángulo: Solicitar la base y la altura de un rectángulo. Calcular y mostrar el área correspondiente.
3. Conversión de temperatura: Solicitar una temperatura en grados Celsius y convertirla a grados Fahrenheit.
4. Salario semanal: Solicitar la cantidad de horas trabajadas en la semana y el valor por hora. Calcular y mostrar el salario semanal.
5. Salario con horas extra: Solicitar horas trabajadas y valor por hora. Si el empleado trabajó más de 40 horas, las horas adicionales se pagan al 150%. Calcular el salario total.
@@ -23,3 +24,4 @@
9. Venta con IVA: Solicitar el valor de una venta sin impuestos. Calcular el IVA (19%) y mostrar el valor del IVA y el total con impuesto incluido.
10. Compra de varios productos: Solicitar la cantidad de productos comprados y el precio de cada uno. Calcular el total de la compra.
11. Comisión por ventas: Solicitar el valor total de ventas realizadas por un vendedor. Calcular una comisión del 5% y mostrar el total a recibir.
"""