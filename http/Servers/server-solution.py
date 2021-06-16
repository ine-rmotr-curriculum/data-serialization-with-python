#!/usr/bin/env python
from pathlib import Path
from urllib.parse import quote
from mimetypes import guess_type
import os
from os.path import join, getsize
from flask import Flask, request, Response, send_file, jsonify
app = Flask(__name__)


def linkify(pth):
    return f'<a href="{quote(str(pth))}">{pth.name}</a>'


def make_tree(path, prefix='', linkify=lambda pth: pth):
    space =  '    '
    branch = '│   '
    tee =    '├── '
    last =   '└── '
    path = Path(path)
    contents = list(path.iterdir())
    pointers = [tee] * (len(contents) - 1) + [last]
    for pointer, path in zip(pointers, contents):
        if path.name.startswith(('.', '__pycache__')):
            continue
        yield (f"{prefix}{pointer}" +
               f"{linkify(path)}" +
               f"{'/' if path.is_dir() else ''}")
        if path.is_dir(): # extend the prefix and recurse:
            extension = branch if pointer == tee else space 
            yield from make_tree(path, prefix=prefix+extension, linkify=linkify)

dirpage = """<html>
<head><title>Directory of %s/</title></head>
<body>
<h2>Tree from directory %s/</h2>
<pre>
%s
</pre></body>
</html>
"""

@app.route('/')
def basepath():
    root = "."
    tree = '\n'.join(make_tree('.', linkify=linkify))
    return Response(dirpage % (root, root, tree), mimetype='text/html')


@app.route('/<path:filepath>')
def get_path(filepath):
    q = Path(filepath)
    if q.exists():
        if q.is_dir():
            root = q.name
            tree = '\n'.join(make_tree(root, linkify=linkify))
            return Response(dirpage % (root, root, tree))
        else:
            filetype = guess_type(filepath)[0]
            return send_file(filepath, mimetype=filetype)
    else:
        return f"{filepath} is not a file path!"


@app.route('/file-sizes')
def file_sizes():
    sizes = {}
    for root, dirs, files in os.walk('.'):
        if '.ipynb' not in root and '__pycache__' not in root:
            for fname in files:
                fpath = join(root, fname)
                sizes[fpath] = getsize(fpath)
    return jsonify(sizes)


if __name__ == '__main__':
    # Expose to all external-facing IP addresses
    from werkzeug.serving import WSGIRequestHandler
    WSGIRequestHandler.protocol_version = "HTTP/1.1"
    app.run(host='0.0.0.0', port=2553)

