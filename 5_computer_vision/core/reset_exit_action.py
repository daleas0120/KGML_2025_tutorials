from qtpy.QtWidgets import QApplication

class reset_exit:
    """
    This class handles the action of resetting or exiting.

    Author: Yasmin Kassim
    """

    def __init__(self, plugin):
        """
        Initializes the commute of resetting and exitting VASCilia with a reference to the main plugin.

        Args:
            plugin: The main plugin instance that this action will interact with.
        """
        self.plugin = plugin

    def exit_button(self):
        # Remove all layers safely
        while self.plugin.viewer.layers:
            self.plugin.viewer.layers.remove(self.plugin.viewer.layers[0])

        # Close the Napari viewer
        self.plugin.viewer.window.close()

    def reset_button(self, on_reset_complete=None):

        self.plugin.loading_name.setText("")
        self.plugin.loading_label.setText("")
        QApplication.processEvents()

        while self.plugin.viewer.layers:
            self.plugin.viewer.layers.remove(self.plugin.viewer.layers[0])

        attributes_to_reset = [
            "analysis_stage", "labels"
        ]
        for attr in attributes_to_reset:
            setattr(self.plugin, attr, None)

        print("✅ Plugin reset complete.")



