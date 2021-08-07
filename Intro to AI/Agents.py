#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Agent:
    def __init__(self, name, environment, actuators, sensors, performance):
        self.name = name
        self.environment = environment
        self.actuators = actuators
        self.sensors = sensors
        self.performanceMetrics = performance
        
    def printinfo(self):
        print('Name: %s' % self.name)
        print('Environment: %s' % self.environment)
        print('Actuators: %s' % self.actuators)
        print('Sensors: %s' % self.sensors)
        print('Performance Metrics: %s' % self.performanceMetrics)
        

dog = Agent('dog', 'Real world', ['legs', 'mouth'], ['eyes' , 'ears', 'nose'] , 
            'age')

butter_passing_robot = Agent('Butter passing robot', 'table', ['hooks', 'hand', 
                                'speaker'], ['camera', 'microphone'], 
                                 ['number of people on table with butter'])

AC = Agent('AC', 'home', ['button', 'change window'], ['temperture reader'], 
           'maintain desired temperture')

id_reader = Agent('ID Reader', 'door', ['LED', 'door lock'], ['Scanner'], 
                  ['Accept those with correct ID', 'deny those with incorrect ID', 
                   'speed of the door'])

microwave = Agent('microwave', 'kitchen', ['heat'], ['buttons'], ['timer'])


dog.printinfo()
print()

butter_passing_robot.printinfo()
print()

AC.printinfo()
print()

id_reader.printinfo()
print()

microwave.printinfo()


# In[ ]:




