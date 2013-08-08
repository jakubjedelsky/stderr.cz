Title: FTP, FTPS a SFTP
Date: 2013-04-08 00:00
Slug: ftp-ftps-a-sftp

Jen pár slov o každém z těchto tří protokolů, abychom si v tom konečně
udělali pořádek a nemuseli se handrkovat, co kdo vlastně myslel. Ve
všech třech případech jde o protokoly používané pro přenos souborů, to je cajk.

-   **FTP** (*File Transfer Protocol*) je z našich tří nejstarší.
    Protokol byl pro TCP/IP definovaný už v roce 1985 a ke svému
    fungování využívá portů 20 a 21. Jde o jednoduchý protokol,
    využívající pouze [pár příkazů][].
-   **FTPS:** Jde o ten *stejný* jednoduchý protokol FTP, jen je obalený
    vrstvou SSL/TLS (proto "S" na konci, stejně jako u HTTPS). Na straně
    serveru (kde jej většinou obsluhuje stejný daemon jako FTP) musí být
    dostupný a nakonfigurovaný certifikát, klient se pak proti serveru
    autorizuje příkazem `AUTH TLS` (nebo `AUTH SSL`).
-   **SFTP:** Přehozené písmenko a už to dělá zmatky; opět jde o přenos
    souborů, ale se samotným protokolem FTP to nemá (skoro) nic
    společného. Zkratka SFTP znamená *SSH File Transfer Protocol* nebo
    *Secure FTP*. Protokol byl navržený jako rozšíření SSH pro přenos
    souborů, dokáže ale pracovat i nad protokolem jiným, který se kromě
    šifrování musí postarat i o autorizaci.

Takže až budete po svém adminovi chtít připravit SFTP, nezlobte se, že
se se svým oblíbeným FTP programem k serveru nepřipojíte. A vůbec, v
dnešní době už můžete použít [něco rozumnějšího][].

### Více čtení:

- FTP: [na české Wikipedii][], [RFC][]  
- FTPS: [na české Wikipedii][1], [RFC][2]  
- SFTP: [na české Wikipedii][3]

  [pár příkazů]: http://en.wikipedia.org/wiki/File_Transfer_Protocol#List_of_FTP_commands
    "Seznam příkazů FTP, Wikipedie"
  [něco rozumnějšího]: http://cs.wikipedia.org/wiki/Git
  [na české Wikipedii]: http://cs.wikipedia.org/wiki/File_Transfer_Protocol
  [RFC]: http://tools.ietf.org/html/rfc959
  [1]: http://cs.wikipedia.org/wiki/FTPS
  [2]: http://tools.ietf.org/html/rfc4217
  [3]: http://cs.wikipedia.org/wiki/SSH_file_transfer_protocol
