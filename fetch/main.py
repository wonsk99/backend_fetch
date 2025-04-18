from fastapi import FastAPI, HTTPException

import uuid

from models import Receipt, Item
from services import calculatePoints

RECEIPT_STORE = {}

# Init FastAPI
app = FastAPI()

## Endpoints
# POST - process receipt
@app.post("/receipts/process")
def processReceipts(receipt: Receipt):
	receiptId = str(uuid.uuid4())
	points = calculatePoints(receipt)
	
	RECEIPT_STORE[receiptId] = points
	return {"id": receiptId}

# GET - get points
@app.get("/receipts/{r_id}/points")
def getPoints(r_id: str):
	if r_id in RECEIPT_STORE:
		points = RECEIPT_STORE[r_id]
		return {"points": points}
	raise HTTPException(status_code=404, detail=f"Receipt not found for id: {r_id}")
