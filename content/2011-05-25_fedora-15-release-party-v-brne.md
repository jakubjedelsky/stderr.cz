Title: Fedora 15 Release Party v Brně
Date: 2011-05-25 16:48
Slug: fedora-15-release-party-v-brne

Včera podle plánu vyšla finální podoba [Fedory 15][] a při té
příležitosti se v Brně uskutečnila [Fedora 15 Release Party][]. Záštitu
nad akcí přebrala brněnská pobočka [Red Hatu][], jejíž zaměstnanci tu
prezentovali svoji práci - a zároveň novinky ve Fedoře.

*Předem upozorňuji, že jsem si nedělal poznámky a to, co zde píši,
doluji z hlavy, kde se mi nemuselo uchytit úplně všechno. <s>Zároveň se
předem omlouvám za kvalitu fotografií. Vše bylo foceno telefonem bez
blesku a na některých obrázcích je vidět dost prd. Ale stačí pro
nasátí atmosféry, která byla velice fajn.</s> Fotky už nejsou.*

**Aktualizace:** [report z Release Party][] sepsal i jeden z pořadatelů
Jiří Eischmann (v en a s hezčíma fotkama).

**Aktualizace II.:** Na LinuxExpres.cz se objevily [videa a
prezentace][].

### Sraz v 18:00

Všechno začínalo v šest večer. Cestou na Purkyňovu, kde je sídlo Red
Hatu, jsem se už nemohl dočkat ... až navštívím tamní záchod. Našel jsem
a zábava mohla začít. Oficiální uvítání a začátek byl vcelku originální:
"Přednášky začnou asi za půl hodiny, zatím se běžte najíst." Občerstvení
(burgery, tortilly a muffiny) zajistilo [Giraffy][], tak předpokládám,
že se všichni olizovali až za ušima. První velký dík pořadatelům!  

### Gnome 3

Kolem půl sedmé začal první bod programu: představení **Gnome 3** z
pohledu vývojáře tohoto grafického prostředí **Tomáše Bžatka**. Osobně
jsem si s názorem na prostředí prošel asi touto cestou: *WTF?! -\> ujde
to -\> zajímavý -\> hezký, už to chci!* Při představování jsem se začal
zase trošku bát. Na vině byl (na můj vkus až příliš) vysoký výskyt
spojení jako *"nefunguje"*, *"nepůjde"*, *"bug"*. Ve výsledku jsem byl
ale spokojený a už teď můžu potvrdit, že pro základní funce je Gnome 3
parádní (před chvílí jsem nainstaloval na notebook). Příjemná byla i
zmínka o programu `gnome-tweak-tool`, který by měl zastupovat některé
funkce Gnome týmem oficiálně nepodporované.

Podle slov Tomáše se pracuje na Gnome 3.2, které by snad mělo být ve
Fedoře 16(?) a podporovat o mnoho více funkcí než teď. Výběrem snad jen
nějaké využití plochy, na které v tuto chvíli nejsou (a co jsem pochopil
nejdou přidat) žádné ikonky a propojení s různými internetovými službami
(facebook, gmail, gtalk). *Díky Tomáši!*

### KDE 4.6 & Fedora Board agenda

Po krátké pauze předstoupil **[Jaroslav Řezník][]**, který nejprve představoval nové
KDE. Zaujalo mě jejich přizpůsobení pro netbooky s podporou dotykové
obrazovky. Rád bych o tom napsal něco víc, ale přiznávám se, že jsem moc
neposlouchal a raději si udělal test o Fedoře běžící na dvou místních
počítačích. A zjistil jsem, že skoro nic nevím :)

Druhá část přednášky patřila "politickému" rozdělení komunity okolo
projektu Fedora. Jaroslav je členem nejvyššího orgánu Fedora Project
Boardu a tak bylo zajímavý zjistit, kdo co má na starosti, jak jsou
členové voleni a dosazovaní a jak se (ne)vládne. Více info o tomto
vedení najdete na wiki fedoraprojektu: [Board][], [FESCo][], apod. *Díky
Jardo!*

### systemd

Spolu s Gnome 3 a SPICE, který ještě přijde, byla
toto přednáška na kterou jsem se nejvíce těšil. O **systemd**, který
uváděl **[Michal Schmidt][]**, jsem se zajímal zatím jen okrajově a
trošku jsem se ho bál. Zavádí totiž spoustu novinek, což my admini
nemáme ze zásady rádi. Při bližším pohledu, a Michalově zdůvodnění co a
proč je řešeno právě takhle, ten systém vypadá vlastně docela dobře.

