import json
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from redis_om import get_redis_connection, HashModel
#consumers.py
import consumers

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_methods=['*'],
    allow_headers=['*']
    )

redis = get_redis_connection(
        host="redis-19889.c290.ap-northeast-1-2.ec2.cloud.redislabs.com",
        # username="default",
        port="19889",
        password="EL7cQheuQ6LThat3tXBtZ3TjbOqJ3ezV",
        decode_responses=True
    )

class Delivery(HashModel):
    budget: int = 0
    notes: str = ''
    class Meta:
        database = redis

class Event(HashModel):
    delivery_id: str = None
    type: str
    data: str
    class Meta: 
        database = redis

# http://localhost:8000/deliveries/01HKPYHB4R3CAA9N6H4MZCCMVH/status
# Check and Get state in Redis
@app.get('/deliveries/{pk}/status')
async def get_state(pk: str):
    state = redis.get(f'delivery:{pk}')

    if state is not None:
        return json.loads(state)

    state = build_state(pk)
    redis.set(f'delivery:{pk}', json.dumps(state))
    return state

def build_state(pk: str):
    pks = Event.all_pks()
    all_events = [Event.get(pk) for pk in pks]
    events = [event for event in all_events if event.delivery_id == pk]
    state = {}

    for event in events:
        state = consumers.CONSUMERS[event.type](state, event)

    return state

# http://localhost:8000/deliveries/create
@app.post('/deliveries/create')
async def create(request: Request):
    body = await request.json()
    delivery = Delivery(budget=body['data']['budget'],notes=body['data']['notes']).save()
    event = Event(delivery_id=delivery.pk, type=body['type'], data=json.dumps(body['data'])).save()
    state = consumers.CONSUMERS[event.type]({}, event)
    redis.set(f'delivery: {delivery.pk}', json.dumps(state))
    return state

@app.post('/event')
async def dispatch(request: Request):
    # get body request
    body = await request.json()
    delivery_id = body['delivery_id']
    state = await get_state(delivery_id)
    event = Event(delivery_id=delivery_id, type=body['type'], data=json.dumps(body['data'])).save()
    new_state = consumers.CONSUMERS[event.type](state, event)
    redis.set(f'delivery: {delivery_id}', json.dumps(new_state))
    return new_state
