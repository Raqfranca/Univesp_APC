""" 
Dada a lista de notas de trabalho de casa dos alunos notas = [9, 7, 7, 10, 3, 9, 6, 6, 2] escreva:
"""

notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]

# (a) Uma expressão que avalia para o número de 7 notas.

print(7 in(notas));

# (b) Uma instrução que muda a última nota para 4.

notas.pop(8);

notas.insert(8, 4);

print(notas);

#(c) Uma expressão que avalia para a nota mais alta.

notas.sort();

print(notas);

#(d) Uma expressão que avalia para a média das notas. 

quantidade = len(notas);

print(quantidade);

media = sum(notas)/quantidade;

print(media);



