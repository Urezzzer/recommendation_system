from app import db, Locations, Categories, Groups, Users, PersonalRecs, ExpandRecs, Ranks
import pandas as pd
from tqdm import tqdm
from sqlalchemy import inspect
from flask import jsonify


def object_as_dict(obj):
    return {c.key: getattr(obj, c.key)
            for c in inspect(obj).mapper.column_attrs}


def load_data():
    Locations.query.delete()
    Categories.query.delete()
    Groups.query.delete()
    PersonalRecs.query.delete()
    ExpandRecs.query.delete()
    Users.query.delete()
    Ranks.query.delete()
    db.session.commit()

    locations = pd.read_csv('backend_data/locations.csv', sep=';')
    for i, row in tqdm(locations.iterrows()):
        db.session.add(Locations(district=row['district'], region=row['region']))
        db.session.commit()

    value = object_as_dict(Locations.query.filter_by(district='юго-восточный административный округ').first())
    l_success = bool(value)

    categories = pd.read_csv('backend_data/categories.csv', sep=';')
    for i, row in tqdm(categories.iterrows()):
        db.session.add(Categories(category_1=row['category 1'], category_2=row['category 2'], name=row['name']))
        db.session.commit()

    value = object_as_dict(Categories.query.filter_by(category_1='физическая активность').first())
    c_success = bool(value)

    groups = pd.read_csv('backend_data/groups.csv', sep=';')
    for i, row in tqdm(groups.iterrows()):
        db.session.add(Groups(group_id=row['group_id'], category_1=row['category 1'], category_2=row['category 2'],
                              name=row['name'], district=row['district'], region=row['region'], street=row['street'],
                              home=row['home'], online=row['online'],
                              description=row['description'],
                              weekday_1=row['weekday_1'],
                              weekday_2=row['weekday_2'],
                              active_schedule=row['active_shedule'],
                              popularity=row['popularity']))
        db.session.commit()

    value = object_as_dict(Groups.query.filter_by(district='юго-восточный административный округ').first())
    g_success = bool(value)

    users = pd.read_csv('backend_data/users.csv', sep=';')
    for i, row in tqdm(users.iterrows()):
        db.session.add(Users(user_id=row['user_id'],
                             sex=row['sex'],
                             age=row['age'],
                             active_in_months=row['active_in_months'],
                             active_in_years=row['active_in_years'],
                             user_district=row['user_district'],
                             user_region=row['user_region'],
                             history=row['history'],
                             name=row['name']))
        db.session.commit()

    value = object_as_dict(Users.query.first())
    u_success = bool(value)

    per_recs = pd.read_csv('backend_data/predict_best.csv', sep=';')
    for i, row in tqdm(per_recs.iterrows()):
        db.session.add(
            PersonalRecs(user_id=int(row['user_id']), group_id=int(row['group_id']), score=float(row['score'])))
        db.session.commit()

    expand_recs = pd.read_csv('backend_data/predict_to_expand.csv', sep=';')
    for i, row in tqdm(expand_recs.iterrows()):
        db.session.add(
            ExpandRecs(user_id=int(row['user_id']), group_id=int(row['group_id']), score=float(row['score'])))
        db.session.commit()

    ranks = pd.read_csv('backend_data/group_scores_to_rank.csv', sep=';')
    for i, row in tqdm(ranks.iterrows()):
        db.session.add(Ranks(user_id=int(row['user_id']),
                             group_id=int(row['group_id']),
                             score=float(row['score'])))
        db.session.commit()

    value = object_as_dict(Ranks.query.first())
    r_success = bool(value)

    return jsonify({
        'success': u_success and g_success and c_success and l_success and r_success
    })

# load_data() # Необходимо перенести папку backend_data из research в server