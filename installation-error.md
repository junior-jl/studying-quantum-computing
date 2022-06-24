Erro:
```
cysignals must be compiled without _FORTIFY_SOURCE
```

Solution:

```
CFLAGS="-Wp,-U_FORTIFY_SOURCE" pip3 install --user --extra-index-url https://<user>:<pass>@pypi.netsquid.org netsquid
```
