import psycopg2 as psc
import json

conn = psc.connect("dbname='medic_data' user='heknt'")
cur = conn.cursor()

with open('symptoms.json') as f:
    s_data = json.load(f)
cur.execute("select * from symptoms")
colnames = [desc[0] for desc in cur.description]
for i in s_data:
    d = [json.dumps(i[j]) if type(i[j])==dict else str(i[j]) for j in colnames]
    cur.execute("""insert into symptoms values (%s,%s,%s,%s,%s,%s,%s,json_array_elements(%s::json[]),%s,%s,%s,%s)""",tuple(d))
#    d=[]
#    for j in colnames:
#        if type(i[j]) == dict:
#            print("EWWER")
#            d.append(json.dumps(i[j]))
#        elif type(i[j]) == str:
#            d.append(str(i[j]).replace(' ','_'))
#        elif type(i[j]) == list:
#            d.append("jsonb_array_elements("+str(i[j])+"::jsonb)")
#        else:
#            d.append(str(i[j]))
#    cur.execute(f"""insert into symptoms { cn[0],cn[1],cn[2],cn[3],cn[0],cn[1],cn[2],cn[3], } values {tuple( i[j] for j in colnames )}""")
#    cur.execute(f"""insert into symptoms ({ ', '.join([j for j in colnames]) }) values ({ ', '.join(d) })""")
#    cur.execute(f"""insert into symptoms ({ ', '.join([j for j in colnames]) }) values {tuple( jsonb_array_elements(j::jsonb) if type(d)==dict else j for j in d )}""")

with open('conditions.json') as f:
    c_data = json.load(f)
cur.execute("select * from conditions")
colnames = [desc[0] for desc in cur.description]
for i in c_data:
    cur.execute(f"""insert into conditions {tuple( j for j in colnames )} values {tuple( i[j] for j in colnames )}""")

cur.close()
conn.commit()
conn.close()


#for i in s_data:
#    cur.execute(f"""insert into (id, name, common_name, sex_filter, category, seriousness, extras, children, image_url, image_source, parent_id, parent_relation) values ({id[i]}, {name[i]}, {common_name[i]}, {sex_filter[i]}, {category[i]}, {seriousness[i]}, {extras[i]}, {children[i]}, {image_url[i]}, {image_source[i]}, {parent_id[i]}, {parent_relation[i]})""")
