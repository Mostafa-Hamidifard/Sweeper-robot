#pragma once
// Define structs to represent the JSON structure
struct BrushControl {
  float speed = 0.0;
  int onOff = 0;
};

struct DesiredAngle {
  int mode = 0;
  float bias = 0.0;
  float amp = 0.0;
  float period = 0.0;
};

struct PIDGains {
  float kp = 0.0;
  float ki = 0.0;
  float kd = 0.0;
};

struct Frame {
  int mode = 0;
  float bias = 0.0;
  float amp = 0.0;
  float period = 0.0;
};

// Main struct to hold all the data
struct SettingData {
  BrushControl brushData;
  DesiredAngle desiredAngleData;
  PIDGains currentGains;
  Frame FrameData;
};


class DataManager {
public:
  struct SettingData data;
  
private:
}
