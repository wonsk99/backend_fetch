from pydantic import BaseModel

## Define models for receipt
class Item(BaseModel):
	shortDescription: str
	price: str
class Receipt(BaseModel):
	retailer: str
	purchaseDate: str
	purchaseTime: str
	total: str
	items: list[Item]
