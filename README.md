This is a cool christmas project to add some coolness to your christmas tree.

![IMG_0051](https://github.com/SamG105/Raspberry-pi-controlled-Christmas-tree/assets/134083336/d80150f5-7567-4824-851b-ef092d5c5ab1)

you  will need:
1. raspberry pi (I used pi 4 model B)
2. 16x2 lcd
3. arduino (I used an Uno)
4. optinally a water level sensor
5. 3 mosfets (I used IRFZ44N)
6. breadboard·s
7. 4x 220Ω resistors
8. 3x 1㏀ resistors
9. 1 potentiometer or a correctly sized resistor
10. breadboard wires of all types, depending on your setup
11. an enclosure
12. wire terminal block
13. RGB led strip
14. RGB led wire
16. I would also recommend a fan & heatsink for the pi
17. 3d printing filament
18. appropriate power supplies for all the equipment


Steps: 
1) print the star!
   print all the reqired pieces:
   2x Star side
   1x Star support
   6x Star outside diffuser
   6x star inside diffuser

   I recommand prining in white but you can also paint the parts once they are prited and assembled

   Tip: you can split the sides do they fit on your 3d printer's bed

2) assemble the star
   I will upload some pictures to help guide the assembly.

   note: the track in the side pieces is made to accomaodate 2 led strips faceing inward and outward.

   First, drill a hole for the cable on the side that will be the back.
   Then, place your Leds in the track and solder the wires after passing them in the hole.
   Glue the diffusers on the outside and the inside while keeping the Leds in the track. The diffusers should fit in one place.
   Glue the support on the bottom tip of the star.
   Glue the front of the star.

3) connect the LCD to the pi
   find instructions online for your LCD and modify the pins in the python file
   here is one: https://pimylifeup.com/raspberry-pi-lcd-16x2/

4) connect the pi and the arduino using serial:
   https://roboticsbackend.com/raspberry-pi-arduino-serial-communication/

5) water level sensor wiring
   refer to the Arduino sketch for the pins and your sensor for the voltage.

6) LEDs wiring
   I used the pins as follows : R:9, G:10, B:11

   I will detail the wiring for on chanel (color) the others are the same

   source: led strip wire
   drain: led power supply ground
   gate: arduino output trought a 220Ω resistor AND connect to ground trought a 1㏀ resistor.

   Tip: Connect the arduino and power supplie grounds together.

7) upload all the code
8) have fun!
   
