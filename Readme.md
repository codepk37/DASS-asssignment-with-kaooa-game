1)
RUN :python mdirectory.py
Enter name of CSV file <file_name>.csv
1:shows directory(prints data) 
2:we can update current data to csv as need (to improve perfoemance)
9:we can store current data in other csv file
10: it automatically updates csv with data before exiting

rest [3:8] do update,entry,deletion operations
Data stored has Unique roll number 




2)
make file input_2.txt 
code supports input in [("3cm", "N"), ("4.5mm", "NW"),("2mm", "SE"),("23mm","E")]  similiar format above file , in same directory

RUN: python map.py


It will plot all distances in 2D, incduced by movements

On terminal it also prints relative direction and distances at end like:

Output on terminal after execution:
21.23223304703363    4.767766952966369
WRT starting point direction:     North-East
WRT starting point distance:     21.76095866181785 




3)
Run :python kaooa.py

All rules mentioned are followed:https://www.whatdowedoallday.com/kaooa/ are followed

Used Pygame.
Display represents Crows eaten ,which player should play and name of player winning game
USE SINGLE CLICK over dots
->When Dot to move is selected: prints "initial pos selected" then select 2nd dot position to move
->if mistakenly selected first dot, reselect any dot to flush request incorrect request
Initially chance by chance, Player1 locates crow by selcting first on OUTER SINGLE dot, then on vaccant dot of game till 7 crows
After that Player1 can move crow by selecting from_dot and to_dot once.
Initially Player2 locates Vulture from red dot initially, onwards when chance comes select from_dot, then to_dot
Ensured restrictions to follow rule like: if there exits crow eating possibility then eagle cant make adjacent movements
Code- make sure's colours of Vulture (RED) , CROWS (GREEN) have correct color switching ,and invalid moves not happening
OUTER DOT vanishes once all 7 crows have taken and becomes unresponsive (had ind=-1) Pseudo dot
Unoccupied Dots have SKIN color

CLOSING: close game window gui to exit game gracefully
