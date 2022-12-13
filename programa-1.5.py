a = int(input('Primeiro Bimestre: '))
b = int(input('Segundo Bimestre: '))
c = int(input('Terceiro Bimestre: '))
d = int(input('Quarto Bimestre: '))
media = (a + b + c + d) /4
if a <= 10 and b <=10 and c <= 10 and d <= 10:
    print('media: {}' .format(media))
else:
    print('foi informado alguma nota errada')
