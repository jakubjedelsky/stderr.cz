Title: exCurr: převodník měn
Date: 2010-10-13 12:01
Slug: excurr-prevodnik-men

Občas mívám nutkání koukat po různých zahraničních e-shopech,
novinkách, které se u nás (zatím) neprodávají a sním o tom, že bych si
**právě toto** mohl jednou koupit. Asi jako každý. Jedinou překážkou mi
byla cena - převádět z hlavy eura nebo dolary na naše koruny se mi
nechce. Proto jsem dlouho používal převodník měn na webu [finance.cz][],
ale ono je to takové zdlouhavé... Ve volných chvílích jsem si tedy
napsal vlastní skript (python) - převodník měn pro příkazovou řádku.  

### Co to je

Skript exCurr funguje vlastně úplně jednoduše - z webu ČNB stáhne
aktuální kurzovní lístek a s ním dále pracuje (převod z jedné měny do
druhé zvládne každý, jde o trojčlenku :) ). Pomocí přepínače `-h` je
možné zobrazit nápovědu:

```text
Usage: exCurr.py [options] CASTKA

Prevede CASTKA z nebo na CZK (ceske koruny) podle aktualniho kurzu Ceske
narodni banky (CNB). Hodnota je zaokrouhlena na dve desetinna mista. Pro
oddeleni desetinnych mist pouzijte tecku.

Options:
  -h, --help            zobrazi tuto napovedu a skonci
  -f KOD_MENY, --from=KOD_MENY
                        Urcuje z jake meny bude prevadet na CZK
  -t KOD_MENY, --to=KOD_MENY
                        Urcuje na jakou menu bude z CZK prevadet.
  -l, --list            vypis kurzu dle CNB (Ceska nardni banka)
  -a                    Vypise dostupne kody men a skonci.
```

### Příklady

Převedení 100 amerických dolarů (USD) na koruny:

```text
$ ./exCurr.py -f USD 100
1772.70 CZK
```

Převedení 50 korun na filipínské peso:

```text
$ ./exCurr.py -t PHP 50
123.27 PHP
```

### Stažení

Kód je dostupný na [github.com][], kde můžete stahovat aktuální zdroják
ve formě [.tar.gz][] nebo [.zip][]. Nebo pomocí git:

```text
git clone http://github.com/jakubjedelsky/exCurr.git
```

### Chyby

Chyby můžete psát sem do komentářů nebo jako [Issues][] na webu githubu. Díky :)

  [finance.cz]: http://www.finance.cz/bankovnictvi/financni-kalkulacky/prevodnik/
  [github.com]: http://github.com/jakubjedelsky/exCurr
  [.tar.gz]: http://github.com/jakubjedelsky/exCurr/tarball/master
  [.zip]: http://github.com/jakubjedelsky/exCurr/zipball/master
  [Issues]: http://github.com/jakubjedelsky/exCurr/issues
