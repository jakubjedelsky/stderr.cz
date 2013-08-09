Title: Synchronizace e-mailových účtů (IMAP)
Date: 2010-08-25
Slug: synchronizace-e-mailovych-uctu-imap

Většina uživatelů se ke svým e-mailům nedostane jinak než přes protokol
POP3 nebo IMAP (což vlastně úplně stačí). Problém nastává ve chvíli, kdy
chceme e-maily zálohovat, synchronizovat nebo migrovat jinam. Hodní
správcové nám můžou někam nahrát např. tarball, příp. data zkopírovat
pomocí `rsync`.  
  
Pokud jste ale na takové nenarazili (nebo je nechcete
otravovat, protože mají fakt hodně práce :)), bude se Vám hodit utilitka
napsaná v perlu - `imapsync`. Výhodou je, že ji nemusíte spouštět ani na
jednom ze serverů, můžete tak převést e-maily z Hotmail ke Googlu nebo
jinak dle chuti.

Jak tedy na ni? Nejdříve ji nainstalujeme standardně z repozitáře (balík
se nachází snad ve všech distribucích), připravte se na spoustu
závislostí (ve výsledku ale zabere cca 4MB):

```text
# Debian a klony
$ apt-get install imapsync 
# RHEL a klony
$ yum install imapsync
```

Volby `imapsync` můžeme rozdělit do 3 kategorií: globální, zdrojový
(označovaný jako 1) a cílový (2) server. Před samotným kopírováním je
dobré použít přepínač `--dry`, který provede pouze simulaci a
zkontroluje, zda se lze k serverům připojit a data přesouvat.

Pro připojení je dobré si ujasnit, zda se připojujeme se zabezpečením
SSL (volba `--ssl1` nebo `--ssl2`) a také na jaký port se připojujeme
(`--port1`/`2`). Informace o všech volbách včetně pár příkladů vám dají
[manuálové stránky][]. Já jsem se po chvilce pátrání dostal např k
tomuto:

```text
$ imapsync --syncinternaldates --noauthmd5   
>    --host1 domain.tld --user1 uzivatelske_jmeno --password1 heslo --port1 143   
>    --host2 domena.cz --user2 user@domena.cz --password2 heslo --ssl2
```

  [manuálové stránky]: http://linux.die.net/man/1/imapsync
