links used:
https://www.101computing.net/creating-sprites-using-pygame/
https://www.pygame.org/wiki/GettingStarted
https://docs.python.org/2/tutorial/controlflow.html#unpacking-argument-lists

remember to install python with pip and environment variables
installer should get you to being able to cmd "pip install pygame" to deploy libraries

herp de derp
card format:
nimi, kuvake artwork tiedostonimi, stamcost, range, target taulukko (7 boolia), defend_target taulukko (7 bool), attackpower taulukko (7 inttiä 0-2), defendpower taulukko (7 inttiä 0-2)
take initiative bool, kuvaus (datastoressa _ delimitereillä, muutetaan space delimiteriks kun tuodaan objectiin)
				
"""Hits follows the format of
head, right arm, right torso, right leg, left arm, left torso, left leg"""
"""stats are
strength, quickness, foresight and fortitution"""

card stack resolving graph

1 2 3		1 2 3
x           x          
  x   		  x      
    x           x   

opener			opponent
1-1				1-2
2-2				2-3
3-3				

