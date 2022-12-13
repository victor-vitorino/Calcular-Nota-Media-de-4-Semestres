
a = int(input('Entre com a nota do Primeiro Bimestre: '))
while a> 10:
    a = int(input('Nota inválida. Primeiro Bimestre: '))
b = int(input('Entre com a nota do Segundo Bimestre: '))
while b> 10:
    b = int(input('Nota inválida. Segundo Bimestre: '))
c = int(input('Entre com a nota do Terceiro Bimestre: '))
while c> 10:
    c = int(input('Nota inválida. Terceiro Bimestre: '))
d = int(input('Entre com a nota do Quarto Bimestre: '))
while d> 10:
    d = int(input('Nota inválida. Quarto Bimestre: '))
media = (a + b + c + d) / 4
print('media: {}' .format(media))