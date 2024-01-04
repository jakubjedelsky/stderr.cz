Title: O mně
Slug: o-mne

### Co je to ten stderr?

```text
NAME
    stdin, stdout, stderr - standard I/O streams
SYNOPSIS
     #include
     extern FILE *stderr;
 
DESCRIPTION
     Under normal circumstances every Unix program has three
     streams opened fot it when it starts up, one for input,
     one for output, and one for printing diagnostic or error
     mesages.
 
     The input stream is referred to as ‘‘standard input’’; the
     output stream is referred to as ‘‘standard output’’; and
     the error stream is referred to as ‘‘standard error’’.
     These terms are abbreviated to form the symbols used to
     refer to these files, namely stdin, stdout, and stderr.
(...)
```
