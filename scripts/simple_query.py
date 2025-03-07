from ollama import Client
import json
import time
from config.config import G_cur_host_port
# Common definitions
module = 'phi4-mini'

def query(cur_model, cur_host_port, query_list):
    """
     Returns the query response for each element in a list
    """
    client = Client(
      host=cur_host_port,
      headers={'x-some-header': 'some-value'}
    )
    response_list = []
    for q in query_list:
        response_list.append(
            client.chat(model=cur_model, messages=[q]).message.content
        )
    return response_list

q_list = [
      {
        'role': 'user',
        'content': 'Why is the sky blue?. reply in markdown'
      },
      {
        'role': 'user',
        'content': 'When the  sky is blue?. '
      },
]
res_list = query(cur_model= module,
                 cur_host_port=G_cur_host_port,
                 query_list=q_list)
for i in range(0,len(res_list)):
    print("------------------------")
    print(i+1)
    print("------------------------")
    print(f"\t{res_list[i]}")
