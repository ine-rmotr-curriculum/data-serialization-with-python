from flask import Flask, request, send_file, jsonify, abort
app = Flask(__name__)

from collections import Counter
from tempfile import NamedTemporaryFile
from json import loads
from matplotlib import pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from PIL import Image

@app.route('/prominent-colors', methods=['POST'])
def cluster():
    img = Image.open(request.files['image'])
    k = int(request.form.get('k', 6))
    colors, freqs = prominent_colors(img, k)
    # Fixup: labels are NumPy ints rather than Python ints
    freqs = {int(k):v for k, v in freqs.items()}
    return jsonify([colors.tolist(), freqs])

@app.route('/rgb2hex', methods=['POST'])
def rgb2hex():
    "Convert a list-of-lists of RBB colors into their HTML hexcodes"
    rgbs = loads(request.form.get('rgbs', '[]'))
    hexcodes = []
    for rgb in rgbs:
        r, g, b = rgb
        hexcodes.append(f"#{r:02x}{g:02x}{b:02x}")
    return jsonify(hexcodes)

@app.route('/centroids', methods=['POST'])
def centroids():
    try:
        with NamedTemporaryFile() as imgfile:
            colors = loads(request.form['colors'])
            counts = loads(request.form['counts'])
            plt.pie(counts, labels=colors, colors=colors)
            plt.axis('equal')
            plt.savefig(imgfile, dpi=75)
            imgfile.flush()
            return send_file(imgfile.name, mimetype='image/png')
    except:
        abort(503)

def prominent_colors(img, k=6):
    "Identify `k` centroids and pixel counts in colorspace of an image"
    pixels = np.asarray(img).reshape(-1, 3)
    model = KMeans(n_clusters=k)
    model.fit_predict(pixels)
    freqs = Counter(model.labels_)
    colors = np.rint(model.cluster_centers_).astype(np.uint8)
    return colors, freqs

