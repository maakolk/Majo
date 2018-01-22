int sensorValue;
int sensorValue2;
int frequency;
int potiValue;
int ledValue;
int start;
unsigned long current;
unsigned long next;

// constants won't change. Used here to set a pin number:
const int ledPin =  3;// the number of the LED pin

void setup() {
  // start serial port at 9600 bps:
  Serial.begin(115200);

  // set the digital pin as output:
  pinMode(ledPin, OUTPUT);
  next = 0;
}

// the loop function runs over and over again forever
void loop() {
 current = micros();
 if(next == 0)
  next = current - 1;
 if(current > next){
   next += 1000;
   sensorValue = analogRead(A0);
   Serial.println(sensorValue);
 }
 // //>>>>>>>>>>>>>>>>>>>>>>>
 sensorValue2 = analogRead(A1);
 frequency = map(sensorValue2, 0,1023, 1, 201);
    
 // //>>>>>>>>>>>>>>>>>>>>>>>>
 ledValue = ( sin( 2.0 * PI * current * frequency / 1000000.0) + 1) * 100;
 analogWrite(ledPin, ledValue);

}

