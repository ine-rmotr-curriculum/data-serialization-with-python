from pathlib import Path
import shutil
import os
import gzip, bz2, lzma

pyfile = Path(shutil.which('python'))
bashfile = Path(shutil.which('bash'))
token = Path('token.asc')

def do_compress(files=[pyfile, bashfile, token]):
    for file in files:
        content = file.read_bytes()
        with gzip.open(f'tmp-{file.name}.gz', 'w') as f:
            f.write(content)
        with bz2.open(f'tmp-{file.name}.bz2', 'w') as f:
            f.write(content)
        with lzma.open(f'tmp-{file.name}.xz', 'w', format=lzma.FORMAT_XZ) as f:
            f.write(content)

def find_sizes(files=[pyfile, bashfile, token]):
    result = dict()
    for file in files:
        result[file.name] = file.stat().st_size
        for ext in ['gz', 'bz2', 'xz']:
            name = f'tmp-{file.name}.{ext}'
            result[name] = Path(name).stat().st_size
    return result
