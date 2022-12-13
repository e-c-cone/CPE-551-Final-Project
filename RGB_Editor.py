from PIL import ImageTk, Image, ImageFilter, ImageOps

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
                pixel = data[x, y]
                #edit red value by slider value
                r = pixel[0] + num
                if r > 255:
                    r = 255
                elif r < 0:
                    r = 0
                b = pixel[1]
                g = pixel[2]
                data[x,y] = (r, g, b)

        return self.rgb_img
        
    def set_blue(self, image, num):
        #convert to rgb so we can edit individual rgb values
        self.rgb_img = image.convert('RGB')
        data = self.rgb_img.load()
        #iterate through RGB values and modify the red value based on the given num
        for x in range(image.width):
            for y in range(image.height):
                pixel = data[x, y]
                #edit blue value by slider value
                r = pixel[0] 
                b = pixel[1] + num
                if b > 255:
                    b = 255
                elif b < 0:
                    b = 0
                g = pixel[2]
                data[x,y] = (r, g, b)

        return self.rgb_img
        
    def set_green(self, image, num):
        #convert to rgb so we can edit individual rgb values
        self.rgb_img = image.convert('RGB')
        data = self.rgb_img.load()
        #iterate through RGB values and modify the red value based on the given num
        for x in range(image.width):
            for y in range(image.height):
                pixel = data[x, y]
                #edit green value by slider value
                r = pixel[0] 
                b = pixel[1]
                g = pixel[2] + num
                if g > 255:
                    g = 255
                elif g < 0:
                    g = 0
                data[x,y] = (r, g, b)

        return self.rgb_img

    def set_brightness(self, image, num):
    #convert to rgb so we can edit individual rgb values
        self.rgb_img = image.convert('RGB')
        data = self.rgb_img.load()
        #iterate through RGB values and modify the red value based on the given num
        for x in range(image.width):
            for y in range(image.height):
                pixel = data[x, y]
                # multiply all rgb values by given value (0-100) by 50
                # <1 darkens them image, >1 brightens it
                r = int(pixel[0] * (num/50))
                b = int(pixel[1] * (num/50))
                g = int(pixel[2] * (num/50))
                data[x,y] = (r, g, b)

        return self.rgb_img
