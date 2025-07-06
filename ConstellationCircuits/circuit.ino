// Arduino UNO Constellation Circuit
// Jr. DEEP Summer, 2025
// Course: The Human Computer
// By: Ashwini Wijeyakumar

/*
************************************************
Part 1: Light Up An LED.

1. Connect power line to 5V.
2. Connect GND to ground line.
3. Connect short end of LED to ground line.
4. Connect long end of LED to 1k resistor.
5. Connect other end of resistor to a digital pin.


void setup()
{
  pinMode(2, OUTPUT);
  digitalWrite(2, HIGH);
}

void loop()
{
  delay(10); // Delay a little bit to improve simulation performance
}

*/

/* 
***************************************************
Part 2.a: Blink an LED.

1. Wiring stays the same as Part 1.

Part 2.b: Realize that adding more LEDs to a path dims.
2. Add another LED to the pathway - notice how it gets dimmer.
3. Now, add another resistor at the same NODE and add the LED onto the new path.
Run the code. Notice how the lights are brighter. Explain that this is what we call parallel circuits.


void setup()
{
  pinMode(2, OUTPUT);
}

void loop()
{
  digitalWrite(2, HIGH);
  delay(100);
  digitalWrite(2, LOW);
  delay(100);
}

*/

/*
****************************************************
Part 3: Light up the Orion.
1. Wiring follows Part 3, see image of Orion.
	It will be split into 3 parallel circuits. Use 500-1K ohm resistors.
    Students should realize the middle circuit is dimmer than the sides.
    Explain this is because there is more "load" in the middle circuit.
    To solve this, you can split the circuit into multiple parallel circuits
    or reduce the resistor value.
*/
void setup()
{
  pinMode(2, OUTPUT);
  pinMode(8,OUTPUT);
}

void loop()
{
  digitalWrite(8, LOW);
  delay(100);
  digitalWrite(8, HIGH);
  delay(100);
}

/*
****************************************************
Part 4: Zodiac Constellations
1. In teams, students will work together to break down their own zodiac constellation
	and make them blink in the same way we did the Orion.
    See slides for each zodiac's constellation: https://www.canva.com/design/DAGrjYCwEbg/GwmMOtlAT4dy4zzPLCMmDQ/edit?utm_content=DAGrjYCwEbg&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton
*/
