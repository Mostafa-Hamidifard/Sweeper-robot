#include "definitions.h"
#include "util_functions.h"
#include <Encoder.h>
#include <PID_v1.h>
#include <AccelStepper.h>

Encoder* encoder;
PID* myPID;
AccelStepper* stepper;
double Setpoint=0.5, Input=0, Output=0;
double Kp=0.6, Ki=0.4, Kd=0.3;


void setup_stepper(AccelStepper* stepper){
  // before reaching equilibrium point
  stepper->setMaxSpeed(SETUP_MOTOR_MAX_SPEED_PULSE);
  stepper->setAcceleration(SETUP_MOTOR_ACCELERATION);
  stepper->moveTo(STEPPER_DEFAULT_VALUE);
  while(stepper->run());
  stepper->setCurrentPosition(0);
  stepper->setMaxSpeed(MOTOR_MAX_SPEED_PULSE);
  stepper->setAcceleration(MOTOR_ACCELERATION);
}

void setup() {
  Serial.begin(9600);
  encoder = new Encoder(ENCODER_A, ENCODER_B);
  stepper = new AccelStepper(1, MOTOR_STEP_PIN, MOTOR_DIR_PIN);

  setup_stepper(stepper);

  myPID = new PID(&Input, &Output, &Setpoint, Kp, Ki, Kd, DIRECT);
  myPID->SetSampleTime(CONTROL_SAMPLE_TIME);
  myPID->SetMode(AUTOMATIC);
  myPID->SetOutputLimits(-PID_OUT_LIMIT,PID_OUT_LIMIT);

}



long time1 = 0;
long time2 = 0;
void loop() {

  if (millis() - time1 > CONTROL_SAMPLE_TIME*1000){
    time1 = millis();
    Input = getCurrentAngle(encoder);
    myPID->Compute();
    float den_out = denormalize_output(Output);
    update_stepper(stepper,den_out,0);

  }

  if (millis()-time2 > 500){
    time2 = millis();
    print_info(Input,Output,stepper->currentPosition());
  }
  stepper->run();
}
