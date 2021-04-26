from tempfile import NamedTemporaryFile
from matplotlib import pyplot as plt
from fractal.mandelbrot import mandelbrot
from fractal.visualize import make_canvas
from flask import Flask, request, send_file
app = Flask(__name__)

@app.route('/mandelbrot')
def mandel_service():
    x = float(request.args['x'])
    y = float(request.args['y'])
    size = float(request.args['size'])
    pixels = int(request.args.get('pixels', 400))
    canvas = make_canvas(mandelbrot, x=x, y=y, size=size, pixels=pixels)
    with NamedTemporaryFile() as imgfile:
        fig, ax = plt.subplots(figsize=(7, 7))
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        ax.imshow(canvas)
        plt.savefig(imgfile)
        imgfile.flush()
        return send_file(imgfile.name, mimetype='image/png')