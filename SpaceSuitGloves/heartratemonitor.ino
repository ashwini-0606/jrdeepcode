#include <Wire.h>
#include <LiquidCrystal_I2C.h>

// Initialize I2C LCD at address 0x27, 16 columns and 2 rows
LiquidCrystal_I2C lcd(0x27, 16, 2); 

// Pulse Sensor Pin
const int pulseSensorPin = A0;
const int buzzer = 10;

// BPM Calculation Variables
int pulseThreshold = 550;
int pulseSignal = 0;
bool pulseDetected = false;

unsigned long lastBeatTime = 0;
unsigned long currentTime = 0;
int BPM = 0;

void calculateBPM() {
  pulseSignal = analogRead(pulseSensorPin);
  currentTime = millis();

  // Detect rising edge
  if (pulseSignal > pulseThreshold && !pulseDetected) {
    unsigned long IBI = currentTime - lastBeatTime;
    lastBeatTime = currentTime;

    if (IBI > 300 && IBI < 2000) {
      BPM = 60000 / IBI;
    }
    pulseDetected = true;
  }

  if (pulseSignal < pulseThreshold) {
    pulseDetected = false;
  }

  delay(10);
}

void setup() {
  pinMode(buzzer, OUTPUT);
  Serial.begin(9600);

  lcd.init();          // Initialize LCD
  lcd.backlight();     // Turn on backlight
  lcd.setCursor(0, 0);
  lcd.print("Pulse Sensor");
  lcd.setCursor(0, 1);
  lcd.print("Initializing...");
  delay(2000);
  lcd.clear();
}

void loop() {
  calculateBPM();

  // Print to Serial
  Serial.print("BPM: ");
  Serial.println(BPM);

  // Print to LCD
  lcd.setCursor(0, 0);
  lcd.print("Heart Rate:    "); // Clear old digits
  lcd.setCursor(0, 1);
  lcd.print("BPM: ");
  lcd.print(BPM);
  lcd.print("   "); // Clear extra digits

  delay(250);
}
