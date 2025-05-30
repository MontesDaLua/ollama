"""
test simple query to GenAi server
"""
from ollama import Client
from config.config import G_CUR_HOST_PORT

def get_ollama_client(host):
    """
    Returns a client to the server
    """
    client = Client(
      host=host,
      # use static headres
      headers={'x-some-header': 'some-value'}
    )
    return client


def simple_query(cur_model, cur_host_port, query_list):
    """
     Returns the query response for each element in a list
    """
    client = get_ollama_client(host=cur_host_port)
    response_list = []
    for q in query_list:
        response_generator = client.chat(model=cur_model, messages=[q])
        full_response = ""
        for chunk in response_generator:
            # get just the message
            if chunk[0] == "message":
                full_response += chunk[1].content
        # print(full_response)
        response_list.append(full_response)
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
            'When the  sky is blue?',
            'reply in Portuguese'
        ])
      },
]

res_list = simple_query(cur_model=MODULE,
                 cur_host_port=G_CUR_HOST_PORT,
                 query_list=q_list)
for r in res_list:
    print("------------------------")
    print(f"\t{r}")

# if __name__ == '__main__':
#     unittest.main()
