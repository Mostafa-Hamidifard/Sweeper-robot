#include "CommunicationManager.h"

void SerialManager::SerialManager(DataManager* data_manager) {
  this->dataManager = data_manager;
}

void SerialManager::setBrush(bool enable, float value) {
  if (!enable) {
    digitalWrite(BRUSHCONFIG.IN1pin, 0);
    digitalWrite(BRUSHCONFIG.IN2pin, 0);
    return;
  }
  if (value >= 0) {
    digitalWrite(BRUSHCONFIG.IN1pin, 1);
    digitalWrite(BRUSHCONFIG.IN2pin, 0);
  } else {
    digitalWrite(BRUSHCONFIG.IN1pin, 0);
    digitalWrite(BRUSHCONFIG.IN2pin, 1);
  }
  float absvalue = fabs(value);
  float en_value = map(absvalue, 0, 100, 0, 255);
  analogWrite(BRUSHCONFIG.ENpin, en_value);
}


void SerialManager::handleInputData(const String& input) {
  jsonString += input;
  Serial.println("jsonString is:");
  Serial.println(jsonString.c_str());
  if (jsonString.endsWith("\n")) {
    int len = jsonString.length();
    jsonString.remove(len - 1);
    parseJson();
    jsonString = "";
  }
}


void SerialManager::parseJson() {
  DeserializationError error = deserializeJson(jsonDoc, jsonString);
  if (error) {
    Serial.print(F("JSON parse failed: "));
    Serial.println(error.c_str());
    Serial.println("The input string is:");
    Serial.println(jsonString);
    jsonString = "";
    return;
  }

  // Extract and store values, keeping the previous data if the new one is unavailable
  if (jsonDoc.containsKey("brush_control")) {
    JsonObject brushControl = jsonDoc["brush_control"];
    if (brushControl.containsKey("speed")) {
      controllerSetting.brushControl.speed = brushControl["speed"];
    }
    if (brushControl.containsKey("off/on")) {
      controllerSetting.brushControl.onOff = brushControl["off/on"];
    }
    setBrush(controllerSetting.brushControl.onOff, controllerSetting.brushControl.speed);
  }

  if (jsonDoc.containsKey("desired_angle")) {
    JsonObject desiredAngle = jsonDoc["desired_angle"];
    if (desiredAngle.containsKey("mode")) {
      controllerSetting.desiredAngle.mode = desiredAngle["mode"];
    }
    if (desiredAngle.containsKey("bais")) {
      controllerSetting.desiredAngle.bias = desiredAngle["bais"];
    }
    if (desiredAngle.containsKey("amp")) {
      controllerSetting.desiredAngle.amp = desiredAngle["amp"];
    }
    if (desiredAngle.containsKey("period")) {
      controllerSetting.desiredAngle.period = desiredAngle["period"];
    }
  }

  if (jsonDoc.containsKey("controller")) {
    JsonObject controller = jsonDoc["controller"];
    if (controller.containsKey("kp")) {
      controllerSetting.controller.kp = controller["kp"];
    }
    if (controller.containsKey("ki")) {
      controllerSetting.controller.ki = controller["ki"];
    }
    if (controller.containsKey("kd")) {
      controllerSetting.controller.kd = controller["kd"];
    }
  }

  if (jsonDoc.containsKey("frame")) {
    JsonObject frame = jsonDoc["frame"];
    if (frame.containsKey("mode")) {
      controllerSetting.frame.mode = frame["mode"];
    }
    if (frame.containsKey("bais")) {
      controllerSetting.frame.bias = frame["bais"];
    }
    if (frame.containsKey("amp")) {
      controllerSetting.frame.amp = frame["amp"];
    }
    if (frame.containsKey("period")) {
      controllerSetting.frame.period = frame["period"];
    }
  }

  // Debugging: Print the stored structured data
  Serial.println("Deserialized Values (current state):");
  Serial.print("Brush Control - Speed: ");
  Serial.println(controllerSetting.brushControl.speed);
  Serial.print("Brush Control - On/Off: ");
  Serial.println(controllerSetting.brushControl.onOff);

  Serial.print("Desired Angle - Mode: ");
  Serial.println(controllerSetting.desiredAngle.mode);
  Serial.print("Desired Angle - Bias: ");
  Serial.println(controllerSetting.desiredAngle.bias);
  Serial.print("Desired Angle - Amplitude: ");
  Serial.println(controllerSetting.desiredAngle.amp);
  Serial.print("Desired Angle - Period: ");
  Serial.println(controllerSetting.desiredAngle.period);

  Serial.print("Controller - Kp: ");
  Serial.println(controllerSetting.controller.kp);
  Serial.print("Controller - Ki: ");
  Serial.println(controllerSetting.controller.ki);
  Serial.print("Controller - Kd: ");
  Serial.println(controllerSetting.controller.kd);

  Serial.print("Frame - Mode: ");
  Serial.println(controllerSetting.frame.mode);
  Serial.print("Frame - Bias: ");
  Serial.println(controllerSetting.frame.bias);
  Serial.print("Frame - Amplitude: ");
  Serial.println(controllerSetting.frame.amp);
  Serial.print("Frame - Period: ");
  Serial.println(controllerSetting.frame.period);
}