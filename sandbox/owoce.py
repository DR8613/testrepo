# lista
lista = [1]
lista = [1, 2, 3] #cyfry typ intger

koszyk = ['jablko1', 'jablko2', 'jablko3', 'garsc malin'] # typ string


#petla
#for element in koszyk:  #element - dowolny element
#	print (element)
#	print ('malina')



for owoc in koszyk:
	print ('1.Wyciagam', owoc)
	print ('2.Myje', owoc)
	print ('3.Zjadam', owoc)

	if owoc =='garsc malin':
		continue
	print ('4.Wyrzucam ogryzek', owoc)
	print ()

print ('Skonczylem')
