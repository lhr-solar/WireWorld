# WireWorld
This repository contains information the wiring of all the electrical systems in the casr


## Setup
### Downloads
Install the Diagrams.net desktop app (https://github.com/jgraph/drawio-desktop/releases/tag/v21.6.1)

Download Python (https://www.python.org/downloads/)

Download git (https://git-scm.com/downloads)

If you're in Wire Harnessing or Enclosures download KiCAD (https://www.kicad.org/download/)

### Setting up Git
If you don't see yourself viewing any boards then download GitHub Desktop (https://desktop.github.com/) :vomiting_face:

If you see will be using Git for anything else (ie you’re a part of Wire Harnessing or Enclosures) then follow these guides for setting up SSH :sunglasses::
1. https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent
2. https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account

### Cloning the Repo
When you clone the repo you need to make sure that you're putting the folder somewhere that's easily accessible to you and somewhere that makes sense.
There are 2 ways to do this:
1. Use the ```cd``` command to navigate to your goal location. (information on how to use this command is in the ``Useful Commands`` secton)
2. (Windows only) Nvigate to where you want to clone the repo in File Explorer
right click empty space -> Show more options -> Start Git Bash

Once you've entered your cloning designation or choice, run the command ```git clone```
The repository should now be copied into your folder 🥳
Make sure to cd into your repository right after since when you clone a repo your computer won’t put you into that directory
NOTE: When cloning board repositories you’ll run ```git clone —recursive``` which will clone the submodule repository used to store the common KiCAD symbols and 3D models for their boards. Since as of 2023 this repo doesn’t use any submodule repositories you don’t need to add the recursive part, you can if you’d like.

## Useful Commands
1. ```cd``` is a command used to navigate between directories on your computer. The way you use it is you type ```cd [file directory]``` for example if I’m in my Documents folder and want to enter my LHR folder I’ll run ```cd LHR``` and I’ll be placed into my LHR folder. Something to else to keep in mind is that when you open your terminal or Git Bash you may be in your most root directory so you’ll need to navigate from your root to what folder you want. For example, if I’m in my root directory I’ll go ```cd Documents/LHR/WireWorld``` to navigate to my WireWorld folder. Pressing tab will autofill directories. Doing ```cd ..``` will go back one directory.
2. ```ls``` is a command that will display all files inside a directory.
3. ```ctrl + c``` doesn't work for copying in terminal, you need to use ```ctrl + ins```
4. ```ctrl + v``` doesn't work for pasting in terminal, you need to use ```shift + ins```
5. ```git branch``` this command will print which branch you are on
6. ```git checkout``` will switch which branch you're on. The way you use it is you do ```git checkout [branch name]``` if you are making a new branch do ```git checkout -b [new branch name]``` 
When you a push a new branch to the repo you need to do ```git push --set-upstream origin [branch name]```
7. ```git pull``` will pull changes from the remote repository to your local folder


## Pushing to this repository 
Make sure you’re not pushing to main, you should only be pushing to main though a Pull Request
1. Make sure you’re cd’d into your repository
2. Run ```git pull``` so you’re up to date with any other changes
3. Run  ```git status``` to check which files are different on your local folder from the repo
4. Run ```git add [file you want to push]``` if you want to push all your files run ```git add .```
5. Run ```git commit -m [a commit message that describes the changes you’ve made]```
6. Run ```git push```
Only files that you did ```git add``` for will be pushed to the remote repository
7. Revel in how cool you feel :sunglasses: rn

## Wiring Diagram Formatting
For the sake of :sparkles:	aesthetic :sparkles: we want to keep all wiring diagrams in the same formatting including: colors, sizing, wire thickness, and any descriptions. Note we work in dark mode because dark mode is cool.
- Colors:
    1. For PWR wires: #FF0000
    2. For GND wires: #F0F0F0
    3. For CAN wires: #2D7600
    4. For Ethernet wires:
    5. For misc GPIO wires:
    7. For I2C wires:
    8. For SPI wires:
    9. For IsoSPI wires: #006EAF
- Wire thickness:
    1. Non-HV wire has a line thickness of 6 pt
    2. HV wire has a line thickness of 20 pt
- Board formatting:
    1. Boards should have a board name + board dimensions (in mm) 
    2. The thickness of the box should be around 6 pt for extra readability
    3. Rounded corners are great
- Misc formatting:
    1. Indicate the area around an enclosure with non-filled 7 pt dashed line
    2. Wire text font size is usually 30 pt, but for any HV or large bundles of wires, the standard is 50 pt

## Making a Pull Request
In order to push to main you need to make a pull request where people can review your changes and make any modifications if needed before the changes are introduced into main.
1. In the browser version of GitHub, go to the Pull Requests tab -> New Pull Request
2. Figure out which branches you want to merge to
3. Add a comment explaining your changes
4. Add reviewers for your changes (currnet reviewers can be seen below)
5. Resolve any merge conflicts
6. ??
7. Profit


Reviewers:
1. Hanna Nguyen
2. Lakshay Gupta