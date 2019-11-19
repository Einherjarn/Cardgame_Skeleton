https://github.com/Einherjarn/Cardgame_Skeleton
----------------------------------------------------------
python cardgame LOOSELY based on the cardgame audatia,
which itself is based on historical european martial arts

group project for TAMK, advanced programming languages
Kristian Suuronen
Jari Pelkonen
Miika Isoviita
----------------------------------------------------------

links used:
https://www.101computing.net/creating-sprites-using-pygame/
https://www.pygame.org/wiki/GettingStarted
https://docs.python.org/2/tutorial/controlflow.html#unpacking-argument-lists

remember to install python with pip and environment variables
installer should get you to being able to cmd "pip install pygame" to deploy libraries

herp de derp
card format:
name,art filename,stamcost,range,target (7 bools),deftarg (7 bools),attackpower (7ints, 0-2),defpower (7ints, 0-2),initiative bool,description ('_' for spaces, converted when read in)
			
target format (anything to do with bodyparts is in this order)
head, right arm, right torso, right leg, left arm, left torso, left leg

modifier stats
strength, quickness, foresight and fortitution

card stack resolving graph
1 2 3		1 2 3
x           x          
  x   		  x      
    x           x   
opener			opponent
1-1				1-2
2-2				2-3
3-3			-> last opponent action put on top of stack for next exchange

very basic gameplay balancing, early dev testing concept

greatsword deck
	- focus on high value cards, strong attacks
	- weak defense, likely to run out of stam/cards sooner
	
vs.
	
longsword deck
	- all-arounder
	- focus on hybrid cards for continuous pressure