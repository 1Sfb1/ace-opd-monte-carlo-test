# Schat π met Monte Carlo

Testinzending voor de ACE-opdracht "Schat π met Monte Carlo". Gemaakt om het sollicitantenportaal te testen; geen echte sollicitatie.

## Uitvoeren

```
python -m unittest -v
python monte_carlo.py
```

Alleen de Python-standaardbibliotheek; getest met Python 3.12.

## Uitleg

`estimate_pi(n, seed)` trekt `n` punten in het eenheidsvierkant [0, 1) × [0, 1) en telt hoeveel er in de kwartcirkel x² + y² ≤ 1 vallen.

**De factor 4.** De kwartcirkel met straal 1 heeft oppervlakte π/4; het vierkant heeft oppervlakte 1. De fractie punten binnen de kwartcirkel benadert dus π/4, en vier keer die fractie benadert π.

**Meer punten, stabielere schatting.** Elke schatting is een gemiddelde van toevallige treffers. De spreiding van zo'n gemiddelde neemt af met 1/√n: honderd keer meer punten geeft ongeveer tien keer minder spreiding. Met vaste seeds 1, 2, 3 en 42:

| n | seed 1 | seed 2 | seed 3 | seed 42 |
|---|---|---|---|---|
| 100 | 3.2000 | 3.0000 | 3.0000 | 3.1200 |
| 10 000 | 3.1416 | 3.1356 | 3.1440 | 3.1260 |
| 100 000 | 3.1378 | 3.1436 | 3.1347 | 3.1373 |

Bij 100 punten liggen de uitkomsten 0,2 uit elkaar, bij 100 000 punten minder dan 0,01.

**Reproduceerbaar.** Elke aanroep maakt een eigen `random.Random(seed)` en trekt per punt eerst x, dan y. Dezelfde `n` en `seed` geven daarom altijd dezelfde uitkomst, los van andere code die random gebruikt.

## Bronnen en licenties

Geen externe bronnen of bibliotheken. Code onder de MIT-licentie.

## AI-assistenten

Claude (Anthropic) schreef deze testinzending, inclusief code, tests en README, om het ACE-portaal te testen.
