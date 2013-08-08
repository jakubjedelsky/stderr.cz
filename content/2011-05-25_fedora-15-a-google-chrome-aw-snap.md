Title: Fedora 15 a Google Chrome: "Aw, Snap!"
Date: 2011-05-25 18:30
Author: Jakub Jedelsky
Slug: fedora-15-a-google-chrome-aw-snap

Po aktualizaci notebooku na Fedoru 15 se mi v prohlížeči Google Chrome,
který s oblibou používám, začala zobrazovat chybová stránka s nápisem
"Aw, Snap!" značící, že je něco špatně s vykreslováním webu. Začalo to
na Twitteru, pak na dalších webech a nekonec už i po spuštění samotného
prohlížeče. Odkaz z chybové stránky vás navede na [Chrome help][], ale
pro novou Fedoru (a vůbec pro linux) jen stěží najdete radu. Tak jsem
zapátral a...

...je to v SELinuxu. Notebook jsem si přeinstaloval tak, že jsem
zachoval pouze oddíl s `/home` a zrovna pro procesy google-chrome se
zřejmě nějak změnily požadavky na kontext v `.config` adresáři, kam si
Chrome ukládá uživatelské nastavení a cache. Do teď (ve Fedoře 14) mi
fungovalo následující:

```bash
$ ls -dZ .config/google-chrome
drwx------. kuba kuba system_u:object_r:file_t:s0      google-chrome
```

Nově SELinux vyžaduje změnu kontextu pro data uživatele, což provedeme
příkazem `chcon`:

```bash
$ cd ~/.config
$ sudo chcon -Rv unconfined_u:object_r:config_home_t:s0 google-chrome
$ ls -dZ google-chrome
drwx------. kuba kuba unconfined_u:object_r:config_home_t:s0 google-chrome
```

  [Chrome help]: http://www.google.com/support/chrome/bin/answer.py?hl=en&answer=95669
