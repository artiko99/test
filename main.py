# x= True
# y= False
# print(x)
# print(y)

# if 5 == 5:
#   print("Prawda")
# print("Koniec")

# z=10
# m=10
# if m>z:
#   print("M większe")
# elif m<z:
#   print("M mniejsze")
# else:
#   print("równe")

# wiek = 22
# kasa = 5

# if wiek>22 or kasa>4:
#   print("Mozesz wejsc")
# else:
#   print("nie moze wejsc")

# from random import randint
# los = randint(1,10)
# odp= -1
# i=0
# print("Zgadnij liczbe z przedziału 1 - 10")

# while odp != los:
#   i += 1
#   odp = int(input("Podaj liczbę: "))
#   if odp > los:
#     print("Niestety, wylosowana liczba jest mniejsza od twojej")
#   elif odp < los:
#     print("Niestety wylosowana liczba jest większa od twojej")
# print("Brawo! Odgadłeś za", i, "razem.")

# lista = [1,2, "c", "d", "e"]
# print (lista)
# print(lista[4])
# lista[2] = 3
# print(lista)
# tekst ="Hello World"
# print(tekst[1])
# print (lista + ["f", "g"])
# print(lista * 3)
# print("Ilość elementów", len(lista))
# lista.append("a")
# print(lista)
# lista.append(["o", "p"])
# print(lista)
# print(lista[6][1])
# lista.insert(4, "l")
# print(lista)
# print("Ilość", lista.count(4))
# print("index:", lista.index(2))
# lista.remove("a")
# print(lista)
# lista2 = [7, 4, 6, 1, 9]
# print("Min:", min(lista2))
# print("Max:", max(lista2))
# lista2.sort()
# print(lista2)
# lista2.reverse()
# print(lista2)
# lista2.clear()
# print(lista2)

lista = ["Barcelona", "to", "najlepszy", "klub", "na", "świecie"]
i=0
while i < len(lista):
  print(lista[i])
  i+=1
for x in lista:
  print(x)
print(list(range(10)))
for y in range(4, 25, 4):
  print(y)

def func(x):
  return x * x
  