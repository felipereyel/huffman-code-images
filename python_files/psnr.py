images_configs = [
  {
      "name": "lena.ascii.pgm"
  },
  {
      "name": "baboon_ascii.pgm"
  }
]

"""# **Calculo do PSNR**

**Abrir imagens**
"""

def open_image2(fname):
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
    image = data[3:]
    
    return image, dimensions, vmax

"""**Calculo do PSNR**"""

def calc_psnr(original, decoded, vmax):
    MSE = 0
    for i in range(len(original)):
        MSE += (original[i] - decoded[i])**2
    
    if MSE == 0:
        return "infinito"
    else:
        return (vmax**2) / MSE

"""**Execucao**"""

for config in images_configs:
    image_original, _, vmax = open_image2(config["name"])
    image_decoded, *_ = open_image2(f'{config["name"]}.huff.pgm')
    # assert np.array_equal(image_original, image_decoded)
    print(f"O PSNR do processo para {config['name']} eh: {calc_psnr(image_original, image_decoded, vmax)}")

"""Obteve-se o valor do PSNR infinito, ou seja, a compressão é do tipo sem
perdas, visto que a codificação de Huffman altera apenas a forma de armazenar a mesma informação.
"""
