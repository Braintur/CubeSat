//Include Libraries
#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>


//create an RF24 object
RF24 radio(9, 8);  // CE, CSN

//address through which two modules communicate.
const byte address[6] = "00001";
//https://lastminuteengineers.com/nrf24l01-arduino-wireless-communication/
void setup()
{
  Serial.begin(9600);
  
  radio.begin();
  radio.openReadingPipe(0, address);
  radio.startListening();
}

void loop()
{
  //Read the data if available in buffer
  if (radio.available())
  {
    int text[2];
    radio.read(&text, sizeof(text));
    Serial.print(text[0]);
    Serial.print(",");
    Serial.println(text[1]);
  }
}
