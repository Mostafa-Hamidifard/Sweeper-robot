#define ENCODER_A 2 //OK
#define ENCODER_B 3 //OK

#define MOTOR_STEP_PIN 7  //OK
#define MOTOR_DIR_PIN 6  //OK

#define MOTOR_MAX_SPEED_PULSE 40000  // NEED TO BE Tuned
#define MOTOR_ACCELERATION 200000     // NEED TO BE Tuned

#define SETUP_MOTOR_MAX_SPEED_PULSE 4000  // NEED TO BE Tuned
#define SETUP_MOTOR_ACCELERATION 20000    // NEED TO BE Tuned

#define STEPPER_DEFAULT_VALUE 13100 // OK

#define ENCODER_RESOLUTION 2400 //OK

#define SHAFT_MIN_DEGREE 0 //OK
#define SHAFT_MAX_DEGREE 35 //OK

#define PID_OUT_LIMIT 1 //OK
#define PID_OUT2PULSE 6000 //OK
#define CONTROL_SAMPLE_TIME 0.01 // in seconds //OK


// These define's must be placed at the beginning before #include "TimerInterrupt.h"
// _TIMERINTERRUPT_LOGLEVEL_ from 0 to 4
// Don't define _TIMERINTERRUPT_LOGLEVEL_ > 0. Only for special ISR debugging only. Can hang the system.
#define TIMER_INTERRUPT_DEBUG         0
#define _TIMERINTERRUPT_LOGLEVEL_     0

#define USE_TIMER_1     true
#define USE_TIMER_3     true
#if ( defined(__AVR_ATmega644__) || defined(__AVR_ATmega644A__) || defined(__AVR_ATmega644P__) || defined(__AVR_ATmega644PA__)  || \
        defined(ARDUINO_AVR_UNO) || defined(ARDUINO_AVR_NANO) || defined(ARDUINO_AVR_MINI) ||    defined(ARDUINO_AVR_ETHERNET) || \
        defined(ARDUINO_AVR_FIO) || defined(ARDUINO_AVR_BT)   || defined(ARDUINO_AVR_LILYPAD) || defined(ARDUINO_AVR_PRO)      || \
        defined(ARDUINO_AVR_NG) || defined(ARDUINO_AVR_UNO_WIFI_DEV_ED) || defined(ARDUINO_AVR_DUEMILANOVE) || defined(ARDUINO_AVR_FEATHER328P) || \
        defined(ARDUINO_AVR_METRO) || defined(ARDUINO_AVR_PROTRINKET5) || defined(ARDUINO_AVR_PROTRINKET3) || defined(ARDUINO_AVR_PROTRINKET5FTDI) || \
        defined(ARDUINO_AVR_PROTRINKET3FTDI) )
  #define USE_TIMER_2     true
  #warning Using Timer1, Timer2
#else          
  #define USE_TIMER_3     true
  #warning Using Timer1, Timer3
#endif