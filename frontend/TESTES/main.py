from tkinter import *
import cv2

root = Tk()
root.title('Model Definition')
# root.geometry('{}x{}'.format(900, 700))
# root.minsize(900, 700)
# root.maxsize(900, 700)

root.geometry('{}x{}'.format(600, 500))
root.minsize(600, 400)
root.maxsize(600, 400)

# create all of the main containers
center = Frame(root, bg='gray2', width=450, height=650, padx=3, pady=3)
btm_frame = Frame(root, bg='white', width=450, height=45, pady=3)

# layout all of the main containers
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

center.grid(row=1, sticky="nsew")
btm_frame.grid(row=3, sticky="ew")

# create the center widgets
center.grid_rowconfigure(0, weight=1)
center.grid_columnconfigure(0, weight=1)

ctr_mid = Frame(center, bg='yellow', width=250, height=190, padx=3, pady=3)
ctr_mid.grid(row=0, column=0, sticky="nsew")
#ctr_mid.grid(row=0, column=0, sticky="nsew",padx=5, pady=5)

# create the btm_frame widgets
btm_frame.grid_rowconfigure(0, weight=1)
btm_frame.grid_columnconfigure(1, weight=1)

btn_esquerda = Button(btm_frame, text ="Camera")
btn_direita = Button(btm_frame, text ="relatório")
btn_esquerda.grid(row=0, column=0,padx=5, pady=5)
btn_direita.grid(row=0, column=1, padx=5, pady=5)

class MyVideoCapture:
    def __init__(self, video_source=0):
    # Open the video source
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)

        # Get video source width and height
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

    # Release the video source when the object is destroyed
    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()
        self.window.mainloop()

video = MyVideoCapture(0)


root.mainloop()