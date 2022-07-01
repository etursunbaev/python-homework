#!/usr/bin/python3

car_specs = {'Model':'Mersedes C180',
          'Color':'Black',
          'Transmission Type':'Automatic',
          'Fuel Type':'Petrol'}

for key in sorted(car_specs):
    print("%s: %s" % (key, car_specs[key]))