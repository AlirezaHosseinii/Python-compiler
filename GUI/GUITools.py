dark_bg_color = 'black'
light_bg_color = 'white'
button_color = 'light blue'
hover_color = 'yellow'
import sys


# def set_shortcuts(root):
#     root.bind('<Control-c>', on_exit)
#     root.bind('<Control-f>', findText)
#     root.bind('<Control-h>', findReplaceText)

def on_execute_button_hover(execute_button, event=None):
    execute_button.configure(bg=hover_color)


def on_excute_button_leave(execute_button, event=None):
    execute_button.configure(bg=button_color)


def on_test_button_hover(test_button, event=None):
    test_button.configure(bg=hover_color)


def on_test_button_leave(test_button, event=None):
    test_button.configure(bg=button_color)
