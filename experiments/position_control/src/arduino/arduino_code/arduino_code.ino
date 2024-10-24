int vib_begin = 3;
int vib1_pin = 3;
int vib2_pin = 4;
int vib3_pin = 5;
int vib4_pin = 6;
int vib5_pin = 7;



void setup() {
  for (int i=0; i < 5; i++){
    int pin_number = vib_begin + i; 
    pinMode(pin_number,OUTPUT);
    analogWrite(pin_number,0);
  }
  // Initialize serial communication
  Serial.begin(9600);
  Serial.flush();
}
// int key = "";
// int value = "";

void loop() {
  // Check if there is any data available to read
  if (Serial.available() > 0) {
    // Read the incoming string
    String inputString = Serial.readStringUntil('\n');

    // Parse the string into individual values
    char inputArray[200];
    inputString.toCharArray(inputArray, 100);
    char *token = strtok(inputArray, ",");
    
    int values[5];
    int count = 0;
    // Loop through the tokens and store them in the array
    while (token != NULL) {
      if (count < 5) {
        values[count] = atoi(token); // Convert the token to an integer
        count++;
      }
      token = strtok(NULL, ",");
    }
    // Check if exactly 5 values were received
    if (count == 5) {
      for (int i = 0; i < 5; i++) {
        Serial.print("Received value ");
        Serial.print(i + 1);
        Serial.print(": ");
        Serial.println(values[i]);
        int pin_number = vib_begin + i; 
        analogWrite(pin_number, values[i]);
      }
    } else {
      Serial.println("Error: Exactly 5 values are required.");
    }
  }
}
