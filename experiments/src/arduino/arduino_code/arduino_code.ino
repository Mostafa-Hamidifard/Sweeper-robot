#include "TaskManager.cpp"
#include "CommunicationManager.cpp"

SerialManager serialManager;
TaskScheduler taskManager;

  


void setup() {
  Serial.begin(115200);
  pinMode(8,OUTPUT);
  pinMode(9,OUTPUT);
  pinMode(10,OUTPUT);

}

  // struct_brush BRUSHCONFIG = { 10, 8, 9 };
void loop() {
  if (Serial.available() > 0) {
  serialManager.handleInputData(Serial.readString());
  }
}

