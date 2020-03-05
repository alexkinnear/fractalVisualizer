from tkinter import Tk, Canvas, PhotoImage, mainloop
import GradientFactory

def paint(fractal, imagename='branches.png'):
    """Paint a Fractal image into the TKinter PhotoImage canvas.
    This code creates an image which is 512x512 pixels in size."""
    SIZE = fractal.config['pixels']
    SIZE = int(SIZE)


    GradScheme = GradientFactory.makeGradient(fractal)

    # Figure out how the boundaries of the PhotoImage relate to coordinates on
    # the imaginary plane.
    minx = fractal.config['centerx'] - (fractal.config['axislength'] / 2.0)
    maxx = fractal.config['centerx'] + (fractal.config['axislength'] / 2.0)
    miny = fractal.config['centery'] - (fractal.config['axislength'] / 2.0)

    # Display the image on the screen
    window = Tk()
    img = PhotoImage(width=SIZE, height=SIZE)
    canvas = Canvas(window, width=SIZE, height=SIZE, bg=GradScheme.getColor(0))
    canvas.pack()
    canvas.create_image((SIZE/2, SIZE/2), image=img, state="normal")

    # At this scale, how much length and height on the imaginary plane does one
    # pixel take?
    pixelsize = abs(maxx - minx) / SIZE

    for row in range(SIZE, 0, -1):
        for col in range(SIZE):
            x = minx + col * pixelsize
            y = miny + row * pixelsize

            i = fractal.count(complex(x, y))

            color = GradScheme.getColor(i)
            img.put(color, (col, SIZE - row))
        window.update()  # display a row of pixels


    # Output the Fractal into a .png image
    img.write(imagename + ".png")
    print("Wrote picture " + imagename + ".png")

    # Call tkinter.mainloop so the GUI remains open
    mainloop()
