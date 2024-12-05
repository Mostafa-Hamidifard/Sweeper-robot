// #include "TaskManager.h"
// void TaskScheduler::addTask(void (*task)(), unsigned long interval) {
//   // Register tasks with specific intervals
//   tasks[numTasks].taskFunc = task;
//   tasks[numTasks].interval = interval;
//   tasks[numTasks].lastRun = millis();
//   numTasks++;
// }

// void TaskScheduler::runTasks() {
//   for (int i = 0; i < numTasks; i++) {
//     if (millis() - tasks[i].lastRun >= tasks[i].interval) {
//       tasks[i].taskFunc();          // Run the task
//       tasks[i].lastRun = millis();  // Update the last run time
//     }
//   }
// }

