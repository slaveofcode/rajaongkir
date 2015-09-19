import requests
import json
from json.encoder import JSONEncoder
from httplib import OK, CREATED, NO_CONTENT

JNE = u'jne'
POS = u'pos'
TIKI = u'tiki'
ALL_COURIER = u'all'


class ApiRequest(object):
    """Basic Api request with using requests library

    """
    json_encoder_class = JSONEncoder

    def __init__(self, endpoint):
        self.endpoint = endpoint

    def get(self, headers={}, url_parameters={}):
        return requests.get(
            self.endpoint,
            params=url_parameters,
            headers=headers
        )

    def post(self, headers={}, url_parameters={}, payload={}):
        return requests.post(
            self.endpoint,
            data=json.dumps(payload, cls=self.json_encoder_class),
            params=url_parameters,
            headers=headers
        )

    def put(self, headers={}, url_parameters={}, payload={}):
        return requests.put(
            self.endpoint,
            data=json.dumps(payload, cls=self.json_encoder_class),
            params=url_parameters,
            headers=headers
        )

    def delete(self, headers={}, url_parameters={}):
        return requests.delete(
            self.endpoint,
            params=url_parameters,
            headers=headers
        )

    def options(self, headers={}, url_parameters={}):
        return requests.options(
            self.endpoint,
            params=url_parameters,
            headers=headers
        )


class RajaOngkirApi(object):

    key_list = u'rajaongkir'

    def __init__(self, api_key):
        self.api_key = api_key

    @classmethod
    def __grab(cls, json_results):
        return json_results.get(cls.key_list)

    def __get(self, service_endpoint, params=None):
        """Separate GET request into individual method,
        because it's will be used multiple times, short-code=better

        :param service_endpoint: `str` specific api endpoint
        :param params: `dict` url parameter to include
        :return: `dict` results of returned api
        """
        req_params = {
            u'headers': {
                u'Accept': u'application/json',
                u'key': self.api_key
            }
        }

        if params is not None:
            req_params[u'params'] = params

        api = ApiRequest(endpoint=service_endpoint)
        response = api.get(**req_params)

        return self.__grab(response.json()) if response.status_code == OK else None

    def provinces(self):
        """Get list of all provinces

        :return:
        """
        return self.__get(u'{}province'.format(self.endpoint))

    def province_by_id(self, province_id):
        """Get specific province by id

        :param province_id:
        :return:
        """
        return self.__get(u'{}province'.format(self.endpoint), params={u'id': province_id})

    def cities(self):
        """Get list of all cities

        :return:
        """
        return self.__get(u'{}city'.format(self.endpoint))

    def city_by_id(self, city_id):
        """Get specific city by id

        :param city_id:
        :return:
        """
        return self.__get(u'{}city'.format(self.endpoint), params={u'id': city_id})

    def city_by_province_and_city(self, province_id, city_id):
        """Get specific city by province and city id

        :param province_id: int
        :param city_id: int
        :return:
        """
        return self.__get(u'{}city'.format(self.endpoint), params={u'id': city_id, u'province': province_id})

    def cost_between_city(self, source, destination, weight_in_grams=0, courier=ALL_COURIER):
        """Get cost result

        :param source: `int` city id of source place
        :param destination: `int` city id of destination
        :param weight_in_grams: `int` weight in grams
        :param courier: `str` the courier type
        :return:
        """
        post_data = {
            u"origin": source,
            u"destination": destination,
            u"weight": int(weight_in_grams),
            u"courier": courier
        }

        api = ApiRequest(endpoint=u'cost')
        response = api.post(
            headers={
                u'key': self.api_key,
                u'Accept': u'application/json',
                u'Content-Type': u'application/json',
                u'charset': u'utf8'
            },
            payload=post_data
        )

        return self.__grab(response.json()) if response.status_code == OK else None