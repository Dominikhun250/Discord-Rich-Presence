from pypresence import Presence
import time

client_id = "000000000000" #Aplication client id
RPC = Presence(client_id)

RPC.connect()

RPC.update(
    state="Message",
    large_image='application image',
    small_image='application image',
    large_text="By: Dominikhun250",
    small_text="This a image text",
    buttons=[
        {"label": "Button 1", "url": "https://dominikhun250.hu/"}, 
        {"label": "Button 2", "url": "https://dominikhun250.hu/"}
    ]
)

print("Successful connent.")

while True:
    time.sleep(60)

    #By: Dominikhun250