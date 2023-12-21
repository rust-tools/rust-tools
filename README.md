# Rust Raid Cost Calculator
After many struggles, we finally produced a functional webapp that contains a Raid Cost Calculator for the game Rust by Facepunch.

Built by Olivier Broekman and Bernd van Ruremonde (FreezeSpell), using dependencies from rustLabs.

# How to Use
To run this webapp locally, run the file /webapp/__script.py__ and then go to http://127.0.0.1:5000 in your browser. NOTE: Internet Explorer is not fully supported, and not tested properly. Most of the functionality should still be there, though. Webapp was mainly tested in Orion browser, built on Apple's WebKit.

Once you have the app opened, you firstly have to select your options in the top menu. After, you can input the name of the deployable/building/vehicle you want to raid and click "BOOM!". The output will be displayed in the white text box at the bottom.
Make sure that you have the correct item type selected (e.g. deployable, vehicle, building), otherwise it will throw an error.  

# Directory Guide
A guide to what file does what and what folder contains what. Use this if you're unsure what a certain file does!  

## /webapp/
Contains all the files that are necessary for running the webapp. This includes an edited copy of __functions.py__ (__pythonFunctions.py__), meaning that this folder together with /data/ could run the app standalone.
### /static/
/font/, /img/, and __/style.css__ are responsible for the look and feel of the webapp. We suggest you leave these alone. __/suggests.json__ and it's subfiles contain a list of items that the search suggest will suggest, but do _not_ contain every item, so it will not suggest for every single item.
### /templates/
Has one file, __/index.html__, which contains the build of the webapp, including some simple JS.
### /pythonFunctions.py
An edited copy of __/functions.py__ to work with the other files specifically for the webapp. Contains the functions that calculate and output the correct data.
### /script.py
The main file for the webapp. Contains the code that actually renders the webpage. Run this to open the webapp locally.  

## /data/
2 files: items.json, a file with _all_ items and IDs in Rust, and rustlabsDurabilityData.json, a file with the accompanying health and damage data, extracted from rustLabs.  

## /wip/
Contains files that were mostly used for initial development, but also when we work on something separate from the main files.  

## /
The root folder for the project, containing the files used for running the app in console/terminal.
### /functions.py
Has the unedited, original functions that calculate the raid cost used in __main.py__.
### /main.py
Runs the cost calculator in the system console or terminal.  

### /requirements.txt
Contains the required pip packages to run the app. Use $pip install -r requirements.txt   
  

# Known Bugs
- Vehicle & Building types return "Not a valid item name or ID." as item in the output box
- Search suggest does not contain every item
- Search suggest sometimes suggests invalid items (e.g. car)
- Background does not stretch properly

Find a bug? Let us know!