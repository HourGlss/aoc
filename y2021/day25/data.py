test_input = """v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>"""

real_input = """.......v>vv....>..v.....>.vv...vvv..>.v>vv..>v.v...>>v...>.v>>.v.v...v.>>v..v.>.v...v.v..>v..>..>..v>.....>v>..>>.>>>.....>..>.......>>>v..
>.vv>.>.v.>..vv>>.>v>>.vv.v.>>v>...v...vv>>>vv.v.v.v>...>>.v....v>.vv>...v....>.>...v..v.>.v...v.>...v...>.vv>.v..v>v>.v...>>v>.vvv.v>>>..v
.v.>v>.v>.....v.>....v>.>v>>.v...vv.vv..v......>>..>>..v>vvv.>v>>.>v...>.v....v..v.vv.vv.v>>.v...vv..>....vvvv...>.>>.v>..v.vv.>.v.v>......
>v>v>vv>v>.v..v>v.vv..v>>..>vv.>>v...>.vv.v.........v>>..v>>v>...v...v...>.v..v....v.v..>>..>..>v>>vvv>.>v.>>.....>.vv...>.>>...>.v...vv.>v
.v.v...>vv...v....v..>..>..>...vv..v..v..>....v>v..........>....>.>>.....v....>.>.>.>v.>.>v>...vv>>.v..v>..v.>>>......>>.>.v.v.>>....>>.>.>
......>.....v.v..>....>..v...>>>....v.vv..v....>...>.>.v...>...vv...v..>.>..v>....>.>>..>>>.>.>....>..v>v..>>>..>.vv.....>..v.>v..v.v..>>>>
..v...>.....vv.vv..>.>......v>>>>>....v>v...v.v>..v>.>>..v..vvvv..>...v...v.v.v..>.>>>vv..>>..>>.vv.>..v..v..vv>.....v..v.v.>vv..vv>.>>..>v
>.v...>>>vv>>.....>vv.>>.v>.v..v>v..v..v>.vvv..>.v>....>.vv>v>.v.>>..v>.v>.....>...v>.>>.>..>.>vv...>>vv.>.>>vv>..vv>.>..>....>.>v.>>vvv...
.v.>v..v>..>.vv>vv.>>...v>.v.>v.vv>>.>v>v>vvv..>..>.>vv>>.v.....v.....v.>..v..vv.v....v.v>>..>..>.>..>.>>v....>..v>..v.v.>>....>.v.v>v..v..
...>>....v.v..vvvv>v.>>..>>vvv.>v>.>>>v>v.>v..v>...v>..v..>..vv.vv....>>vvvv..vvv.v..v...>.......>>.>v>vvv...vv>>..v.>.>.>.vv.v.>..v..v>vvv
v>>v.>vv.>v.>..vv>.>.v>....>......>>v.>..>>..>vv>.>...vv....>.>.>...v...v.vv>.vv..vv>v>.>>.v>>v.>..>.v.>v.>.vvv..>....>>v>.v....>v...v.v>.v
..v....>.v>>vvv..v...vvvvv>.>...>..>>......v>.>>.vvv..vv>.vv>v...v..>v.>..>..v..v>v>....>..>.>.>>>...vv.v.v....>>...>v...>.v>.vv..>>>......
v>>.>.v...>v...v.>>...>>.v>>vv......>.>.v.....>v.>vv..>.>..>>>.v.>v.....v.v.>...>>...>.>>>.vv>......v..>.v..>vvv....>.v.>vv>vv>v.>v>>>.>>v.
.v>>>>v.>...vv>v>..v.vvv..v....vvvvv>>..>v>...v.>....>>.v>.>.v..v.v.v.....>.vv..>v.........vvv...v>>>>v>v>>>>.v..>...>v.>......v.>.>.v.v.v.
>>.>v.v....>.v..v.>v.>v..v>..>.v..>>.vv.>..>v>>.v.>...>vv.vvv.>.v.>v>v.v..>..>..>>...v....vvv.v>...>.>..v..>.vv..>.v>.vvv.>>>v>.>.>>...v.>>
>...>>.vv...vv.>>..v>v....>v>>v..v.>...>>...v..>vvvvv.v>..>..v>...vv>.v.>.vv>>.>..v>..>..>vv.v.>.>...>.vv>.v.v>.>v>v....>v>.v.v...>v.>.....
v.v.vv.vvv>.v>...>..>>v..v....v..>>v......v..vv>v>>v>..v..>.>.>v...v>v.v>vv....>vv..>>>vv...>..>...vv.>.v>v.v>v>v..v>.>v.>v.v..v>>vv..v.>.v
>v.>>vv>>...>>>>>>>vv>...>.>...v.>..vv.....>.v........>.>.v>>>v>v...v.vv.v...>>v..>..v..v.>...>v.v>vv.vvv..vv>v.v...v.>>.v>..>>>......vvvv.
.v..>v.......>>...>.v......>..>.vv.v>..>.>....v.>.>vv>>.>.>.v>>.......>>>.v>.>.>>v..>.vv.v...v>v..vvvvv..v.>.>.vv.>..vv.v.>..v>.....>vvvv.>
>>vv..>vv.v.....vv..v>v...>.>....v>vv>>.>v.v.>v...v.....v..>..>.v.>vv.>.vv>.v..v..v>v.v.>.v>>>v.vv.>>v.>>v>..>..>.v....>>.>>vv.v..>>....v..
>v..>v....>v.>v..v.>....v.v.vvv.>v.>..v..>>..>...>.v...>>>.>.v>.v>.v.vv..v.>v.v>>.v..>>vv>v.>..v.v..v..v>..vvv>>v.>>v>.....v......vv.>>>.>>
>..>.>>v.>.v>..v.v.v>v...>v.>>v.v...v..v.vv.>>.>v.v...v...>v.v.vv.v....v>>vv.>..vv....v.v>v>>....v...v..v>.vvvv.v...v..v.v........>>..vvv.v
>..v..>.vvv.v.>.vvv>.vvvv.....v>v..>..>>.>>vvv>v....>....>....v...>...v...v.>.>...v>v......>.v...>...v.....>>......>..>v.>.v>....v>......v.
v..>..>vv..>v>........v.>>v.v>..v>....>.v.>>..>v>.v>..>..>.>v.>>>.>v..>v.v.>.>.v.>vv...v..v.v..>.vv.>v.v..v>...vv>>........v.>.>....v...>vv
...>.v......v>>.>.v.v...vv>>.>>v.v>vv..v.......v..>.>>>.v.v..vv>>.>>.v..>>>..v..>vv.v..>..>v..vv>>>v>.v...>.v.vvvvv>.v>.>>>>>>v>.>.v>v>v.v.
v>.v.>.vv>>.>..v.v>..v>.>..>v.>v>.>v.>>..v.v>..v.>...v.v.....v>...v...vv.v.v>v.v>...>.vv>>.........vv.vvv....v.>>>>>>v.v.v>.vv.>v...>v.vv>>
.vv.v.>v.>....v>v.>vv>.vvvv>vv.>...>..>.>v>...>.>>..>v>v.>>.....v..vvv>.v.>.vvvv>.>.>..v.....v..>>.v...>>.v..>v.v>..>>..>..v..>>....v.>>v.>
vv.v....v>.v.>..>.vv>..>.>.vvv.v.vv>v.v.......>.v.>..v...>.v.>..>........v>>.>>.>>......v....>v.v>v>v..>>.v..>.....>>>>>>>.....v.>.....>>v.
v...>vv...v>vv>v.>v.>.>>.v..>..v>v>.vvv..v.>..>>vv..>v.v.>.....>......vvv>.v.>...vv>v....vvv..>>.>vv>v.....vv...>..>.>.>v..>v..v......>.v.>
.>v.....>.>vvvv...vv.v>.vv.>.>>v..v.>.v.>>.>.v>>>>.v..vvv>.v.v..>.>v>>.>..>v..v.>...>.v...>>v...v>..>.>vv.>v>..v.>v.v....>.v.vv>>..v>>v..v>
...v.v...vvv.v.>.>..v>>>>..vvv>.>..>v..v.>v.v....v>v>..>>vv....>..>.>.vv.v...v>>..>.vv..>>vv...>.v.vv>>.>>>>>..>.v...vv.vv.....>..>.v>v.>>.
.>.v.....>v.>..v>>>.v>...v.>..>.>>v..vvv...v.>..v>v......>..v....v.vv..>vv..v.>...v.v..>.>.>..>v.v.>..v.>>v>.vv....>...vv>......>vv.>.>>v>.
v>.>..v>>>...v>.v.>......>>.v>v..>>.>.v.v.>..>>.......>vv.>>v.>v>.v.v.v..v>v.>>.v...>..>v..>.>..>>.v>v....>.v...>>.>.v.v...>>.v...>..>.....
>>>v.>...>vvv>>.>.v.v>.....v>v.>.v..>>v.>v>v.v.vv....>.>>.v..v..vvv........>.>vv>v.>v.v.v.>.>.>>.v>>>>>>v.>.vv>..v..>..v..>........>.>.>.>>
>.>..vvvvv.>..>>...>..v..>.>>>.>.v..>>..>.v.>....v...>>>vv.>v....>.....>.>.v.>..>>...........>.>..>..>v>.vv..>>...v>v.>....v.>..vvv...v....
....v>....>v.>.......v.v....v.>v.v...vv>>.v.>v...>>>>.>v>..>.>>.v>.>v.v>vv>.>v...v...vvv.v......v..>>>v.....v..>v......vv...>vv.....>>..>vv
.>>.v>>>vv.v>v>v.v.....v..vvvv...>.vv>.>v........v>.v..>.vvvv>..>v..>.v...>.v.vvv.>.>...v>>>v.....>.v.v>>vv.v..>v>>.>.>v..>.>vvv.........>.
v.vv>v>..v..v..>.v>.v.>..vvv>>>..>..v.>v...vv>.vv..v.>.>vv>>.v.vv>>vvv>>.>v.v..>v.>v.vvv..>...>.>.>.>..v>....vvv..>>>..>.>.v..v..>>..v.>>.>
.vv>..vv..v.>....>.>..>v>v>v>...>.v>v.v...v..vv>.>...>.v.>...vv.v.vv.>vv..>....v>...v>.>.v>.vv.>>v...v>..>>.>vv>.vv......>v.v.vv..v.v..vv.v
.vv.v..v.>...v.v...v...v.>..>v.v.v>>.vvv.>>.>v.>>.>.>..v...vv.>>.v>..>.vv...>>.v.....v>..v.>>v>v..v.v..v.>>v..>vv....vvvvv.>...v.>v>>v.>.>.
v.v.>>>>..vvv>.>.v.v.vv>..vvvv......>>.>.>..v>..v>.v.>v>>..v>>>>..>.v.v>.vvv..v>.........>...vv.....>vvv.>v.......v...v>v>.>.>v.v>....vv...
v>v..>.>..>v.>.v.v.>v>>>.>.>..>.........vvvv.>.>.v....>>>.v>..v>.>.>..>v.>.v>>>vvv.>.....>>.v.>...v.v>v>.v>>>.>...>>>v.vv>.>.v>>>>.v.>...>>
vv..>.v>vv>>.v>...>vv....>v>.v..>.v.v.>.......v.>...vvv>>vv>.vv.v>>..vv..vvv....v..v>>>...>v>>...>v>..>>>..v..>..v...>....vvv.....v.>v..>>>
...>.v>...>.>...v...>.v.....v..>.v>v>>.v..>..v>>.>>>.>vv...>vv.v..v....>.v.>vv..>.>..v....vv>..v.....>>.>.vv...>.v..>..v.>..v..>.v......v.>
....v>.v>.....>>v>vvv.v>>>v>>.v.v.>..vvv.>>.>.>.>.>>v.v.>>.>.>..>>.v>.v.v..>...vvvv>.v.>>.v>vv..>v>.>>.>v...v.>>.vv.v..>>.>>>>...vvv.vv>.>.
v.v>..v>...vv..vv..v.>v>>vv.>v.>....>..>vv...v.>>..v.>>.>.v>v.>>vv>>>>v......>>v>v..v.>...v.>v>.>.>.>>>vv.v.v>v.>.>v>.vv>.v>.....>.>vv>.>>>
v.>v>.>>v>.>.>v>.>vv>......vv>>..>>.>vvv..v.v.>>>.v.>v.v.>..>>....>>.v..>>...>...v........v>v....v>.>v.vv.>>.vv>v.vv>v.v>.>>.vv....vvvvvv..
.vvvv>>..v.>>.>..>..>.>.>.v.>..>v>..v..v>.v>.>>v...v...>...v.v.>>>v....>v.v..v...>..v..>>.......>>.v..>vv..>vv.....>>>.....v.>>...>.>v.>...
.>>.>.>.vv>.>.....v>v...>v.v>vv>...>...>.....>...v...v.>.vv>>v>.>>v...>..v>....>..>...v..>...vv>.v..v..>vv..>.vvvv>v..>.>v.>..vv>....v..>.>
.v...>...>.v..v..>>.>..........>..v.>.vv..>..v..vvvvv......>>vvv>v.>.>>.>.....>.v>.>v.>....vvvv.>v.>.>..>.v..v>v.vv>v>.>>>..vvv...>..v.v.>.
vv.v.....>>.>>v>>v.>......v>v>>>.vv...>v.>v....>..vvv..>v>...>..>v.>>.>>.vv....vvv.v>vv>..v>>.....vv..v>v.>.v....vv....vvv.>.vv.v.>>..>.>.>
.v>.>..v..>vv.>v..>v..>v.vv.....v>>>v.vv>>..>.>>>.vvvvvv..v.v..>>.......>.vv>>>v>v>...v>>.>.>.v>.v.v.v.>>.v>.>>.>v>.vv>..v>.vv...v.>v>v>v.>
.v>v.v.v>v>.>.>.v>v..>..>>.v...v>>..>vvv.v>>v>.>.v..>>..vv..>..>>.vv.v.v.>>>...>v>..>.....v.vv.>.>vv>>..vv..v....vv.v...v>>vv>....v.>vv..>.
.>>.>...v..v.>>....v.>>vvvv...>>..>.>v.v>vv..>v.vvv..vv...>>....v.v..v.>v>.>>.v..vv.v..>..>v>v>..>.v..>..v...v.v..>v..>vv..>.v>....>v..vvvv
>.v.>>>>v>>....v.vv..>.....v>v.v..>.>v.>...v>>v..>>.v>vv.vv>.v.>.v.v..v>.>v>>......vv>>..v.>....>v>>>.>v.>>.v.v..v>.vv.v.>..>..>>.>vv...v.>
v...vv...>..v.>.>.v>.v.>..>vvvv>..v>v....vv>v.>.>..v>>.v>.>>...>.v>.>v>>......>..v>>v.v......v.v>..>.>>..>....>v...v.vv.>....>vv.v.v...v>v>
.>>>>>...v.v>.>.>......>.v>v>.....vv..vv.>.v..>.v.>>>....v......>......>>.>>v.>v..>.>..>.>.>..v>vvvv..v...>v..v.>.>.>>vvv>...vv..>v>>..>.>.
.v..v.vv>...>>v.>vv>vvv.>.......>v..>..>.v>>...>.>>vvv.v....v......>>.>.>>.vv.>..>.v....v..vv>..v>..>vv.>vv...v..v>.v>v>>>>.>>.>.v.>v....v.
.v..>v.v>>..>v>vvv..>>v>..vvv>v>.>..>.>>>..>...vv.>v>vv...>.>>v.>...>.>.v.v.>>.>v...>vv>..v.>.v.>..>>v.......v>..>v..>>..........>>vvv>..v.
.....v..v..v.>>.>vv.>>>>.....vvvvvv.....>..>>...v.>>>>>.vvvvv>>.v>.>v.v>.>..v.>v.>..>....>...>.v..v..>..v....v....>.v>.v>>v....>..>.v.v..v.
v.v.>....vvv.>>v.>.>..v>v>>...>.vv>v>>>v..>>>>...v>v..v.v>v..v>..>>...v>v>..vv...>v..>>vv.>>>v.>....>v>..>>.v.....>.>.v>v...>..........>v.>
>.>>....>.v.>.>>>.v>.v...v.vv.vv>...v.>...>>>>vv.>..>>...>>>...>v>..>.....v.v>..v..v..>v>.....v>..>...v>>..v..>vv.v.v...>v.>.>>>..v.v.>v...
.....>vv.>....>>>vvv.>..v..v>.v.v>vv.vv>.>>...v>...v.v.>.>v>.vvv.>.>v>>>.>v.vv..>>...>.vv...>>.vv....v...v>vvvv.>v.>.vv.v...vv..vv.>...vv>>
v.v.>.vvv>......>.>..v...v>>v.>.>.v..>...v>.>.>...vv.v......>v>.v.v.v>...>..>vvv>v.v......>.>..>v.>>>.vvvvv>>>...v........>v.>v>.v.>v>.>>.>
...v..vvvvvvvvv.v..v>>v..v.v..v....>...vv...v..>.>v>>.>...v>>..>>v...v.vvvv.>v..v..v.....v.v....vv.v..>v..v>vv..v>>..v>>.vv..v.v.>v>>>>.vvv
...v>..>>..>>v..>....v..>>.>v.vv.>v>>.>.v>....>v.....v...>>>v..>.>..v..v>.v.>.v.>v.v>v>v....v>..v>...v>v...vvvvv>.>vv>>.v.vvv.>..v..>>.v...
.>..>>.v>>>.>.v.v.v>.>.v.v..v>v>..>v...>v>>.>vvv...v..v>.>.>v....>vv..v...>v.v.v.>.v.>v..>.v>.>.....v.v.>v>.v...v>.>.>......vvv>...>.v.....
>.vv>.>>vvv......>.>..>>.....>>.v..>vvv>.>>..>v..vv..>......>v>.>..vv>v.>v.>.>v.vvv>vv..>v.v.>>>..vv>...>v....v>.v..vvvvvvv...v>.......v...
....vv>.>vv>..>>......v...>v>.>v>.vv>..>>...vv>.v>v.>.>v.>.>vv...v...>.v.vvv>..>.>>>.>v.vv>v.v..vv>.>>.v...v>.>v..vv>.....v..>.>......>.v..
v.>..v..v>v>v..>v>>v>vvv>vv..v....>.v....v...v>v>>>..>..>>.vvv..v>.>>v>..>......>..v.vv.v.>..>v>vv.>>>.>.vv.v..>..v>vv.v.>.v>...vv>>..v>.v.
v.v>>>>....>>.vv..v....>.vv..v>.vv>v>vvv....>..v.v.>v..v..>>v>...>>..v.>v.v...........>.v...>>>>.>v>v..>>..>v...v.v.vv.v>vv..v.vv.v.vv>>>.v
v.........>.vv>v>.v...>>>....v>..v.v.>vv.>.>.v>vvvv>v.v..v>>>>>>>>>>>...>.>vvv..>v>..v....>.v>>.>>v...v.....v..>>.>>v.vv.>.vv..v>..>.v>vv..
.v>vv>v.v.v>..v.>...>>..v.>>.>...>.vv.....>>v>.v>....vv.v>.>.>...v>>>..>....>...v>v..v>>vv>..v.v.>vv.v>....vvvv.>>>v..v..>vv...v.......v..v
.>..>vv>.>...v>v.vv>>v..>..v.>vv..>..v>>>...v.v...v>.v...vv....vv...>v.>>..>>v.>..v.v.v.v.>.v>v.v>v.>...>.>.v>.>..>v>.v..>.>..vvv>..vv.v.vv
v.>v.vv.v>.>.>...>..v.......>..v.>...>v.v..>v..v>>v>>...v>...vv>v...>.>>v..v.>....>.>.>.v.>>...>>>.v..>.v...>v.v>vv>>..v.vvv.v..>...>>>..>.
v>.v>..v.v.>>.vvv.vv>..>.>.......v>.v.....>..>...>.v..vv>v.v..>v>v.>>..>>..>>.....v......>..v>>.>>.v>vvv>v.....vv.v.>.vvv>v>v...>..>>>.>>>.
v.v.>....>>vv.v.v.vv>v>.v..>>.>v>v..>.vv>.v..>.>..v.vv.....v..>.>>.>>v.v..>v..v..v.....>>.v>v>...v.....>.....>..vvv....>...v>>>..>....>>..>
>..>...v>..v>v>vvv>....v.>v..v.>v>v.v>>.....v.>v>>v.>.>v>.>...v>>>.v..v>.v>.vvv...vvv.......v.>>.>..v.>......v>v..>.>.>>....>>..v.v>v.vv.>.
......>>...>......v>....v..>..>.>...v>v>..>vv.v.>>...v>>...v>.v.>>.v>..>.vv.v.>>....>vv.>>.vv...>vv>v..>>v>v...>>.>.v..>v.vv......>.v.>.vv.
.>.vvv...v>..>...vv..>>...vv.v.>v......v>.>.....>..v.v>.v>.>......v.v..vv.>..v..>....vv.>.>>..>.>.>v>.>..vv.vv.>>v..v>..>..>......>v..>..v>
...v.>>.>.>>..>....v>......v..vv.v>.vvv>.>..>.>vv.vv.vvv>..>>.vv..>..v.v...v..vv....v>...v>.v.>.vvvv.>..vv.....>>..v..>>.....vv...>.>v.>.>.
vv.vv..vv>vvv..>...vv.vvv.>..vv....>..v>.....vv.v..v.>.v.vv>>.>>.......v>.>.>.>v...vvv>..v..>...>>.>..>>.v.>v>>v.v>.v.>>.....>.>>.v..v...vv
v.>>v..vv..vv...>v...>v......v.vv>.>....v.>......vv>.>.>v>v>.>vv.vvv.v.vv>vv.>.v.v..v......>v.>..>v>..>..v.v>vv.>....vv>.vv>..v..>v>v.v>>v.
...v>>...>v>..v.>.>..>>>...v>v.vv.vv>...vv.v...>>v.v>...>...v>>.>v>..>>...>......>>v.v>vv>v...vvv.>....>.v.v.v>..>>>.v>>vv>.....>vvvv>>..>.
.v.vv>>..vv...>..v>>vv>v>....v.....v...v>>.v.v..>vv...v>>v.v.>.>v..>>>.>.....>..v...>.vv>.>>...vv....>vv.vv....>>.vvv>v>.v>.vv>>..>v..>>vv>
>..v......>..v>.>.>>>.>v.>.vv..v.>>v>>>..>..v>v..>...>..>>.>.v.>vv..v.>..>.......v.>v....>.>>......>...>.v.>>.>....v.>>....>.>>.v.vv..>.>v.
>.>>>...>...v..v>...vv>.v>..>.>>v>..>.v>>>v....>v>v....vvv..v..v>v.>........>v..v>>...v.....v....vv..>.....v>vv..v>>.>v>>..v.>v>.v>....>>..
vv>>.>>vv...>v.v>..v......vv...>>..vvv>.>>vv.>.>>..>>..>v.>>>>......v>.vvv....>vv>>.v>.>.>.v..>>v.vv>>.>vv...>>.vvv..v...v>v.v.........>.>.
..vv...vv.>.>>..vvvv......v.>.>>>>v>>.......v.>v...v...>..vv.>v.....v.>>>...>.v..v.v>.v>.v.>>.v...v>>..>v....>.v>v>v>>....>>v>.v....v>.v.>.
>.v.>..>vv...>..>v>.......>v.v>v..v>..>v.v.v>.vvv.v..>.v.>>vvv>v>.>....>..v.v..v...>>.v>..v...>>>...>v>.>..v.>>v.>v.>..>...v>>.>....vvv....
>v...>v.>>..vv>>.>.v>v..v>.v..v>...>.v.>>>v>..>..v.>.>v..>..v...>..>....>..>.vv...>.>v.>>..>..v...>..>>....>>.v>....>..>>.>>>.vv.v.........
>v>>.>vv.v.v>v.v.>>...>v...>.>.....v.v...v...>.v..v>...vv.v>>vv..v.>>>v>.v.....v.v>.......v...>.....v..>.v.v.>..vv.>...>.>...>>v.v>......>>
v.v>..>.v>.>.>.>>>.....>.vv..>.v.v>....>v>.>.vvv>v.>....v..>>....v>v.>.>v.vvv.>.>.vvv>>.vv..>>v...v>.v>>.>>....v>..v...>.v>..>.....>vvv>.v.
vv....>.v>v.>.>...>.......>>.>>>.v...>.v>...vv.>>>vv..vv>>.v...>>.v...>v>...>....v>.v....>.>...v.v..>>.>.vv>..>>>>v.>>>>.vv.v.v.v...>>..>..
>..vv..>v..>v...>.vv.v>>.vv.vv.vvvvv>v.>...>..v..>v.vvv>>>...>>>v.v....>v...v.>v>vvv....v........v..v>.>>v>v>v..v.>vv>v.>v.>>....>>>vv.>v.v
..>v>>....>>....v...v.>...v....>.>>vvv..>>..>....v....v>>.>>>>....v.....v>.>>..v...v.vv..v...>.>>...v>>>...>.vv..>v>..>>>.vv>>..v>v.vv..>.>
v>.>..>>..v>>vv>..v>.v..v..v>..>.v.v...v..v....v..v.>.>v.>....>>..v.vv>..>.v.v...>>...>v.....>>v>.v..v.vv.>>vv.v>.v.v.>v.v>>vv...v.>..>vv.v
...v>>>v.v>.>v.v.>.>.v....>.>.v>...v.v>>..>.>....vv>.>v..vv.>......>v.>..v.>.>v>v.>v>.v>v.........vv.>.>v..>>....vvv>.v.v.vv.v..vv..vv>..>.
vvv>.v...v.>....>>v.vv.v>>v>>>..v>.>>..>.....v....>v.v.v...vv>...v>.v>>>.>>.v.....>..vvv..>.>vv>..v..>vvv....vv.vvv>....v..v>.>..v>>v>.>>>v
..>v>.>....vv..>..>v>vv>>..v.>>vvvv>>..v..>vv.....>>.>.v>..vv.vvv.v.v>v>>..vv..>>v>...>>vv...v.>v>>...v.>v...>v>..vv....>.vv.v>v.>>v...v..>
.>.>>>>.>.>..>v.v.>>.....vv>.v...>v....>v>.v.>>v>>.>.vv>..>vvvv.>>>.vv.v..vv.v.vv>>>>.>..v....v>vv>........>......v..v.>.v.>.>.>.>....>..>.
v..>>v>.vv......>>v...v.vv.v>v.v.vv>.>.>.v>..v>vv...>..v....v.v>vv..>>....>>>....>...>>..>>v..v.>v..v>vv...>>>.>.>>.v..>..v>v..vv>.>v.>....
...>...v.........>v>v..>..>>v...v>.v.v>>.vv...vv>>v>v...>..v.v.v>.>..v>..v..>>.>.......>...v..v..>>>vv..>...vv.v.v.v>..v.>>v>v.vv>..>.vv.v.
..>>.v.v>..>v...>vv.>...>.v.v....v.vvvvv...>v.>v..>>.v...>v.....>..>.>v.>v>.>.>..>>>....>.>>.>.>....v>......>>>.>>>>.>v.vv.>..v......>..vv.
.>>vv.v..>.vv.v.vv.vv>....v.>...>vv.v.>>v..v.>...>.>>....>vv...v>>.>.>.>v>...>.v..vv.>v.v.......>..v>..>..v.vv.v.v.>...>..>.>..>...>.>v....
..>v>....>...>>....>...>>>..vv.>>................v>v..>v.v>>..>v>>>..>>v.>v.>vv.vvv>..>.v>.>..>v..vvv.>vvv.>.>>v..vv..>>...v.vv.v.>>>vvv.>.
v>...>.v>>>.vv>vv>vv...>..v>.v.v>v...v....>..>v....v.>>.>>v>.>...v.>>..vv.....vv..vv..v....>..v...>v..v>v..>>>>>....>v.>vv.vvv.>..v...>..v.
>vvv>..>...v..>.>>>.>>.v.v.>vv>..v.v.>v>v.vvv...v.>>...v..vv.....v.>.v.v>>.>..>.v>>v.vvv.vv...vv.....vv.v>.v>...>..vvv>v..>>.vvv>>v>.v..v>.
...>...>>..vv>>>.>>vv>v.vv>>v>..>>>vv.>>>v.>>v..>....v......vv.vv..v......>>.vvv>.>v...>v.>..>..>.>vv>>......>vv.v.v.v.....>v>...>...>.>>>.
.>.>..>.v.>v..>.>>.v....>v.>v...v.>vv.vv..>..>>..vv..>.v.....vvv>.vv.>.>vvv.>.v.v..>.....vv..>.....>v>v...v.....v....>vv.>.>>.v..v.vv>.>v>.
.v.>...>>.>v>>>.vv.v.v>..>>..>.>v..vvv>..v.v>>.>.v>vvv..>.v...>..v.v.>>.v.v...v>>v.vv..>.>....>....>......v.>.>>>>v.>>..>v.v.v.v.vvvv...>..
.>.v.v>.>..>v.v....>vv>..>>>vv..v....>...>>v.v.v..>...v>.v.>.vv>>>v.>..v..vv...>.>.>>.vv..vvv>..v..>.>v...>.>.v>v.......v.v.v>>>..vv>>>...>
.vv>v.>.v>>.>vv>v......>>...>v>..v.>>>>v.>..>>...v>...>v>...>.>...>....>.>.v...v>>.>>.vvv>>vv>>vv>v.>v>>vv.....>.vv>.v..v>.v......v.vv>vvv.
v>v.>>.v....v.>>.v...v>>vvv.v>.>vvv>v.>...>.vvvv.>...>...>.v...vv.>>v.>..>.vv.vvvvv.v....v>>vvv....>>.>..>v>...>v...>.>.>..vv>>>>vv....>>>.
v...v>v...vv..>.v.>.vv>v>>>>....>...>v>>vv..v...v....>>......v..>>>.vv>>v.>v>..v.v.v.....vv...v.vv.v.vvv>.>>..>...v>..vvv.v.>..v...vv...v..
.>.......v.>.>v....>...>>.v..>v......v.v...>v..>..>.>v.>>..v..v...>....vv>>..vv.>>v..>vvvvv.v>...v>..vvv.....v>v.v...v.>.......>.vvv....v.>
vv..>.>>.v>>>vvv.vvv...v>....>.>.vvv....>v.>v..v..vvvv>v.>..>..v>.vv>.v.>>......vvvv>.v..vv..........v.>.....v..v..vv..>.vv>.v>.>v>>v>.v.v.
v>.>vv.>.>v....>.>v.>vvv>.>.v>.>v>..vv.....>.v>v.v....v>...>..vv>....>v.vvv.>>..>v...v>..v.v..v.>>..vv>..vv...v.vv...v.....v....>.v>vv..>>v
>..>....>.>v..>>v.v.....v.v>v>..v.v>.v>>.>...v.v....vv>>v>.v..vv>vvv.>.....>.v....v..v.>>>..vv.vv.>...vv.>.v>>...vv>v.v...>....>.>.....>.>.
vv....>..>>>..v>>v.v.>v>>..>.>v....>.v..>v.....v>>....>.>..vv....v.......>>>>v>>>>>v>v..v.v..>v>>vvvvv.>..>.v.>v....v>.v..>v>v..>>...>.v.>v
>..vv>..>v.v>..>>v..v..v.>>v.v.>.vv>...>.v.v.>v>...>>...v.v..>>..vv>..>...>...>>.>.>..v..>v..v...v>...v>.v..v>.>.....v.>.>.v.>>vv..vv>.v.>v
>...vv..>.v.>.v>....>>>.....>...v..>..v.vv.>v..>v.v.vv.>.v>..v.v..v.>...>..v.vvvv...>.v.>.v>>.v.vv>v>.>>v>.>>v>v.>v.vvv.>.v>v.vv.v>>.v>..>>
.>v>.v.v....v..v>>..v>>..>..>vv.>v..>v>>v......vv.vv.vvv>.v.>v.v>...v...v..>.>..>.v>....v>..v>v.>..>>>.>.v>>......v>.>....>.v.>.v>.v>v..>..
vvv..>....>.>..v...v...>.v.>>....v>.>.>vvv..v>.vv.v.>vvv...v>>>vv>..>v>..>.....v.>>>v>vvv>....>.v>.>....v.vv>v..v..v..>v..vv>vv.vvv.v..>>..
>v.v.>.>...>.>>.>>v.v.v>..>.>..vv>..>v.>.v>..v.v.vv..v>..>>..>>>...>>v.>>.>>v.......>v.v...v..>>>.>v>>....v>>.>....>v.>.>v>v.>.>v>..>v...v.
v.>.>.v.v>.v.....v>..>v.>..>v...v>.v..>v.v..>>.v...>vv.v.vv....v..vv.v.>.v>....v.vv...v..>.v>.>.>>.>.>.>.>.v.>>vv.vvv.>...>.v.>.>..>>v.>..>
>>>.v.>v...>.>.....>.>>..v>>>...v.>.>.vvv>.vv.v.>v.vv....v..>..v..>.>.v..>.>.v>...vv.v.v..>..>.v.>>..>>>v.>.vv..vv>.>>.v>v>..>.>...vvv..>..
vv.>>>v.v.vvv.>>........vv...>.>..>v.>v>>vvv..vv.>..>>v..>..v>v.>..v>...>.>...vv>..>>..>vv>....vv....v...>....vvv.>>>v...>...v.>.>.....>>>.
v.v...vvvv.>..vv..>vv...vvvv>.v>v....vv..>>>vv>.v.vv.v.v.v.....>vv..>.>..v>v.v..>vvv>>.v..vvv.>...v.>....v>>v>>>.>v.v..>vv.vv...vv.>>v..>>.
>.v.>...v..v>v....>v...>.v.vvv>.>vv>v......v>>v>.>..>vv...>.v>..>v>vv>v>vv...vv......>>..>.>v.....>...>.>v>v....>.>...v>>.v..v....>.v>....v
.>v>.>>>v>...>v.>v.v.vv.>>.v>..>v>..v.vv>....v>.......v>vv>...v....vv>...>>.>..v>vv>vv.v..v.>..>..vv.v.>v.>.>..vv..v.>.>...>>v>....vv...v.v
..>>.>..>>vvv>v>.>>..v.v>.v.>.v.>.>v>>v.v.>>>v>vv>....v..>vv>.v.vv>>>....v....v>.>v.v.v.>>..v>>vvv.>..v.v>...>v...vv>.>>v>vv.v.vv.v..>..>..
>.>>v...v>.>.>>..v........v...v>.>>>..>v.v.v>v>....>v>v.>v>....>>>.>.v>>>.>.v.....>...v..v>..v>....>>.>>vvv.v>.vv..v.>v.>..v.>v..>..v.>>v>>
..>v>>>v....>v.v..>vv>.v>.>...>v>..>...v..>.>>v>.>....>>..>v.>v..>v..v.v...vv.vv>..>>..>v.v>>.vv.v........>v.v>.v.v>.>>..vv.v>vv.>v>>v.....
.v.v>.>v>>v.>v>vv.v.v>.v.....>.>>.vv...vv.vvv>v..>.v...v>.>>v.>>vvv>>>v.vv>...vv>.v.>v>>v..>.v.vv..v>vv..v.>..>...>.>..vv.>.v>.....vv>.>>>.
.>>>vvv.v.>..>vv.v.vv...v...>.v.v.v.>vvvvv>>>>.v>..v.........>.>.>v.vv.v....>>>v...>..v>>.....vv>v....>..vvv>.v.>>v>>>vvv>.v.v>vv.vv.v.v.v.
>.v>vv.>.......>....>v.v...>>..>v..v>...>vvv>v..v>.>.v..>vv.v.vv.>......>.>.vvv.vv>v...>v>>.v..v.>.>....v.>.>...v.v.v.....>>...v.v.v.>v...v"""