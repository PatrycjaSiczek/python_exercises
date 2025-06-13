from collections import Counter
import matplotlib.pyplot as plt

plik = "pan-tadeusz.txt"
plik2 = "szyfr.txt"
alfabet = list("aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż")

def litery(plik):
    with open(plik, 'r', encoding='utf-8') as f:
        tekst = f.read().lower()
        litery = [znak for znak in tekst if znak in alfabet]
        return Counter(litery)
        
    
licznikPanaTadeusza = litery(plik)
licznikszyfr = litery(plik2)
literyWPanTadeusz = [lit for lit, _ in licznikPanaTadeusza.most_common()]
literyWSzyfr = [lit for lit, _ in licznikszyfr.most_common()]

slownik = dict(zip(literyWSzyfr, literyWPanTadeusz))
reczne_zmiany = {'o': 'z', 'r': 'o', 'g': 'w', 'a': 'n'}
for klucz, nowa in reczne_zmiany.items():
    if klucz in slownik:
        slownik[klucz] = nowa
if 'o' in slownik:
    slownik['o'] = 'z'
if 'r' in slownik:
    slownik['r'] = 'o'
if 'g' in slownik:
    slownik['g'] = 'w'
if 'a' in slownik:
    slownik['a'] = 'n'
    
    
with open(plik2, 'r', encoding='utf-8') as f:
    szyfr = f.read().lower()

odszyfrowano = ''.join(slownik.get(l, l) for l in szyfr)


with open('deszyfrat.txt', 'w', encoding='utf-8') as f:
    f.write(odszyfrowano)
    
print("\n Co na co sie zamienia?:")
for szyfr_litera, pan_litera in slownik.items():
    print(f"{szyfr_litera} → {pan_litera}")

def histogram(counter, tytul):
    litery, liczby = zip(*sorted(counter.items()))
    plt.bar(litery, liczby)
    plt.title(tytul)
    plt.xlabel("Litera")
    plt.ylabel("Liczba wystąpień")
    plt.tight_layout()
    plt.show()

histogram(licznikPanaTadeusza, "Wystepowanie Liter w Panu Tadeuszu")
histogram(licznikszyfr, "Wystepowanie Liter w pliku Szyfr")

print("\nNa co chcesz zamienic? :")
for litera in literyWSzyfr:
    obecna = slownik.get(litera, '?')
    nowa = input(f"{litera}:   ").strip().lower()
    if nowa:
        slownik[litera] = nowa

odszyfrowany_poprawiony = ''.join(slownik.get(l, l) for l in szyfr)

with open('deszyfrat2.txt', 'w', encoding='utf-8') as f:
    f.write(odszyfrowany_poprawiony)