Co mě potěšilo je možnost dvojího nastavení: systémem v /lib/systemd a
administrátorem v /etc/systemd, přičemž administrátorská nastavení mají
vyšší prioritu. Dalšími zajímavými fičurkami jsou třeba "jakože jedoucí"
služby, kdy `systemd` vytvoří pouze odpovídající socket a až ve chvíli,
kdy na něj přijde nějaký dotaz, spustí správnou službu (dobrým příkladem
je cups). Nebo, zmíněno jen na okraj, je fajn možnost omezení zdrojů
(např. CPU) pro jednotlivé služby. Přednáška se jinak ubírala spíše
směrem k základním funkcím (a srovnání se stávajícími), jako je
nastartování a ukončení služby.. *Díky Michale!*

Pokud vás systemd zajímá, přečtěte si [seriál od Lennarta
Poetteringa][], samotného autora systému.

### Power management improvements

Další na řadě byl **Jaroslav Škarvada** s povídáním o **spotřebě a (elektrickém)
vytížení** (hlavně) notebooků. Ze začátku jsem se trošku lekl, s jakou
rychlostí nastoupil. Asi během dvou minut jsme byli na pátém slajdu z
devíti a já z toho neměl skoro nic. Naštěstí jsme se chvilku zdrželi u
zajímavého nástroje `powertop`, který, i když je stále ve verzi beta, už
umí ohlídat pár věcí a umožní šetření baterie u notebooků. Během
přednášky se rozvinula krátká diskuze o dalších možných možnostech a
změnách. *Možná by taky bylo dobré pohlídat si [žrouty energie v
kernelu][].* *Díky Jardo!*

### SPICE support in virt-manager

Protože už byl v přednáškách malinko skluz, tak i ta předposlední o protokolu **SPICE**
od **Luboše Kocmana** byla zrychlená. Šlo o představení projektu, který
má v budoucnu nahradit VNC a bylo nám představeno, jak je v nové Fedoře
dostupný a jak je s ním možné pracovat. Do času se vešel i příklad (a to
přece vystačí za tisíc slov), kde Luboš ukázal, jak SPICE dokáže
kontrolovat myš, přenášet video a audio a kolik toto všechno "žere" dat
na síti. Osobně jsem se na tuto přednášku těšil, o SPICE jsem si dřív
četl a docela mě jeho možnosti zaujaly. Asi bych to mohl využít na svém
RHEL virtuálu, pro přípravu na RHCSA/RHCE. *Díky Luboši!*

Slajdy z tohoto povídání si můžete stáhnout na [Google docs][].

### Závěrem..

Na úvod závěru poznamenám, že jsem vynechal poslední přednášku o
**novinkách v Ext4** od **Lukáše Czernera**. Zapůsobila jednak únava po
náročném dni a pak kamarádi čekající v hospodě :).

První brněnskou Fedora Release Party hodnotím na výbornou. Vydařila se
jak po organizační stránce, kdy sice utíkal čas přednášek, ale ani jedna
nebyla mimo téma a všechny byly v rukou odborníků, tak po stránce
návštěvnosti - co jsem napočítal, sešlo se zde kolem 50 lidí (nechci ale
kecat). Nemohl jsem si nevšimnout, že se jednotlivé výstupy nahrávaly,
doufám, že se videa spolu se slajdy brzo objeví na netu a já se budu
moct dokouknout na ext4.

A na úplný závěr: Velký dík brněnským redhaťákům za akci!

  [Fedory 15]: http://fedoraproject.org/
  [Fedora 15 Release Party]: https://fedoraproject.org/wiki/Release_Party_F15_Brno
  [Red Hatu]: http://www.cz.redhat.com/
  [report z Release Party]: http://eischmann.wordpress.com/2011/05/25/fedora-15-release-party-in-brno/
  [videa a prezentace]: http://www.linuxexpres.cz/aktuality/fedora-15-release-party-v-brne
  [Giraffy]: http://www.giraffy.cz
  [Jaroslav Řezník]: https://fedoraproject.org/wiki/JaroslavReznik
  [Board]: http://fedoraproject.org/wiki/Board
  [FESCo]: http://fedoraproject.org/wiki/Development/SteeringCommittee
  [Michal Schmidt]: https://fedoraproject.org/wiki/User:Michich
  [seriál od Lennarta Poetteringa]: http://0pointer.de/blog/projects
  [žrouty energie v kernelu]: http://www.root.cz/zpravicky/linuxova-jadra-maji-stale-problemy-se-spotrebou-energie/
  [Google docs]: https://docs.google.com/viewer?a=v&pid=explorer&chrome=true&srcid=0By4Xswv8v79mNWUyOGU2NDctZWYyMS00ZmZjLTliYWYtNWJlY2M4ZTNmNWM4&hl=en_US
