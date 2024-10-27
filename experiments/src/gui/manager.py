from .window import Window, Window_manager
from .window_experiment_selection import ExperimentSelection
from .window_experiment_position_control import PositionControlWindow
from typing import List


# Vibration Experiment Manager
class VEManager(Window_manager):
    def create_windows(self) -> List[Window]:
        window1 = ExperimentSelection(title="experiment_selection")
        window1.create_window()
        window2 = PositionControlWindow(title="position_control")
        window2.create_window()
        return [window1, window2]

    def experiment_selection2position_control_check(self):
        if self.current_window.position_control_clicked:
            self.current_window.position_control_clicked = False
            return True
        return False

    def experiment_selection2position_control_action(self, id) -> None:
        self.current_window.window.hide()
        future_window = self.windows[id]
        future_window.window.un_hide()

    # def subject_info2familiarization_check(self) -> bool:
    #     subject_info_window = self.current_window
    #     if not hasattr(subject_info_window, "user_info_saved"):
    #         raise AttributeError("No attribute with name of 'user_info_saved'.")
    #     if subject_info_window.user_info_saved:
    #         # user_info has been saved and We are ready to go to the familiarization window
    #         return True
    #     else:
    #         return False

    # def subject_info2familiarization_action(self, id) -> None:
    #     self.current_window.close()
    #     future_window = self.windows[id]
    #     future_window.window.un_hide()

    # def familiarization2main_experiment_check(self) -> bool:
    #     fam_window = self.current_window
    #     if not hasattr(fam_window, "start_main_exp_pressed"):
    #         raise AttributeError("No attribute with name of 'start_main_exp_pressed'.")
    #     if fam_window.start_main_exp_pressed:
    #         return True
    #     else:
    #         return False

    # def familiarization2main_experiment_action(self, id) -> None:
    #     self.current_window.close()
    #     future_window = self.windows[id]
    #     future_window.window.un_hide()
