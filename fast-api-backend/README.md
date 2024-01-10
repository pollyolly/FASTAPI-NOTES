#### Delivery Create
Python
```vim
# http://localhost:8000/deliveries/create
@app.post('/deliveries/create')
async def create(request: Request)
```
Request Body
```vim
{
    "type": "CREATE_DELIVERY",
    "data": {
        "budget": 58,
        "notes": "Pick 2 pizzas"
    }
}
```
Response Body
```vim
{"id":"01HKPYHB4R3CAA9N6H4MZCCMVH","budget":58,"notes":"Pick 2 pizzas","status":"ready"}
```
#### Delivery Status
Python
```vim
@app.get('/deliveries/{pk}/status')
async def get_state(pk: str)
```
Request Body
```
http://localhost:8000/deliveries/01HKPYHB4R3CAA9N6H4MZCCMVH/status
```
Response Body
```
{"id":"01HKPYHB4R3CAA9N6H4MZCCMVH","budget":58,"notes":"Pick 2 pizzas","status":"ready"}
```

#### PostMan
GET: http://localhost:8000/deliveries/01HKPYHB4R3CAA9N6H4MZCCMVH/status

Request Body
```vim
{
    "type": "CREATE_DELIVERY",
    "data": {
        "budget": 50,
        "notes": "Pick 2 pizzas"
    }
}
```
Response
```
{
    "id": "01HKPYHB4R3CAA9N6H4MZCCMVH",
    "budget": 58,
    "notes": "Pick 2 pizzas",
    "status": "ready"
}
```
POST: http://localhost:8000/deliveries/create

Request Body
```vim
{
    "type": "CREATE_DELIVERY",
    "data": {
        "budget": 58,
        "notes": "Pick 2 pizzas"
    }
}
```
Response
```
{
    "id": "01HKS60JSCY2N9SCQ5F5RKKWSP",
    "budget": 58,
    "notes": "Pick 2 pizzas",
    "status": "ready"
}
```
