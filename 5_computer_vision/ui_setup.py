"""
Napari Plugin UI for the KGML Workshop

This module builds the user interface for the Napari plugin developed by Yasmin Kassim
as part of the coding tutorial for the Knowledge-Guided Machine Learning (KGML) workshop.

The interface includes:
- Dataset loading
- Segmentation method selection
- Instance segmentation generation
- Label filtering based on size
- Measurement and CSV export
- Reset and exit functionality

Author: Dr. Yasmin Kassim
"""


import os
from qtpy.QtWidgets import QLabel, QVBoxLayout, QWidget, QPushButton, QComboBox
from qtpy.QtGui import QPixmap
from qtpy.QtCore import Qt, QSize
from core.reset_exit_action import reset_exit
# from core.open_image_action import OpenImageAction
# from core.segmentation_action import SegmentationAction
# from core.InstanceSegmentationAction import InstanceSegmentationAction
# from core.delete_action import DeleteAction
# from core.measuements_action import LabelMeasurement
def create_ui(plugin):
    print("create_ui called")  # Debugging print statement
    container = QWidget()
    layout = QVBoxLayout(container)

    layout.setContentsMargins(0, 0, 0, 0)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    logo_path = os.path.join(script_dir, 'assets', 'logo.png')
    logo_pixmap = QPixmap(logo_path)
    logo_size = QSize(300, 100)
    scaled_logo_pixmap = logo_pixmap.scaled(logo_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)

    logo_label = QLabel()
    logo_label.setPixmap(scaled_logo_pixmap)
    logo_label.setAlignment(Qt.AlignCenter)
    logo_label.setContentsMargins(0, 0, 0, 0)
    layout.addWidget(logo_label)

    #------------------ put all the code here ---------------------------


    #----------------------------------------------------------------

    buttons_info = [
        ("Reset ", lambda: reset_exit(plugin).reset_button()),
        ("Exit ", lambda: reset_exit(plugin).exit_button())
    ]

    for text, func in buttons_info:
        button = QPushButton(text)
        button.clicked.connect(func)
        button.setMinimumSize(plugin.BUTTON_WIDTH, plugin.BUTTON_HEIGHT)
        layout.addWidget(button)

    plugin.loading_label = QLabel("")
    layout.addWidget(plugin.loading_label)

    plugin.loading_name = QLabel("")
    layout.addWidget(plugin.loading_name)

    print("create_ui completed")  # Debugging print statement

    return container
