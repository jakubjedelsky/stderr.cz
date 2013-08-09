Title: Python: jak na User-Agent
Date: 2010-10-07 19:00
Slug: python-jak-na-user-agent

V poslední době si "hraju" s Pythonem a mám rozpracované
některé programy, vyžadující data z webu. Pro tuto práci jsem si oblíbil
knihovnu `urllib2`, která nabízí požadovanou funkčnost (je vlastně
nějaká jiná?). Dosud jsem používal jednoduché stažení dat z webu pomocí
`urllib2.urlopen(url)`, ale co když je třeba svoji aplikaci nějak
identifikovat?  
  
K identifikaci klienta připojujícího se pomocí protokolu HTTP (nejen)
slouží [hlavička User-Agent][], která označuje program a verzi (+ může
[další info][]). V pythonní knihovně urllib2 to lze řešit pomocí třídy
[Request][] a funkce `add_header()`. Viz následující kód:

```python
>>> import urllib2
>>> request = urllib2.Request('http://dev.stderr.cz/')
>>> request.add_header('User-Agent','MujSkvelyProgram/0.1')
>>> opener = urllib2.build_opener()
>>> data = opener.open(request).read()
```

Jedinou změna oproti `urllib2.urlopen(url)` je "rozkrokování" neboli
vytvoření samotného dotazu (`request`), přidání hlavičky a zpracování
pomocí openeru ("otvíráku"?). Pomocí *openeru* můžete dále zpracovávat
výjimky, přesměrování a chyby.

  [hlavička User-Agent]: http://www.w3.org/Protocols/HTTP/HTRQ_Headers.html#user-agent
  [další info]: http://www.useragentstring.com/
  [Request]: http://docs.python.org/library/urllib2.html#urllib2.Request
