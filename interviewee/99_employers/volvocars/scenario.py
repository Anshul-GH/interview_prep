# The task is about developing the Perception Function for self-driving vehicles. 

# The perception function should perceive the environment surrounding the vehicle
# and provides the rest of the self-driving function with required information. 

# Assume that the vehicle is only equipped with a front looking camera and a front
# looking radar. 

# Your task is to produce a draft for a working meeting, where you, together with
# the team will discuss how to develop the function.

# For your information, the output from the perception function will be used by
# Path Planner and Actuator Control modules to drive the vehicle. 
# However, development of these functions are out of the scope for your task.
from PIL import Image

class Camera:
    def __init__(self, instance, image):
        self.instance = instance
        self.image = image

    def detect_entities(self):
        entities = {}
        img = Image.open(self.image)
        # logic to process the image and detect entities
        # detected entities are added to the collection

        return entities
        


class Radar:
    def __init__(self, instance, angle, velocity):
        self.instance = instance
        self.angle = angle        
        self.velocity = velocity    
    
    def calculate_distance(self):
        distances = {}
        if self.entities:
            for entity in self.entities:
                # perform distance calculations based on angle
                # and velocity for each identified entity
                return distances
        


class SelfDrivingCar:    
    def __init__(self, cam_obj=None, rad_obj=None):
        self.cam_obj = cam_obj
        self.rad_obj = rad_obj
        
    def perception(self):
        if self.cam_obj:
            self.entities = self.cam_obj.detect_entities()
        
        if self.rad_obj:
            self.current_dist = self.rad_obj.calculate_distance()

        # logic to reconcile the distances and entities
        # if valid, the entities and current_distance values
        # can be used by subsequent methods


        

