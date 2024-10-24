#include "definitions.h"
#include <Encoder.h>
#include <AccelStepper.h>

void print_info(float input, float output,long stepper_current_pos){
  Serial.print("Input is: ");
  Serial.print(input);
  Serial.print(", Output is: ");
  Serial.print(output);
  Serial.print(", stepper_current_postion is: ");
  Serial.println(stepper_current_pos);
  
}
// converting encoder pulses to degrees
float pulse2degree(float pulse) {
  return pulse / ENCODER_RESOLUTION * 360;
}
// It normalizes the input degree to 0 to 1 based on the range
float normalize_degree(float degree) { 
  return (degree - SHAFT_MIN_DEGREE) / (SHAFT_MAX_DEGREE - SHAFT_MIN_DEGREE);
}

//  It denormalizes PID output limited by (-PID_OUT,PID_OUT) to a range of pulses
long denormalize_output(float output) {
  return  (long) (output * PID_OUT2PULSE);
}


float getCurrentAngle(Encoder* encoder) {
  float Input = pulse2degree(encoder->read());
  return normalize_degree(Input);
}


void update_stepper(AccelStepper* stepper ,long denormalized_output, long stepper_default_pulse){
    long out = denormalized_output + stepper_default_pulse; // bias input + PID input
    stepper->moveTo(out);
}


