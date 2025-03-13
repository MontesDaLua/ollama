"""
test simple query to GenAi server
"""
from ollama import Client
from config.config import G_CUR_HOST_PORT

def simple_query(cur_model, cur_host_port, query_list):
    """
     Returns the query response for each element in a list
    """
    client = Client(
      host=cur_host_port,
      headers={'x-some-header': 'some-value'}
    )
    response_list = []
    for q in query_list:
        response = client.chat(model=cur_model, messages=[q])
        response_list.append( response.message.content )
    return response_list


# Common definitions
# Module to use in  ollama
MODULE = 'phi4-mini'
# Query list
q_list = [
      {
        'role': 'user',
        'content': ".".join([
            'Why is the sky blue?',
            'reply in markdown'
        ])
      },
      {
        'role': 'user',
        'content': ".".join([
            'When the  sky is blue?'
        ])
      },
]

res_list = simple_query(cur_model= MODULE,
                 cur_host_port= G_CUR_HOST_PORT,
                 query_list=q_list)

for r in res_list:
    print("------------------------")
    print(f"\t{r}")
