#pragma once
#include <ArduinoJson.h>
#include <math.h>
#include "DataManager.h"

class SerialManager {
public:
  DataManager* dataManager;
  static const size_t capacity = JSON_OBJECT_SIZE(20) + 700;  // Modify size if needed
  StaticJsonDocument<capacity> jsonDoc;
  String jsonString = "";

  SerialManager(DataManager* data_manager);
  void setBrush(bool enable, float value);
  void handleInputData(const String& input);
  void parseJson();
};
