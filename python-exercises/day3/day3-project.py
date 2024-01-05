print(r"""
                                       ,.=,,==. ,,_
                      _ ,====, _    |I|`` ||  `|I `|
                     |`I|    || `==,|``   ^^   ``  |
                     | ``    ^^    ||_,===TT`==,,_ |
                     |,==Y``Y==,,__| \L=_-`'   +J/`
                      \|=_  ' -=#J/..-|=_-     =|
                       |=_   -;-='`. .|=_-     =|----T--,
                       |=/\  -|=_-. . |=_-/^\  =||-|-|::|____
                       |=||  -|=_-. . |=_-| |  =|-|-||::\____
                       |=LJ  -|=_-. . |=_-|_| =||-|-|:::::::
                       |=_   -|=_-_.  |=_-     =|-|-||:::::::
                       |=_   -|=//^\. |=_-     =||-|-|:::::::
                   ,   |/&_,_-|=||  | |=_-     =|-|-||:::::::
                ,--``8%,/    ',%||  | |=_-     =||-|-|%::::::
            ,---`_,888`  ,.'''''`-.,|,|/!,--,.&\|&\-,|&#:::::
           |;:;K`__,...;=\_____,=``           %%%&     %#,---
           |;::::::::::::|       `'.________+-------\   ``
          /8M%;:::;;:::::|                  |        `-------
""")
print("Welcome to the Spooky Castle.")
print("Your party is hungry, and is looking for both food and shelter.")
print("Upon reaching the castle gate, you notice that the entryway is open. You have no choice but you proceed.")
print("Once inside, you see a grand stairwell. At the top, there is a hallway to the left or right.")
choice1 = input("Do you go into the left or right stairwell? ")
stairwell = r"""
         -     -                 .      :
         -     -     -                  |          -
   -           -     -    .      .      |    -     -     -
         -     -     -    |      .      |    -     -     -
   -     -     -     -    |      :      |    -     -     -
   -     -     -     -   .|     _|_     |.         -     -
   -     -     -       ._-|             |-_.       -     -
   -     -     -     ._-  |     .       |  -_.     -     -
-.--.--.--.--.--. _ _-_ _ |   E-1-2-3   | _ _-_ _ .--.--.--.--.--.-
 |  |  |  |  |  |`.| | | ||   _______   || | | |.'|  |  |  |  |  |
8888888888888888L_|`.88888|  |   |   |  |88888.'|_J8888888888888888
       |:     `888L_|`.|  |  |   |   |  | :|.'|_J888'    :|
       |:       `888L_|`. |  |   |   |: | .'|_J888'      :|
       |:        |`888L_|`.  |   |   |  .'|_J888'        :|
_______<:________|:_`888L_|) |   |   | (|_J888':|________:|________
       |:        |:   `888L. |___|___| .J888'  :|        :|
       |:        |:     `88|/_________\|88'    :|        :|
 __..--       _.-'        ,|L_________J|.      `-._      ``--..__
'         _.-'            |/___________\|          `-._          ``
                        .c|L___________J|c.            `-.
                      .' |/_____________\| `.
                    .'|  |L_____________J|  |`.
                  .'  | _/               \_ |  `.
                .'|   _//                 \\_   |`.
              .'  | _///                   \\\_ |  `.
          _______________________________________________
        .'                                               `.
      .'                                                   `.
    .'                                                       `.
"""
dead = r"""
                  _  /)
                 mo / )
                 |/)\)
                  /\_
                  \__|=
                 (    )
                 __)(__
           _____/      \\_____
          |  _     ___   _   ||
          | | \     |   | \  ||
          | |  |    |   |  | ||
          | |_/     |   |_/  ||
          | | \     |   |    ||
          | |  \    |   |    ||
          | |   \. _|_. | .  ||
          |                  ||
          |  name goes here  ||
          |                  ||
  *       | *   **    * **   |**      **
   \))ejm97/.,(//,,..,,\||(,,.,\\,.((//
"""
dead2 = "Wrong choice. You and your party were eaten by zombies."
dead3 = "Wrong choice. You and your party were eaten by sharks."
dead4 = "Wrong choice. Behind the red door was a dragon, who thought you looked tasty."
dead5 = "Wrong choice. Behind the blue door was a ghost, who thought your souls looked tasty."
doorway = r"""
88888888888888888888888888888888888888888888888888888888888888888888888
88.._|      | `-.  | `.  -_-_ _-_  _-  _- -_ -  .'|   |.'|     |  _..88
88   `-.._  |    |`!  |`.  -_ -__ -_ _- _-_-  .'  |.;'   |   _.!-'|  88
88      | `-!._  |  `;!  ;. _______________ ,'| .-' |   _!.i'     |  88
88..__  |     |`-!._ | `.| |_______________||."'|  _!.;'   |     _|..88
88   |``"..__ |    |`";.| i|_|MMMMMMMMMMM|_|'| _!-|   |   _|..-|'    88
88   |      |``--..|_ | `;!|l|MMoMMMMoMMM|1|.'j   |_..!-'|     |     88
88   |      |    |   |`-,!_|_|MMMMP'YMMMM|_||.!-;'  |    |     |     88
88___|______|____!.,.!,.!,!|d|MMMo * loMM|p|,!,.!.,.!..__|_____|_____88
88      |     |    |  |  | |_|MMMMb,dMMMM|_|| |   |   |    |      |  88
88      |     |    |..!-;'i|r|MPYMoMMMMoM|r| |`-..|   |    |      |  88
88      |    _!.-j'  | _!,"|_|M)(MMMMoMMM|_||!._|  `i-!.._ |      |  88
88     _!.-'|    | _."|  !;|1|MbdMMoMMMMM|l|`.| `-._|    |``-.._  |  88
88..-i'     |  _.''|  !-| !|_|MMMoMMMMoMM|_|.|`-. | ``._ |     |``"..88
88   |      |.|    |.|  !| |u|MoMMMMoMMMM|n||`. |`!   | `".    |     88
88   |  _.-'  |  .'  |.' |/|_|MMMMoMMMMoM|_|! |`!  `,.|    |-._|     88
88  _!"'|     !.'|  .'| .'|[@]MMMMMMMMMMM[@] \|  `. | `._  |   `-._  88
88-'    |   .'   |.|  |/| /                 \|`.  |`!    |.|      |`-88
88      |_.'|   .' | .' |/                   \  \ |  `.  | `._    |  88
88     .'   | .'   |/|  /                     \ |`!   |`.|    `.  |  88
88  _.'     !'|   .' | /                       \|  `  |  `.    |`.|  88
88 vanishing point 888888888888888888888888888888888888888888888 fL 888
"""
boat = r"""
                   ~;
                  ,/|\,
                ,/' |\ \,
              ,/'   | |  \
            ,/'     | |   |
          ,/'       |/    |
        ,/__________|-----' ,
       ___.....-----''-----/
       \                  /
   ~~-~^~^~`~^~`~^^~^~-^~^~^~-~^~^
     ~-^~^-`~^~-^~^`^~^-^~^`^~^-~^
"""
treasure = r"""
                            _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
            jgs '-._'-.|| |' `_.-'
                    '-.||_/.-'
"""

if choice1 == "left":
    print(stairwell)
    print("You feel like you made the better choice.")
    print("In front of you, you see a long hallway with a doorway at the end.")
    print("You open the door and come upon a massive room filled with water.")
    print("You can see an empty dock in front of you, and another dock on the far side of the room.")
    choice2 = input("Your party needs food. Do you swim now or wait and see if something happens? ")
    if choice2 == "wait":
        print(boat)
        print("You feel like you made the better choice as a boat appears before your party seemingly out of no where.")
        print("You step onto the boat and it takes you to the other dock.")
        print("When the boat reaches the other side of the room, you see three doors.")
        print("The doors are colored red, blue, and yellow.")
        choice3 = input("Which door do you open?")
        if choice3 == "red":
            print(dead)
            print(dead4)
        if choice3 == "blue":
            print(dead)
            print(dead5)
        if choice3 == "yellow":
            print(treasure)
            print("You walk into the room and are instantly taken aback by a giant feast with a massive chest full of treasure in the center. You won!")
    else:
        print(dead)
        print(dead3)
else:
    print(dead)
    print(dead2)