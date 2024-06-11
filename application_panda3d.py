# Panda3D Engine
from direct.showbase.ShowBase import ShowBase

class Panda3DApplication(ShowBase):

    def __init__ (self):

        ShowBase.__init__(self)
        self.scene = self.loader.loadModel("models/environnemenet")
        self.reparentTo(self.render)
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-10, 40, 0)

# Temporary Main Guard
if __name__ == "__main__":
    panda3D_instance = Panda3DApplication()
    panda3D_instance.run()


        