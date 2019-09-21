import json
import random

FOODS = [  # <1>
    'pizza',
    'burgers',
    'salad',
    'soup',
]


# 1st version
def random_food(request):
    food = random.choice(FOODS)  # <1>

    if request.headers.get('Accept') == 'application/json':  # <2>
        return json.dumps({'food': food})
    else:
        return food  # <3>


# 2nd version
def random_food(request):
    food = random.choice(FOODS)

    if request.headers.get('Accept') == 'application/json':
        return json.dumps({'food': food})
    elif request.headers.get('Accept') == 'application/xml':  # <1>
        return f'<response><food>{food}</food></response>'
    else:
        return food


# 3rd version
def random_food(request):
    food = random.choice(FOODS)

    formats = {  # <1>
        'application/json': json.dumps({'food': food}),
        'application/xml': f'<response><food>{food}</food></response>',
    }

    return formats.get(request.headers.get('Accept'), food)  # <2>


# Initial function
def random_food(request):  # <2>
    return random.choice(FOODS)  # <3>


# Extract functions
def to_json(food):  # <1>
    return json.dumps({'food': food})


def to_xml(food):
    return f'<response><food>{food}</food></response>'


def random_food(request):
    food = random.choice(FOODS)

    formats = {  # <2>
        'application/json': to_json,
        'application/xml': to_xml,
    }

    format_function = formats.get(  # <3>
        request.headers.get('Accept'),
        lambda val: val  # <4>
    )
    return format_function(food)  # <5>


# Full separation
def get_format_function(accept=None):  # <1>
    formats = {
        'application/json': to_json,
        'application/xml': to_xml,
    }

    return formats.get(accept, lambda val: val)


def random_food(request):  # <2>
    food = random.choice(FOODS)
    format_function = get_format_function(request.headers.get('Accept'))  # <3>
    return format_function(food)
