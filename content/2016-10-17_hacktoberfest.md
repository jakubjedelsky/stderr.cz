Title: Hacktoberfest 
Slug: hacktoberfest
Date: 2016-10-17

Přispějte do opensource projektu a dostanete za to (kromě dobrého pocitu) tričko. Na získání dárku máte už ale jen 14 dní! Během měsíce října totiž probíhá [Hacktoberfest](https://hacktoberfest.digitalocean.com/) - projekt společností DigitalOcean a Github, který má přimět lidi něco pro <abbr title="OpenSouce Software">OSS</abbr> dělat. Abyste odměnu získali, stačí 4 (slovy: čtyři) pull requesty do opensource projektů umístěných na Githubu. A to se vyplatí.

<center>
[![Banner](/images/hacktoberfest_banner.png)](https://hacktoberfest.digitalocean.com/)
</center>

Pokud se chcete zůčastnit, potřebujete pouze účet na Githubu, zaregistrovat se na [stránce projektu](https://hacktoberfest.digitalocean.com) a začít bušit do klávesnice. Bacha na to, že do Hacktoberfestu se počítají pouze pull requesty vytvořené právě na Githubu. Ale klidně přispějte i jinde, je to chválihodné :)

Pojďme se do toho pustit, je to fakt jednoduchý:

Git a Github
===

Git je nástroj pro správu verzí. Github je služba, která podporuje vývoj a sdílení softwaru za pomoci právě `git`u.

Přiznávám, že jsem líný se tu o tom více rozepisovat, protože návodů, kterak používat `git` je asi [bambilión](http://necyklopedie.wikia.com/wiki/Bambilion). Takže - do hloubky jde [Pro Git](https://git-scm.com/book/cs/v1), který má web i v češtině. Pro rychlejší zorientování je třeba web s podtitulem [no deep shit](http://rogerdudler.github.io/git-guide/). A pak [Google](http://lmgtfy.com/?q=how+to+git), že jo.

Github vezmeme zkratkou:

* po registraci si nezapomeňte [nastavit SSH klíč](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/)
* [forkněte](https://help.github.com/articles/fork-a-repo/) si projekt, který chcete upravovat
* vytvořte lokální klon (`git clone`) a vlastní větev (`git branch`)
* upravujte a commitujte
* `git push` do svého forku
* a na závěr [vytvořte pull request](https://help.github.com/articles/creating-a-pull-request/)

Co, kde a jak mám upravovat?
====

Pokud nejste přispěvatelem do nějakého projektu, může být tento krok nejsložitější. Zkusím nabídnout pár možností:

* pokud nějaký OSS program **každodenně používáte**, pak víte o jeho chybách. Zkuste se na ně blíže zaměřit.
* **dokumentace** je jádrem každé knihovny. Chybí vám něco? Zkuste to sami doplnit.
* Github má **vyhledávání**. Zkuste label [hacktoberfest](https://github.com/search?l=&q=state%3Aopen+label%3Ahacktoberfest&ref=advsearch&type=Issues&utf8=%E2%9C%93), [easyfix](https://github.com/search?utf8=%E2%9C%93&q=state%3Aopen+label%3Aeasyfix&type=Issues&ref=searchresults), apod. Umí filtrovat i podle jazyka.
* (tento web je hostovaný na githubu. Kdybyste třeba našli překladfalep... ;) )

Ještě není od věci tomu dodat trošku štábní kultury. Aby <abbr title="Pull Request">PR</abbr> za něco stál, tak by měl:

* mít srozumitelný komentář
* být složený jen ze souvisejících commitů, které mají srozumitelnou commit message
* mít testy (pokud se používají)
* procházet testy
* respektovat coding style projektu
* odpovídat dalším požadavkům, které lze často najít v CONTRIBUTING souboru
* být pouze jeden (tzn. pokud plánujete změnu, použijte force push do stejné větve, neotvírejte zbytečně stejný problém vícekrát)

Kdybyste se chtěli inspirovat, tak moje PR můžete najít v projektech `py3status` ([[1](https://github.com/ultrabug/py3status/pull/505)]) a `asciinema` ([[2](https://github.com/asciinema/asciinema/pull/180)], [[3](https://github.com/asciinema/asciinema/pull/179)], [[4](https://github.com/asciinema/asciinema/pull/181)], ...)

A úplně na závěr prosba: pokud jste se dočetli až sem a zápisek vám k něčemu byl, tak mi dejte vědět. Ať už pull requestem, tak třeba komentářem. Díky.

<center>
![Happy Hacking](/images/hacktoberfest.png)
</center>
