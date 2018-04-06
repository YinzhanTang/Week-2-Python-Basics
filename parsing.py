city = input('City:')
state = input('State:')
city_state = city+', '+state
print(city_state)
if ',' not in city_state : # substring
    raise ValueError('no comma')

comma_index = city_state.find(',')
city = city_state[:comma_index]
state = city_state[comma_index+2:]

result = city[0]. islower()
if result is True:
    city = city.capitalize()

if len(state)!= 2:
    raise ValueError('invalid state abbrev:' + state)

result = state.islower()
if result is True:
    state = state.upper()

print('City:', city)
print('State:',state)
