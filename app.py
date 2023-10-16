from fastapi import FastAPI, Body
import uvicorn
app = FastAPI()

"""
CREATE - post (Body)
READ - get
UPDATE - put
DELETE - delete
"""

@app.get("/")
def check_connectivity():
    return {"status_code":200, "status":"connected"}

@app.post("/save/data")
def save_user_data(user_data: dict = Body(...)):
    return {"status_code":201, "status":"success", "data":user_data}


if __name__ == "__main__" :
    uvicorn.run(app, host="0.0.0.0", port=8080)