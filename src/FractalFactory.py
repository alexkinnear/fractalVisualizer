from Mandelbrot import Mandelbrot
from Julia import Julia
from Mandelbrot3 import Mandelbrot3


def makeFractal(mydict):
        if mydict['type'] == 'mandelbrot':
            mandelbrotObject = Mandelbrot(mydict)
            return mandelbrotObject
        elif mydict['type'] == 'julia':
            juliaObject = Julia(mydict)
            return juliaObject
        elif mydict['type'] == 'mandelbrot3':
            mandelbrot3Object = Mandelbrot3(mydict)
            return mandelbrot3Object










