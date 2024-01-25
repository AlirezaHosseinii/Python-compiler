dark_bg_color = 'black'
light_bg_color = 'white'
button_color = 'light blue'
hover_color = 'yellow'
import sys
def set_shortcuts(root):
    root.bind('<Control-c>', on_exit)
    root.bind('<Control-f>', findText)
    root.bind('<Control-h>', findReplaceText)

def on_execute_button_hover(self, event):
    self.execute_button.configure(bg=self.hover_color)

def on_excute_button_leave(self, event):
    self.execute_button.configure(bg=self.button_color)

def on_test_button_hover(self, event):
    self.test_button.configure(bg=self.hover_color)

def on_test_button_leave(self, event):
    self.test_button.configure(bg=self.button_color)

