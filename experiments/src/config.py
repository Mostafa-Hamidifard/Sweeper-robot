import os

DATA_SAVE_PATH = os.path.join(os.getcwd(), "data\\position_control")

os.makedirs(DATA_SAVE_PATH, exist_ok=True)

window_experiment_selection_layout_config = {
    "font_large": ("Arial", 18),
    "font_medium": ("Arial", 16),
    "font_small": ("Arial", 14),
    "btn_color": "#2C3E50",
}
window_experiment_position_control_layout_config = {
    "font_large": ("Arial", 18),
    "font_medium": ("Arial", 16),
    "font_small": ("Arial", 14),
    "btn_color": "#2C3E50",
    "axes_size": (400, 600),
}


arduino_config = {
    "port": "COM13",
    "baudrate": 115200,
}
