#include <AccelStepper.h>
#include <Encoder.h>

void print_info(float input, float output,long stepper_current_pos);
float pulse2degree(float pulse);
float normalize_degree(float degree);
long denormalize_output(float output);
float getCurrentAngle(Encoder* encoder);
void update_stepper(AccelStepper* stepper ,long denormalized_output, long stepper_default_pulse);