import os

from django.conf import settings

from api.core import APIUpdateError, APIClient
from .helpers import (
    check_orientation,
    detect_color_image,
    hash_file_name,
    make_preview,
    get_rotation,
    rotate,
    resize,
    Image
)
from .models import ImageData, ImageFile


class APIDeleteError(Exception):
    pass


def delete_visor(file_name):
    try:
        image_data = ImageData.objects.get(img_file__file_name=file_name)
    except ImageData.DoesNotExist:
        image_data = None

    if image_data:
        image_data.delete()

    client = APIClient()
    try:
        visor = client.get_file(file_name)
        res = client.delete_visor(visor['_key'])
    except APIUpdateError:
        raise APIDeleteError('File \'{}\' could not be deleted'.format(file_name))
    except KeyError:
        raise APIDeleteError('File \'{}\' not found in api'.format(file_name))
    else:
        if not res:
            raise APIDeleteError('File \'{}\' could not be deleted'.format(file_name))


def import_file(file_path, file_name, file_info=None):
    """
    Does file import based on file path and name and eventual file info
    :param file_path: Path to the file
    :param file_name: File name (with extension)
    :param file_info: File info from API
    :return: tuple of objects (ImageData, ImageFile)
    """
    orientation = check_orientation(file_path)
    color = detect_color_image(file=file_path)
    rotation = get_rotation(file_path)
    rotate(file_path, rotation)
    thumb_name = 'thumb_' + file_name
    preview_name = 'prev_' + file_name

    original = Image.open(file_path)

    ext_original = file_name
    original.save(os.path.join(settings.ORIGINAL_ROOT, ext_original))

    ext_thumb = thumb_name
    thumb = resize(file_path, os.path.join(settings.THUMB_ROOT, ext_thumb), settings.MIN_THUMB_SIZE)
    # thumb = resize_and_crop(file_path, os.path.join(settings.THUMB_ROOT, ext_thumb), size=(128, 128))

    ext_prev = preview_name
    preview = make_preview(file_path, os.path.join(settings.PREVIEW_ROOT, ext_prev), size=(1000, 1000))

    if not preview:
        preview_name = 'None'
    if not thumb:
        thumb_name = 'None'

    img = ImageFile(file_name=file_name,
                    original_name='original/' + ext_original,
                    thumb_name='thumb/' + ext_thumb,
                    preview_name='preview/' + ext_prev,
                    is_new=True,
                    color=color,
                    orientation=orientation)

    img.save()
    img_data = ImageData(img_file=img)
    img_data.save()
    return img, img_data
