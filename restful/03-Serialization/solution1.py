from matplotlib import pyplot as plt
from fractal.julia import julia
from fractal.visualize import make_canvas
from flask import Flask, request, jsonify, request
app = Flask(__name__)

@app.route('/julia')
def _julia():
    pixels = int(request.args.get('pixels', 400))
    # touch-up URL encoding for complex given
    c = complex(request.args.get('c', "-0.1+0.65j").replace(' ', '+'))
    x = float(request.args['x'])
    y = float(request.args['y'])
    size = float(request.args['size'])
    canvas = make_canvas(julia, x, y, size, pixels, kws={'c': c})
    return jsonify(canvas.tolist())
