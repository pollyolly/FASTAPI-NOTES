import json

from fastapi import HTTPException

def create_delivery(state, event):
    data = json.loads(event.data)
    return {
        "id": event.delivery_id,
        "budget": int(data["budget"]),
        "notes": data["notes"],
        "status": "ready"
    }

CONSUMERS = {
        "CREATE_DELIVERY": create_delivery,
    }
