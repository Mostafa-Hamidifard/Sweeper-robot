import PySimpleGUI as sg
from .window import Window
from ..config import window_experiment_position_control_layout_config as layout_config
from ..arduino.SerialCommunication import SerialCommunication
import numpy as np
from typing import List
import utils


class PositionControlWindow(Window):
    def __init__(self, title="position_control"):
        self.serial_interface = SerialCommunication()
        # Todo: set the default values
        self.pid_slider = {
            key: sg.Slider(
                range=(0, 1),
                size=(40, 20),
                orientation="horizontal",
                font=layout_config["font_small"],
                resolution=0.01,
                key=f"SLIDER_{key.upper()}",
            )
            for key in ["kp", "ki", "kd"]
        }
        super().__init__(title)
        self.data = {
            "brush_control": {"speed": 0.0, "off/on": 0},
            "desired_angle": {"mode": 0, "bais": 0.0, "amp": 0.0, "period": 0.0},
            "controller": {"kp": 0.0, "ki": 0.0, "kd": 0.0},
            "frame": {"mode": 0, "bais": 0.0, "amp": 0.0, "period": 0.0},
        }
        self.back_pressed = False

    def close(self):
        self.serial_interface.close()
        super().close()

    def _create_emergency_section(self):
        self.start_stop_btn = sg.Button("Start", size=(10, 1), font=layout_config["font_medium"], key="START_BTN")
        self.home_btn = sg.Button("Home", size=(10, 1), font=layout_config["font_medium"], key="HOME_BTN")
        emergency_layout = [[self.start_stop_btn, self.home_btn]]  # done
        self.action_keys += ["START_BTN", "HOME_BTN"]
        return sg.Frame("Emergency", emergency_layout)

    def _create_brush_section(self):
        self.brush_off_radio = sg.Radio("Off", "brush_status", default=True, font=layout_config["font_small"])
        self.brush_on_radio = sg.Radio("On", "brush_status", font=layout_config["font_medium"])
        self.brush_speed_input = sg.Input(size=(5, 1), default_text="0", font=layout_config["font_medium"], key="SPEED_INPUT")
        self.brush_speed_set_btn = sg.Button(
            "Set",
            size=(5, 1),
            font=layout_config["font_medium"],
            key="BRUSH_SPEED_SET_BTN",
        )
        brush_layout = [
            [
                self.brush_off_radio,
                self.brush_on_radio,
                self.brush_speed_input,
                self.brush_speed_set_btn,
            ]
        ]
        self.action_keys += ["BRUSH_SPEED_SET_BTN"]
        return sg.Frame("Brush control", brush_layout, expand_x=True)

    def _create_pid_tuning_section(self):
        self.PID_set_btn = sg.Button(
            "Set",
            size=(5, 1),
            font=layout_config["font_medium"],
            key="PID_SET_BTN",
        )
        pid_tune_layout = [
            [
                sg.Text("Kp:", size=(3, 1), font=layout_config["font_medium"]),
                self.pid_slider["kp"],
            ],
            [
                sg.Text("Ki:", size=(3, 1), font=layout_config["font_medium"]),
                self.pid_slider["ki"],
            ],
            [
                sg.Text("Kd:", size=(3, 1), font=layout_config["font_medium"]),
                self.pid_slider["kd"],
            ],
            [self.PID_set_btn],
        ]

        self.action_keys += ["PID_SET_BTN"]

        return sg.Frame("PID Tuning", pid_tune_layout, expand_x=True)

    def _create_desired_position_section(self):
        self.des_pos = {
            "mode_radio": {
                "constant": sg.Radio(
                    "Constant",
                    "desired_position_mode",
                    font=layout_config["font_medium"],
                ),
                "square": sg.Radio(
                    "Sqaure wave",
                    "desired_position_mode",
                    font=layout_config["font_medium"],
                ),
                "sine": sg.Radio(
                    "Sine wave",
                    "desired_position_mode",
                    font=layout_config["font_medium"],
                ),
            },
            "input": {
                "amp": sg.Input("0", size=(5, 1), font=layout_config["font_medium"]),
                "bias/constant": sg.Input("0", size=(5, 1), font=layout_config["font_medium"]),
                "period": sg.Input("0", size=(5, 1), font=layout_config["font_medium"]),
            },
            "set_btn": {
                sg.Button(
                    "Set",
                    size=(5, 1),
                    font=layout_config["font_medium"],
                    key="DES_POS_SET_BTN",
                )
            },
        }

        layout = [
            [
                self.des_pos["mode_radio"]["constant"],
                self.des_pos["mode_radio"]["square"],
                self.des_pos["mode_radio"]["sine"],
            ],
            [
                sg.Text("Bias/Constant:", font=layout_config["font_small"]),
                self.des_pos["input"]["bias/constant"],
                sg.Text("Amplitude:", font=layout_config["font_small"]),
                self.des_pos["input"]["amp"],
                sg.Text("Period (sec):", font=layout_config["font_small"]),
                self.des_pos["input"]["period"],
            ],
            self.des_pos["set_btn"],
        ]
        self.action_keys += ["DES_POS_SET_BTN"]
        return sg.Frame("Desired angle", layout, expand_x=True)

    def _create_frame_section(self):
        self.frame_pos = {
            "mode_radio": {
                "constant": sg.Radio(
                    "Constant",
                    "frame_mode",
                    font=layout_config["font_medium"],
                ),
                "trapezoid": sg.Radio(
                    "Trapezoid wave",
                    "frame_mode",
                    font=layout_config["font_medium"],
                ),
                "sine": sg.Radio(
                    "Sine wave",
                    "frame_mode",
                    font=layout_config["font_medium"],
                ),
            },
            "input": {
                "amp": sg.Input("0", size=(5, 1), font=layout_config["font_medium"]),
                "bias/constant": sg.Input("0", size=(5, 1), font=layout_config["font_medium"]),
                "period": sg.Input("0", size=(5, 1), font=layout_config["font_medium"]),
            },
            "set_btn": {
                sg.Button(
                    "Set",
                    font=layout_config["font_medium"],
                    size=(5, 1),
                    key="DES_FRAME_SET_BTN",
                )
            },
        }

        layout = [
            [
                self.frame_pos["mode_radio"]["constant"],
                self.frame_pos["mode_radio"]["trapezoid"],
                self.frame_pos["mode_radio"]["sine"],
            ],
            [
                sg.Text("Bias/Constant:", font=layout_config["font_small"]),
                self.frame_pos["input"]["bias/constant"],
                sg.Text("Amplitude:", font=layout_config["font_small"]),
                self.frame_pos["input"]["amp"],
                sg.Text("Period (sec):", font=layout_config["font_small"]),
                self.frame_pos["input"]["period"],
            ],
            self.frame_pos["set_btn"],
        ]
        self.action_keys += ["DES_FRAME_SET_BTN"]
        return sg.Frame("Frame Motor control", layout, expand_x=True)

    def _create_save_section(self):
        self.save_btn = sg.Button("Save config", key="SAVE_CONFIG_BTN", font=layout_config["font_medium"])
        self.back_btn = sg.Button("Go to main Page", key="BACK_BTN", font=layout_config["font_medium"])
        layout = [self.save_btn, self.back_btn, sg.Push()]
        self.action_keys += ["SAVE_CONFIG_BTN", "BACK_BTN"]
        return layout

    def generate_layout(self) -> List:
        # canvas section
        self.angle_canvas = sg.Canvas(size=(640, 380), key="CANVAS_ANGLE", background_color="#f7f7f7")
        self.motors_canvas = sg.Canvas(size=(640, 380), key="CANVAS_MOTORS", background_color="#f7f7f7")
        column_layout_figures = [
            [self.angle_canvas],
            [self.motors_canvas],
        ]

        column_layout_controls = [
            [self._create_emergency_section(), self._create_brush_section()],
            [self._create_desired_position_section()],
            [self._create_pid_tuning_section()],
            [self._create_frame_section()],
            self._create_save_section(),
        ]
        layout = [
            [
                sg.Column(column_layout_controls, vertical_alignment="top"),
                sg.Column(column_layout_figures),
            ]
        ]
        return layout

    def START_BTN_handler(self, window, event, value):
        self.serial_interface.connect()
        self.serial_interface.start_listening(None)

    def BRUSH_SPEED_SET_BTN_handler(self, window, event, value):
        self.data["brush_control"]["speed"] = float(value["SPEED_INPUT"])

        if value[self.brush_off_radio.key]:
            self.data["brush_control"]["off/on"] = 0
        if value[self.brush_on_radio.key]:
            self.data["brush_control"]["off/on"] = 1

        self.serial_interface.send_value(self.data)

    def DES_POS_SET_BTN_handler(self, window, event, value):
        co_k = self.des_pos["mode_radio"]["constant"].key
        sq_k = self.des_pos["mode_radio"]["square"].key
        si_k = self.des_pos["mode_radio"]["sine"].key
        mode2int = {"constant": 0, "square": 1, "sine": 2}
        mode = mode2int["constant"]
        if value[co_k]:
            mode = mode2int["constant"]
        elif value[sq_k]:
            mode = mode2int["square"]
        elif value[si_k]:
            mode = mode2int["sine"]

        bias_value = value[self.des_pos["input"]["bias/constant"].key]
        amp_value = value[self.des_pos["input"]["amp"].key]
        period_value = value[self.des_pos["input"]["period"].key]

        self.data["desired_angle"]["mode"] = float(mode)
        self.data["desired_angle"]["bias"] = float(bias_value)
        self.data["desired_angle"]["amp"] = float(amp_value)
        self.data["desired_angle"]["period"] = float(period_value)

        self.serial_interface.send_value(self.data)

    def PID_SET_BTN_handler(self, window, event, value):
        kp_value = value[self.pid_slider["kp"].key]
        ki_value = value[self.pid_slider["ki"].key]
        kd_value = value[self.pid_slider["kd"].key]
        self.data["controller"]["kp"] = float(kp_value)
        self.data["controller"]["ki"] = float(ki_value)
        self.data["controller"]["kd"] = float(kd_value)

        self.serial_interface.send_value(self.data)

    def DES_FRAME_SET_BTN_handler(self, window, event, value):
        co_k = self.frame_pos["mode_radio"]["constant"].key
        sq_k = self.frame_pos["mode_radio"]["trapezoid"].key
        si_k = self.frame_pos["mode_radio"]["sine"].key
        mode2int = {"constant": 0, "trapezoid": 1, "sine": 2}
        mode = mode2int["constant"]
        if value[co_k]:
            mode = mode2int["constant"]
        elif value[sq_k]:
            mode = mode2int["trapezoid"]
        elif value[si_k]:
            mode = mode2int["sine"]

        bias_value = value[self.frame_pos["input"]["bias/constant"].key]
        amp_value = value[self.frame_pos["input"]["amp"].key]
        period_value = value[self.frame_pos["input"]["period"].key]

        self.data["frame"]["mode"] = float(mode)
        self.data["frame"]["bias"] = float(bias_value)
        self.data["frame"]["amp"] = float(amp_value)
        self.data["frame"]["period"] = float(period_value)

        self.serial_interface.send_value(self.data)

    def SAVE_CONFIG_BTN_handler(self, window, event, value):
        utils.save_experiment_config(self.title, self.data)

    def BACK_BTN_handler(self, window, event, value):
        self.back_pressed = True
        self.HOME_BTN_handler(window, event, value)
        self.SAVE_CONFIG_BTN_handler(window, event, value)

    def HOME_BTN_handler(self, window, event, value):
        print("((HOME_BTN_handler)) NOT implemented!")
