pyweek17
========

Submission PyWeek challenge #17

[Repository on Github](https://github.com/5hassay/pyweek17)

Theme: "Moon"

# How to Run the Game

There is an executable for Windows 32-bit to use or one can use the source and run it with Python.

## Using Python

Uses [Python v3.3.2](http://www.python.org/download/) and [Pygame v1.9.2](https://bitbucket.org/pygame/pygame/downloads)!

1. Download all the files. [Quick link to the zip](https://github.com/5hassay/pyweek17/archive/master.zip).
2. Run `main.py` with Python, such as with one's console on their computer. The latter is recommended to see the exit status of the program.
3. The rest is straight forward except the rules of the game, which is below.
4. Extra information:
    * It isn't recommended to mess with init.txt. It was a feature that didn't meet its intended implementation.

## Using the executable (win32)

1. Download the [exe](https://github.com/5hassay/pyweek17/blob/master/build/exe.win32-3.3.zip?raw=true) located in the ```build``` directory.
2. Extra the zip into some folder (there's a lot of required files that come with the exe).
3. Run main.exe.

# How to Play the Game (Rules)

* In a game, you have a planet at the center, as well as a number of orbital rings centered on the planet, which are the orbits for the various moons also seen.
* When the Play button is selected, asteroids will begin moving towards the planet.
* The objective is to have the moons, one or several or all, collide with the asteroids, thereby protecting the planet.
* If an asteroid collides with a moon, the asteroid is destroyed, but the moon is fine. However, if an asteroid collides with the planet, the player loses and must try again.
* Moons may be moved left or right on their orbit by pressing or holding the LEFT or RIGHT arrow keys on the keyboard, respectively.
* So, if asteroids are getting passed moons with their current orbit, the player can adjust the orbit to hopefully have the moon collide with asteroids.
* The Reset button can be used at any time to put the moons back to their original (or player set) locations, and remove the asteroids from the screen.
* When the player has all asteroids destroyed and the planet was not hit, the player wins and is directed back to the level menu screen.
* Additional notes:
    * Moons further out in orbits and larger in size will move slower, and moons in lower orbits (closer to the planet) and that are smaller in size will move faster.
    * There is no limit to how many asteroids a moon can destroy.

# Known Problems

1. There is a minor rendering error with the planet where little chunks of it will be missing.
2. Planets render a little weird.
3. The smallest planet is a bit hard to see.
4. Yes, the code is pretty gross. This is because of time constraints (due to the nature of the project (one week to complete) and life). If you're looking to mess with the source, good luck, and sorry!

# Notes on Source and Assets

* All Python code was written from scratch by the authors Dickson Wong and Lucas Ashbury-Bridgwood.
* Images made by Dickson Wong.
* Sound effects made by Lucas Ashbury-Bridgwood using [sfxr](http://www.drpetter.se/project_sfxr.html).

# License

* This is released under the GNU GENERAL PUBLIC LICENSE Version 3. See the LICENSE file that was distributed with this game.
