Title: Prohlížení webu přes SSH tunel
Date: 2011-02-28
Slug: prohlizeni-webu-pres-ssh-tunel

*U příležitosti aktualizace na Wordpress 3.1 (se jménem Reinhardt,
zvoleného podle jazzového kytaristy Jeana "Django" Reinhardta; že by
to byla [provokace][] nebo naznačení [budoucí cesty][] projektu?) tu
uveřejním článek, který ve stavu "rozepsán" už nějakou dobu visí v
administraci.*

Existuje mnoho sítí, kde se nemusíte cítit zrovna bezpečně; ať je to
wifi v kavárně, mobilní připojení nebo sdílení připojení se sousedy. A
jsou situace, kdy byste rádi schovali to, na co koukáte. Co kdyby vás
někdo sledoval, že ano. Nebo jiná situace: jste za firewallem a chcete
se kouknout na zakázané weby (např. umístěné v intranetu). V takovém
okamžiku se hodí mít jiný počítač/server umístěn v nějaké důvěryhodnější
síti, "protunelovat" se na něj skrze ssh a veškerý HTTP(S) provoz z
prohlížeče směřovat skrz toto připojení.  

### SSH tunel

Nejdříve si zvolíme, na jakém portu ($PORT) chceme, aby spojení
naslouchalo na našem počítači (zvolíte-li vyšší než 10000, nic tím asi
nezkazíte) a připojíme se pomocí:

```bash
ssh -fND localhost:$PORT user@myserver
```

kde user je uživatel a myserver jméno vašeho vzdáleného serveru.

### Tunelujeme Firefox

[Firefox][] umožňuje nastavit proxy pomocí kontextového menu: *Úpravy
-\> Předvolby*. V sekci *Rozšířené* je tab *Síť*. Proxy se nastavuje
(nečekaně) v *Nastavení připojení...*, kde stačí zaškrtnout volbu *Ruční
konfigurace proxy serverů*, jako SOCKS server zadat *localhost* a jako
port náše výše zvolené číslo portu.

Webový provoz nyní směřuje přes ssh, ale, jak se můžete například pomocí
Wireshark, ne všechen. Firefox se stále dotazuje místních DNS serverů,
pozorný čtenář (čti útočník) tedy stále ví, kam koukáte. I toto lze
vyřešit: do řádku pro zadání URL napíšeme *about:config*, čímž se
dostaneme do rozšířené konfigurace prohlížeče. Zde stačí změnit hodnotu
`network.proxy.socks_remote_dns` na *True* a je vše hotovo.

### Tunelujeme Google Chrome

*Toto bych dříve asi ani nezmiňoval, ale nedávno jsem na notebooku, se
kterým se do "divných" sítí dostávám nejčastěji, přešel z Firefoxu na
Chrome. Kvůli rychlosti.*

Do nastavení [Google Chrome][] se lze dostat pomocí ikonky šroubováku(?)
vedle řádku pro zadávání URL a kontextového menu *Nastavení*. Zde se,
pod panelem *Pod pokličkou*, skrývá tlačítko pro *Změnu nastavení
proxy*. Dále postupujeme jako dříve u Firefoxu: Použijeme *Ruční
nastavení proxy*, do políčka pro SOCKS server zapíšeme *localhost*; port
jsme si dříve zvolili. Zavřeme a skoro vše funguje.

Skoro. Opět je tu problém s DNS servery, kdy se Chrome stále dotazuje
místních a útočník tak ví, kam koukáte. I když jsem hledal, nenašel
jsem, zda lze tento problém nějak vyřešit. Pokud o něčem víte, zmiňte se
v komentářích.

Zdroj: [http://wiki.freaks-unidos.net/weblogs/azul/firefox-ssh-tunnel][]

  [provokace]: http://www.djangoproject.com/
  [budoucí cesty]: http://www.google.cz/search?q=django+blog+howto
  [Firefox]: http://firefox.mozilla.cz/
  [Google Chrome]: http://www.google.com/chrome
  [http://wiki.freaks-unidos.net/weblogs/azul/firefox-ssh-tunnel]: http://wiki.freaks-unidos.net/weblogs/azul/firefox-ssh-tunnel
