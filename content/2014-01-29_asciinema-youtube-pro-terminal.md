Title: asciinema: YouTube pro terminál ve Fedoře
Slug: asciinema-youtube-pro-terminal-ve-fedore
Date: 2014-01-29

Na nástroj [asciinema](http://asciinema.org) jsem poprvé narazil na [HackerNews](https://news.ycombinator.com/item?id=6556106) a zamiloval si jej na první pohled. Jedním příkazem zaznamenat, co se odehrává v terminálu, odeslat "video" na server a sdílet. Nebo si jej vložit na vlastní stránky. A sdílet. Video dávám schválně do uvozovek - ve skutečnosti se jedná o textový výstup (terminálový emulátor napsaný v javascriptu) a příkazy si můžete pěkně vykopírovat. V době videotutoriálů a ukázek možností různých nástrojů je to moc pěkné řešení. O kousek níž se můžete podívat, jak jsem si pěkně zahrál `moon-buggy`.

<center><script type="text/javascript" src="https://asciinema.org/a/7412.js" id="asciicast-7412" async></script></center>

Jedná se kompletně o opensource - [klient](https://github.com/sickill/asciinema) je napsaný v Pythonu a dostupný přes pip, [serverová](https://github.com/sickill/asciinema.org) část je pak postavená nad Ruby on Rails. Chopil jsem se příležitosti, zkusil si balíček zabalit do rpm a projít procesem dodání do repozitářů Fedory. Chvilku to trvalo (hlavně proto, že to byl můj první příspěvek balíkem), ale klienta si už teď můžete nainstalovat jak ve Fedoře, tak i z repozitářů EPELu. Zatím tedy jen z testovacích větví, ale během pár dní by se to mělo dostat do stabilních:

Pro Fedoru 19 a 20: 
```text
yum --enablerepo=updates-testing asciinema
```

Pro instalaci z EPEL repozitáře, např. do RHEL, CentOSu, aj:
```text
yum --enablerepo=epel-testing install asciinema
```

Zkoušejte, testujte a hlašte bugy.
