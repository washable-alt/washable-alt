# Day 33 


Learning of concepts for API and understanding the terms Latitude and Longitude

Application Programming Interface (API) is a set of commands, functions, protocols, and objects, that programmers can use to create software or interact with an external system. 

Your Program -> Sends a Request -> External System

External System -> Sends a Response -> Your Program

Latitude and Longitude API

Latitude is a measure of distance north or south of the equator. Latitude is a measure of distance north or south of the equator, which is an imaginary horizontal line around the exact mid-point of the earth between the 2 poles. 

Longitude is a measure of distance east or west of prime meridian. Prime meridian is the imaginary vertical line that runs down the outside of the globe from the North Pole to the South Pole. 

They are measured in degrees - Each degree can be divided up to 60 minutes, each minute can be divided up into 60 seconds.

`Great Sphinx of Giza in Egypt`
29°58′31″N 29 degrees, 58 minutes, 31 seconds North of Equator
31°8′15″E 31 degrees East of Prime Meridian

For the Sunrise and Sunset API, twilight is the period of time before sunrise and after sunset, in which the atmosphere is partially illuminated by the sun, being neither totally dark or completely lit. 

Goal: To automate sending of email when the ISS is overhead of your current longitude and latitude.

Automate using crontab and VirtualBox, as long as the VirtualBox is not being shut down.
Crontab allows the file to be run every 60 seconds. 

`* * * * * /path/to/your-bash-script-name.sh`

If you are using the crontab to automate the sending of email, then you need to comment out the time.sleep(60) and change the `while` loop to an `if` statement.  

I automate it into trash because I do not want to see the mail if the ISS station is not overhead of me. Nonetheless, I still can see the coordinates of the ISS station. 

![iss_not_overhead](https://github.com/washable-alt/washable-alt/assets/127829594/918734d5-53f8-4b58-b5df-098e0d92db33)


