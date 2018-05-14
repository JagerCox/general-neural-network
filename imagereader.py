from PIL import Image


def read_image_umbralized(path):
    image_file = Image.open(path)
    image_file = image_file.convert('1')
    return image_file


def create_synthetic(path, height, width, values=[]):
    img = Image.new('RGB', (height, width))
    pixels = img.load()

    t = 0
    for i in range(height):
        for j in range(width):
            v = values[t]
            pixels[i, j] = (int(v), int(v), int(v))  # To complete RGB
            t += 1
    img.save(path)


def extract_pixel_gray_scale(img):
    values = []
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            values.append(img.getpixel((i, j)))
    return values
