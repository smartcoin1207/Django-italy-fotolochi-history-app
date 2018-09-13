from api.core import APIUpdateError, APIClient


class APIDeleteError(Exception):
    pass


def delete_image_data(image_data):
    if not image_data.api_id:
        return image_data.delete()

    client = APIClient()
    try:
        res = client.delete_visor(image_data.api_id)
    except APIUpdateError as e:
        raise APIDeleteError('File \'{}\' could not be deleted'.format(image_data.title))
    else:
        if not res:
            raise APIDeleteError('File \'{}\' could not be deleted'.format(image_data.title))
        return image_data.delete()
