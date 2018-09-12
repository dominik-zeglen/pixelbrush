from PIL import Image

from pdb import set_trace
def save_image(img_data, size, filepath):
    w, h, c = img_data.shape
    img_data = img_data.repeat(int(size[1] / w) + 1, 0)
    img_data = img_data.repeat(int(size[0] / h) + 1, 1)
    img = Image.fromarray(img_data)
    img.save(filepath)
