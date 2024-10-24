#include <AccelStepper.h>
 
int step_pin = 7;
int dir_pin = 6;
AccelStepper stepper(1, step_pin, dir_pin);
void setup()
{  
  // Change these to suit your stepper if you want
  stepper.setMaxSpeed(40000);
  stepper.setAcceleration(40000);
  // stepper.moveTo(2*3200);
  stepper.moveTo(5000);
}
 
void loop()
{ 
    while(stepper.run()){}
    stepper.moveTo(4000);
    while(stepper.run()){}
    stepper.moveTo(5000);

}