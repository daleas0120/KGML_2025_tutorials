import matplotlib
matplotlib.use('Qt5Agg')
import os
import json
import napari
from ui_setup import create_ui
from qtpy.QtWidgets import QApplication

class NapariPlugin:
    """
    Napari Plugin for the KGML Workshop

    This plugin was developed by Dr. Yasmin Kassim for the coding tutorial
    of the KGML (Knowledge-Guided Machine Learning) Workshop.

    It provides a structured user interface in Napari to demonstrate
    interactive image analysis and machine learning workflows.
    """

    def __init__(self):
        """Initialize the NapariPlugin class with default settings and configuration."""
        self.load_config()
        self.setup_variables()
        self.viewer = napari.Viewer()
        self.initialize_ui()

    def load_config(self):
        """Load the configuration from the 'config_kgml.json' file."""
        config_path = os.path.join(os.path.dirname(__file__), 'config_kgml.json')
        with open(config_path, 'r') as f:
            self.config = json.load(f)

    def setup_variables(self):

        """Set up the initial variables based on the loaded configuration."""
        self.rootfolder = self.config.get('rootfolder', os.path.dirname(os.path.abspath(__file__)))
        # Initialize other attributes
        self.analysis_stage = None
        self.BUTTON_WIDTH = self.config.get("button_width", 70)
        self.BUTTON_HEIGHT = self.config.get("button_height", 40)

    def initialize_ui(self):
        """Initialize the user interface for the Napari plugin."""
        container = create_ui(self) # Create the UI container using the imported function
        self.viewer.window.add_dock_widget(container, area="right", name='Napari-KGML') # Add the container to the viewer
        app = QApplication([])  # Create a QApplication instance
        self.viewer.window.qt_viewer.showMaximized()  # Maximize the viewer window
        app.exec_()  # Execute the application

if __name__ == "__main__":
    plugin = NapariPlugin()  # Instantiate the NapariPlugin class
    napari.run()  # Run the Napari application
