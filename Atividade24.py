# Crie um programa que receba uma quantidade indefinida de números do usuário. O programa deve calcular a média desses números e parar quando o usuário digitar -1.

med = 0
count = 0

while True:
    N = int(input("Digite seu numero, para parar -1"))

    if N ==-1:
        break
    med += N

    count+=1

    if count>0:
        media = med/count
print(media)