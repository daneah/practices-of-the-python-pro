print(col1_name + ',' + col2_name + ',' + col3_name + ',' + col4_name)
print(first_val + ',' + second_val + ',' + third_val + ',' + fourth_val)


DELIMITER = '\t'
print(DELIMITER.join([col1_name, col2_name, col3_name, col4_name]))
print(DELIMITER.join([first_val, second_val, third_val, fourth_val]))


"""
>>> us_capitals_by_state = {  # <1>
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    ...
}
>>> capitals = us_capitals_by_state.values()  # <2>
dict_values(['Montgomery', 'Juneau'])
>>> capitals.sort()  # <3>
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'dict_values' object has no attribute 'sort'
>>> sorted(capitals)  # <4>
['Albany', 'Annapolis', ...]
"""


def get_united_states_capitals():  # <1>
    us_capitals_by_state = {'Alabama': ...}
    capitals = us_capitals_by_state.values()
    return sorted(capitals)


US_CAPITALS_BY_STATE = {'Alabama': 'Montgomery', ...}  # <1>
US_CAPITALS = sorted(US_CAPITALS_BY_STATE.values())  # <2>
