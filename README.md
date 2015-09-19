# rajaongkir
Simple Python class to grab api data from rajaongkir.com, you can use it by Django, Flask or any framework you used.
 
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
    list_of_city = api.city_by_id(province_id)
     
    # get city by id
    city = api.city_by_id(city_id)
    
    # get the cost 
    cost = api.cost_between_city()
