from app import db, app, Locations, Categories, Groups, Users, PersonalRecs, ExpandRecs
import json
from flask import request, jsonify
from sqlalchemy import inspect
from sqlalchemy.exc import IntegrityError
from sqlalchemy.sql.expression import func
from sqlalchemy.sql.operators import ilike_op
from sqlalchemy import or_

def object_as_dict(obj):
    return {c.key: getattr(obj, c.key)
            for c in inspect(obj).mapper.column_attrs}


@app.route('/init', methods=['GET'])
def init():
    """Метод получения пользователей для ротации и категорий фильтрации"""
    """ return:
    { "users": [],
      "categories": [
                {"name": "string",
                "options": []},
                ... ,
                {"name": "string",
                "options": []},
      ],
      "presets": [
                {
                "name": "",
                "value_type": "boolean"
                },
                ...,
                {
                }
                ]
    }"""

    # getting users from db
    users = [101347983, 101352015, 101431770]

    # getting categories from db
    group_categories_from_db = [object_as_dict(row) for row in
                                Categories.query.all()]

    group_categories_dict = {}
    for elem in group_categories_from_db:
        if elem['category_1'] not in group_categories_dict.keys():
            group_categories_dict[elem['category_1']] = []
        else:
            group_categories_dict[elem['category_1']].append(elem['category_2'])

    group_categories = []
    for item in group_categories_dict.items():
        group_categories.append({'category': item[0],
                                 'subcategory': item[1]})

    group_categories = {'name': 'Направления',
                        'options': group_categories}

    # format
    format = {'name': 'Формат',
              'options': ['Онлайн', 'Очно']}

    # getting locations from db
    locations_from_db = [object_as_dict(row) for row in
                         Locations.query.all()]

    locations_dict = {}
    for elem in locations_from_db:
        if elem['district'] not in locations_dict.keys():
            locations_dict[elem['district']] = []
        else:
            locations_dict[elem['district']].append(elem['region'])

    locations = []
    for item in locations_dict.items():
        locations.append({'category': item[0],
                          'subcategory': item[1]})

    locations = {'name': 'Район',
                 'options': locations}

    # weekdays
    weekdays = {'name': 'Дни недели',
                'options': [{'full': 'Понедельник', 'short': 'Пн'},
                            {'full': 'Вторник', 'short': 'Вт'},
                            {'full': 'Среда', 'short': 'Ср'},
                            {'full': 'Четверг', 'short': 'Чт'},
                            {'full': 'Пятница', 'short': 'Пт'},
                            {'full': 'Суббота', 'short': 'Сб'},
                            {'full': 'Воскресенье', 'short': 'Вс'}]}

    categories = [group_categories, format, locations, weekdays]

    presets = [
        {"name": "Рядом с вами",
         "value_type": "boolean"}
    ]

    return {
        "users": users,
        "categories": categories,
        "presets": presets
    }


@app.route('/search_results', methods=['POST'])
def search_results():
    """Метод получения результатов поиска"""
    """arguments: 
    { "user": "",
      "string_to_search": "",
      "categories": [
                {"name": "string",
                "options": []},
                ... ,
                {"name": "string",
                "options": []}
                    ],
      "presets": [
                {
                "name": "",
                "value": bool
                },
                ...,
                {
                }
                ]
    }"""
    """ return:
    {
    groups: [{
        "region": "",
        "street": "",
        "home": "",
        "online": bool, 
        "name": "",
        "description": "",
        "group_id": "",
        "active_schedule": [[weekday, time], [weekday, time]] or [[weekday, time]],
        "active_group": bool
    },
    ... ,
    {
    }],
    number_of_groups: integer
    }"""

    x = request.json
    categories = x['categories']

    user_id = x['user_id']
    string_to_search = x['string_to_search']
    presets = x['presets']

    preset_close_to_user = False
    popular = False
    for preset in presets:
        if preset['name'] == 'Рядом с вами':
            preset_close_to_user = True
        if preset['name'] == 'Популярное':
            popular = True

    for filter in categories:
        if filter['name'] == 'Направления':
            directions = filter['options']
            directions = [subdirection['name'] for direction in directions for subdirection in direction['options']]
        elif filter['name'] == 'Формат':
            format = filter['options']
            if len(format) == 2 or len(format) == 0:
                format = ''
            elif len(format) == 1:
                if format[0]['name'] == 'Очно':
                    format = False
                elif format[0]['name'] == 'Онлайн':
                    format = True
        elif filter['name'] == 'Дни недели':
            weekdays = filter['options']
            weekdays = [weekday['name'] for weekday in weekdays]
        elif filter['name'] == 'Район':
            locations = filter['options']
            locations = [region['name'] for location in locations for region in location['options']]

    filter_list = list()
    filter_list.append(Groups.name.like(f'%{string_to_search.lower()}%'))

    if type(format) == bool:
        filter_list.append(Groups.online == format)
    if weekdays:
        filter_list.append(or_(Groups.weekday_1.in_(weekdays), Groups.weekday_2.in_(weekdays)))
    if locations:
        filter_list.append(Groups.region.in_(locations))
    if directions:
        filter_list.append(Groups.category_2.in_(directions))
    if preset_close_to_user:
        user_region = object_as_dict(Users.query.filter(Users.user_id == user_id))['user_region']
        filter_list.append(Groups.region == user_region)

    groups = [object_as_dict(row) for row in
                  Groups.query.filter(*filter_list)]

    return {"groups": groups,
            "number_of_groups": len(groups)}


