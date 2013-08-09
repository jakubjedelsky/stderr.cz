Title: Zkroť si svůj cron
Date: 2010-09-16 12:00
Slug: zkrot-si-svuj-cron

V tomto krátkém článku nechci popisovat funkci cronu ani práci s
ním, to si ostatně můžete najít třeba na [wikipedii][]. Chci zde jen ve
třech jednoduchých bodech zdůraznit maličkosti, které by mohly usnadnit
práci jak uživatelům, tak adminům. Ale pozor, ne vše může všude fungovat
- změny konzultujte s dokumentací svého systému.  

1.  **Přehledné plánování:** používejte "dělení" a "od-do". Teď budu
    trošku přehánět, ale předtavte si, že chcete spouštět úlohu každý
    druhý měsíc, v pracovní dny, po 8 hodinách a každých 5 minut.
    Máte-li nyní potřebu vypisovat všechny hodiny, minuty, dny a měsíce
    koukněte na toto:

    ```text
    */5   */8   *   */2   1-5  /cesta/k/programu
    ```

2.  **Usměrněte výstup:** téměř každý spuštěný skript *něco* vypisuje
    nebo ukládá. Pokud se o zpracování tohoto výstupu nepostaráte, pak
    věřte, že půjde do mailboxu uživatele, příp. se vám bude donekonečna
    ukládat na disk. Nejjednodušší je usměrnit výstup do `/dev/null`,
    chcete-li sledovat log, pak jej nezapomeňte rotovat.  
      
      
    Potlačení všech výstupů:

    ```text
    * * * * *     /cesta/k/ukecanemu/skriptu > /dev/null > 2>&1
    ```

    Směrování do logu:

        # vse do jednoho logu
        * * * * *     /cesta/k/ukecanemu/skriptu > /var/log/vas_log 2>&1
        # rozdeleni standardniho vystupu a error logu (stderr)
        * * * * *     /cesta/k/ukecanemu/skriptu > /var/log/vas_log 2> /var/log/vas_error_log

    Pro odesílání výstupu e-mailem slouží proměná MAILTO umístěná v
    samotném crontabu:

    ```text
    MAILTO=vas@email.tld
    * * * * *     /cesta/k/ukecanemu/skriptu
    ```

    Pozor dávejte na programy, které výstup automaticky ukládají.
    Nejčastějším příkladem je `wget`, u kterého vám směřování do
    `/dev/null` nepomůže ani kdybyste se na hlavu stavěli. Zrovna pro
    `wget` použijte přepínač `-O /dev/null`.

3.  **Ochrana před smazáním:** pokud k úpravě cronu používáte příkaz
    `crontab -e`, je možné (mě se to již párkrát stalo a není to nic
    příjemného), že se jednoduše upíšete, místo `-e` kliknete na `-r` a
    celá tabulka je smazaná. Naštěstí existuje přepínač `-i`, který
    zajišťuje optání se před samotným mazáním..

    Do uživatelského souboru `~/.bashrc` tedy stačí přidat jen alias:

    ```bash
    alias crontab="crontab -i"
    ```

Máte nějaké další tipy jak si zjednodušit, zefektivnit nebo zabezpečit
práci s cronem? Podělte se.. :)

  [wikipedii]: http://cs.wikipedia.org/wiki/Cron
