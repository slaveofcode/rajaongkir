[![Build Status](https://travis-ci.org/slaveofcode/rajaongkir.svg?branch=v1.0.1)](https://travis-ci.org/slaveofcode/rajaongkir)

# rajaongkir
Simple Python module to grab api data from rajaongkir.com (http://rajaongkir.com/dokumentasi/starter), 
you can use it by Django, Flask or any framework you used.

If you have no `ApiKey` you can create one here: [http://rajaongkir.com/akun/daftar](http://rajaongkir.com/akun/daftar)
 
## Install
    # Directly install from last stable release
    
    pip install git+ssh://git@github.com/slaveofcode/rajaongkir@1.0.1
    
    #Or with official pypi
    
    pip install rajaongkir
 
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

I'm using unittest to test the whole functionality of RajaOngkirApi class, 
you can run it by using console or set your test in pycharm using Unittest configuration
 
Please take a not you must set your `API_KEY` inside of rajaongkirapi_tests.py to make sure the api works

Here's some sample while you runs the test over the console or terminal

    >> python test/unit/rajaongkirapi_test.py
    
    >> Ran 7 tests in 4.322s
    
    >> OK
    
Other choice you can run the test by using nosetests, make sure nosetest already installed, 
or you can run command `pip install nose` to install them

    >> nosetests
    
    >> ----------------------------------------------------------------------
    
    >> Ran 7 tests in 4.899s
    
    >> OK

    

    