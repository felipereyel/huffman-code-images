images_configs = [
  {
      "name": "lena.ascii.pgm"
  },
  {
      "name": "baboon_ascii.pgm"
  }
]

"""# ***Codificando as imagens***"""

import numpy as np
import json
from heapq import heappush, heappop, heapify
from collections import defaultdict

"""**Abre e estrututa a imagem**"""

def open_image(fname):
    with open(fname) as f:
        lines = f.readlines()

    for l in list(lines):
        if l[0] == '#':
            lines.remove(l)

    data = []
    for line in lines[1:]:
        data.extend([int(c) for c in line.split()])

    vmax = data[2]
    dimensions = (data[1],data[0])
    image_flat = np.array(data[3:])
    
    return image_flat, dimensions, vmax

"""**Faz a analise de frequencia**"""

def calc_freqs(image):
    freqs = {}
    total = 0

    for pixel in image:
        key = str(pixel)
        total += 1
        if freqs.get(key, False):
            freqs[key] += 1
        else:
            freqs[key] = 1
    return freqs, total

"""**Calcula Huffman**"""

def huffman(freqs):
    heap = [[wt, [sym, ""]] for sym, wt in freqs.items()]
    heapify(heap)
    while len(heap) > 1:
        lo = heappop(heap)
        hi = heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    codewords = {}
    for sym, wt in heap[0][1:]:
        codewords[sym] = wt
    return codewords

"""**Salva codewords em arquivo**"""

def save_codewords(name, codewords, dimensions, vmax):
    content = json.dumps({
        "codewords": codewords,
        "dimensions": dimensions,
        "vmax": vmax
    })
    f = open(f"{name}.json","w")
    f.write(content)
    f.close()

"""**Codifica e salva imagem em arquivo**"""

def code_and_save_image(name, image, codewords, dimensions, vmax):
    # Code as binary
    code = ""
    for pixel in image:
        key = str(pixel)
        code += codewords[key]
    
    content = json.dumps({
        "codewords": codewords,
        "dimensions": dimensions,
        "vmax": vmax,
        "code": code
    }, indent=4)

    f = open(f"{name}.huff","w")
    f.write(content)
    f.close()

"""**Calcula comprimento medio de codewords**"""

def avg_codeword(codewords, freqs, total):
    avg = 0
    for key in codewords:
        avg += len(codewords[key]) * freqs[key]
    return avg/total

"""**Execucao**"""

for config in images_configs: 
    image, dimensions, vmax = open_image(config["name"])
    freqs, total = calc_freqs(image)
    codewords = huffman(freqs)
    code_and_save_image(config["name"], image, codewords, dimensions, vmax)
    print(f"O comprimento medio do codeword para {config['name']} eh: {avg_codeword(codewords, freqs, total)}")
