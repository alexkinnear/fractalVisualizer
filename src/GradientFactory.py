import sys

import GradBlacktoWhite
import GradGreentoRed
import GradWhitetoOrange


def makeGradient(fractal):
    if len(sys.argv) < 3:
        GradBlacktoWhiteObject = GradBlacktoWhite.GradBlackToWhite(fractal)
        return GradBlacktoWhiteObject
    elif len(sys.argv) == 3:
        GradientName = sys.argv[2]
        if GradientName == 'GradBlacktoWhite':
            GradBlacktoWhiteObject = GradBlacktoWhite.GradBlackToWhite(fractal)
            return GradBlacktoWhiteObject
        elif GradientName == 'GradGreentoRed':
            GradGreentoRedObject = GradGreentoRed.GradGreenToRed(fractal)
            return GradGreentoRedObject
        elif GradientName == 'GradWhitetoOrange':
            GradWhitetoOrangeObject = GradWhitetoOrange.GradWhiteToOrange(fractal)
            return GradWhitetoOrangeObject
        else:
            raise NotImplementedError("Invalid gradient requested")