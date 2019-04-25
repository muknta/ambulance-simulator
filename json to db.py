import json
import psycopg2
from app.op.сonfig import * # config folder


with open('medic_data\symptoms.json', 'r') as json_file:
    json_data = json.load(json_file)
    conn = psycopg2.connect(database=Config.database, host=Config.host, user=Config.user) #from config folder
    conn.set_client_encoding('UTF8')
    cur = conn.cursor()
    for i in json_data:
        try:
            cur.execute(
                      u"insert into symptoms values(%s, %s, %s, %s, %s, %s, %s)",
                       (i['id'], i["name"], i["common_name"], i["sex_filter"], i["category"],
                      i["seriousness"], i["parent_relation"])
                       )
        except:
            print('Already exists')
        conn.commit()
    conn.close()
    cur.close()
