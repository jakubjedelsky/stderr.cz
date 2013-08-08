Title: MySQL: přidání uživatele a databáze (a pár poznámek)
Date: 2010-12-17
Slug: mysql-pridani-uzivatele-a-databaze-a-par-poznamek

Další článek z velmi nepravidelné série "[Základy administrátora][]" se
zaměřuje na tu úplně nejprvotnější práci s MySQL - vytvoření databáze a
uživatele. Samozřejmě z řádky, pokud máš phpMyAdmin, můžeš si to ručně
naklikat..

Může Ti to připadat jako hloupost, ale věř, že dnes už existuje tolik
služeb, které vyžadují MySQL, že se tyto základní jednoduché příkazy
hodí znát "jako svoje boty". Už jen proto, že naklikání z nějakého
webového/grafického rozhraní jednoduše zdržuje.  
  
Ve všech případech začneme tím, že se přihlásíme na MySQL server (pod
účtem root):

```bash
$ mysql -u root -p -h localhost
Enter password:
mysql>
```

### Jak na databázi

Začněme databází, k jejímu vytvoření použijeme příkaz `CREATE DATABASE`:

```mysql
mysql> CREATE DATABASE jmeno_databaze;
```

Hotovo. Snad ještě zdůrazním, že jméno databáze musí splňovat pár
požadavků:

-   maximální délka je 64 znaků
-   nesmí obsahovat mezeru
-   nesmí obsahovat znaky `/`, `\`, `.` a znaky, které nejsou povolené v
    názvech souborů
-   nejjednodušší je použít anglickou abecedu a znak _ oddělující
    slova

**Pozor na nastavení kódování.** MySQL server může být nastaven
všelijak - při zakládání databáze se Ti může hodit nastavení možného
kódování pomocí `CHARACTER SET` třeba na univerzální UTF-8. Stejně tak
porovnávání se nastavuje pomocí `COLLATE`, v ČR se hodí
`utf8_czech_ci`. Více info o MySQL a jazycích je na [Intervalu][].
Celý příkaz by byl pak:

```mysql
mysql> CREATE DATABASE jmeno_databaze CHARACTER SET utf8 COLLATE utf8_czech_ci;
```

### Jak na uživatele

Vytvoření uživatele je tak jednoduché, že na to zase stačí jeden příkaz:

```mysql
mysql> CREATE USER 'uzivatel'@'localhost' IDENTIFIED BY 'nejake-heslo';
```

V tuto chvíli máte vytvořeného uživatele, který se může z lokálního
stroje(!) přihlásit a...to je skoro vše. Ještě jsme mu nedali práva k
žádné databázi.

Odkud se uživatel přihlašuje nám určuje řetězec za @ - pokud je zde
`'localhost'` nebo `'127.0.0.1'` je přihlášení možné jen z lokálního
stroje. Zadat zde můžeme jak *jméno počítače*, tak *IP adresu*. Chceš-li
vytvořit uživatele, který se může přihlašovat *odkudkoliv*, je třeba
příkaz trošku upravit:

```mysql
mysql> CREATE USER 'uzivatel'@'%' IDENTIFIED BY 'nejake-heslo';
```

Právě znak procenta (`%`) MySQL serveru říká, že tento uživatel se může
přihlásit z jakéhokoliv počítače.

### Jak to dát dohromady

Už máme databázi i uživatele, takže nám zbývá jen je spojit neboli
přiřadit uživateli `uzivatel` práva k databázi `jmeno_databaze`:

```mysql
mysql> GRANT ALL PRIVILEGES ON jmeno_databaze.* TO 'uzivatel'@'localhost';
```

Vytvoření uživatele a přiřazení práv můžeme spojit do jednoho příkazu:

```mysql
mysql> GRANT ALL ON jmeno_databaze.* TO ‘uzivatel’@'localhost' IDENTIFIED BY ‘nejake-heslo’;
```

S právy k databázím není žádná sranda a je dobré je přidělovat s
rozumem. Pro bližší nastudování koukněte do [dokumentace][].

### Zdroje

MySQL Reference Manual: [adding user][]  
MySQL Reference Manual: [create database][]  
Interval.cz: [MySQL - čeština a slovenština][Intervalu]

  [Základy administrátora]: http://dev.stderr.cz/category/zaklady-administratora/
  [Intervalu]: http://interval.cz/clanky/mysql-cestina-a-slovenstina/
  [dokumentace]: http://dev.mysql.com/doc/refman/5.5/en/grant.html
  [adding user]: http://dev.mysql.com/doc/refman/5.1/en/adding-users.html
  [create database]: http://dev.mysql.com/doc/refman/5.0/en/create-database.html
