""" Comece executando as instruções de atribuição:
s1 = 'ant'
s2 = 'bat'
s3 = 'cod'

Escreva expressões Python usando s1, s2 e s3 e os operadores + e * a fim de avaliar para:
"""

s1 = ' ant '
s2 = ' bat '
s3 = ' cod '

#a.'ant bat cod'

print(s1+s2+s3);

#b.'ant ant ant ant ant ant ant ant ant ant'

print(s1*10);

#c.'ant bat bat cod cod cod'

print(s1 + s2*2 + s3*3);

#d. 'ant bat ant bat ant bat ant bat ant bat ant bat ant bat'

print((s1 + s2)*7);

#e. 'batbatcod batbatcod batbatcod batbatcod batbatcod'

teste1 = s2+s2+s3;

teste1Sem = teste1.split();

print(teste1Sem*5);



