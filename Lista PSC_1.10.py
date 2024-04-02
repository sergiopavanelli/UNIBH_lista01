A = input("Informe o valor de A: ")
B = input("Informe o valor de B: ")
C = input("Informe o valor de C: ")
area_triangulo = (float(A)*float(C))/2
area_circulo = 3.14159*float(C)**2
area_trapezio = (float(A)+float(B))*float(C)/2
area_quadrado = float(B)**2
area_retangulo = float(A)*float(B)
print("TRIANGULO:", "{:.3f}".format(area_triangulo))
print("CIRCULO:", "{:.3f}".format(area_circulo))
print("TRAPEZIO:", "{:.3f}".format(area_trapezio))
print("QUADRADO:", "{:.3f}".format(area_quadrado))
print("RETANGULO:", "{:.3f}".format(area_retangulo))