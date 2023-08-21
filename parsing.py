import re

text = """
5. Sales:
  5.1. Customer Service: Your primary focus should be on providing excellent customer service. This includes answering customer queries promptly and resolving any issues professionally.
  5.2. Return/Exchange Policy: An easy-to-understand return/exchange policy can help build trust with your customers.
  5.3. User-Friendly Purchasing Process: Make sure the purchasing process is user-friendly. It should be easy for customers to buy, make payments and track shipment of products.
  5.4. After-Sales Service: Good after-sales service can lead to repeat business. Send follow-up emails after purchase, ask for reviews, offer tips on how to use the product, etc.
  5.5. Referrals: Encourage satisfied customers to refer your business to their contacts. You can incentivize them by providing discounts on future purchases for successful referrals.
"""

pattern = r"(\d+\.\d+)\. (.*?): (.*)"

matches = re.findall(pattern, text)

for match in matches:
    pointer_number = match[0]
    pointer_title = match[1]
    pointer_body = match[2]
    
    print(f"Indexed numbers: {pointer_number}")
    print(f"Topic titles: {pointer_title}")
    print(f"Body of the text: {pointer_body}")
   