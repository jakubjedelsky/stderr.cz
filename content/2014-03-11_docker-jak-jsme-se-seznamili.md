Title: Docker: jak jsme se seznámili
Date: 2014-03-11
Slug: docker-jak-jsme-se-seznamili

Dění kolem lehkých linuxových kontejnerů jde spíše kolem mě. Až na [Docker](https://www.docker.io/) - čím déle jej sleduju, tím víc se mi líbí. A konečně jsem se dopracoval i k tomu si s ním trošku pohrát.

<center>
![Docker logo](https://www.docker.io/static/img/docker-top-logo.png)
</center>

*Chvilka nezajímavého povídání:* Potřeboval jsem testovat a upravovat SQL dotazy nad MySQL. Už jsem vyrostl z toho, že si všechno nainstaluju do svého systému a pak nevím, co mi kde běží - snažím se jej naopak udržovat tak nějak v čistotě. Taky se mi s daty nechtělo pracovat na vzdáleném serveru - třeba ve vlaku je připojení dost mizerný. A v neposlední řadě se mi nechtělo kvůli MySQL serveru rozcházet KVM virtualizaci. Takže ideální čas pro Docker. *Konec nezajímavého povídání. Teda jak pro koho...*

Znám pouze základy, takže tu nečekejte připravený Dockerfile (to třeba později, hehe), ale jen "tupý" postup, jak si rozběhnout jednoduchý MySQL server. Zároveň jsem dost línej rozepisovat, co jednotlivé příkazy přesně znamenají. Naštěstí u každého můžete použít `--help` nebo nakouknout do [dokumentace](http://docs.docker.io/en/latest/reference/commandline/).

Vše začíná stažením obrazu (image) systému, který chcete použít. Já vyrůstal s rpm, takže CentOS byla jasná volba:
```text
$ docker pull centos
```
Zkusíme kontejner nastartovat a hned se přepnout do příkazové řádky:
```text
$ docker run -t -i centos /bin/bash
bash-4.1#
```
Systém si zaktualizuju, nainstaluju balíčky, které potřebuju ...
```text
bash-4.1# yum -y update
bash-4.1# yum -y install mysql mysql-server
```
... a zkusím pustit MySQL server (což mi skončilo chybou).
```text
bash-4.1# service mysqld start
/etc/init.d/mysqld: line 23: /etc/sysconfig/network: No such file or directory
```

Tento soubor se načítá jen pro dodatečné funkce; init skript uspokojíme i prázným souborem. Služba pak naběhne jak má:
```text
bash-4.1# touch /etc/sysconfig/network
bash-4.1# service mysqld start
Initializing MySQL database: ...
(...)
Starting mysqld: [  OK  ]
```

Funguje! Jen po odhlášení z kontejneru zjistíte, že nic neběží a že i vytvoření network souboru bylo zbytečné.

Abych si upravený obraz mohl spustit a připojit se na něj, je potřeba změny commitnout (omlouvám se za to cizí slovo, ale nějak mě nenapadá český ekvivalent). Docker pracuje s otisky podobně jako git (odtud ten commit) - nazývá je jednoduše ID. Poslední změněný obraz ukáže příkaz ps:
```text
$ docker ps -l
CONTAINER ID   IMAGE        COMMAND     CREATED         STATUS   PORTS   NAMES
e5055fbceaec   centos:6.4   /bin/bash   9 minutes ago   Exit 0           cocky_brown

```

A o commit se postará příkaz ... wait for it ... commit:
```text
$ docker commit e5055fbceaec centos/mysql
```
Tímto jsme řekli, že změny, které jsou v otisku `e5055fbceaec` chceme uložit pod `centos/mysql`.

Teď už zbývá jen MySQL v kontejneru spustit a přesměrovat si porty:
```text
docker run -d -p :3306:3306 centos/mysql /usr/bin/mysqld_safe
```

A to je vše. Teď se jen musíme ze systému připojit ...
```text
# mysql -u root -h 0.0.0.0
ERROR 1130 (HY000): Host '172.17.42.1' is not allowed to connect to this MySQL server
```
... a zjistíme, že to vlastně úplně nejde. Proč? To nechám na pozorném čtenáři, případně do dalšího článku.

Závěrem snad jen - běžící kontejnery vypíše příkaz `ps` a zastaví `stop`:
```text
$ docker ps
CONTAINER ID        IMAGE                 COMMAND                CREATED              STATUS              PORTS                    NAMES
beae68f2b5a3        centos/mysql:latest   /usr/bin/mysqld_safe   About a minute ago   Up About a minute   0.0.0.0:3306->3306/tcp   focused_nobel
$ docker stop beae68f2b5a3
```
