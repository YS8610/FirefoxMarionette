# Browser Automation using Firefox, Marionette an Python
  
## Installation  
You will need to install marionette driver.  
``` pip install marionette-driver ```  
  
You will also need to install the Firefox developer edition  
https://www.mozilla.org/en-US/firefox/developer/  
  
## Setting up Firefox developer edition Browser  
You need create a shortcut target the path as below  
``` <path to browser> -marionette```  
  
Type ```about:config``` in the browser address path and ensure that you have a setting `marionette.port` set at 2828. If it is missing, then you have to create that setting.  
  
## Running the script  
You will need to open up Firefox developer edition browser first with the flag `-marionette`. After that, you can start to run the script
