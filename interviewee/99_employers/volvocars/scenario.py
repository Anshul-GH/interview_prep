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
import cv2

FRONT_CAMERA = 0
class Camera:
    def __init__(self, instance, stream=None):
        self.instance = instance
        self.stream = stream

    def process_stream(self):
        if not self.stream:
            # reading streaming video from the front camera
            self.stream = cv2.VideoCapture(FRONT_CAMERA)

            # simplified logic to convert stream into images or frames
            for frame in self.stream:
                if not self.images:
                    self.images = [frame]
                else:
                    self.images.append(frame)
                    

    def detect_entities(self):
        entities = {}
        if not self.images:
            for image in self.images:
                img = Image.open(image)
                # logic to process the image and detect entities
                # detected entities are added to the collection
        else:
            self.process_stream()
            self.detect_entities()

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


        

