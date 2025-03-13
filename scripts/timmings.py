"""
Simple timming test to access local ollama
"""
import time
from ollama import Client
from config.config import G_CUR_HOST_PORT

def timmings(n_request, cur_model, cur_host_port):
    """
    Display timming to access local ollama server
    """
    start_time = time.time()
    client = Client(
      host=cur_host_port,
      headers={'x-some-header': 'some-value'}
    )
    warm_time = time.time()
    for _ in range(0,n_request):
        client.chat(model=cur_model, messages=[
          {
            'role': 'user',
            'content': 'Why is the sky blue?. reply in markdown'
            ,
          },
        ])
    end_time = time.time()
    print(f"(Model{cur_model}-Warm up Time :\
         {warm_time-start_time:.6f} seconds")
    print(f"(Model{cur_model}-Query Time :\
         {end_time-warm_time:.6f} seconds")
    print(f"(Model{cur_model}-Average Query Time for\
         {n_request} Requests: {(end_time-warm_time)/n_request} seconds")
    print(f"(Model{cur_model}-Total  Query Time for\
        {n_request} Requests: {(end_time-warm_time)} seconds")

# Common definitions
G_N_REQUEST = 1
module_list = [
 #'llama3.2',
 #'lama2-uncensored:latest',
 'phi4-mini',
  #'deepseek-r1'
]

for G_cur_model in module_list:
    timmings(n_request=G_N_REQUEST,
             cur_model=G_cur_model,
             cur_host_port=G_CUR_HOST_PORT)
