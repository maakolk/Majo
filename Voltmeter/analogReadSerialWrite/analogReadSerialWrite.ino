int sensorValue;
unsigned long time;

void setup() {
  // start serial port at 9600 bps:
  Serial.begin(9600);
}

// the loop function runs over and over again forever
void loop() {
 delay(20);
 sensorValue = analogRead(A0);
 Serial.print(millis());
 Serial.print(",");
 Serial.println(sensorValue);
}
