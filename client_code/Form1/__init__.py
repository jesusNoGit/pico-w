from ._anvil_designer import Form1Template
from anvil import *
import anvil.server


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

       

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    
    self.button_1.visible = False
    self.button_2.visible = True
    anvil.server.call("pico_fn")

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    
    self.button_2.visible = False
    self.button_1.visible = True
    anvil.server.call("pico_fn")
    
    



