from random import randint

from fastapi import FastAPI, Body, HTTPException, status

app = FastAPI()


@app.get("/ping")
def ping_pong():
    return {"message": "pong"}


ITEMS = {}


@app.post("/item", tags=["Items"])
def create_item(item: str = Body(...)):
    item_id = item + str(randint(0, 10000000000000000))
    ITEMS[item] = item_id
    print(ITEMS)
    return {"item": item, "id": item_id}


@app.get("/item/{item_id}", tags=["Items"])
def get_item_by_id(item_id: str):
    for key, values in ITEMS.items():
        if item_id == values:
            return key
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"user with user_id: '{item_id}' not found")


@app.delete("/item/{item_id}", tags=["Items"])
def delete_item_by_id(item_id: str):
    for key, values in list(ITEMS.items()):
        if item_id == values:
            ITEMS.pop(key)
            print(f"User {key} with id {item_id} deleted")
            return f"User {key} with id {item_id} deleted"
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"user with user_id: '{item_id}' not found")


@app.patch("/item/{item_id}", tags=["Items"])
def patch_item_name_by_id(item_id: str, new_name):
    for key, values in list(ITEMS.items()):
        if item_id == values:
            old_name, key = key, new_name
            ITEMS.pop(old_name)
            ITEMS[new_name] = item_id
            return f"Item {old_name} patched, new name is {new_name}"
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"item with item_id: '{item_id}' not found")
