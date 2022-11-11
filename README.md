# Canvas User Info Project
### cidi-get-canvas-ids
Center for Instructional Design and Innovation - Utah State University

* Created by Emma Lynn (a02391851@usu.edu)
* Supervised by Neal Legler, CIDI Director (neal.legler@usu.edu)
* On request from Alisa Taylor, Instructional Designer & Neal Legler, CIDI Director

This repository contains code which will return the corresponding Canvas IDs, given a list of A-numbers.

_Note: This program has only been tested on Macs up to this point. If you want to use this on another OS, you are welcome to try it and if there are issues please follow the Bug Report instructions at the bottom of this page to indicate your interest in better support for other Operating Systems._

## Start here!
In these instructions, I will walk you through the entire process of running this program.
We will be running the program using the Command Line. When I give you a command to run, it will look like this:
```
COMMAND
```
Press enter on your keyboard to run the commands once they have been entered.

Commands may or may not output text. Do not worry if some commands do not display any output.

* _A note: the terminal is an entirely text based application, so you won't be able to navigate the text with your mouse, you will need to use the arrows on the keyboard._


### Instructions

First you will need to get a copy of this project onto your computer.

_If you have experience with git and/or GitHub, feel free to simply clone the project onto your computer in the normal way. Then skip to setting up your environment._

_If you do not have experience with git/GitHub and would like to try cloning the project instead of downloading the project, follow the instructions in the Cloning a Repository section closer to the bottom of this page. 
The benefit of this method is that as maintenance is performed on the program, you will be able to easily access the updated version of the project._

* Navigate to the Launchpad and open the Terminal application on your computer.

* On GitHub, click the green Code button. In the dropdown, click Download ZIP.
* Unwrap the ZIP file.
* Navigate into the downloaded project with the following command.
```
cd Downloads/cidi-get-canvas-ids-main
```

First we need to prepare your input file.
* Your file should be a list of A-numbers, with nothing else in the file. It should be a .txt file.
  * Put each A-number on its own line
* Move your file into the project's folder
  * This can be done by opening finder, locating your input file, and dragging it into this project's folder (probably called cidi-get-canvas-ids-main)
    
Now we need to set up your environment with your specific settings.

* Now, run the following command:
```commandline
pip3 install python-dotenv --user
```

* _If you receive an error here that says something like:_
```commandline
xrun: error: invalid active developer path (/Library/Developer/CommandLineTools), missing xcrun at: /Library/Developer/CommandLineTools/usr/bin/xcrun
```
* _Run:_
```commandline
xcode-select --install
```
* _And try the previous command again._
    
*  Run the following commands:
```commandline
touch .env
```
```commandline
nano .env
```

  *  Your command line has now been turned into a simple text editor. Copy the text below and paste into the file, replacing the filler text with your information.
  ```commandline
CANVAS_API_TOKEN=token
SOURCE_FILE=source_file
```

* token should be replaced with your personal API key. If you don't have one, see the bottom of this page.
* source_file should be replaced with the name of your input file, INCLUDING the extension
  * Ex. `SOURCE_FILE=a-numbers.txt`, `SOURCE_FILE=ANumbers.txt`, etc

* Once you have correctly filled in the text, press `CTRL + X` on your keyboard, followed by the `y` key, and then the `enter` key.


* Your environment has now been set up!

Running the program:

* Run the following command:
```commandline
python3 parseData.py
```
* The program will now begin running. Depending on the number of IDs you are retrieving, it may take several minutes.
* When the program is complete, the generated output file should be opened in your default .csv application. It can also be found at `userInfo.csv` in the folder holding the program

If you would like to change your data set input, repeat the above steps, beginning at the command:
```commandline
nano .env
```

### Cloning a GitHub repository:
* Run the following commands:
```commandline
cd Desktop
```
```commandline
git clone https://github.com/elynn-usu/cidi-get-canvas-ids.git canvas-id-script
```
```commandline
cd canvas-id-script
```
* _If you receive an error that says something like:_
```commandline
xrun: error: invalid active developer path (/Library/Developer/CommandLineTools), missing xcrun at: /Library/Developer/CommandLineTools/usr/bin/xcrun
```
* _Run:_
```commandline
xcode-select --install
```
* _And try the previous command again._

You should now have a copy of the project on your computer. To get the latest changes before running the program in the future, run the following commands 
(after opening a new terminal window):
```commandline
cd Desktop/canvas-id-script
```
```commandline
git pull origin master
```
The project should update with any changes and bug fixes.

_If you are having issues with cloning the project, feel free to go back and try downloading the zip as is instructed in the original instructions. You can also email me (a02391851@usu.edu) and I can help you set everything up if you would prefer._

You can now return to the original instructions. Begin at the section on setting up your environment.

## Bug Reports
If something behaves unexpectedly, or you run into a problem with the program, please let me know.

Send bug reports to a02391851@usu.edu with the subject line "Bug Report - Canvas User Info".

Please include:
* What you expected to happen
* What actually happened
* As much output from the terminal as possible - copy and pasted, not in a screenshot
* Look in the cidi-get-canvas-ids-main folder. The files canvasData0000000.txt and contextReport0000000.txt may have been created (where 0000000 is a 7 digit number). Please attach these files to your bug report if they have been created. 
* Your input file
* What OS you're using (Windows, Mac)
* Any other information that you think could be useful

I will get back to you with an update, most likely within 2 business days. Thank you.

## Getting an API key
https://learninganalytics.ubc.ca/for-students/canvas-api/ is a really great resource that walks you through creating an API key.
 Log in to canvas at `usu.instructure.com` instead of the ubc.ca link. Everything else in the `Generate your Canvas access token` section should be applicable.
 
Canvas will only show you your token once. Be sure to copy it down somewhere secure. 

**DO NOT share your access token with anyone.**

Anyone with your token has the ability to **act as you** in Canvas. If you believe your token may have been exposed, **delete it right away**. (Link to deletion instructions below.)
 Your token should be password protected at the very least.

Deletion instructions: https://community.canvaslms.com/t5/Student-Guide/How-do-I-manage-API-access-tokens-as-a-student/ta-p/273