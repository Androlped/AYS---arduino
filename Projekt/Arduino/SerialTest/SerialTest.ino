int incomingByte = 0;   // for incoming serial data
int loadInitialize[] = {108,111,97,100,32,48,32,49,32,50,32,51,10};
void setup() {
        Serial.begin(115200);     // opens serial port, sets data rate to 9600 bps
}

void loop() {

        // send data only when you receive data:

                // read the incoming byte:
                for(int i=0;i<13;i++){
                  incomingByte = loadInitialize[i];

                  // say what you got:
                  Serial.print("I received: ");
                  Serial.println(incomingByte);
                }

  delay(1000);
}
