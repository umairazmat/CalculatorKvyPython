import os
import csv
import kivy 
      
# base Class of your App inherits from the App class.   
# app:always refers to the instance of your application  
from kivy.app import App
    
# this restrict the kivy version i.e 
# below this kivy version you cannot 
# use the app or software 
kivy.require('1.9.0')
 
# for making multiple buttons to arranging
# them we are using this
from kivy.uix.gridlayout import GridLayout
 
# for the size of window
from kivy.config import Config
 
# Setting size to resizable
Config.set('graphics', 'resizable', 1)
## Config.set('graphics', 'width', '400')
## Config.set('graphics', 'height', '400')

from xml.etree.ElementTree import Element, SubElement, ElementTree


# Creating Layout class
class CalcGridLayout(GridLayout):
  
    # Function called when equals is pressed
            
    def calculate(self, calculation):
    
        if calculation:
            try:
                # Solve formula and display it in entry
                # which is pointed at by display
                a = str(eval(calculation))
                self.display.text = a
                return a
            except Exception:
                self.display.text = "Error"

                
    def submit_data_xml(self, instance):
        result = self.display.text
        data = Element('data')
        history = SubElement(data, 'history')
        history.set('result', result)
        tree = ElementTree(data)
        if not os.path.exists('data1.xml'):
            tree.write('data1.xml')
        else:
            tree.parse('data1.xml')
            root = tree.getroot()
            history = SubElement(root, 'history')
            history.set('result', result)
            tree.write('data1.xml')
    
    def submit_data_csv(self, instance):
        result = self.display.text
        filename = 'data.csv'
        with open(filename, mode='a') as file:
            writer = csv.writer(file)
            writer.writerow([result])
  
 # Creating App class
class CalculatorApp(App):
  
    def build(self):
        return CalcGridLayout()
  
# creating object and running it
calcApp = CalculatorApp()
calcApp.run()