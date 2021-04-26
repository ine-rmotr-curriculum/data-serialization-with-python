from tempfile import NamedTemporaryFile
import json
from matplotlib import pyplot as plt
from flask import Flask, request, send_file
app = Flask(__name__)

@app.route('/visualize', methods=["POST"])
def visualize():
    data = json.loads(request.data)
    fmt = data.get('format', 'png')
    canvas = data.get('arr', [[0]])

    with NamedTemporaryFile() as imgfile:
        fig, ax = plt.subplots(figsize=(7, 7))
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        ax.imshow(canvas)
        plt.savefig(imgfile)
        imgfile.flush()
        return send_file(imgfile.name, mimetype=f'image/{fmt}')