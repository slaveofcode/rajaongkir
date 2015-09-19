# rajaongkir
Simple Python class to grab api data from rajaongkir.com (http://rajaongkir.com/dokumentasi/starter), 
you can use it by Django, Flask or any framework you used.
 
## Install
    pip install git+ssh://git@github.com/slaveofcode/rajaongkir@master
 
## How to Use ?

    from rajaongkir.api import RajaOngkirApi
    
    # initialization
    api = RajaOngkirApi(api_key='YourRajaOngkirApiKeyHere')
    
    # get province list
    list_of_city = api.provinces()
    
    # get city list
    list_of_city = api.cities()
    
    # get cities based on province_id 
    list_of_city = api.cities_by_province(province_id)
     
    # get city by id
    city = api.city_by_id(city_id)
    
    # get the cost (55 is Bekasi, 23 is Bandung, 1000 grams = 1 kg, 'all' = all courier
    cost = api.cost_between_city(55, 23, 1000, 'all')


## Run The Test

I using unittest to test the whole functionality of RajaOngkirApi class, 
you can run it by using console or set your test in pycharm using Unittest configuration
 
Please take a not you must set your `API_KEY` inside of rajaongkirapi_tests.py to make sure the api works

Here's some sample while you runs the test over the console or terminal

    >> python test/unit/rajaongkirapi_test.py
    
    >> Ran 7 tests in 4.322s
    
    >> OK

    