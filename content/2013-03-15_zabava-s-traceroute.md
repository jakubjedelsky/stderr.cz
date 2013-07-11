Title: Zábava s traceroute
Date: 2013-03-15 07:42
Author: Jakub Jedelsky
Slug: zabava-s-traceroute

`traceroute` je užitečný nástroj - projde a vypíše uzly, přes které váš
dotaz prochází, u každého vrátí čas odezvy a ... skončí. Vlastně docela
nuda. Pak jsem ale narazil na tento twít:

<blockquote class="twitter-tweet"><p>Dejte si traceroute na 216.81.59.173 a chvíli si počkejte :)</p>&mdash; Adéla (@adela_cz) <a href="https://twitter.com/adela_cz/statuses/312287606052380672">March 14, 2013</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>
  
Zkuste to:
```text
traceroute -m 120 -q1 216.81.59.173
```

Výsledem bude opět výpis uzlů, ale počkat.. Jak by řekl anonymní
komentující: *"Go home traceroute, you're drunk!"* Po přeskákání
nejblžších uzlů se můžete začíst do úvodu Star Wars: Episode IV. Boží!
Na svědomí si to vzal [Ryan Weber][]. *Vycucnutý výsledek je pod
článkem.*

### Hvězdné války v ASCII

Pokud vás ten úvod navnadil a rádi byste díl viděli celý, zkuste se přes
telnet připojit na towel.blinkenlights.nl.

```text
telnet towel.blinkenlights.nl
```

### Nyan Cat!

Podobná hříčka je [nyan cat][] přes telnet (ňaňání bez zvuku vydržíte
dloho):

```text
telnet miku.acm.uiuc.edu
```

### MUD

Fantazii se meze nekladou. Textových Multi User Dungeonů přes telnet
ještě pár běží (i když nejlepší už asi mají za sebou). Namátkou:

```text
telnet aardmud.org
telnet zombiemud.org
```

### a další ...

Telehack vám řekne vtip, vypočítá příklad nebo spustí traceroute:

```text
telnet telehack.com
```

Výmluvy, proč se spojení ukončilo, nabízí autoři hvězdných válek v ascii
(viz výše):

```text
telnet towel.blinkenlights.nl 666
```

A konečně ten osekaný výpis z traceroute:

```text
    Episode.IV
    A.NEW.HOPE
    It.is.a.period.of.civil.war
    Rebel.spaceships
    striking.from.a.hidden.base
    have.won.their.first.victory
    against.the.evil.Galactic.Empire
    During.the.battle
    Rebel.spies.managed
    to.steal.secret.plans
    to.the.Empires.ultimate.weapon
    the.DEATH.STAR
    an.armored.space.station
    with.enough.power.to
    destroy.an.entire.planet
    Pursued.by.the.Empires
    sinister.agents
    Princess.Leia.races.home
    aboard.her.starship
    custodian.of.the.stolen.plans
    that.can.save.her
    people.and.restore
    freedom.to.the.galaxy
    0-----I-------I-----0
    0------------------0
    0-----------------0
    0----------------0
    0---------------0
    0--------------0
    0-------------0
    0------------0
    0-----------0
    0----------0
    0---------0
    0--------0
    0-------0
    0------0
    0-----0
    0----0
    0---0
    0--0
    0-0
    00
    I
    By.Ryan.Werber
    Blizzards.Breed.CCIE.Creativity
    Please.Try.Again.Tracerote.to.obiwan.scrye.net
    read.more.at.beaglenetworks.net
```

  [Ryan Weber]: http://beaglenetworks.net/post/42707829171/star-wars-traceroute
    "Star Wars Traceroute"
  [nyan cat]: http://www.youtube.com/watch?v=QH2-TGUlwu4 "Nyan Cat"
