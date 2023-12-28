# Rust Raid Cost Calculator
After many struggles, we finally produced a functional webapp that contains a Raid Cost Calculator for the game Rust by Facepunch.

Built by Olivier Broekman and Bernd van Ruremonde (FreezeSpell), using dependencies from rustLabs.

# Directory Guide
A guide to what file does what and what folder contains what. Use this if you're unsure what a certain file does!  

## Root
The root directory contains all files that are necessary for the webapp to run, and for deployment.

## /consoleapp/
A standalone script that works through the console. Has the same functionality as the webapp, but doesn't look as nice.

## /data/
This contains the files that are used for calculating the raid cost etc.

## /static/
This contains all the files that are used for styling and functionality, so fonts, JS files, etc.

## /templates/
Contains all the html files that are used to render the website


  

# Known Bugs
- Search suggest does not contain every item
- Search suggest sometimes suggests invalid items (e.g. car)
- Homing missile is suggested for non-airborne targets
- Pages missing

Find a bug? Let us know!