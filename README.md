# CS467_TBAG
Capstone: Text-Based Adventure Game
<br/>
Python Version: 3.10
---
##How to Run Program
1. Download files
2. Ensure you have python 3.10 installed.
   1. If not, install python 3.10
3. From terminal, navigate to downloaded location.
4. Type `python main.py`
---
##Midpoint Archive Walk Through
##Commands:
**Commands** are currently two word commands. For example:
</br>
* `look room`
* `use tv`
* `go [navigation option]`

##Verbs:
The available verbs and their synonyms currently include the following:
1. go or [move, walk, run, travel]
2. take or [get, grab, pick-up]
3. drop or [put-down, release]
4. look or [examine, inspect]
5. use or [activate, operate]

##Walk Through Main Room Example
Once you run the game you will be given the description of the room with feature descriptions, and you will be given a prompt:
</br>
`What would you like to do? `
</br>
Try using some commands listed above such as `examine poster`. But to get through the game do the following:
1. `use tv`
   1. You will see a code `UHF-73` being described after you use the tv.
2. `use tablet`
   1. To unlock the tablet type in `UHF-73`.
   2. Type `q` to exit out of tablet mode. 
3. `look room`
   1. If you looked at the poster before this step `examine poster` will reveal a change, but it is currently not required to exit the room.
4. `go 1`
   1. This will take you out of the main room and into the room that was unlocked by the tablet. 

##Walk Through Room One Example
Once you are inside this room, we have only currently implemented the mechanics, so do the following:
1. `go 1`
   1. You will notice the room is locked. 
   
2. 'examine desk'
   1. You will notice a remote control object. You will need this.
   
3. 'take remote'
   1. This puts the remote in your inventory. You can look in your inventory at any time by typing 'inventory'
4. 'use commodore'
   1. Type `0` to win the game. The game is in progress. 
5. `look room`
6. `go 1`
   1. Exists back to the main room we started, if you forgot the remote, the game will tell you. 

## Walk through Back in Main Room Example
Now that you are back in the main room, you should have your remote. Type `inventory` to make sure. If it is not in your inventory do the following:
1. `go 1`
2. `grab remote`
3. `go 1`

With your remote in hand you can unlock the next level by doing the following:
1. `use remote`
   1. This brings a use remote interface that you can either increase the channel, decrease the channel or quit the interface with the following commands:
      1. `+`
      2. `-`
      3. `q`
2. `+`
   1. Increasing the channel will show a new code on the tv. Note this code. 
3. `q`
   1. This leaves the use remote interface.
4. `look room`
   1. Notice that there is now a new navigation option. 
   2. `examine poster` will also show a change in the poster. 
5. `go 2`

This is the end of the tutorial. During anytime, you can experiment with the commands. For example try to `take tv` or drop something in your inventory with the command `drop` + the name of the item in your inventory. 


