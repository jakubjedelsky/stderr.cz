Title: CentOS: Rozšíření PECL pro PHP 5.2.x a 5.3.x
Date: 2010-12-02 17:39
Slug: centos-rozsireni-pecl-pro-php-5-2-x-a-5-3-x

V základních repozitářích distribuce [CentOS][] 5.5 je dostupná verze
PHP 5.1(.6), která už mnoha zákazníkům (docela pochopitelně) nedostačuje
a požadují verze vyšší. Využít lze jak PHP 5.2.x, kde balíky jsou v
repozitáři CentOS Testing nebo PHP 5.3.x z repozitáře remi.

Pro tyto verze ale většinou neexistují rozšíření PECL ve formě balíku -
nejsou dostupné pomocí yum. Musíme si tedy zkompilovat vlastní (a do
budoucna s tím počítat, protože např. při aktualizaci PHP se může
všechno rozbít..).  

Začneme instalací balíků, které potřebujeme pro instalaci/kompilaci:

```text
$ yum install php-devel gcc php-pear
```

Samotná instalace probíhá pomocí příkazu `pecl`. Pokud tedy chceme
instalovat rozšíření `fileinfo`, použijeme tento příkaz:

```text
$ pecl install fileinfo
```

Upravíme soubor `php.ini`, tak aby se naše rozšíření načetlo:

```text
$ cat /etc/php.d/fileinfo.ini
extension=fileinfo.so
```

A jsme na konci. Stačí znovunačíst nastavení webserveru a vše (by mělo)
funguje jak má.

```text
$ service httpd reload
```

Pro rychlé ověření můžete zkusit zavolat phpinfo z příkazové řádky:

```text
$ php -r "phpinfo();" | grep "fileinfo"
/etc/php.d/fileinfo.ini,
fileinfo
fileinfo support => enabled
```

Úplně jednoduché. PECL se sám postará o co je třeba, ale přece jen je
CentOS postaven nad rpm balíčky, proto někdy v budoucnu ukážu, jak si
takový balíček jednoduše vytvořit.

  [CentOS]: http://www.centos.org
