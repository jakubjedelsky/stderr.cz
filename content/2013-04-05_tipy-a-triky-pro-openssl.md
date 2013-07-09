Title: Tipy a triky pro OpenSSL
Date: 2013-04-05 10:00
Author: Jakub Jedelsky
Slug: tipy-a-triky-pro-openssl

Kdo si ještě nevygeneroval svůj self-signed certifikát nebo alespoň CSR
pro certifikační autoritu, jako by nebyl. OpenSSL je opensource
implementace pro SSL a TLS a díky pár příkazům dokážete vygenerovat
klíč, CSR i samotný certifikát. A zpětně pak tyto data zkontrolovat nebo
převést na jiný formát. Jen je vhodné si zapamatovat pár přepínačů a
možností, které se ze začátku nemusí zdát úplně intuitivní. Sepsal jsem
mé nejoblíbenější.  

### Generujeme …

… samotný privátní klíč (RSA):

    openssl genrsa -out klic.key 2048

… CSR s novým klíčem

    openssl req -new -newkey rsa:2048 -nodes -keyout klic.key -out zadost.csr

… CSR s již existujícím klíčem

    openssl req -new -key klic.key -out zadost.csr

… vlastní certifikát (self-signed) bez CSR na jeden rok

    openssl req -x509 -nodes -newkey rsa:2048 -keyout klic.key -days 365 -out certifikat.crt

… vlastní certifikát z CSR

    openssl x509 -req -in zadost.csr -days 356 -signkey podpisovyklic.key -out certifikat.crt

### Kontrolujeme …

… certifikát

    openssl x509 -text -noout -in certifikat.crt

… CSR

    openssl req -text -noout -in zadost.csr

… privátní klíč

    openssl rsa -check -in klic.key

… certifikát webserveru

    openssl s_client -connect dev.stderr.cz:443

Jako malý bonus zkontrolujeme platnost certifikátu webové stránky.
Spustil jsem to pro původní web abych se ujistil, že certifikát je opravdu
už skoro dva měsíce propadlý. Včetně výstupu:

    $ echo "" |\ 
    > openssl s_client -connect dev.stderr.cz:443 2>/dev/null |\
    > openssl x509 -noout -dates
    notBefore=Feb 23 12:58:12 2012 GMT
    notAfter=Feb 22 12:58:12 2013 GMT

### Převádíme …

… PKCS\#12 (.pfx, .p12 které má rád např. MS Exchange) na PEM
(certifikát + privátní klíč v jednom souboru)

    openssl pkcs12 -in certifikat.pfx -out certifikat.pem -nodes

… zpět z certifikátu a klíče na PKCS\#12

    openssl pkcs12 -export -inkey klic.key -in certifikat.crt -out certifikat.pfx

### Zdroje a doporučené čtení:

 * [Dokumentace OpenSSL](http://www.openssl.org/docs/apps/openssl.html)
 * [OpenSSL HOWTOs](http://www.openssl.org/docs/HOWTO/)
