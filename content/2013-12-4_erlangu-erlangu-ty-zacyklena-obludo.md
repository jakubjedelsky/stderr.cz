Title: Erlangu, Erlangu, ty zacyklená obludo
Date: 2013-10-29
Slug: erlangu-erlangu-ty-zacyklena-obludo

Jsem fanouškem Fedory, RHELu a od nich odvozených distribucí. Ale RPM, nad kterým tyto distribuce pracují, občas nabízí nepěkná překvapení. Ne chybou samotného principu (mnohdy), ale občas se některý vývojář nechá unést. Zkuste si nainstalovat takový [Erlang](http://www.erlang.org/). `Yum` nenabídne jen jeden balíček se základním prostředím pro vývoj nebo spuštění. On si tam dotáhne hned všechny subbalíčky, které k vývoji ani nepotřebujete (o takovém `unixODBC` nemluvě). Na toto naštěstí už existuje [bug](https://bugzilla.redhat.com/show_bug.cgi?id=784693). Pěkné, ale skrývá se tu ještě jedna vypečenost...

Udělám malou odbočku a zamířím k [Puppetu](http://puppetlabs.com/), který jsem začal využívat. Pokud v něm chci odstranit balíček, použiji něco takového:

```puppet
package { 'mujsuperbalicek':
	ensure	=> absent,
}
```
Na distribucích založených nad RPM pak Puppet použije:

```bash
/bin/rpm -e mujsuperbalicek
```

Výhradu k tomu mám jednu velkou - musíme myslet na všechny závislosti a jednu po druhé sem vypsat, což je dost otravný a zdlouhavý. Teď ale přichází na řadu balík `erlang` - pokud jej chcete pomocí příkazu `rpm` odstranit, zahlásí, že potřebuje nejdřív odstranit `erlang-examples` (proboha, proč?!). Ok, řeknete si v duchu, odstraníme nejprve `erlang-examples` - ale ono to nejde, protože vyžaduje balíček ... počkej si ... `erlang`! No není to zábavné?

Yum si s tím naštěstí poradí, takže puppetům nezbývá nic jiného než tato ošklivost:

```puppet
exec { 'remove-erlang':
	command	=> '/usr/bin/yum -y remove erlang',
	onlyif	=> '/bin/rpm -q erlang'
}
```

Ale abych jen nebrbral, tak už je na to otevřený [bug](https://bugzilla.redhat.com/show_bug.cgi?id=1038314).
