Title: Útočí na mě z...
Date: 2011-12-19 16:00
Slug: utoci-na-me-z

Čas Vánoční je čas pohody, klidu a míru. To platí jen do určité chvíle.
Třeba dokud na váš server nezačnou útočit z ... Číny.

Jedná se o celkem aktuální aférku, o které se (pěkně blbě, takže to ani
nečtěte) rozepsala [Lupa.cz][], nějaké detaily o probíhajících útocích
jsou na [rcnoviny.cz][].  
  
Ochrana proti takovému DDOS útoku není žádná sranda a jako admin
serveru máte jen omezené pole působnosti. Dokud útočníci nezahltí linku
(pak to řešte se svým ISP) a data k vám tak ještě putují, máte jen pár
možností, jak se těch nevyžádaných zbavit:

-   **Omezení počtu současných připojení:** je elegantní řešení. Pokud
    je ale botnet velký, stačí útočníkovi pouze omezený počet spojení a
    stejně vás položí. Naopak můžete omezit uživatele, kteří jsou za
    velkým NATem. Zkusit to ale preventivně můžete:
        
        # zablokování portu 80 (webserver) nad 20 současných připojení
        iptables -A INPUT -p TCP --syn --dport 80 -m connlimit --connlimit-above 20 -j REJECT

-   **Omezení připojení za časový úsek:** má podobné omezení, jako výše
    uvedené.

        # zablokování nových TCP spojení
        iptables -A INPUT -p tcp --syn -m limit --limit 1/s --limit-burst 3 -j RETURN

-   **Omezení přístupu z konkrétní země:** je dobré v případě, že na
    server útočí právě botnet, který je jen (nebo alespoň z podstatné
    části) v jedné konkrétní zemi a zároveň máte to štěstí, že s ní
    nemusíte komunikovat. Veškeré subnety rozdělené podle zemí najdete
    na webu [ipdeny.com][]. Pro omezení příchozích spojení z Číny proto
    provedeme:

        wget http://www.ipdeny.com/ipblocks/data/countries/cn.zone
        while read SUBNET ; do iptables -I INPUT -s $SUBNET -j REJECT ; done < cn.zone

Žádné z výše popsaných řešení není úplně nejlepší, ale může pomoci při
první obraně systému. Další bezpečnostní otázky řešte s dokumentací
systému, manuálem k `iptables` a v neposlední řadě se svým ISP, který za
tučnou úplatu určitě rád pomůže.

Máte nějaké další tipy, jak útokům předejít? Podělte se..

**Zajímavé zdroje:**

-   [http://cs.wikipedia.org/wiki/Botnet][]
-   [http://www.ipdeny.com/ipblocks][]
-   [http://www.cyberciti.biz/faq/iptables-connection-limits-howto/][]
-   [http://www.cyberciti.biz/tips/howto-limit-linux-syn-attacks.html][]

  [Lupa.cz]: http://www.lupa.cz/clanky/tisice-tuzemskych-e-shopu-melo-vypadky-muze-za-to-masivni-ddos-utok/
  [rcnoviny.cz]: http://www.rcnoviny.cz/2011/12/ddos-tok-na-strnky-s-rc-modely/
  [ipdeny.com]: http://www.ipdeny.com/ipblocks/
  [http://cs.wikipedia.org/wiki/Botnet]: http://cs.wikipedia.org/wiki/Botnet
  [http://www.ipdeny.com/ipblocks]: http://www.ipdeny.com/ipblocks
  [http://www.cyberciti.biz/faq/iptables-connection-limits-howto/]: http://www.cyberciti.biz/faq/iptables-connection-limits-howto/
  [http://www.cyberciti.biz/tips/howto-limit-linux-syn-attacks.html]: http://www.cyberciti.biz/tips/howto-limit-linux-syn-attacks.html