@app.route('/personal_recommendations', methods=['POST'])
def personal_recommendations():
    """Метод получения пользовательских рекомендаций"""
    """arguments: user_id"""
    """ return:
    [{
        "region": "",
        "street": "",
        "home": "",
        "online": bool, 
        "name": "",
        "description": "",
        "group_id": "",
        "active_schedule": [[weekday, time], [weekday, time]] or [[weekday, time]],
        "active_group": bool
    },
    ... ,
    {
    }]"""

    user_id = str(request.form['user_id'])
    groups_to_rec = [object_as_dict(row)['group_id'] for row in
                     PersonalRecs.query.filter(PersonalRecs.user_id == user_id)]

    groups = [object_as_dict(row) for row in
              Groups.query.filter(Groups.group_id.in_(groups_to_rec))]
    return groups


@app.route('/expand_recommendations', methods=['POST'])
def expand_recommendations():
    """Метод получения рекомендаций для вывода пользователя из информационного пузыря"""
    """arguments: user_id"""
    """ return:
    [{
        "region": "",
        "street": "",
        "home": "",
        "online": bool, 
        "name": "",
        "description": "",
        "group_id": "",
        "active_schedule": [[weekday, time], [weekday, time]] or [[weekday, time]],
        "active_group": bool
    },
    ... ,
    {
    }]"""
    user_id = str(request.form['user_id'])
    groups_to_rec = [object_as_dict(row)['group_id'] for row in
                     ExpandRecs.query.filter(ExpandRecs.user_id == user_id)]

    groups = [object_as_dict(row) for row in
              Groups.query.filter(Groups.group_id.in_(groups_to_rec))]
    return groups


@app.route('/create_new_user', methods=['POST'])
def create_new_user():
    """Метод для получения результатов теста"""
    """"""
    # получаю результаты, формирую пользователя new в БД и записываю.
    # Просчитываю для него рекомендации и записываю в БД.
    test_results = request.json

    status = "не готово"
    return {"status": status}

# import pandas as pd
# from tqdm import tqdm
#
# @app.route('/', methods=['GET'])
# def load_data():
#     Locations.query.delete()
#     Categories.query.delete()
#     Groups.query.delete()
#     PersonalRecs.query.delete()
#     ExpandRecs.query.delete()
#     Users.query.delete()
#
#     locations = pd.read_csv('backend_data/locations.csv', sep=';')
#     for i, row in tqdm(locations.iterrows()):
#         db.session.add(Locations(district=row['district'], region=row['region']))
#         db.session.commit()
#
#     value = object_as_dict(Locations.query.filter_by(district='юго-восточный административный округ').first())
#     l_success = bool(value)
#
#     categories = pd.read_csv('backend_data/categories.csv', sep=';')
#     for i, row in tqdm(categories.iterrows()):
#         db.session.add(Categories(category_1=row['category 1'], category_2=row['category 2'], name=row['name']))
#         db.session.commit()
#
#     value = object_as_dict(Categories.query.filter_by(category_1='физическая активность').first())
#     c_success = bool(value)
#
#     groups = pd.read_csv('backend_data/groups.csv', sep=';')
#     for i, row in tqdm(groups.iterrows()):
#         db.session.add(Groups(group_id=row['group_id'], category_1=row['category 1'], category_2=row['category 2'],
#                               name=row['name'], district=row['district'], region=row['region'], street=row['street'],
#                               home=row['home'], online=row['online'],
#                               description=row['description'],
#                               weekday_1=row['weekday_1'],
#                               weekday_2=row['weekday_2'],
#                               active_schedule=row['active_shedule']))
#         db.session.commit()
#
#     value = object_as_dict(Groups.query.filter_by(district='юго-восточный административный округ').first())
#     g_success = bool(value)
#
#     users = pd.read_csv('backend_data/users.csv', sep=';')
#     for i, row in tqdm(users.iterrows()):
#         db.session.add(Users(user_id=row['user_id'],
#                              sex=row['sex'],
#                              age=row['age'],
#                              active_in_months=row['active_in_months'],
#                              active_in_years=row['active_in_years'],
#                              user_district=row['user_district'],
#                              user_region=row['user_region']))
#         db.session.commit()
#
#     value = object_as_dict(Users.query.filter_by(sex=1).first())
#     u_success = bool(value)
#
#     per_recs = pd.read_csv('backend_data/demo_best_predict.csv', sep=';')
#     for i, row in tqdm(per_recs.iterrows()):
#         db.session.add(PersonalRecs(user_id=str(row['user_id']), group_id=str(row['group_id'])))
#         db.session.commit()
#
#     expand_recs = pd.read_csv('backend_data/predict_to_expand.csv', sep=';')
#     for i, row in tqdm(expand_recs.iterrows()):
#         db.session.add(ExpandRecs(user_id=str(row['user_id']), group_id=str(row['group_id'])))
#         db.session.commit()
#
#     return jsonify({
#         'success': u_success and g_success and c_success and l_success
#     })
