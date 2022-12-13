a = int(input('Primeiro Bimestre: '))
if a> 10:
    a = int(input('Você digitou errado. Primeiro Bimestre: '))
b = int(input('Segundo Bimestre: '))
if b> 10:
    b = int(input('Você digitou errado. Segundo Bimestre: '))
c = int(input('Terceiro Bimestre: '))
if c> 10:
    c = int(input('Você digitou errado. Terceiro Bimestre: '))
d = int(input('Quarto Bimestre: '))
if d> 10:
    d = int(input('Você digitou errado. Quarto Bimestre: '))
media = (a + b + c + d) / 4
print('media: {}' .format(media))
