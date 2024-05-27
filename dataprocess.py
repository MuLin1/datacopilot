import json
import numpy as np
def preprocess_data(data):
    input_texts = []
    target_texts = []

    for item in data:
        question = item['question']
        table_id = item['table_id']
        sel_cols = ', '.join(item['keywords']['sel_cols'])
        try:
            conds = ' AND '.join([f"{cond[0]} = '{cond[2]}'" for cond in item['sql']['conds']])
            input_text = f"{question}"
            target_text = f"SELECT {sel_cols} FROM {table_id} WHERE {conds}"
        except KeyError:
            input_text = f"{question}"
            target_text = f"SELECT {sel_cols} FROM {table_id}"


        input_texts.append(input_text)
        target_texts.append(target_text)

    return input_texts, target_texts

# Example
data = [
    {"id": 830062281, "question": "帮我挑几只定投的指数基金", "table_id": "FundTable",
     "sql": {"sel": [1], "agg": [0], "limit": 0, "orderby": [], "asc_desc": 0, "cond_conn_op": 0,
             "conds": [[3, 2, "指数型"]]}, "keywords": {"sel_cols": ["基金名称"], "values": ["指数型"]}}

]


with open('antsql1/antsql1_dev.jsonl','r',encoding='utf8') as f:
    cnt = 0

    for line in f:

        data = json.loads(line)
        input_texts, target_texts = preprocess_data([data])
        print(input_texts,target_texts)
        cnt +=1
        if cnt >10:
            break