"""  Traduza os comandos a seguir para expressões Booleanas em Python e avalie-as:
"""

#a) A soma de 2 e 2 é menor que 4.

teste1 = (2 + 2) < 4;

print(teste1);

#b. O valor de 7 // 3 é igual a 1 + 1.

teste2 = (7 // 3) == (1 + 1);
print(teste2);

#c. A soma de 3 ao quadrado e 4 ao quadrado é igual a 25.

teste3 = (3**2 + 4**2) == 25;

print(teste3);

#d. A soma de 2, 4 e 6 é maior que 12.

teste4 = (2 + 4 + 6 ) > 12;
print(teste4);

#e. 1387 é divisível por 19.

teste5 = (1387%19) == 0;
print(teste5);

#f. 31 é par. (Dica: o que o resto lhe diz quando você divide por 2?)

teste6 = (31%2) == 0;
print(teste6); 

#g. O preço mais baixo dentre R$ 34,99, R$ 29,95 e R$ 31,50 é menor que R$ 30,00.

preco = 34.99, 29.95, 31.50;

menor_preco = min(preco);

teste7 = menor_preco < 30.00;

print(teste7);