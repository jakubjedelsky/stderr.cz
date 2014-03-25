Title: Docker: Jak jsme se seznámili - 2.díl
Slug: docker-jak-jsme-se-seznamili-2-dil
Date: 2014-03-23

V [první části](http://stderr.cz/docker-jak-jsme-se-seznamili) seznamování jsem skončil dost narychlo. Na jednu stranu jsem nechtěl zatěžovat hlavu váženého čtenáře dlouhým čtením a na druhou jsem psal v noci a už se mi chtělo spát. Zkusím tu tedy dokončit zprovoznění MySQL pod Dockerem (pokud se vám to ještě nepovedlo). Tentokrát vám na začátek dopřeju lehce teorie. Pokračovat pak budu v podobném duchu - z pohledu člověka, který k Dockeru jen lehce přičuchl. Pokud mě doplníte v komentářích jako u prvního dílu (doporučuju přečíst), máte u mě veliký dík!

<center>
![Docker logo](https://www.docker.io/static/img/docker-top-logo.png)
</center>

Mimochodem, Docker [oslavil 20. března první narozeniny](http://blog.docker.io/2014/03/happy-birthday-docker/). Takže vše nej a hodně spokojených uživatelů do dalších let!

### Z praxe k teorii

Více do hloubky jsem se Dockerem začal zabývat až díky komentáři od [AoJ](http://stderr.cz/docker-jak-jsme-se-seznamili#comment-1281963896) - byla tu teda jistá pravděpodobnost, že zkušenějšímu dockeristovi mohly při čtení běhat mžitky před očima. Neručím za to, že to bude lepší. Dovolte mi se, před nastartováním MySQL, lehce otřít o teorii.

#### Obraz versus kontejner

*TL;DR:* Docker rozlišuje mezi obrazem ([Image](http://docs.docker.io/en/latest/terms/image/)), což je neměnný a read-only stav systému, a kontejnerem ([Container](http://docs.docker.io/en/latest/terms/container/)) - read-write vrstvou nad obrazem.

Jednotlivé obrazy se rozlišují pomocí ID, jsou uklády v repozitářích (např. `centos`) a odděleny tagy (např. `6.4`). V okamžiku, kdy nějaký obraz chceme použít, Docker jej vezme a přidá vrstvu [Union File Systému](http://docs.docker.io/en/latest/terms/filesystem/), který už je zapisovatelný. Této vrstvě (ke které jsou připojené nějaké další informace, jako třeba nastavení sítě) se pak říká kontejner.

Kontejner může mít dva stavy: **běžící** (running) a **ukončený** (exited). Běžící je asi pochopitelný - to je ten, kde běží nějaký proces (bash, mysql, ...). Ale ten ukončený (nebo zastavený, chcete-li), ten zmátl nejen mě. Pokud jste totiž z obrazu kontejner pustili, změnili, zastavili a opět spustili, byly všechny změny pryč. Je to právě tím, že jste si druhým spuštěním vytvořili nový kontejner z původního read-only obrazu. Původní kontejner je ale stále uložený - tyto kontejnery si můžete vypsat pomocí `docker ps -a`.

Ukončený kontejner můžete opět nastartovat se všemi parametry (`docker start`), můžete jej smazat (`docker rm`) nebo si změny, které jste udělali, commitnout do obrazu (to je ten `docker commit` z prvního dílu). Commitem si můžete změnit stávající obraz nebo vytvořit nový. Pokud si už chvilku s Dockerem hrajete, pak těch kontejnerů budete mít dost a každý si bere nějaké místo z disku, není od věci je tak promazat:

    :::text
    docker rm $(docker ps -a -q)

### Z teorie zpět k praxi (dokončení)

Skončil jsem tím, že jsem se zkusil připojit k MySQL server. Zareagoval tak, že poslal chybu: `ERROR 1130 (HY000): Host '172.17.42.1' is not allowed to connect to this MySQL server`. Pokud jste se s tím nikdy nesetkali, tak blahopřeju. Chyba neznamená nic jiného, než že uživat root nemá právo k přihlášení z jiného systému (ta zpráva je vlastně docela jasná). Čeká nás tak drobná oprava kontejneru. Vezmu to rychle, protože se víceméně jen opakuji:

 1. Vypneme běžící kontejner
    
    Ten jsem našel a vypnul už posledně, posloží k tomu `docker ps` a `docker stop`.

 2. Přihlásíme se do bashe a pod ním do mysql

    I přihlášení do bashe kontejneru jsme absolvovali, pak jen mysql spustíme a přihlásíme se (protože z 'localhostu' to jde).

        :::text
        $ docker run -t -i centos/mysql /bin/bash
        bash-4.1# service mysqld start
        bash-4.1# mysql -u root
        mysql>

 3. Opravíme práva

    Tady už od Dockeru uhýbám víc než chci, ale pojďme to nastavit (na bezpečnost teď nehledíme):

        :::text
        mysql> GRANT ALL ON *.* TO 'root'@'%';
        mysql> quit;
        bash-4.1# exit

 4. Protože chceme používat původní obraz, commitneme do něj změny

    Další opáčko:

        :::text
        $ docker ps -l
        CONTAINER ID      (...)
        9fcaef7a2b56      (...)
        $ docker commit 9fcaef7a2b56 centos/mysql

 5. A nastartujeme kontejner

        :::text
        $ docker run -p :3306:3306 -d centos/mysql /usr/bin/mysqld_safe

A je hotovo, můžete setřít pot z čela. Pokud se teď zkusíme přihlásit, neměli bychom mít problém a můžeme s mysql vesele pracovat:

    :::text
    $ mysql -u root -h 0.0.0.0
    mysql> 

A příště to všechno zkompletujeme pod jeden [Dockerfile](https://www.docker.io/learn/dockerfile/), abychom to na jiném systému mohli sběhnout všechno na jeden příkaz. Toto je jedna z důležitých věcí, kvůli které je Docker tak oblíbený.
