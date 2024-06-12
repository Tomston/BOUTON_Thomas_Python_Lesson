# Panda3D Engine
from direct.showbase.ShowBase import ShowBase
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Point3


class Panda3DApplication(ShowBase):

    def __init__ (self):
        ShowBase.__init__(self)
        
        # Load the environment model 
        self.scene = self.loader.loadModel("models/environment")
        # Reparent the model to render
        self.scene.reparentTo(self.render)
        # Apply scale and position transforms on the model
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-10, 40, 0)

        # Load and transform the panda actor
        self.pandaActor = Actor("models/panda-model",
                                {"walk": "models/panda-walk4"})
        
        self.pandaActor.setScale(0.005, 0.005, 0.005)
        self.pandaActor.reparentTo(self.render)
        # Loop its animation
        self.pandaActor.loop("walk")

        # Create the four lerp intervals needed for the panda to
        # walk back and forth.
        posInterval1 = self.pandaActor.posInterval(13,
                                                   Point3(0, -10, 0),
                                                   startPos=Point3(0, 10, 0))
        posInterval2 = self.pandaActor.posInterval(13,
                                                   Point3(0, 10, 0),
                                                   startPos=Point3(0, -10, 0))
        hprInterval1 = self.pandaActor.hprInterval(3,
                                                   Point3(180, 0, 0),
                                                   startHpr=Point3(0, 0, 0))
        hprInterval2 = self.pandaActor.hprInterval(3,
                                                   Point3(0, 0, 0),
                                                   startHpr=Point3(180, 0, 0))

        # Create and play the sequence that coordinates the intervals.
        self.pandaPace = Sequence(posInterval1, hprInterval1,
                                  posInterval2, hprInterval2,
                                  name="pandaPace")
        self.pandaPace.loop()
        """"
        When the pandaPosInterval1 interval is started, it will gradually adjust the position of the panda from (0, 10, 0) to (0, -10, 0) 
        over a period of 13 seconds. Similarly, when the pandaHprInterval1 interval is started, the heading of the panda will rotate 180 degrees 
        over a period of 3 seconds.

        The pandaPace sequence above causes the panda to move in a straight line, turn, move in the opposite straight line, and finally turn again. 
        The code pandaPace.loop() causes the Sequence to be started in looping mode.
        """

# Temporary Main Guard
if __name__ == "__main__":
    panda3D_instance = Panda3DApplication()
    panda3D_instance.run()


        