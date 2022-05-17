def delta(a, b, c):
  cont=((b*b)-(4*a*c))
  return cont

def linha1(a, b, delt):
  result = (b+delt)/(2*a)
  return result

def linha2(a, b, delt):
  result = (b-delt)/(2*a)
  return result
 
import math

A = int(input("Numero A: "))
B = int(input("Numero B: "))
C = int(input("Numero C: "))

resultD = delta(A, B, C)
print(resultD)
if(resultD<0):
  print("Não existe")
elif (resultD==0):
  raiz = math.sqrt(resultD)
  print(raiz)
  x1 = linha1(A, -B, raiz)
  print(f"Resultado: {x1}")
else:
  raiz = math.sqrt(resultD)
  print(raiz)
  x1 = linha1(A, -B, raiz)
  x2 = linha2(A, -B, raiz)
  print(f"Resultado: {x1}, {x2}")

