# gimp-luminosity-masks
### GIMP Luminosity Mask plugin

Luminosity mask is a sweet method for tuning images, and more information below the hood can be found for example [here](https://www.gimp.org/tutorials/Luminosity_Masks/).

However, manual workflow requires furious mouse clicking, and after few images I could not resist anymore the idea to write Python script to make life easier. Plugin has been tested on Win10_64bit and with Gimp 2.8 & 2.10. 

### Installation instructions
1. Download plugin file from this repository 
2. Close GIMP 
3. Move downloaded **create_luminosity_masks.py** file into path `C:\Users\<your_user_name>\AppData\Roaming\GIMP\2.10\plug-ins` 
4. Done 

### Usage
1. Start GIMP
2. Open desired image
3. Select (or make active) the image from **layers-brushes** window 
4. Browse into **Colors>Auto>Luminosity masks...** 
5. Briefly one should find created masks in **layers-brushes** window 
6. Enjoy 
