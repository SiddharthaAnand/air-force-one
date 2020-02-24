## AIR FORCE ONE
A 2-D game built using pygame. 

# Back story
You were the captain of a mission which was supposed to carry out 
a deadly operation and retrieve hostages from an enemy location.
But, you were back-stabbed by one of your own lieutenant. All your 
wing commanders have surrendered and you are the one who is fighting
to go back to base.

The enemy has a huge amount of ammunition and missiles which have 
been fired at you continuously through their high-tech surface-to-air
machines. You have to save yourself since your ammunition is completely 
over. You have the radar technology to see the missiles coming from
a little far off and have little time to recover.

# How to play?
This is still in development mode. You need to clone this repository
using the following command and then you can play.
```python
$ git clone repo
```
Switch to the repository.
```python
$ cd air-force-one
```
Make sure you have activated your virtual environment so that this
does not mess with your existing environments.

Install the requirements.

```python
pip install -r requirements.txt
```
Now, run.
```python
$ python src/game_controller.py
```

Start your mission!

# Concepts
Surface
Window
Event Loop
Key Events
Sprites

# Architecture
The source code is divided into entities denoted by various components.
There is a single Game Controller that handles the startup, continuance
and exit of the game. Specifically, the event loop is present in 
game_controller.py module. 

Missiles, Jet and Clouds are an extension of Sprites. Anything that 
you want to interact with in a game can be called a Sprite. 

```python
src/
```
This consists of the source code.
```python
assets/
```
This directory consists of all the images being used in the game.

# Newer additions
1. Score board for your current score
2.  High Score to keep track of your earlier better mission capability
3. Change of sky color in enemy territory
4. 


# How to contribute?
1. Create Issues on your own, or pick one from Issues tab.
2. Create an issue branch and work on it.
3. Create PR and give me some time to review and merge. :)