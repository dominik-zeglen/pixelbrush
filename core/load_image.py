from PIL import Image


def get_transformed_size(original_size, target_size):
    return (int(x * target_size / max(original_size)) for x in original_size)


def load_image(filepath, target_size):
    img = Image.open(filepath)
    size = img.size

    return (img.resize(get_transformed_size(size, target_size)), size)
