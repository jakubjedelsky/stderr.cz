Title: ARC raid a obnova hesla
Date: 2010-10-25 23:19
Slug: arc-raid-a-obnova-hesla

Stalo se mi to, co by se správcům stávat nemělo - zapoměl jsem (nebo
jsem se překlepl, to už teď nezjistím) přístupové heslo ke správě HW
RAIDu. Je to, s prominutím, průser v okamžiku, kdy chcete vyměnit disk,
zjistit jejich stav, nastavit nový Volume Set nebo s tím dělat jakékoliv
jiné nastavení, protože prostě ... nemůžete. Jednalo se o řadič
**ARC-1680**.  
  
Samotná oficiální dokumentace (ať k řadiči nebo FAQ) žádné informace o
obnově zapomenutého hesla neobsahuje a většina vygůglovaných výsledků
hlásí obnovu pomocí jakéhosi placeného rescue cd (jehož web vypadá
naprosto nedůvěryhodně). Naštěstí jsem po chvíli hledání narazil na
užitečný [link][], kde je univerzální (a *funkční*) heslo pro zařízení
Areco (výrobce ARC řadičů). Je to:

```text
MNO974315743924
```

Otestované řadiče jsou v [komentářích][] k původnímu blogpostu, já k nim
přidávám právě ARC-1680. A ještě důležitá poznámka na závěr: *Heslo
nefunguje při přístupu přes web (logicky), úpravy s ním lze provádět
pouze přes CLI nebo McBIOS.*

Pokud by někdo měl s tímto blogpostem problém, [napište][].

  [link]: http://phaq.phunsites.net/2007/01/12/master-password-for-areca-arc-1210-controller/
  [komentářích]: http://phaq.phunsites.net/2007/01/12/master-password-for-areca-arc-1210-controller/#comments
  [napište]: http://dev.stderr.cz/kontakt/
