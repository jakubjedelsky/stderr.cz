Title: Jak dostat vlastní RPM do Fedory
Slug: jak-dostat-vlastni-rpm-do-fedory
Date: 2014-04-04

*TL;DR:* Toto není návod na sestavení RPM. Jen jsem si potřeboval utříbit a sepsat postup pro doručení již připraveného balíčku do repozitářů Fedory a EPELu. Ani nechci zabíhat do detailu - většinou odkazuji na příslušnou [wiki](http://fedoraproject.org/wiki/) (ale často jsem se neudržel).

Postup jsem popsal pro balíček `vertica-python`, který si tuto cestu už absolvoval. Hned na začátek doporučuji nastavit filtr e-mailu - do gmailu mi naskákalo celkem kolem 30 zpráv ve 13 vláknech.

### Všechno začíná (a končí) v bugzille

Každý nový balíček se musí pěkně [jmenovat](https://fedoraproject.org/wiki/Packaging:NamingGuidelines) a splnit [pár jednoduchých podmínek](https://fedoraproject.org/wiki/Packaging:ReviewGuidelines), aby prošel kontrolou od některého z jiných vývojářů. Ke komunikaci slouží ticket typu [Review Request](https://bugzilla.redhat.com/bugzilla/enter_bug.cgi?product=Fedora&format=fedora-review), kam kromě základních informací pošlete odkaz své SPEC a SRPM soubory. Pokud jde o váš úplně nejprvnější balík, je potřeba si sehnat svého [sponzora](https://fedoraproject.org/wiki/How_to_get_sponsored_into_the_packager_group), který se za nováčka "zaručí" a bude mu případně pomáhat. Potom, co vám ostatní najdou spoustu chyb, vy je úspěšně opravíte (nebo obhájíte) a někdo nastaví flag `fedora-review` na `+`, zažádáme o nový repozitář.

Žádost o repozitář, ze kterého pak probíhá vlastní sestavení balíku, jde opět formou komentáře do Review Request ticketu. Zároveň s tím změníme flag `fedora-csv` na `?` (aby si nás admini všimli). Komentář vypadá nějak takto, vzor je opět na [wiki](http://fedoraproject.org/wiki/Package_SCM_admin_requests):

```text
New Package SCM Request
=======================
Package Name: vertica-python
Short description: A native python adapter for the Vertica database
Owners: kubo
Branches: f19 f20 el6 epel7
```

K tomu snad jedinou poznámku - větev `master` (pro `rawhide`) dostanete automaticky.

Do pár hodin pak máte odpověď od některého z adminů, že je repozitář připravený, flag `fedora-csv` se změní na `+`.

### Repozitář, sestavení a zveřejnění

Zdrojové kódy se SPEC souborem a případnými patchi (nebo patchemi, patchema? Pačema?) se ukládají do [veřejně přístupného](http://pkgs.fedoraproject.org) `git`ovského repozitáře. Fedora nabízí pro práci (nejen) s tímto repozitářem nástroj `fedpkg`, ale obejdete se i bez něj. Ale ne zde v dalších krocích.

Nejprve si repozitář naklonujeme k sobě...
```bash
fedpkg clone vertica-python
```

...a naimportujeme schválený SRPM balík
```bash
cd vertica-python
fedpkg import /var/lib/mock/fedora-rawhide-x86_64/result/vertica-python-0.2.0-4.fc21.src.rpm
```

Import na nás vyrukuje s logem, který zkontrolujeme a změny [commitneme](http://fedoraproject.org/wiki/Join_the_package_collection_maintainers#Import.2C_Commit.2Cand_Build_Your_Package). Vše pošleme do vzdáleného repozitáře a spustíme build na [koji](http://koji.fedoraproject.org):
```bash
# hele ho, git!
git commit -m "Initial import (#1080669)"
git push
fedpkg build
```

V tuto chvíli se sestavuje balíček pro `rawhide`. Můžeme zatím vesele pokračovat s dalšími větvemi (od nejvyšší verze dolů):

```bash
fedpkg switch-branch f20
git merge master
git push
fedpkg build
fedpkg switch-branch f19
...
..
.
```

V [koji](http://koji.fedoraproject.org) už teď máme uložená sestavení, která (předpokládám) prošla - můžeme tak začít balíček ládovat do repozitářů. Toto probíhá pomocí nástroje [Bodhi](https://admin.fedoraproject.org/updates). Pro všechny větve (kromě `masteru` a aktuálně `epel7`, který je v betě) pošleme požadavek na zařazení do testovacích repozitářů (udělat to lze i přes webové rozhraní Bodhi):
```bash
git checkout f20 # nebo fedpkg switch-branch f20
fedpkg update
```

Update bude chtít vyplnit pár informací. Nás zajímají řádky:

 * `type=` (jde o opravu chyby, vylepšení nebo nový balíček?)
 * `request=` (žádáte o testovací nebo stable repozitář?)
 * `bugs=` (ID v Bugzille)
 * `notes=` (u nového balíčku krátký popis).

Pro `vertica-python` to vypadalo takto:
```bash
[ vertica-python-0.2.0-4.fc20 ]

# bugfix, security, enhancement, newpackage (required)
type=newpackage

# testing, stable
request=testing

# Bug numbers: 1234,9876
bugs=1080669

# Changelog:
# - remove buildrood tag
# - edit dateutil patch for el6 
#
# Here is where you give an explanation of your update. 
notes=A native python adapter for the Vertica database

# Enable request automation based on the stable/unstable karma thresholds
autokarma=True
stable_karma=3
unstable_karma=-3

# Automatically close bugs when this marked as stable
close_bugs=True

# Suggest that users restart after update
suggest_reboot=False
```

Po uložení se žádost zpracuje a dostaneme potvrzení:
```text
Creating a new update for  vertica-python-0.2.0-4.fc20 
Update successfully created
================================================================================
     vertica-python-0.2.0-4.fc20
================================================================================
    Release: Fedora 20
     Status: pending
       Type: newpackage
      Karma: 0
    Request: testing
       Bugs: 1080669 - Review Request: vertica-python - A native Python adapter
           : for the Vertica database
      Notes: A native Python adapter for the Vertica database
  Submitter: kubo
  Submitted: 2014-03-31 13:35:36
   Comments: bodhi - 2014-03-31 13:35:49 (karma 0)
             This update has been submitted for testing by kubo.

  https://admin.fedoraproject.org/updates/vertica-python-0.2.0-4.fc20

```

Na posledním řádku je vidět i odkaz, kde můžete sledovat, jak se požadavek zpracovává a kudy rpm cestuje. Cesta do stabilních repozitářů Fedory trvá týden, pro EPEL jsou to hned týdny dva. Mezitím vám jiní uživatelé (QA) můžou dávat veselý a smutný smajlíky. Za tři veselý se do stabilního repozitáře dostanete hned, dobrý ne?

### Končíme na Bugzille

Kecám. Pokud vše projde jak má a balíček se prokouše až do stabilních repozitářů, pak Bodhli za vás ticket automaticky zavře. Takže se už o nic nemusíte starat.

A na závěr nezbývá než popřát všem RPM balíkům šťastnou cestu.
