import FractalFactory
from ImagePainter import paint
import Config


fractalObject = FractalFactory.makeFractal(Config.mydict)
paint(fractalObject)

