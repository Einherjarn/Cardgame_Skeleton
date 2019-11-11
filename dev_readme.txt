links used:
https://www.101computing.net/creating-sprites-using-pygame/
https://www.pygame.org/wiki/GettingStarted

remember to install python with pip and environment variables
installer should get you to being able to cmd "pip install pygame" to deploy libraries

herp de derp
card format:
nimi, kuvake artwork tiedostonimi, stamcost, range, target taulukko (7 boolia), defend_target taulukko (7 bool), attackpower taulukko (7 inttiä 0-2), defendpower taulukko (7 inttiä 0-2)
take initiative bool, kuvaus (datastoressa _ delimitereillä, muutetaan space delimiteriks kun tuodaan objectiin)

main program hierarchy:
playcard
 call on-play modifier functions
    opponent playcard
     call on-play modifier functions
        resolve cards
         call status modifier functions on current cards (str-> +dmg etc)
         calculate attack vs defend power, check target, range, etc
            outcome decided
                call on-outcome modifier functions
                apply effects on stamina/hp, check for game over