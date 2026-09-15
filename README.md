# basne.stderr.cz

Básně. Jedna báseň na obrazovku, další čeká pod ní rozostřená.

## Nová báseň

Nový soubor `content/RRRR-MM-DD-slug.md`:

```
Title: Název básně
Slug: nazev-basne
Date: 2026-09-15

první řádek
druhý řádek

druhá strofa
```

Jeden konec řádku = zlom řádku (`nl2br`), prázdný řádek = nová strofa.
Básně se řadí od nejnovější. Každá má vlastní odkaz `basne.stderr.cz/#slug`.

## Build

```
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
./build.sh html
./build.sh serve     # http://localhost:8000
./build.sh regenerate
```

Publikuje se samo přes `.github/workflows/publish.yml` při pushi do `main`.
