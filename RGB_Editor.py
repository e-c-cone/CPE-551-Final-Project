from PIL import ImageTk, Image, ImageFilter, ImageOps
import numpy as np

class RGB_Editor:

    def __init__(self):
        self.message = "I am the constructor!"
        self.rgb_img = None
        
    def set_red(self, image, num):
        #convert to rgb so we can edit individual rgb values
        self.rgb_img = image.convert('RGB')
        data = self.rgb_img.load()
        #iterate through RGB values and modify the red value based on the given num
        for x in range(image.width):
            for y in range(image.height):
                pixel = data[x,y]
                #edit red value by slider value
                r = pixel[0] + num
                g = pixel[1]
                b = pixel[2]
                #print("Increasing r by", num)
                if r > 255:
                    r = 255
                elif r < 0:
                    r = 0
                new_val = (r, g, b)
                self.rgb_img.putpixel((x, y), new_val)
                
        return self.rgb_img
        
    def set_blue(self, image, num):
        #convert to rgb so we can edit individual rgb values
        self.rgb_img = image.convert('RGB')
        data = self.rgb_img.load()
        #iterate through RGB values and modify the red value based on the given num
        for x in range(image.width):
            for y in range(image.height):
                pixel = data[x,y]
                #edit blue value by slider value
                r = pixel[0] 
                b = pixel[1] + num
                #print("Increasing b by", num)
                if b > 255:
                    b = 255
                elif b < 0:
                    b = 0
                g = pixel[2]
                new_val = (r, g, b)
                self.rgb_img.putpixel((x, y), new_val)

        return self.rgb_img
        
    def set_green(self, image, num):
        #convert to rgb so we can edit individual rgb values
        self.rgb_img = image.convert('RGB')
        data = self.rgb_img.load()
        #iterate through RGB values and modify the red value based on the given num
        for x in range(image.width):
            for y in range(image.height):
                pixel = data[x,y]
                #edit green value by slider value
                r = pixel[0] 
                b = pixel[1]
                g = pixel[2] + num
                #print("Increasing g by", num)
                if g > 255:
                    g = 255
                elif g < 0:
                    g = 0
                new_val = (r, g, b)
                self.rgb_img.putpixel((x, y), new_val)

        return self.rgb_img

    def set_brightness(self, image, num):
    #convert to rgb so we can edit individual rgb values
        self.rgb_img = image.convert('RGB')
        data = self.rgb_img.load()
        #iterate through RGB values and modify the red value based on the given num
        for x in range(image.width):
            for y in range(image.height):
                pixel = data[x,y]
                # add positive values for luminance, negative for darkness
                r = int(pixel[0] + num)
                b = int(pixel[1] + num)
                g = int(pixel[2] + num)
                # make sure values stay between 0-255
                if r > 255:
                    r = 255
                elif r < 0:
                    r = 0
                if g > 255:
                    g = 255
                elif g < 0:
                    g = 0
                if b > 255:
                    b = 255
                elif b < 0:
                    b = 0
                new_val = (r, g, b)
                self.rgb_img.putpixel((x, y), new_val)

        return self.rgb_img

    def add_noise(self, image, amount):

        output = np.copy(np.array(image))
        # generate salt noise
        salt = np.ceil(amount * output.size * 0.5)
        noise = [np.random.randint(0, i - 1, int(salt)) for i in output.shape]
        # set randomly selected values to 1 to create light noise
        output[noise] = 1

        #generate pepper noise
        pepper = np.ceil(amount* output.size * 0.5)
        noise = [np.random.randint(0, i - 1, int(pepper)) for i in output.shape]
        # set randomly selected values to 0 to create darkened noise
        output[noise] = 0

        return Image.fromarray(output)
