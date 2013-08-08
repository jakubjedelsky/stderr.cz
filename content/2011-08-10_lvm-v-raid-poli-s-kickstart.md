Title: LVM v RAID poli s kickstart
Date: 2011-08-10
Slug: lvm-v-raid-poli-s-kickstart

[Anaconda][] při instalaci CentOS 6 pomocí kickstart souboru trpí
zvláštním nešvarem: při rozdělení disků pro použití LVM může zahlásit
chybu *new lv is too large to fit in free space* ([celý výpis chyby][]);
i když to není pravda. Kde je problém?

Začnu tím, jak chci mít disky rozděleny:  
Mějme dva identické disky, které budou v softwarovém RAIDu 1
(mirroring), rozděleny budou na \~250MB /boot a zbytek pro LVM, ve
kterém bude swap a /. Podle [dokumentace][] jsem začal s tímto:

```bash
# initialize and partitioning
clearpart --all --initlabel
part raid.11    --size=256      --asprimary  --ondrive=sda
part raid.12    --size=1 --grow              --ondrive=sda
part raid.21    --size=256      --asprimary  --ondrive=sdb
part raid.22    --size=1 --grow              --ondrive=sdb

# RAID
raid /boot      --fstype ext4   --device md0    --level=RAID1 raid.11 raid.21
raid pv.01      --fstype ext4   --device md1    --level=RAID1 raid.12 raid.22

# LVM
volgroup sysvol pv.01
logvol swap     --vgname=sysvol --fstype=swap   --size=8192        --name=swap
logvol /        --vgname=sysvol --fstype=ext4   --size=1 --grow    --name=root
```

Což skončilo chybou výše zmíněnou, která je už samozřejmě nahlášená v
[Bugzille][]. Po chvilce pročítání problému jsem zjistil, že Anaconda
ignoruje parametr --grow a nedokáže si velikost disku vypočítat. Bere
tak velikost oddílu pro LVM jako 1MB; a tam se 8GB, které tam cpeme pro
swap nevejde. **Heuréka**.

Dočasné řešení (dokud nevyjde CentOS s aktualizovanou instalačkou) je
tedy používat velikost raid oddílu větší než je součet logických svazků
*(např.: 9000 \> 8192 + 1)*:

```bash
part raid.11    --size=256      --asprimary  --ondrive=sda
part raid.12    --size=9000 --grow           --ondrive=sda
part raid.21    --size=256      --asprimary  --ondrive=sdb
part raid.22    --size=9000 --grow           --ondrive=sdb
```

  [Anaconda]: http://fedoraproject.org/wiki/Anaconda
  [celý výpis chyby]: http://pastebin.com/BsrRipue
  [dokumentace]: http://docs.redhat.com/docs/en-US/Red_Hat_Enterprise_Linux/6/html/Installation_Guide/s1-kickstart2-options.html#s2-kickstart2-options-part-examples
    "32.4.1. Advanced Partitioning Example"
  [Bugzille]: https://bugzilla.redhat.com/show_bug.cgi?id=677915
    "Bug 677915"
