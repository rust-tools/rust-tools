# Rust Raid Cost Calculator
After many struggles, we finally produced a functional webapp that contains a Raid Cost Calculator for the game Rust by Facepunch.

# How to Use
To run this webapp locally, run the file /webapp/script.py and then go to http://127.0.0.1:5000 in your browser. NOTE: Internet Explorer is not fully supported, and not tested properly. Most of the functionality should still be there, though.

Once you have the app opened, you firstly have to select your options in the top menu. After, you can input the name of the deployable/building/vehicle you want to raid and click "BOOM!". The output will be displayed in the white text box at the bottom.
Make sure that you have the correct item type selected (e.g. deployable, vehicle, building), otherwise it will throw an error.

# Directory Guide


# Known Bugs
- Vehicle & Building types return "Not a valid item name or ID." as item in the output box
- Search suggest does not contain every item
- Search suggest sometimes suggests invalid items (e.g. car)
- Background does not stretch properly

Find a bug? Let us know!