# Validação de tipos de triângulos

while True:
       v1 = float(input('Primeiro lado: '))
       v2 = float(input('Segundo lado: '))
       v3 = float(input('Terceiro lado: '))
       if v1 == v2 and v1 == v3:
              print("Os valores informados acima FORMAM um triângulo EQUILÁTERO")
       elif v1 == v2 or v1 == v3 or v3 == v2:
              print("Os valores informados acima FORMAM um triângulo ISÓSCELES")
       elif v1 < v2 + v3 and v2 < v1 + v3 and v3 < v1 + v2:
              print("Os valores informados acima FORMAM um triângulo ESCALENO")
       else:
              print("Os valores informados acima NÃO FORMAM um triângulo")