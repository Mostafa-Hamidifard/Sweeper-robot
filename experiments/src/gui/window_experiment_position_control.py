import PySimpleGUI as sg
from .window import Window
from ..config import window_experiment_position_control_layout_config as layout_config
from ..config import arduino_config
from ..arduino.SerialCommunication import SerialCommunication
import numpy as np
from typing import List


class PositionControlWindow(Window):
    def __init__(self, title="position_control"):
        self.serial_interface = SerialCommunication()
        # Todo: set the default values
        print("set the default values for kp ki and kd and define their range")
        self.pid_slider = {
            key: sg.Slider(
                range=(0, 1),
                size=(40, 20),
                orientation="horizontal",
                font=layout_config["font_small"],
                resolution=0.01,
            )
            for key in ["kp", "ki", "kd"]
        }
        super().__init__(title)

    def _create_emergency_section(self):
        self.start_stop_btn = sg.Button(
            "Start", size=(10, 1), font=layout_config["font_medium"]
        )
        self.home_btn = sg.Button(
            "Home", size=(10, 1), font=layout_config["font_medium"]
        )
        emergency_layout = [[self.start_stop_btn, self.home_btn]]  # done
        return sg.Frame("Emergency", emergency_layout)

    def _create_brush_section(self):
        self.brush_off_radio = sg.Radio(
            "Off", "brush_status", default=True, font=layout_config["font_small"]
        )
        self.brush_on_radio = sg.Radio(
            "On", "brush_status", font=layout_config["font_medium"]
        )
        self.brush_speed_input = sg.Input(
            size=(5, 1), default_text="0", font=layout_config["font_medium"]
        )
        self.brush_speed_set_btn = sg.Button(
            "Set",
            key="BRUSH_SPEED_SET_BTN",
            size=(5, 1),
            font=layout_config["font_medium"],
        )
        brush_layout = [
            [
                self.brush_off_radio,
                self.brush_on_radio,
                self.brush_speed_input,
                self.brush_speed_set_btn,
            ]
        ]
        return sg.Frame("Brush control", brush_layout, expand_x=True)

    def _create_pid_tuning_section(self):
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
        ]
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
                "bias/constant": sg.Input(
                    "0", size=(5, 1), font=layout_config["font_medium"]
                ),
                "period": sg.Input("0", size=(5, 1), font=layout_config["font_medium"]),
            },
            "set_btn": {
                sg.Button(
                    "Set",
                    "DES_POS_SET_BTN",
                    size=(5, 1),
                    font=layout_config["font_medium"],
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
        return sg.Frame("Desired angle", layout, expand_x=True)

    def _create_frame_section(self):
        self.frame_pos = {
            "mode_radio": {
                "constant": sg.Radio(
                    "Constant",
                    "desired_position_mode",
                    font=layout_config["font_medium"],
                ),
                "trapezoid": sg.Radio(
                    "Trapezoid wave",
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
                "bias/constant": sg.Input(
                    "0", size=(5, 1), font=layout_config["font_medium"]
                ),
                "period": sg.Input("0", size=(5, 1), font=layout_config["font_medium"]),
            },
            "set_btn": {
                sg.Button(
                    "Set",
                    "DES_FRAME_SET_BTN",
                    font=layout_config["font_medium"],
                    size=(5, 1),
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
        return sg.Frame("Frame Motor control", layout, expand_x=True)

    def _create_save_section(self):
        self.save_btn = sg.Button(
            "Save config", key="SAVE_CONFIG", font=layout_config["font_medium"]
        )
        self.back_btn = sg.Button(
            "Go to main Page", key="BACK", font=layout_config["font_medium"]
        )
        layout = [self.save_btn, self.back_btn, sg.Push()]
        return layout

    def generate_layout(self) -> List:
        # canvas section
        self.angle_canvas = sg.Canvas(
            size=(640, 380), key="CANVAS_ANGLE", background_color="#f7f7f7"
        )
        self.motors_canvas = sg.Canvas(
            size=(640, 380), key="CANVAS_MOTORS", background_color="#f7f7f7"
        )
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
        # self.action_keys += ["START_FAM", "NEXT_VIB"]
        # self.element_keys.append("GRAPH")
        return layout
