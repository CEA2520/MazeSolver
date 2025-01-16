from tkinter import Tk, BOTH, Canvas

class Window:

    def __init__(self, width, height):
        self.__root = Tk()	        #creates top level window
        self.__root.mainloop()     #runs continuously until top level window is closed
        self.__root.title("Maze Solver") #replace [title goes here] with title
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width) #creates drawable area on window
        self.__canvas.Pack(fill=BOTH, expand=1)
        self.__running = False 
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running == True:
            self.redraw()
        print("window closed...")

    def close(self):
        self.__running = False