from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from pybars import Compiler

from os import environ

import json

from problem import problem_map
from searcher.Searcher import Searcher
compiler = Compiler()

app = FastAPI()

hbs = open('./template.hbs').read()

template = compiler.compile(hbs)
html = template({"api": environ.get("API_URL", "http://localhost:8000"), "ws_api": environ.get("WS_URL", "ws://localhost:8000")})



@app.get("/")
async def get():
  return HTMLResponse(html)


@app.get("/map")
async def get():
  return json.dumps({
    "edges": problem_map.get_raw_edges(),
  })

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
  agent = Searcher(problem_map)

  await websocket.accept()

  while True:
    data = await websocket.receive_json()
    print(data)
    if data['action'] == 'start':
      async def sendIteration(response):
        await websocket.send_json(response)
        if data['stepMode'] == True:
          while (await websocket.receive_text()) != 'next': pass
      if data['alg'] == 'normal': await agent.start_a(data['from'], data['to'], sendIteration)
      elif data['alg'] == 'greedy': await agent.start_greedy(data['from'], data['to'], sendIteration) 
      elif data['alg'] == 'uniform': await agent.start_uniform(data['from'], data['to'], sendIteration)
      print('termino')
