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

Once you've entered your cloning designation or choice, run the command ‘’’git clone’’’
The repository should now be copied into your folder 🥳
Make sure to cd into your repository right after since when you clone a repo your computer won’t put you into that directory
NOTE: When cloning board repositories you’ll run ‘’’git clone —recursive’’’ which will clone the submodule repository used to store the common KiCAD symbols and 3D models for their boards. Since as of 2023 this repo doesn’t use any submodule repositories you don’t need to add the recursive part, you can if you’d like.

## Useful Commands
 1.    ```cd``` is a command used to navigate between directories on your computer. The way you use it is you type ```cd [file directory]``` for example if I’m in my Documents folder and want to enter my LHR folder I’ll run ```cd LHR``` and I’ll be placed into my LHR folder. Something to else to keep in mind is that when you open your terminal or Git Bash you may be in your most root directory so you’ll need to navigate from your root to what folder you want. For example, if I’m in my root directory I’ll go ```cd Documents/LHR/WireWorld``` to navigate to my WireWorld folder. Pressing tab will autofill directories. Doing ```cd ..``` will go back one directory.
2. ```ls``` is a command that will display all files inside a directory.


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
For the sake of :sparkles:	aesthetic :sparkles: we want to keep all wiring diagrams in the same formatting including: colors, sizing, wire thickness, and any descriptions

Reviewers:
1. Hanna Nguyen
2. Lakshay Gupta


