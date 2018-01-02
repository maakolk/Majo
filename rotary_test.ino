/*     Arduino Rotary Encoder Tutorial
 *      
 *  by Dejan Nedelkovski, www.HowToMechatronics.com
 *  
 */
 
 #define outputA 6
 #define outputB 7

 int counter = 0; 
 int aState;
 int aLastState;  

 void setup() { 
   pinMode (outputA,INPUT);
   pinMode (outputB,INPUT);
   
   Serial.begin (9600);
   // Reads the initial state of the outputA
   aLastState = digitalRead(outputA);   
 } 

 void loop() { 
   aState = digitalRead(outputA); // Reads the "current" state of the outputA
   // If the previous and the current state of the outputA are different, that means a Pulse has occured
   if (aState != aLastState){     
     // If the outputB state is different to the outputA state, that means the encoder is rotating clockwise
     if (digitalRead(outputB) != aState) { 
       counter ++;
     } else {
       counter --;
     }if (counter ==-0) Serial.println ("N");
      if (counter ==-5) Serial.println ("N/O");
      if (counter ==10) Serial.println ("O");
      if (counter ==-15) Serial.println ("S/O");
      if (counter ==-20) Serial.println ("S");
      if (counter ==-25) Serial.println ("S/W");
      if (counter ==-30) Serial.println ("W");
      if (counter ==-35) Serial.println ("N/W");
      if (counter ==-40) Serial.println ("N");
      if (counter ==-45) Serial.println ("N/O");
      if (counter ==-50) Serial.println ("O");
      if (counter ==-55) Serial.println ("S/O");
      if (counter ==-60) Serial.println ("S");
      if (counter ==-65) Serial.println ("S/W");
      if (counter ==-70) Serial.println ("W");
      if (counter ==-75) Serial.println ("N/W");
      if (counter ==-80) Serial.println ("N");
      if (counter ==0) Serial.println ("N");
      if (counter ==5) Serial.println ("N/O");
      if (counter ==10) Serial.println ("O");
      if (counter ==15) Serial.println ("S/O");
      if (counter ==20) Serial.println ("S");
      if (counter ==25) Serial.println ("S/W");
      if (counter ==30) Serial.println ("W");
      if (counter ==35) Serial.println ("N/W");
      if (counter ==40) Serial.println ("N");
      if (counter ==45) Serial.println ("N/O");
      if (counter ==50) Serial.println ("O");
      if (counter ==55) Serial.println ("S/O");
      if (counter ==60) Serial.println ("S");
      if (counter ==65) Serial.println ("S/W");
      if (counter ==70) Serial.println ("W");
      if (counter ==75) Serial.println ("N/W");
      if (counter ==80) Serial.println ("N");
    
   } 
   aLastState = aState; // Updates the previous state of the outputA with the current state
 }
