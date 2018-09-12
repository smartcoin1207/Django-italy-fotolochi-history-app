import json
import requests

from django.conf import settings


class APIUpdateError(Exception):
    pass


class APIClient:

    VALID_OPS = {
        "categories": "ls_c",
        "visors": "ls_v",
        "places": "ls_l",
        "tags": "ls_t"
    }

    ORIENTATION = {
        "horizontal": 1,
        "vertical": 2,
        "square": 3,
        "panoramic": 4
    }

    def __init__(self, srv=None):
        self.srv = srv or settings.API_SRV

    def _make_request(self, op, data=None):
        payload = {
            "op": op,
            "payload": data or {}
        }
        resp = requests.post(self.srv, data={"data": json.dumps(payload)})
        if resp.status_code > 399:
            raise APIUpdateError(resp.content)
        if resp.json() in ['NO FILE', 'NO DATA', 'NO CMD', 'NO VISOR']:
            raise APIUpdateError('Update failed {}'.format(resp.json()))
        return resp.json()

    def _cache(self, item, func):
        cached = getattr(self, '_' + item, False)
        if not cached:
            cached = func(item)
            setattr(self, '_' + item, cached)
        return cached

    def __getattr__(self, item):
        if item not in self.VALID_OPS:
            return self.__getattribute__(item)
        return self._cache(self.VALID_OPS[item], self._make_request)

    def _prepare_form_data(self, **data):
        payload = {
            'Nome': data.get('title', ''),
            'File': data.get('file_name', ''),
            'Descrizione1': data.get('short_description', ''),
            'Descrizione2': data.get('full_description', ''),
            'Archivio': data.get('archive', 'Pic'),
            'Utenza': '1' if data.get('scope', '') else '0',
            'Creative': 'S' if data.get('creative') else 'N',
            'Rating': str(data.get('rating', 0)),
            'StatoProdotto': data.get('status'),
            'Note': data.get('notes', ''),
            'Supporto': data.get('support', '6x6'),
            'Orientamento': data.get('orientation', '1')
        }
        if data.get('color'):
            payload.update({
                'Colore': data['color']
            })
        if data.get('year') and data.get('month') and data.get('day'):
            payload.update({
                'Data': '{:04}-{:02}-{:02}'.format(data['year'], data['month'], data['day'])
            })
        if data.get('year') and data.get('is_decennary'):
            payload.update({'Anno': '{}'.format(data['year'])})
        if data.get('place'):
            payload.update({
                'Luogo': data['place']
            })
        if data.get('tags'):
            payload.update({
                'Tags': "|".join(data['tags'])
            })
        if data.get('categories'):
            payload.update({
                'Categoria': ";".join(data['categories'])
            })
        return payload

    @property
    def archives(self):
        # TODO: Add real response
        return [('Pic', 'Pic')]

    def update_visor(self, key, **data):
        op = "in_v"
        prepared_data = self._prepare_form_data(**data)
        if key:
            op = "md_v"
            prepared_data = {
                'visor': key,
                'data': prepared_data
            }
        return self._make_request(op, data=prepared_data)

    def get_file(self, filename):
        resp = self._make_request('vk_v', data={'File': filename})
        if resp == 'NO VISOR KEY':
            return None
        return resp
