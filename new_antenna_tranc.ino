#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>
#include <TroykaLight.h>

TroykaLight sensorLight(A1);
//create an RF24 object
RF24 radio(9, 8);  // CE, CSN

//address through which two modules communicate.
const byte address[6] = "00001";

void setup()
{
  radio.begin();
  Serial.begin(9600);
  //set the address
  radio.openWritingPipe(address);
  
  //Set module as transmitter
  radio.stopListening();
  pinMode(7, OUTPUT);
  
}
void loop()
{
  sensorLight.read();
  const int temp = analogRead(A0);

  int lux = sensorLight.getLightLux();

  int int_pack[2];
  int_pack[0] = temp;
  int_pack[1] = lux;

  Serial.println(int_pack[0]);
  Serial.println(int_pack[1]);

  radio.write(&int_pack, sizeof(int_pack));
  delay(500);
  digitalWrite(7, LOW);
  delay(500);
  digitalWrite(7, HIGH);
}