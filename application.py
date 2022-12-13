import tkinter as tk
from tkinter import *
import random
import os
from tkinter.filedialog import askopenfilename, asksaveasfile
from PIL import ImageTk, Image, ImageFilter, ImageOps
from RGB_Editor import RGB_Editor

#Import all the enhancement filter from pillow
from PIL.ImageFilter import (
   BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
   EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN
)

class App():
    def __init__(self):

        # create initial flags and PIL images to avoid garbage collection
        self.opened_flag=0
        self.editor = RGB_Editor()
        self.PIL_img = None
        self.img = None
        self.frogs = []
        # initialize frogs!!!
        for files in os.listdir("./frogs"):
            self.frogs.append(files)
        
        # create window and main frame
        self.window = tk.Tk()
        self.window.title("Image Manipulator")
        self.frame_img = Frame(self.window, bg = "#f3c7f6")
        self.button_frame = Frame(self.window)
        self.frame_img.grid(row = 0, column = 0)
        self.button_frame.grid(row = 0, column = 1)
        
        # create buttons for image filters
        self.btn_open = tk.Button(self.button_frame, text="New Image", command=self.open_file)
        self.btn_save = tk.Button(self.button_frame, text="Save Image", command=self.save_file)
        self.btn_frog = tk.Button(self.button_frame, text="Show me a frog!", command=self.choose_frog)
        self.btn_inverse = tk.Button(self.button_frame, text="Inverse", command=lambda: self.update_canvas("inverse"))
        self.btn_emboss = tk.Button(self.button_frame, text="Emboss", command=lambda: self.update_canvas("emboss"))
        self.btn_reset = tk.Button(self.button_frame, text="Reset", command=lambda: self.update_canvas("reset"))
        self.btn_gray = tk.Button(self.button_frame, text="Grayscale", command=lambda: self.update_canvas("gray"))
        self.btn_solar = tk.Button(self.button_frame, text="Solarize", command=lambda: self.update_canvas("solar"))
        self.btn_flip = tk.Button(self.button_frame, text="Flip", command=lambda: self.update_canvas("flip"))
        self.btn_poster = tk.Button(self.button_frame, text="Posterize", command=lambda: self.update_canvas("poster"))
        self.btn_blur = tk.Button(self.button_frame, text="Blur", command=lambda: self.update_canvas("blur"))
        self.btn_sharp = tk.Button(self.button_frame, text="Sharpen", command=lambda: self.update_canvas("sharp"))
        
        #rgb slider buttons
        self.btn_r = tk.Button(self.button_frame, text="Set R Value", command=lambda: self.use_slider("red"))
        self.btn_b = tk.Button(self.button_frame, text="Set B Value", command=lambda: self.use_slider("blue"))
        self.btn_g = tk.Button(self.button_frame, text="Set G Value", command=lambda: self.use_slider("green"))
        self.btn_bright = tk.Button(self.button_frame, text="Set Brightness", command=lambda: self.use_slider("bright"))
        
        # create rgb value sliders
        self.red_slider = Scale(self.button_frame, from_=-128, to=128, orient=HORIZONTAL)
        self.blue_slider = Scale(self.button_frame, from_=-128, to=128, orient=HORIZONTAL)
        self.green_slider = Scale(self.button_frame, from_=-128, to=128, orient=HORIZONTAL)
        self.bright_slider = Scale(self.button_frame, from_=0, to=100, orient=HORIZONTAL)
        self.bright_slider.set(50)
        
        #labels
        self.red_l = Label(self.button_frame, text = "Red Value Slider")
        self.green_l = Label(self.button_frame, text = "Green Value Slider")
        self.blue_l = Label(self.button_frame, text = "Blue Value Slider")
        self.bright_l = Label(self.button_frame, text = "Brightness Slider")

        # place initial button
        self.btn_open.grid(row = 0, column = 1, padx=(10,10), pady = (10,10))

    def update_canvas(self, change):
        # switch checks for which PIL filter to use -- need to convert to Image to filter, then update the TkImage to display
        match change:
            case "emboss":
                self.PIL_img = self.PIL_img.filter(EMBOSS)
                self.img = ImageTk.PhotoImage(self.PIL_img)
            case "blur":
                self.PIL_img = self.PIL_img.filter(BLUR)
                self.img = ImageTk.PhotoImage(self.PIL_img)
            case "sharp":
                self.PIL_img = self.PIL_img.filter(SHARPEN)
                self.img = ImageTk.PhotoImage(self.PIL_img)
            case "inverse":
                self.PIL_img = ImageOps.invert(self.PIL_img)
                self.img = ImageTk.PhotoImage(self.PIL_img)
            case "gray":
                self.PIL_img = ImageOps.grayscale(self.PIL_img)
                self.img = ImageTk.PhotoImage(self.PIL_img)
            case "poster":
                self.PIL_img = ImageOps.posterize(self.PIL_img, 2)
                self.img = ImageTk.PhotoImage(self.PIL_img)
            case "solar":
                self.PIL_img = ImageOps.solarize(self.PIL_img, 64)
                self.img = ImageTk.PhotoImage(self.PIL_img)
            case "flip":
                self.PIL_img = ImageOps.flip(self.PIL_img)
                self.img = ImageTk.PhotoImage(self.PIL_img)
            case "reset":
                self.img = ImageTk.PhotoImage(Image.open(self.filepath))
                self.PIL_img = Image.open(self.filepath)
                self.PIL_img = self.PIL_img.convert('RGB')
                
        # loading the new filtered image
        self.img_container = self.canvas.create_image(0, 0, anchor=NW, image = self.img)
        self.canvas.grid(row = 1, column = 1, columnspan = 2, padx=(10,10), pady =(10,10), sticky = W)

    def use_slider(self, change):
        # switch checks which rgb value to update
        match change:
            # use RGBEditor functions on Image, then convert back to TkImage to display
            case "red":
                self.PIL_img = self.editor.set_red(self.PIL_img, self.red_slider.get())
                self.img = ImageTk.PhotoImage(self.PIL_img)
            case "blue":
                self.PIL_img = self.editor.set_blue(self.PIL_img, self.blue_slider.get())
                self.img = ImageTk.PhotoImage(self.PIL_img)
            case "green":
                self.PIL_img = self.editor.set_green(self.PIL_img, self.green_slider.get())
                self.img = ImageTk.PhotoImage(self.PIL_img)
            case "bright":
                self.PIL_img = self.editor.set_brightness(self.PIL_img, self.bright_slider.get())
                self.img = ImageTk.PhotoImage(self.PIL_img)

        # loading the image
        self.img_container = self.canvas.create_image(0, 0, anchor=NW, image = self.img)
        self.canvas.grid(row = 1, column = 1, columnspan = 2, padx=(10,10), pady =(10,10), sticky = W)

    def choose_frog(self):
        # choose a random frog from the list!
        num = random.randrange(1, len(self.frogs))
        self.filepath = "./frogs/{}".format(self.frogs[num])
        # reset the image
        self.canvas.destroy()
        # Create a photoimage object of the image in the path
        self.PIL_img = Image.open(self.filepath)
        self.PIL_img = self.PIL_img.convert('RGB')
        self.img = ImageTk.PhotoImage(Image.open(self.filepath))
        self.w, self.h = self.PIL_img.size
        # arranging application parameters
        self.canvas = tk.Canvas(self.frame_img, height = self.h, width = self.w, background = "pink")
        # loading the image
        self.img_container = self.canvas.create_image(0, 0, anchor=NW, image = self.img)
        self.canvas.grid(row = 1, column = 1, columnspan = 2, padx=(10,10), pady =(10,10), sticky = W)    

    def save_file(self):
        """Open a file for editing."""
        self.filepath = asksaveasfile(initialfile = 'edited.jpg', defaultextension=".jpg", filetypes=[("All Files","*.*")])
        
        if not self.filepath:
            return
        
        self.PIL_img.save(self.filepath)
        
    def open_file(self):
        """Open a file for editing."""
        self.filepath = askopenfilename(
            filetypes=[("All Files", "*.*")]
        )
        if not self.filepath:
            return

        #test if there is a current image or not we need to replace
        if self.opened_flag == 0:
            self.opened_flag = 1
        else:
            self.canvas.destroy() #destroys old image so we can replace it with the new one
        # Create a photoimage object of the image in the path
        self.PIL_img = Image.open(self.filepath)
        self.PIL_img = self.PIL_img.convert('RGB')
        self.img = ImageTk.PhotoImage(Image.open(self.filepath))
        self.w, self.h = self.PIL_img.size
        # arranging application parameters
        self.canvas = tk.Canvas(self.frame_img, height = self.h, width = self.w, background = "pink")
        # loading the image
        self.img_container = self.canvas.create_image(0, 0, anchor=NW, image = self.img)
        self.canvas.grid(row = 1, column = 1, columnspan = 2, padx=(10,10), pady =(10,10), sticky = W)

        #place remaining buttons and sliders once an image is available to manipulate
        self.btn_reset.grid(row = 1, column = 0, padx=(10,10), pady = (10,10))
        self.btn_save.grid(row = 9, column = 0, padx=(10,10), pady = (10,10))
        self.btn_frog.grid(row = 9, column = 1, padx=(10,10), pady = (10,10))

        self.btn_emboss.grid(row = 1, column = 1, padx=(10,10), pady = (10,10))
        self.btn_inverse.grid(row = 1, column = 2, padx=(10,10), pady = (10,10))
        self.btn_gray.grid(row = 2, column = 0, padx=(10,10), pady = (10,10))
        self.btn_poster.grid(row = 2, column = 1, padx=(10,10), pady = (10,10))
        self.btn_solar.grid(row = 2, column = 2, padx=(10,10), pady = (10,10))
        self.btn_flip.grid(row = 3, column = 0, padx=(10,10), pady = (10,10))
        self.btn_sharp.grid(row = 3, column = 1, padx=(10,10), pady = (10,10))
        self.btn_blur.grid(row = 3, column = 2, padx=(10,10), pady = (10,10))

        self.red_slider.grid(row = 4, column = 1)
        self.blue_slider.grid(row = 6, column = 1)
        self.green_slider.grid(row = 5, column = 1)
        self.bright_slider.grid(row = 7, column = 1)
        
        self.red_l.grid(row = 4, column = 0, padx=(10,10), pady = (10,10))
        self.blue_l.grid(row = 6, column = 0, padx=(10,10), pady = (10,10))
        self.green_l.grid(row = 5, column = 0, padx=(10,10), pady = (10,10))
        self.bright_l.grid(row = 7, column = 0, padx=(10,10), pady = (10,10))

        self.btn_r.grid(row = 4, column = 2, padx=(10,10), pady = (10,10))
        self.btn_g.grid(row = 5, column = 2, padx=(10,10), pady = (10,10))
        self.btn_b.grid(row = 6, column = 2, padx=(10,10), pady = (10,10))
        self.btn_bright.grid(row = 7, column = 2, padx=(10,10), pady = (10,10))

