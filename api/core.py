import json
import requests
from datetime import datetime

from django.conf import settings

class APIError(Exception):
    pass


class APIUpdateError(Exception):
    pass


class APICategoryError(Exception):
    pass


class APITagError(Exception):
    pass


class APIPlaceError(Exception):
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

    def _prepare_form_data(self, create=True, **data):
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
        if data.get('year'):
            payload.update({'Anno': '{}'.format(data['year'])})
        if data.get('is_decennary'):
            payload.update({'Decennio': 'S'})
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

    def _convert_api_data(self, **data):
        if data.get('Data'):
            date = datetime.strptime(data['Data'], '%Y-%m-%d')
            day, month, year = date.day, date.month, date.year
        else:
            day = month = year = None
        return {
            'archive': data.get('Archivio'),
            'color': data.get('Colore'),
            'place': data.get('Luogo', {}).get('_key'),
            'year': year or data.get('Anno'),
            'file_name': data.get('File'),
            'api_id': data.get('_key'),
            'creative': data.get('Creative'),
            'scope': 'S' if data.get('Utenza', '0') == 1 else 'N',
            'title': data.get('Nome'),
            'tags': data.get('Tags'),
            'is_decennary': True if data.get('Decennio', 'N') == 'S' else False,
            'day': day,
            'month': month,
            'short_description': data.get('DescBreve'),
            'full_description': data.get('DescLunga'),
            'support': data.get('Supporto'),
            'note': data.get('Note'),
            'rating': data.get('Rating'),
            'orientation': data.get('Orientamento'),
            'categories': data.get('Categoria')
        }

    def create_tag(self, value):
        res = self._make_request("in_t", data={"Nome": value})
        return res

    @property
    def archives(self):
        # TODO: Add real response?
        return [('Pic', 'Pic'), ('Other', 'Other')]

    def update_visor(self, key, **data):
        op = "in_v"
        if key:
            op = "md_v"
            prepared_data = {
                'visor': key,
                'data': self._prepare_form_data(create=False, **data)
            }
        else:
            prepared_data = self._prepare_form_data(**data)
        resp = self._make_request(op, data=prepared_data)
        if 'IN DATA' in resp:
            raise APIUpdateError(resp)
        if 'ERR INS VISOR' in resp:
            raise APIUpdateError(resp)
        if 'ERR MOD VISOR' in resp:
            raise APIUpdateError(resp)
        return resp

    def get_file(self, filename, get_content=False):
        resp = self._make_request('vk_v', data={'File': filename})
        if resp == 'NO VISOR KEY':
            return {}
        if get_content:
            try:
                return self._convert_api_data(
                    **self._make_request('dt_v', data={'visor': resp})
                )
            except Exception as exc:
                raise APIError(exc)
        else:
            return {'_key': resp}

    def delete_visor(self, key):
        op = "dl_v"
        resp = self._make_request(op, data={"visor": key})
        if resp == "OK DEL VISOR":
            return True
        return None

    def add_tag_to_visor(self, key, tag):
        op = "ln_t"
        resp = self._make_request(op, data={"tag": tag, "visor": key})
        if resp == 'ERR TAG-VISOR':
            raise APITagError('No connection tag-visor')
        elif resp == 'NO TAG NAME':
            raise APITagError('No such tag')
        elif resp == 'NO VISOR KEY':
            raise APITagError('No visor key')
        return True

    def delete_tag_from_visor(self, key, tag):
        op = "ex_t"
        resp = self._make_request(op, data={"tag": tag, "visor": key})
        if resp == 'ERR TAG-VISOR':
            raise APITagError('No connection tag-visor')
        elif resp == 'NO TAG NAME':
            raise APITagError('No such tag')
        elif resp == 'NO VISOR KEY':
            raise APITagError('No visor key')
        return True

    def add_place_to_visor(self, key, place):
        op = "ln_l"
        resp = self._make_request(op, data={"luogo": place, "visor": key})
        if resp == 'ERR LOC-VISOR':
            raise APIPlaceError('No connection tag-visor')
        elif resp == 'NO LOC NAME':
            raise APIPlaceError('No such place')
        elif resp == 'NO VISOR KEY':
            raise APIPlaceError('No visor key')
        return True

    def delete_place_from_visor(self, key, place):
        op = "ex_l"
        resp = self._make_request(op, data={"luogo": place, "visor": key})
        if resp == 'ERR LOC-VISOR':
            raise APIPlaceError('No connection tag-visor')
        elif resp == 'NO LOC NAME':
            raise APIPlaceError('No such place')
        elif resp == 'NO VISOR KEY':
            raise APIPlaceError('No visor key')
        return True

    def add_category_to_visor(self, key, category):
        op = "ln_c"
        resp = self._make_request(op, data={"cat": category, "visor": key})
        if resp == 'ERR CAT-VISOR':
            raise APICategoryError('No connection category-visor')
        elif resp == 'NO VISOR KEY':
            raise APICategoryError('No visor key')
        return True

    def delete_category_from_visor(self, key, category):
        op = "ex_c"
        resp = self._make_request(op, data={"cat": category, "visor": key})
        if resp == 'ERR EXCL CAT-VISOR':
            raise APICategoryError('No connection category-visor')
        elif resp == 'NO VISOR':
            raise APICategoryError('No visor key')
        return True
