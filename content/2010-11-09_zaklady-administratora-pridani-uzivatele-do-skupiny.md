Title: Základy administrátora: přidání uživatele do skupiny
Date: 2010-11-09 15:54
Slug: zaklady-administratora-pridani-uzivatele-do-skupiny

*Toto je úvodní řeč, kterou můžete ignorovat a skočit rovnou na
samotný článek.*

Nemám rád takové ty řeči jako *"ode dneška Vás budu pravidelně
informovat ..."* nebo *"na tomot blogu budu psát o ..."*, protože to pak
vždycky dopadne stejně: po chvíli (většinou po prvním, úvodním, článku)
to autora přestane bavit a s pravidelným informováním nebo *"super novým
seriálem o ..."* je konec. A tak začnu trošku jinak:

Během práce si dělám poznámky, které příkazy a věci potřebuji jako
systémový administrátor řešit častěji (rozuměj denně) - dovoluji si tak
tvrdit, že jsou potřeba jako **minimální základ každého, kdo chce na
podobné pozici obstát**. A postupně, těžce nepravidelně a dle nálady, to
zde budu publikovat. Většinu věcí lze vygůglovat, to né že ne (i já je
gůglím a zdroje zde samozřejmě budu uvádět), jen to tak nějak shromáždím
na jednom místě a česky (snad). Kategorii jsem si nazval *Základy
administrátora* a určitě je všem jasné, že to bude o Linuxu. Jen dodám,
že většina věcí bude zaměřena na [CentOS][]/[RHEL][], i když základní
příkazy by měly fungovat všude stejně. Ale už konec tlachání..  

Práce s uživateli a skupinami
-----------------------------

Přiřadit uživatele do skupiny můžeme dvěma základními příkazy
`useradd/adduser` a `usermod`. `useradd` (`adduser` je symlink) vytváří
nového systémového uživatele a pomocí přepínačů můžeme upravovat jeho
základní nastavení jako např. domovský adresář (`-d, --home`) nebo login
shell (`-s, --shell`). Oproti tomu `usermod` se stará o uživatele
stávající.

Informace o uživatelích jsou uloženy v souboru `/etc/passwd`, skupiny
můžete najít v `/etc/group`.

### Použití useradd

Při vytváření uživatele můžeme zařazení do skupiny zadat pomocí
přepínače `-G, --groups`. Chceme-li tedy vytvořit uživatele `rex` a
zároveň jej zařadit do skupiny `dynosauri` použijeme:

```text
$ useradd -G dynosauri rex
```

Uživatele můžeme přidat do více skupin najednou, stačí je oddělit
čárkami (bez mezery):

```text
$ useradd -G dynosauri,prvohory rex
```

Tyto skupiny ale již musí existovat, přesvědčit se o tom můžeme v
souboru `/etc/group`.

### Použití usermod

Jak jsem zmínil výše, příkaz `usermod` pracuje s již existujícími účty.
Pro práci se skupinami využijeme přepínače `-a, -G` a `-g`. Pokud tedy
chceme uživatele `rex` zařadit do skupiny `prvohory` použijeme:

```text
$ usermod -a -G prvohory rex
```

Samozřejmě lze změnit i uživatelovu primární skupinu (která má většinou
stejné jméno jako je jméno uživatele):

```text
$ usermod -g dynosauri rex
```

### Zdroj

    man useradd
    man usermod

web [cyberciti.biz][]

  [CentOS]: http://www.centos.org
  [RHEL]: http://www.redhat.com
  [cyberciti.biz]: http://www.cyberciti.biz/faq/howto-linux-add-user-to-group/
