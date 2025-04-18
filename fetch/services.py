import math

from models import Receipt, Item

## Calculate based on rules
def calculatePoints(receipt: Receipt):
	points = 0

	# A) Add 1 point for EVERY alnum in retailer name
	retailerName = receipt.retailer
	alnumsFound = 0
	for c in retailerName:
		if c.isalnum():
			alnumsFound += 1
	points += alnumsFound
	print(f"POINTS: {points}- Adding {alnumsFound}: Found {alnumsFound} alphanumeric characters...")

	# B) Add 50 points if TOTAL is round dollar amount
	total = receipt.total
	if total.endswith(".00"):
		points += 50
		print(f"POINTS: {points}- Adding 50: Total is a round dollar amount...")

	# C) Add 25 points if TOTAL is multiple of 0.25
	# ASSUMPTION: every total value will end with ".XX"
	cents = int(total[-2:])
	if cents % 25 == 0:
		points += 25
		print(f"POINTS: {points}- Adding 25: Total is a multiple of 0.25...")

	# D) Add 5 points for EVERY 2 items on receipt
	itemPairs = len(receipt.items) // 2
	points += itemPairs * 5	
	print(f"POINTS: {points}- Adding {itemPairs * 5}: There are {itemPairs} pairs of items...")

	# E) IF trimmed length of item desc is %3==0, multiply Price by 0.2. Round up to nearest int. Result is number of points to add.
	for item in receipt.items:
		desc = item.shortDescription.strip()
		if len(desc) % 3 == 0:
			trimPts = math.ceil(float(item.price) * 0.2)
			
			points += trimPts
			print(f"POINTS: {points}- Adding {trimPts}: Length of {desc} is multiple of 3...")

	# F) IFF LLM-generated, add 5 points if total is greater than 10
	# llm_generated = False
	# if llm_generated and float(total) > 10:
	#	points += 5 
	#	print("POINTS: {points}- Adding {5}: If I'm understanding this correctly, this should never be hit because the code wasn't LLM-generated? But in the case I misunderstood this rule, then we are adding 5 points because the total is greater than 10. :)")

	# G) Add 6 points if day in date is odd
	# ASSUMPTION: Date will always be provided YYYY-MM-DD 
	day = int(receipt.purchaseDate.split("-")[-1])
	if day % 2 == 1:
		points += 6
		print(f"POINTS: {points}- Adding 6: Purchase day is odd...")

	# H) Add 10 points if time is >2:00PM and <4:00PM
	# ASSUMPTION: Time will always be valid and provided as HH:MM
	timeFormat = int(receipt.purchaseTime.replace(":", ""))
	if timeFormat > 1400 and timeFormat < 1600:
		points += 10
		print(f"POINTS: {points}- Adding 10: Purchase time is between 14:00 and 16:00...")

	print(f"FINAL POINTS: {points}")
	return points
