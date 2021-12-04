# Hej!

`solve.py` lösningar är det jag gjorde första gången (med lite upstädning och ev kommentarer).
`nice.py` är lösningar som jag tog mer tid på för att förbättra.


## Dag 4

Är nöjd med hur [nice.py](4/nice.py) blev snabbare, målet var först att bara snygga till koden.
0.08 sec istället för 0.8 sekunder på min maskin.

Med en Grid klass så kunde jag nu räkna ut vissa saker en enda gång per grid.
Sen använder jag mig mer av `set` också.


## Dag 3

Min [nice.py](3/nice.py) lösning här är jag inte helt nöjd med men det är bättre ändå tror jag.

Att använda for-else är lite obskyrt så vet inte om man egentligen vill använda sig av sånt.
```python
    for i in "...":
        ...
    else:
        raise Exception("...")
```

## Dag 1

[solve.py](1/solve.py) använder en deque som ett "moving window" genom datat och det var så jag löste uppgiften först.
En möjlig förbättring är att använda maxsize så man slipper tänka på att plocka ut element själv.

I python 3.10 finns numera även `itertools.pairwise` som alternativ till `zip(lines, lines[1:])`

```python
    from itertools import pairwise
    print(sum(b > a for a,b in pairwise(lines)))
```