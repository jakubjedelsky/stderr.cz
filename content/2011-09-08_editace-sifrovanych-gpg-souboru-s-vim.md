Title: Editace šifrovaných GPG souborů s vim
Date: 2011-09-08
Author: Jakub Jedelsky
Slug: editace-sifrovanych-gpg-souboru-s-vim

### Motivace

*Začnu zlehka motivací, kterou v klidu můžete přeskočit.*  
Už nějakou chvíli přemýšlím, jak bezpečně uchovávat hesla. Měl jsem na
to jen pár (= dva) požadavků: **bezpečnost** a **dostupnost**.
Bezpečnost je jasná - kromě hesel na "srandastránky" potřebuji uložit
údaje k poměrně citlivým službám. A protože se k heslům potřebuji dostat
nepravidelně jak z kanceláře, tak z domu, tak z nějaké kavárny,
potřebuju nějaké centrální úložiště. Klikátka jsou passé kvůli druhému
požadavku, ukládání do databáze v plaintext na nějakém mém serveru se
zas nekamarádí s prvním požadavkem. A teď babo raď (nebo pište do
komentářů, co používáte vy).

Rozhodnutí padlo na obyčejný texťák zašifrovaný pomocí [GnuPG][]. Jak
jednodché. Tento soubor mám uložený na pracovním pc, který jede nonstop,
takže přes ssh si ho můžu přečíst kdykoliv. Ale přišly další problémy:
jak jej jednoduše editovat? Rozkódovat, přepsat, zakódovat - furt
dokolečka. Admini jsou přece lidé líní..

### vim umí všechno

Mám rád `vim`, protože toho umí spoustu. Třeba rozkódovat, přepsat a
zakódovat GPG soubor - jé, o tom jsem psal o pár řádků výš, jaká náhoda!
Na řešení jsem dnes narazil na [vim wiki][]. Jednoduše si do `~/.vimrc`
přidejte těchto pár řádků:

```vim
" Transparent editing of gpg encrypted files.
augroup encrypted
au!
" First make sure nothing is written to ~/.viminfo while editing
" an encrypted file.
autocmd BufReadPre,FileReadPre      *.gpg set viminfo=
" We don't want a swap file, as it writes unencrypted data to disk
autocmd BufReadPre,FileReadPre      *.gpg set noswapfile
" Switch to binary mode to read the encrypted file
autocmd BufReadPre,FileReadPre      *.gpg set bin
autocmd BufReadPre,FileReadPre      *.gpg let ch_save = &ch|set ch=2
autocmd BufReadPre,FileReadPre      *.gpg let shsave=&sh
autocmd BufReadPre,FileReadPre      *.gpg let &sh='sh'
autocmd BufReadPre,FileReadPre      *.gpg let ch_save = &ch|set ch=2
autocmd BufReadPost,FileReadPost    *.gpg '[,']!gpg --decrypt --default-recipient-self 2> /dev/null
autocmd BufReadPost,FileReadPost    *.gpg let &sh=shsave
" Switch to normal mode for editing
autocmd BufReadPost,FileReadPost    *.gpg set nobin
autocmd BufReadPost,FileReadPost    *.gpg let &ch = ch_save|unlet ch_save
autocmd BufReadPost,FileReadPost    *.gpg execute ":doautocmd BufReadPost " . expand("%:r")
" Convert all text to encrypted text before writing
autocmd BufWritePre,FileWritePre    *.gpg set bin
autocmd BufWritePre,FileWritePre    *.gpg let shsave=&sh
autocmd BufWritePre,FileWritePre    *.gpg let &sh='sh'
autocmd BufWritePre,FileWritePre    *.gpg '[,']!gpg --encrypt --default-recipient-self 2>/dev/null
autocmd BufWritePre,FileWritePre    *.gpg let &sh=shsave
" Undo the encryption so we are back in the normal text, directly
" after the file has been written.
autocmd BufWritePost,FileWritePost  *.gpg silent u
autocmd BufWritePost,FileWritePost  *.gpg set nobin
augroup END
```

A šup s radostí editovat Vaše šifrované soubory. A na závěr poznámka:
pokud používáte více soukromých klíčů, tak myslete na to, že v
konfiguraci se používá přepínač `--default-recipient-self`.

  [GnuPG]: http://cs.wikipedia.org/wiki/GnuPG "GnuPG na Wikipedii"
  [vim wiki]: http://vim.wikia.com/wiki/Edit_gpg_encrypted_files#Related_plugins
    "Edit gpg encrypted files"
