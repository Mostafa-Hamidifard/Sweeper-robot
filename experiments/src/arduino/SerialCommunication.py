import serial
import time
import threading
import json
from ..config import arduino_config


class SerialCommunication:
    def __init__(self):
        self.listening = False
        self.listener_thread = None
        self.connected = False

    def connect(self, serial_port=arduino_config["port"], baud_rate=arduino_config["baudrate"]):
        self.serial_port = serial_port
        self.baud_rate = baud_rate
        try:
            self.ser = serial.Serial(serial_port, baud_rate, timeout=1)
        except:
            print("Serial communication not stablished.")
            print("Please check the wires and arduino board.")
            return
        time.sleep(2)
        # Check if the serial connection is established
        if self.ser.is_open:
            print("Serial connection established.")
        else:
            print("Serial connection failed.")
            inp = input("Attempt again? (y)")
            if inp == "y" or inp == "Y":
                self.connect(serial_port, baud_rate)
            else:
                print("Connection wasn't established. try using connect manually...")

    def send_value(self, dictionary: dict):
        if not hasattr(self, "ser"):
            print("Serial communication has not been initialized.")
            return

        input_string = json.dumps(dictionary) + "\n"
        # Send the string to the Arduino
        encoded_text = input_string.encode("utf-8")
        length = len(encoded_text)
        chunk_len = 100
        for i in range(length//chunk_len + 1):
            print("sent:" ,encoded_text[i*chunk_len : (i+1)*chunk_len] )
            self.ser.write(encoded_text[i*chunk_len : (i+1)*chunk_len])
            time.sleep(0.5) # Assuming A delay of 1 second in the arduino
    def receive_data_thread_func(self, callback):
        while self.listening:
            response = self.ser.readline().decode()
            if response:
                print(f"Arduino response: \n{response}")
                if callback != None:
                    callback(response)

    def start_listening(self, callback):
        if not hasattr(self, "ser"):
            print("Serial communication has not been initialized.")
            return
        if not self.listening:
            self.listening = True
            self.listener_thread = threading.Thread(target=self.receive_data_thread_func, args=(callback,), daemon=True)
            self.listener_thread.start()

    def stop_listening(self):
        if not hasattr(self, "ser"):
            print("Serial communication has not been initialized.")
            return
        time.sleep(0.5)
        if self.listening:
            self.listening = False
            if self.listener_thread:
                self.listener_thread.join(timeout=0.5)

    def close(self):
        if hasattr(self, "ser"):
            self.stop_listening()
            self.ser.close()
            print("connection closed")
        else:
            print("Serial communication has not been initialized.")
