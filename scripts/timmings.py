from ollama import Client
import json
import time
from config.config import G_cur_host_port
# Common definitions
G_NRequest = 1
module_list = [
 #'llama3.2',
 #'lama2-uncensored:latest',
 'phi4-mini',
  #'deepseek-r1'
]

def timmings(NRequest, cur_model, cur_host_port):
    """
    Display timming to access local ollama server
    """
    start_time = time.time()
    client = Client(
      host=cur_host_port,
      headers={'x-some-header': 'some-value'}
    )
    warm_time = time.time()
    for i in range(0,NRequest):
        response = client.chat(model=cur_model, messages=[
          {
            'role': 'user',
            'content': 'Why is the sky blue?. reply in markdown'
            ,
          },
        ])
    end_time = time.time()
    print(f"(Model{cur_model}-Warm up Time : {warm_time-start_time:.6f} seconds")
    print(f"(Model{cur_model}-Query Time : {end_time-warm_time:.6f} seconds")
    print(f"(Model{cur_model}-Average Query Time for {NRequest} Requests: {(end_time-warm_time)/NRequest} seconds")
    print(f"(Model{cur_model}-Total  Query Time for {NRequest} Requests: {(end_time-warm_time)} seconds")

for G_cur_model in module_list:
    timmings(NRequest=G_NRequest, cur_model=G_cur_model, cur_host_port=G_cur_host_port)
