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


class ApiErrorException(Exception):
    pass


class RajaOngkirApi(object):

    key_list = u'rajaongkir'
    endpoint = u'http://rajaongkir.com/api/starter/'

    def __init__(self, api_key):
        self.api_key = api_key

    @classmethod
    def __grab(cls, json_results):
        return json_results.get(cls.key_list)

    @staticmethod
    def __status(response_json):
        """Checking the status of response api

        :param response_json:
        :return:
        """

        if not response_json:
            raise ApiErrorException(u'Response Api is None, cannot fetch the status of api')

        status = response_json.get(u'status')

        assert status is not None, \
            u'Response Status is not Available'

        assert status.get(u'code') == OK, \
            u'Response status not clear, should be any error occurred: {}'.format(status.get(u'description'))

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
            req_params[u'url_parameters'] = params

        api = ApiRequest(endpoint=service_endpoint)
        response = api.get(**req_params)

        return self.__grab(response.json()) if response.status_code == OK else None

    @staticmethod
    def __parse(response_json):
        """Get the actual result of json response

        :param response_json:
        :return:
        """
        return response_json.get(u'results') if response_json is not None else None

    def provinces(self):
        """Get list of all provinces

        :return:
        """
        provinces = self.__get(u'{}province'.format(self.endpoint))

        self.__status(provinces)

        return self.__parse(provinces)

    def province_by_id(self, province_id):
        """Get specific province by id

        :param province_id:
        :return:
        """
        province = self.__get(u'{}province'.format(self.endpoint), params={u'id': province_id})

        self.__status(province)

        return self.__parse(province)

    def cities(self):
        """Get list of all cities

        :return:
        """
        cities = self.__get(u'{}city'.format(self.endpoint))

        self.__status(cities)

        return self.__parse(cities)

    def city_by_id(self, city_id):
        """Get specific city by id

        :param city_id:
        :return:
        """
        city = self.__get(u'{}city'.format(self.endpoint), params={u'id': city_id})

        self.__status(city)

        return self.__parse(city)

    def cities_by_province(self, province_id):
        """Get specific city by province id

        :param province_id:
        :return:
        """
        city = self.__get(u'{}city'.format(self.endpoint), params={u'province': province_id})

        self.__status(city)

        return self.__parse(city)

    def city_by_province_and_city(self, province_id, city_id):
        """Get specific city by province and city id

        :param province_id: int
        :param city_id: int
        :return:
        """
        city = self.__get(u'{}city'.format(self.endpoint), params={u'id': city_id, u'province': province_id})

        self.__status(city)

        return self.__parse(city)

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

        api = ApiRequest(endpoint=u'{}cost'.format(self.endpoint))
        response = api.post(
            headers={
                u'key': self.api_key,
                u'Accept': u'application/json',
                u'Content-Type': u'application/json',
                u'charset': u'utf8'
            },
            payload=post_data
        )

        costs = self.__grab(response.json()) if response.status_code == OK else None

        self.__status(costs)

        return self.__parse(costs)
