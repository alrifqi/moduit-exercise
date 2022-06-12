from typing import Union


class BaseApi():
    def make_response(self, data, message: str = 'success', meta=None):
        if meta is None:
            meta = {}
        response = {"message": message, "meta": meta, "data": data}
        return response
