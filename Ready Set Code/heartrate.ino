#define USE_ARDUINO_INTERRUPTS true
//(2) INCLUDE 2ND PACKAGE
#include <PulseSensorPlayground.h>
//(3) DEFINE AN INTEGER VARIABLE THAT HOLDS THE VALUE OF THE PIN YOUR SENSOR IS CONNECTED TO
int Sensor = 0;
//(4) DEFINE AN INTEGER VARIABLE THAT HOLDS THE VALUE OF A THRESHOLD, THAT WILL DEFINE A HEARTBEAT
int Threshold = 515;
//(5) DEFINE AN INTEGER VARIABLE TO HOLD THE VALUE OF BPM
int myBPM;
//(6) CREATE pulseSensor OBJECT
PulseSensorPlayground pulseSensor;

void setup() {
    //(7) SET UP SERIAL COMMUNICATION
    Serial.begin(600);
    //(8) CONFIGURE THE pulseSensor OBJECT BY ASSIGNING OUR SENSOR TO IT
    pulseSensor.analogInput(Sensor);
    //(9) CONFIGURE THE pulseSensor OBJECT BY ASSIGNING OUR THRESHOLD TO IT
    pulseSensor.setThreshold(Threshold);
    //CREATE pulseSensor OBJECT
    pulseSensor.begin();
}

void loop() {
    //(10) CALCULATE BPM AND STORE IN PREDEFINED VARIABLE FOR BPM
    myBPM = pulseSensor.getBeatsPerMinute();
    //(11) CONSTANTLY TEST TO SEE IF A BEAT HAPPENS - IF BEAT HAPPENS
    if (pulseSensor.sawStartOfBeat()) {
        //(12) PRINT OUT ("A HeartBeat Happened !")
        Serial.println("A HeartBeat Happened !");
        //(13) PRINT OUT ("BPM: ")
        Serial.print("BPM: ");
        //(14) PRINT OUT YOUR BPM
        Serial.println(myBPM);
    }
    //(15) DELAY FOR 20 MS
    delay(20);
}
