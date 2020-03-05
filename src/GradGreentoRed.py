from colour import Color
from Gradient import Gradient


class GradGreenToRed(Gradient):
    def __init__(self, fractal):
        self.config = fractal.config
        self.fractal = fractal
        self.start = Color('#00ff00')
        self.dynamic = [c.get_hex_l() for c in self.start.range_to('#ff0000', self.fractal.config['iterations'])]

    def getColor(self, n):
        return self.dynamic[n]