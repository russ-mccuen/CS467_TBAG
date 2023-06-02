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
##Final Archive Walk Through
##Commands:
**Commands** a mix of verbs and objects of varying lengths. For example:
</br>
* `look room`
* `use tv`
* `go [navigation option]`

##Verbs:
Some of the available verbs and their synonyms are as follows (some will be discovered during gameplay and are not listed:
1. go or [move, walk, run, travel]
2. take or [get, grab, pick-up]
3. drop or [put-down, release]
4. look or [examine, inspect]
5. use or [activate, operate]

---
##Complete Walk Through:
<p><b>Note: This is a walkthrough of <i>exactly</i> what you need to do to complete the game.
   There are other actions/events in the game that you can trigger/explore.
   Please do so, but this guide is designed to take you from beginning to end, nothing more.</b></br>
Once you run the game you will be given the description of the room with feature descriptions, and you will be given a prompt:
</br>
<p>`What would you like to do? `
</br>
The following commands, executed in order, will unlock the next room:
1. `use tv` You will see a code `UHF-73` being described after you use the tv.
2. `use tablet` To unlock the tablet type in `UHF-73`.
3. Type `q` to exit out of tablet mode.
4. `examine letter` On the letter you will see a sentence that ends with `place bar`; you will need this in the next room  
5. `go 1` This will take you out of the main room and into the room that was unlocked by the tablet. 
---
##Walk Through: Room One
The following commands, executed in order, will help you unlock the next room:
1. `examine desk` You will notice a remote control object. You will need this.   
2. `take remote` This puts the remote in your inventory. You can look in your inventory at any time by typing `inventory`
3. `use commodore` Type `place bar` to win the game and unlock the door to the main room.
4. `look room`
5. `go 1` Exits back to the main room we started, if you forgot the remote, the game will tell you. 
---
## Walk Through: Back in Main Room
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
   1. Increasing the channel will show a new code on the tv `UHF-74`. Note this code. 
   2. You can try increasing the channel, but those will not be available until other puzzles are solved.
3. `q`
   1. This leaves the use remote interface.
4. `use tablet`
   1. type `UHF-74` which was the code from the channel you unlocked with the remote.
5. `q`
   1. Exits tablet interface. 
6. `look room`
   1. Notice that there is now a new navigation option. 
   2. `examine poster` will also show a change in the poster. 
7. `go 2`
---
##Walk Through: Room Two
This is the end of the tutorial. During anytime, you can experiment with the commands. For example try to `take tv` or drop something in your inventory with the command `drop` + the name of the item in your inventory. 


