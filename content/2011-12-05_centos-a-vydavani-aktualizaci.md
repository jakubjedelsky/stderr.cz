Title: CentOS a vydávání aktualizací
Date: 2011-12-05 16:44
Author: Jakub Jedelsky
Slug: centos-a-vydavani-aktualizaci

Dnes jen krátce, ale za to se zajímavým odkazem.

Pokud jste uživateli distribuce CentOS, určitě jste si všimli, že
vydávání aktualizací minor verzí se oproti RHELu pořád zpožďuje.
Vývojáři se snaží alespoň hotfixy a security aktualizace distribuovat
přes [Continuous Release repozitář][]. Proč se vývoj táhne [vysvětluje v
maillistu][] Johnny Hughes. Ve zkratce: hledejte za tím rozdělení RHELu
do několika skupin (Server, Workstation, ...), kde ve stejných skupinách
jsou různé balíčky, a zpřísnění politiky pro sdílení některých
souborů/balíčků.

A tak se z CentOS "přebalovačů" stávají opravdoví vývojáři..

  [Continuous Release repozitář]: http://wiki.centos.org/AdditionalResources/Repositories/CR
    "CR Repository"
  [vysvětluje v maillistu]: http://lists.centos.org/pipermail/centos/2011-October/119027.html
    "CentOS maillist"
