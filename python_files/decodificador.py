images_configs = [
  {
      "name": "lena.ascii.pgm"
  },
  {
      "name": "baboon_ascii.pgm"
  }
]

"""# **Decodificando as Imagens**"""

import numpy as np
import json

"""**Abrir informacoes e code**"""

def open_image_info(name):
    f = open(f"{name}.huff", "r")
    content = f.read()
    info = json.loads(content)
    return info["codewords"], info["dimensions"], info["vmax"], info["code"]

"""**Inverter codewords**"""

def calc_decoder(codewords):
    decoder = {}
    for key in codewords:
        decoder[codewords[key]] = key
    return decoder

"""**Decodificar**"""

def decode_code(code, decoder):
    max_code_length = 0
    for key in decoder:
        if max_code_length < len(key):
            max_code_length = len(key)

    decoded = []
    while (len(code) > 0):
        for i in range(1, max_code_length + 1):
            if decoder.get(code[:i], False):
                decoded.append(int(decoder[code[:i]]))
                code = code[i:]
                break
    
    return decoded

"""**Mostrar imagem**"""

def save_image(name, image, dimensions, vmax):
    image_copy = image.copy()
    content = f"P2\n{dimensions[0]} {dimensions[1]}\n{vmax}\n"
    for i in range(dimensions[0]):
        content += " ".join([str(el) for el in image_copy[:dimensions[1]]])
        content += "\n"
        image_copy = image_copy[dimensions[1]:]
    
    f = open(f"{name}.huff.pgm","w")
    f.write(content)
    f.close()

"""**Execucao (> 45 segundos)**"""

for config in images_configs:
    codewords, dimensions, vmax, code = open_image_info(config["name"])
    decoder = calc_decoder(codewords)
    image = decode_code(code, decoder)
    save_image(config["name"], image, dimensions, vmax)
