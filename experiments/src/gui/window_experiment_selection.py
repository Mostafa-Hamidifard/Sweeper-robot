import PySimpleGUI as sg
from ..config import window_experiment_selection_layout_config as layout_config
from .window import Window
from typing import List


class ExperimentSelection(Window):

    def __init__(self, title="experiment_selection"):
        super().__init__(title)
        self.position_control_clicked = False

    def generate_layout(self) -> List:
        layout = [
            [sg.Text("Select the experiment:" + " " * 20, font=layout_config["font_medium"])],
            [sg.Push(), sg.Button("Position Control Tuning", size=(20, 1), font=layout_config["font_small"], key="POSITION_CONTROL_TUNING"), sg.Push()],
            [sg.Push(), sg.Button("Force Control Tuning", size=(20, 1), font=layout_config["font_small"], key="FORCE_CONTROL_TUNING", disabled=True), sg.Push()],
            [sg.Push(), sg.Button("Scenario 1", size=(20, 1), font=layout_config["font_small"], key="SCENARIO_1", disabled=True), sg.Push()],
            [sg.Push(), sg.Button("Scenario 2", size=(20, 1), font=layout_config["font_small"], key="SCENARIO_2", disabled=True), sg.Push()],
        ]
        self.action_keys.append("POSITION_CONTROL_TUNING")
        return layout

    def POSITION_CONTROL_TUNING_handler(self, window, event, values) -> None:
        self.position_control_clicked = True  # Toggle it in window transition

    def FORCE_CONTROL_TUNING_handler(self, window, event, values) -> None:
        pass

    def SCENARIO_1_handler(self, window, event, values) -> None:
        pass

    def SCENARIO_2_handler(self, window, event, values) -> None:
        pass
