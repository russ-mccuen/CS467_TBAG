# CS467_Text_Based_Adventure_Game
Capstone: Text-Based Adventure Game
<br/>
Python Version: 3.10
---
## How to Run Program
1. Download files
2. Ensure you have python 3.10 installed.
   1. If not, install python 3.10
3. From terminal, navigate to downloaded location.
4. Type `python main.py`
5. Type `1` to start the game
---

## Final Archive Walk Through

## Commands:
**Commands** a mix of verbs and objects of varying lengths. For example:
</br>
* `look room`
* `use tv`
* `go [navigation option]`

## Verbs:
Some of the available verbs and their synonyms are as follows (some will be discovered during gameplay and are not listed:
1. go or [move, walk, run, travel]
2. take or [get, grab, pick-up]
3. drop or [put-down, release]
4. look or [examine, inspect]
5. use or [activate, operate]

---
## Complete Walk Through:
<p><b>Note: This is a walkthrough of <i>exactly</i> what you need to do to complete the game.
   There are other actions/events in the game that you can trigger/explore.
   Please do so, but this guide is designed to take you from beginning to end, nothing more.</b></br>
   
Once you run the game you will be given the description of the room with feature descriptions, and you will be given a prompt:
</br>
</br>`What would you like to do? `
</br>
The following commands, executed in order, will unlock the next room:

1. `use tv` You will see a code `UHF-73` being described after you use the tv.
2. `use tablet` To unlock the tablet type in `UHF-73`.
3. Type `q` to exit out of tablet mode.
4. `examine desk` On the desk you will see a letter.
5. `examine letter` On the letter you will see a sentence that ends with `place bar`; you will need this in the next room  
6. `go 1` This will take you out of the main room and into the room that was unlocked by the tablet. 
---

## Walk Through: Room One

The following commands, executed in order, will help you unlock the next room:
1. `examine desk` You will notice a remote control object. You will need this.   
2. `take remote` This puts the remote in your inventory. You can look in your inventory at any time by typing `inventory`
3. `use commodore` Type `place bar` to win the game and unlock the door to the main room.
4. `go 1` Exits back to the main room we started, if you forgot the remote, the game will tell you. 
---

## Walk Through: Back in Main Room

With your remote in hand you can unlock the next level by doing the following:
1. `use remote` This brings a use remote interface 
2. `+` Increasing the channel will show a new code on the tv `UHF-74`. Note this code. 
3. `q` This leaves the use remote interface.
4. `use tablet` Type `UHF-74` to unlock the next room.
5. `q` Exits tablet interface. 
6 `go 2` Travels to next room
---

## Walk Through: Room Two

1. `examine dance floor` This provides you with the dance pattern you will need to leave the room.
2.  `use blacklight` This will show you the code you will need to unlock the next room, `WKRP`.
3.  `go 1` This will prompt you to dance, which is the minigame you need to complete to leave the room.
4.  `dance` This starts the minigame.
5.  Enter the following numbers, **pressing enter after every number**:
   `1`
   `3`
   `4`
   `2`
   `5`
6. `go 1` Takes you back to the main room
---

## Walk Through: Back in Main Room

1. `use tablet`
2. Enter code `WKRP` (all caps) to unlock next room
3. `q` to quit tablet
4. `go 3` to enter next room
---

## Walk Through: Room Three

1. `examine dancing` When you do this you will see a flier on the ground.
2. `examine flier` You will see that Woodstock took place in White Lake, which is your next code.
3. `go 1` to go back to main room
---

## Walk Through: Back in Main Room

1. `use tablet`
2. Enter code `White Lake` to unlock next room
3. `q` to quit tablet
4. `go 4` to enter next room
---

## Walk Through: Room Four

1. `examine Mall Directory` You will see the pizza place's map location is FC-15, which you will need to exit the room
2. On the ground next to the directory you will see a pager
3. `examine pager` On the pager you will see the number `421-6827` which is the code you need to unlock the next room
4. `go 1` This will prompt you to eat pizza before you leave
5. `eat pizza` Will bring up another prompt in which you can get a free slice with the map location
6. `FC-15` Type this to get the free slice and unlock the main room
7. `go 1` returns you to the main room
---

## Walk Through: Back in Main Room

1. `use tablet`
2. Enter code `421-6827` to unlock next room
3. `q` to quit tablet
4. `go 5` to enter next room
---

## Walk Through: Room Five

1. `examine television` You will see a VHS tape on the entertainment center housing the television
2. `take VHS tape` adds tape to your inventory
3. `go 1` to return to main room
---

## Walk Through: Back in Main Room

1. `play vhs` To place tape into TV/VCR combo and see the ending of a basketball game
2. Note the final score, `54-52`, which is the code to unlock the next room
3. `use tablet`
4. Enter code `54-52` to unlock next room
5. `q` to quit tablet
6. `go 6` to enter next room
---

## Walk Through: Room Six

1. `go 1` to try to leave
2. `swim` to swim in reflecting pool
3. `examine coin` that you find in reflecting pool
4. Note date/mint stamp, `2076-P`, which you will need to unlock the next room
5. `go 1` to return to main room
---

## Walk Through: Back in Main Room

1. `use tablet`
2. Enter code `2076-P` to unlock next room
3. `q` to quit tablet
4. `go 7` to enter next room
---

## Walk Through: Room Seven

1. `examine jukebox` you will notice a basseball card
2. `examine baseball card` note the batting average, `.353`, which you will need to unlock the next room
3. `go 1` to try to leave
4. `sit booth` to sit in a booth
5. `eat burger` to eat the burger
6. `go 1` to go back to main room
---

## Walk Through: Back in Main Room

1. `use tablet`
2. Enter code `.353` to unlock next room
3. `q` to quit tablet
4. `go 8` to enter next room
---

## Walk Through: Room Eight

1. `go 1` to try to leave
2. `wear spacesuit` to put on spacesuit
3. `jump` to jump on surface of Mars
4. Note the Mars rover you saw was `Curiosity` as this is the code to unlock the next room
5. `go 1` to return to main room
---

## Walk Through: Back in Main Room

1. `use tablet`
2. Enter code `Curiosity` to unlock next room **(note there is NO SECOND 'u' in Curiosity; check spelling if code fails)**
3. `q` to quit tablet
4. Note room message: `One way. No return. When in doubt, wait.`
5. Since travel is one way, this is a good place to type `savegame` to save your progress
6. Type `SAVE` in all caps to confirm
7. `go 9` to attempt to enter final room
8. Type `yes` to confirm
---

## Walk Through: Final Room

1. Wait for prompt (the game has not crashed)
2. Type `wait`
3. Read prompts, then choose your ending
4. **Enter a number between 1 and 9, inclusive to choose your ending**
5. **If you do not enter a number between 1 and 9, inclusive, and ending will be chosen for you at random**
6. Enjoy your ending
---


---
