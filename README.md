# shifter
A transforming maze game

Start game by running "shifter.py" 
To open custom level number, enter its respective list indix within the "main()" function,
into the level_num variable

Below the level caller, there is a call for a testing level:
uncomment this and comment out the above level call to access

All level layouts are saved using text files
The list of acceptable glyphs can be seen in:
  -the "Settings" class within "library.py" (to create walls of varying brightness)
  -the "level_maker()" function within "game_functions.py" (to create dynamic, or default walls,
                                          as well as the player's starting position and exit position)
                                          
