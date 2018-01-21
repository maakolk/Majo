int sensorValue;
int sensorValue2;
int frequency;
int potiValue;
int ledValue;
int start;
int current;

// constants won't change. Used here to set a pin number:
const int ledPin =  3;// the number of the LED pin

void setup() {
  // start serial port at 9600 bps:
  Serial.begin(9600);

  // set the digital pin as output:
  pinMode(ledPin, OUTPUT);
}

// the loop function runs over and over again forever
void loop() {
 sensorValue = analogRead(A0);
 Serial.println(sensorValue);

 //>>>>>>>>>>>>>>>>>>>>>>>
    sensorValue2 = analogRead(A1);
    frequency = map(sensorValue2, 0,1023, 1, 100);

 //>>>>>>>>>>>>>>>>>>>>>>>>
    current = millis();
    if(current - start > 1 / frequency){
       start = start + 1 / frequency;
    }
    ledValue = ( sin( 2 * PI * millis() / 1000.0 * frequency) + 1) * 10;
    analogWrite(ledPin, ledValue);
}
