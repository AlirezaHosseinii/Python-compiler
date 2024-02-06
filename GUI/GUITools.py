import sys
global current_mode
current_mode = 'dark'

class GUIToolsCLass:
    def __init__(self,workBench):
        self.dark_bg_color = 'black'
        self.light_bg_color = 'white'
        self.button_color = 'light blue'
        self.hover_color = 'yellow'
        self.workbench = workBench

    def on_execute_button_hover(self, event=None):
        self.workbench.execute_button.configure(bg=self.hover_color)


    def on_excute_button_leave(self, event=None):
        self.workbench.execute_button.configure(bg=self.button_color)


    def on_test_button_hover(self, event=None):
        self.workbench.test_button.configure(bg=self.hover_color)


    def on_test_button_leave(self, event=None):
        self.workbench.test_button.configure(bg=self.button_color)
