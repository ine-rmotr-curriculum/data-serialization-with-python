from pickle import load, dumps, dump
from datetime import datetime
from uuid import uuid4
import hashlib
from pathlib import Path
from dataclasses import dataclass
import numpy as np


@dataclass
class Fractal:
    canvas: np.ndarray = None
    timestamp: str = None
    uuid: str = None
    description: str = None
    hash_: str = None
        
    def __str__(self):
        return '\n'.join([
            f"Description: {self.description}",
            f"Timestamp:   {self.timestamp}",
            f"UUID:        {self.uuid}",
            f"Size:        {self.canvas.shape}",
            f"Fingerprint: {self.hash_}"])
        

def make_archive(canvas, comment="Archived Fractal"):
    if canvas.ndim != 2 or canvas.shape[0] != canvas.shape[1]:
        raise ValueError(f"Canvas must be 2-D and square, not {canvas.shape}")
    fractal = Fractal()
    fractal.canvas = canvas
    fractal.timestamp = datetime.now().isoformat()
    fractal.uuid = uuid4()
    fractal.description = comment
    fractal.hash_ = hashlib.sha1(dumps(canvas)).hexdigest()
    return fractal
    
    
                         
    