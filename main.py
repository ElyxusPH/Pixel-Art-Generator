from PIL import Image
import numpy as np

class PixelArt():
    
    def __init__(self):
        import pathlib
        self.dir = pathlib.Path(__file__).parent.resolve()
        
        bg = (255, 255, 255)
        ol = (0 , 0, 0)
        rd = (255, 53, 38)
        sk = (250, 207, 67)
        ls = (247, 213, 96)
        
        self.pixels = [
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, ol, bg, bg, bg, bg, bg, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, ol, sk, sk, ol, bg, bg, bg, ol, sk, sk, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, ol, sk, sk, sk, ol, ol, ol, sk, sk, sk, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, ol, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, ol, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, ol, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, ol, sk, sk, ol, ol, sk, sk, sk, sk, sk, ol, ol, sk, sk, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, ol, sk, sk, bg, ol, sk, sk, sk, sk, sk, bg, ol, sk, sk, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, ol, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, sk, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, ol, sk, sk, sk, ls, ls, ol, ol, ol, ls, ls, sk, sk, sk, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, ol, ls, ls, bg, bg, bg, bg, ol, bg, bg, bg, bg, ls, ls, sk, ol, ol, ol, ol, ol, ol, ol],
        [bg, bg, bg, ol, ls, bg, bg, bg, ol, ol, ol, ol, ol, bg, bg, bg, ls, ls, sk, sk, sk, sk, sk, sk, sk],
        [bg, bg, bg, bg, ol, bg, bg, bg, bg, ol, rd, ol, bg, bg, bg, bg, ol, ls, ls, ls, ls, ls, ls, sk, sk],
        [bg, bg, bg, bg, ol, ls, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ls, ls, ls, ls, ls, ls, ls, sk],
        [bg, bg, bg, bg, bg, ol, ls, ol, bg, bg, bg, bg, bg, bg, ol, ol, ls, ls, sk, sk, sk, sk, sk, ls, ls],
        [bg, bg, bg, bg, bg, bg, ol, sk, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ls, ls, ls],
        [bg, bg, bg, bg, bg, bg, ol, sk, bg, bg, bg, ol, ol, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, ls, sk],
        [bg, bg, bg, bg, bg, bg, ol, sk, bg, bg, ls, sk, ol, bg, bg, bg, ol, ol, ol, ol, ol, ol, bg, ls, ls],
        [bg, bg, bg, bg, bg, bg, bg, ol, ls, ls, ol, bg, bg, ol, bg, bg, ol, bg, bg, bg, bg, ol, ls, ls, ol],        
        [bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, bg, bg, bg, ol, ol, ol, bg, bg, bg, bg, bg, bg, ol, ol, bg],
        ]        
        
    def draw(self):
        
        self.array = np.array(self.pixels, dtype=np.uint8)
        
        self.img = Image.fromarray(self.array)
        self.img = self.img.resize((480, 480), resample=Image.NEAREST)
        self.img.save("pixel-art.png")
    
    
if __name__ == "__main__":
    P = PixelArt()
    P.draw()
