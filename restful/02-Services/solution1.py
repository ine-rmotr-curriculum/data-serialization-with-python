from tempfile import NamedTemporaryFile
from matplotlib import pyplot as plt
from fractal.sierpiński import gasket
from flask import Flask, request, send_file
app = Flask(__name__)

@app.route('/gasket')
def sierpiński_gasket():
    pixels = int(request.args.get('pixels', 3**6))
    N = int(request.args.get('N', 5))
    cmap = request.args.get('cmap', 'viridis')
    with NamedTemporaryFile() as imgfile:
        canvas = gasket(pixels, N)
        fig, ax = plt.subplots(figsize=(7, 7))
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        ax.imshow(canvas, cmap=cmap)
        plt.savefig(imgfile)
        imgfile.flush()
        return send_file(imgfile.name, mimetype='image/png')