from PIL import Image, ImageStat

HORIZONTAL = 1
VERTICAL = 2
SQUARE = 3
PANORAMIC = 4
ORIENTATION_CHOICES = [
    (HORIZONTAL, 'Horizontal'),
    (VERTICAL, 'Vertical'),
    (SQUARE, 'Square'),
    (PANORAMIC, 'Panoramic')
]
ORIENTATIONS = dict(ORIENTATION_CHOICES)


BW = 'B/N'
COLOR = 'COL'
COLOR_CHOICES = [
    (BW, 'B/N'),
    (COLOR, 'Color')
]
COLORS = dict(COLOR_CHOICES)

SUPPORT_35MM = '35mm'
SUPPORT_6X6 = '6x6'
SUPPORT_6X9 = '6x9'
SUPPORT_CHOICES = [
    (None, 'Choose support'),
    (SUPPORT_6X6, SUPPORT_6X6),
    (SUPPORT_35MM, SUPPORT_35MM),
    (SUPPORT_6X9, SUPPORT_6X9)
]
SUPPORTS = dict(SUPPORT_CHOICES)


def check_orientation(file):
    image = Image.open(file)
    size = image.size
    if size[0] > size[1]:
        orientation = HORIZONTAL
    elif size[0] == size[1]:
        orientation = SQUARE
    else:
        orientation = VERTICAL
    return orientation


def resize_and_crop(img_path, modified_path, size, crop_type='top'):
    """
    Resize and crop an image to fit the specified size.

    args:
        img_path: path for the image to resize.
        modified_path: path to store the modified image.
        size: `(width, height)` tuple.
        crop_type: can be 'top', 'middle' or 'bottom', depending on this
            value, the image will cropped getting the 'top/left', 'middle' or
            'bottom/right' of the image to fit the size.
    raises:
        Exception: if can not open the file in img_path of there is problems
            to save the image.
        ValueError: if an invalid `crop_type` is provided.
    """
    # If height is higher we resize vertically, if not we resize horizontally
    img = Image.open(img_path)
    # Get current and desired ratio for the images
    img_ratio = img.size[0] / float(img.size[1])
    ratio = size[0] / float(size[1])
    #The image is scaled/cropped vertically or horizontally depending on the ratio
    if ratio > img_ratio:
        img = img.resize((size[0], round(size[0] * img.size[1] / img.size[0])),
                Image.ANTIALIAS)
        # Crop in the top, middle or bottom
        if crop_type == 'top':
            box = (0, 0, img.size[0], size[1])
        elif crop_type == 'middle':
            box = (0, round((img.size[1] - size[1]) / 2), img.size[0],
                   round((img.size[1] + size[1]) / 2))
        elif crop_type == 'bottom':
            box = (0, img.size[1] - size[1], img.size[0], img.size[1])
        else :
            raise ValueError('ERROR: invalid value for crop_type')
        img = img.crop(box)
    elif ratio < img_ratio:
        img = img.resize((round(size[1] * img.size[0] / img.size[1]), size[1]),
                Image.ANTIALIAS)
        # Crop in the top, middle or bottom
        if crop_type == 'top':
            box = (0, 0, size[0], img.size[1])
        elif crop_type == 'middle':
            box = (round((img.size[0] - size[0]) / 2), 0,
                   round((img.size[0] + size[0]) / 2), img.size[1])
        elif crop_type == 'bottom':
            box = (img.size[0] - size[0], 0, img.size[0], img.size[1])
        else:
            raise ValueError('ERROR: invalid value for crop_type')
        img = img.crop(box)
    else :
        img = img.resize((size[0], size[1]),
                Image.ANTIALIAS)
        # If the scale is the same, we do not need to crop
    img.save(modified_path)
    return True


def make_preview(img_path, modified_path, size):
    img = Image.open(img_path)
    img.thumbnail(size)
    img.save(modified_path)
    return True


def detect_color_image(file, thumb_size=40, MSE_cutoff=22, adjust_color_bias=True):
    pil_img = Image.open(file)
    bands = pil_img.getbands()
    if bands == ('R', 'G', 'B') or bands == ('R', 'G', 'B', 'A'):
        thumb = pil_img.resize((thumb_size, thumb_size))
        SSE, bias = 0, [0, 0, 0]
        if adjust_color_bias:
            bias = ImageStat.Stat(thumb).mean[:3]
            bias = [b - sum(bias)/3 for b in bias]
        for pixel in thumb.getdata():
            mu = sum(pixel)/3
            SSE += sum((pixel[i] - mu - bias[i])*(pixel[i] - mu - bias[i]) for i in [0, 1, 2])
        MSE = float(SSE)/(thumb_size*thumb_size)
        if MSE <= MSE_cutoff:
            #print("grayscale\t")
            color = BW
        else:
            # print("Color\t\t\t")
            color = COLOR
    elif len(bands) == 1:
        #print("Black and white")
        color = BW
    else:
        print("Don't know...")
        color = None
    return color




