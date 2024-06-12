from application import App
import customtkinter

class GUIApplication (App, customtkinter.CTk):

    def __init__ (self):
        self.app_launch()

    def app_launch(self):
        super().__init__()
        self.geometry("1000x800")
        self.title("Python Application")

    def app_menu (self): ...

    def app_options (self): ...

    def app_quit (self): ...

if __name__ == "__main__":
    guiApplication_test_instance = GUIApplication()
    guiApplication_test_instance.mainloop()