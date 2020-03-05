from Fractal import Fractal


class Mandelbrot3(Fractal):
    def __init__(self, config):
        self.config = config

    def count(self, c):
        """Return the color of the current pixel within the Mandelbrot set"""
        z = complex(0, 0)  # z0

        for i in range(self.config['iterations']):
            z = z * z * z + c  # Get z1, z2, ...
            if abs(z) > 2:
                return i
        return self.config['iterations'] - 1