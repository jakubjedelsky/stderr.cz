Title: Vsftpd a pasivní mód FTP
Date: 2010-08-24 17:00
Slug: vsftpd-a-pasivni-mod-ftp

[Vsftpd][] je jednoduchý FTP server, jehož kódy jsou poskytovány pod
licencí GPL. Najdete jej snad již ve všech linuxových distribucích a
pomocí něj beží např. i ftp.redhat.com. Proč? Rychlý, bezpečný, stabilní
a s jednoduchou konfigurací. Pro jednodušší řešení jak dělaný.

### Aktivní vs. pasivní mód (režim)

*Z [wikipedie][]:*

> **Aktivní režim**  
>  Na portu TCP/20 jsou přenášena data (data connection). V aktivním
> režimu navazuje připojení pro přenos dat server, klient naslouchá.
> Problém zpravidla nastává v případě, kdy se klient připojuje z
> privátní sítě a jeho IP adresa je překládána (NAT) nebo se nachází za
> firewallem.
>
> **Pasivní režim**  
>  V pasivním režimu navazuje data connection klient, kterému při
> sestavování připojení poslal server svou IP adresu a TCP port, na
> kterém naslouchá.

Obsáhlejší objasnění (i s pěknými obrázky) můžete najít na
[slacksite.com][] (EN).  

### Konfigurace vsftpd

V systému naleznete pouze jeden - pěkně dokumentovaný - soubor (v RHEL a
klonech je to `/etc/vsftpd/vsftpd.conf`).

Je dobré si projet celou konfiguraci. *vsftpd* má například ve výchozím
nastavení povoleno anonymní přihlašování (nastavit na
`anonymous_enable=NO`). Dobré je povolit uživatelům přístup pouze do
jejich složek, aby se Vám nepotulovali po systému (direktiva
`chroot_local_user=YES`).

Samotné nastavení pro pasivní režim je následující:

```text
# passive mode
pasv_enable=YES
pasv_min_port=20000
pasv_max_port=20100
port_enable=YES
```

Kde pomocí `pasv_enable` povolíme pasivní režim, `pasv_min_port` a
`pasv_max_port` stanoví, jaký rozsah portů se bude využívat - jejich
hodnoty musí být mezi 1024 a 65535 (mnou zvolené jsou čistě náhodné).
Direktiva `port_enable` nám povolí jak aktivní, tak pasivní režim.

FTP server je poté nutné restartovat pro znovunačtení konfigurace:

```text
# pro RHEL
$ service vsftpd restart
# pro jiné
$ /etc/init.d/vsftpd restart
```

### Nastavení firewallu

V konfiguraci jsme použili porty 20000 - 20100. Pro `iptables` musíme
tento rozsah povolit a to umožňuje přepínač `--dport`:

```text
$ iptables -A INPUT -p TCP --dport  20000:20100 -j ACCEPT
```

### Zdroj

[Dokumentace RedHat][]u Vám řekne (skoro) vše.

  [Vsftpd]: http://vsftpd.beasts.org/
  [wikipedie]: http://cs.wikipedia.org/wiki/File_Transfer_Protocol
  [slacksite.com]: http://slacksite.com/other/ftp.html
  [Dokumentace RedHat]: https://www.redhat.com/docs/manuals/enterprise/RHEL-3-Manual/ref-guide/s1-ftp-vsftpd-conf.html
