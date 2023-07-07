
# Qual é o tipo do objeto ao qual essas expressões são avaliadas?

# (a) False + False // Retorna o valor 0 (int), por que ele vai tentar somar 0 + 0 = 0 

teste = False + False;

print(type(teste));


# (b) 2 * 3**2.0 # Retorna float porque quando se multiplica com float o int vira float.

teste1 = 2 * 3**2.0

print(teste1);
print(type(teste1));

# (c) 4 // 2 + 4 % 2 # Retorna int 

teste2 = 4 // 2 + 4 % 2;

print(teste2);
print(type(teste2));

# (d) 2 + 3 == 4 or 5 >= 5 # Retorna boolean 

teste3 = 2 + 3 == 4 or 5 >= 5;

print(teste3);
print(type(teste3));