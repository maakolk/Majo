int sensorValue;

void setup() {
  // start serial port at 9600 bps:
  Serial.begin(9600);
}

// the loop function runs over and over again forever
void loop() {
 sensorValue = analogRead(A0);
 Serial.println(sensorValue);
}
