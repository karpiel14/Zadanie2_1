slowo = "kot"
for x in range(5):
 print("Proba numer: ", x+1)
 slowo_uzytkownika = input("Podaj swoje slowo:")
 if slowo_uzytkownika==slowo:
    print('Gratulacje, odgadles slowo')
    break
else:
 print('Nie udalo ci sie odgadnac slowa')



