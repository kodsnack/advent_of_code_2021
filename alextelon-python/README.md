# Hej!

`solve.py` lösningar är det jag gjorde första gången (med lite upstädning och ev kommentarer).
`nice.py` är lösningar som jag tog mer tid på för att förbättra.

Nedan är lite tankar jag haft kring några av lösningarna.

## Dag 5

Är riktigt nöjd med [nice.py](5/nice.py).

Skapade en egen range funktion så jag slipper tänka på om serien växer eller inte samt hur man ska garantera att ändarna kommer med.

    my_range(3, 0) -> 3, 2, 1, 0
    my_range(0, 3) -> 0, 1, 2, 3

Med `Counter` och `my_range` så blir logiken för axiala och diagonala kort och koncis. 

Parsningen blev med `open('input.txt').read().replace('->', ',')` lite smidigare då alla rader blir 4 komma separerade värden.

Man kan tycka det är onödigt att använda product här:
```python
    elif axial:
        count.update(product(my_range(x, xx), my_range(y, yy)))
```

En enklare lösning (som ej kräver itertools import) hade kunnat se ut så här:
```python
    for i in my_range(x, xx):
        for j in my_range(y, yy):
            count[(i,j)] += 1
```
Anledningen att jag skrev som jag skrev är **inte** främst att det är färre rader. Det är att jag slipper hitta på bra namn åt variabel `i` och `j` ovan.

![drake meme](drake-meme.jpg)

Här är dock ett exempel på vart jag **inte** göra en oneliner och behövde därför hitta på namnet `data`. Men här hade en oneliner känts lite för mycket tycker jag. Dessutom var det ett enkelt temporärt variabelnamn att hitta på.
```python
    data = open('input.txt').read().replace('->', ',')
    for line in data.splitlines():
```
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