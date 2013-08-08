Title: MySQL: unauthenticated user
Date: 2011-12-02 16:00
Slug: mysql-unauthenticated-user

Nedávno jsem narazil na zajímavý problém: MySQL na jednom nepříliš
vytíženém serveru začalo vracet chybu `Too many connections`, i když z
počet spojení běžně stačí s rezervou. Po chvilce pátrání jsme s
programátorem zjistili, že jednou za čas se tam objeví spousta připojení
ze vzdáleného (legitimního) serveru označená jako "unauthenticated
user". Výpis MySQL procesů byl pak plný takovýchto řádek:

```text
| 263718676 | unauthenticated user | 10.0.0.2:51896 | NULL    | Connect     |   NULL | login  | NULL |
```

Po chvilce pátrání jsem zjistil, že nejde o útok - ani nevíte jaká je to
po pár zkušenostech úleva. Chyba byla ve špatné komunikaci s DNS
servery, které dostatečně rychle neodpovídaly.

MySQL se DNS serverů dotazuje téměř při každém uživatelském loginu
(používá sice nějakou vnitřní cache, ale asi to není žádná bomba).
Využívají se k tomu funkce `gethostbyaddr()`, pomocí které se zeptá,
jaký záznam na této IP vězí. Potom nasadí `gethostbyname()` a porovná
vrácenou IP adresu s původní (více rozepsané je to v [dokumentaci][]).
Jednoduché a účinné do okamžku, kdy se zhorší komunikace právě s DNS
servery. Nabízejí se dvě možnosti, jak to vyřešit:

-   **Použijte přepínač [--skip-name-resolve][dokumentaci].** Hodí se
    hlavně v případě, že dopředu nevíte, odkud se k serveru klienti
    připojují. S použitím ale musíte upravit všechny záznamy pro
    povolené uživatele, tak aby ve sloupci Host byly jen IP adresy nebo
    'localhost'.
-   **Zapište záznamy s klienty do `/etc/hosts` souboru.** Funkce
    `gethostbyaddr()` i `gethostbyname()` se nejdříve podívají právě do
    tohoto souboru než aby se dotazovaly jiných serverů. Tato možnost se
    hodí, pokud máte pár jen statických klientů.

Třeba to někomu pomůže..

  [dokumentaci]: http://dev.mysql.com/doc/refman/5.0/en/dns.html
    "MySQL dokumentace"
