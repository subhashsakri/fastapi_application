from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from database import create_database_connection
from models import Configuration

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to my FastAPI application"}

@app.get("/favicon.ico")
async def favicon():
    return {"message": "Favicon not found"}

@app.post("/create_configuration")
async def create_configuration(request: Request, config: Configuration):
    # Create a new configuration
    session = create_database_connection()
    session.add(config)
    session.commit()
    session.close()
    return JSONResponse(content={"message": "Configuration created successfully"}, media_type="application/json")

@app.get("/get_configuration/{country_code}")
async def get_configuration(country_code: str):
    # Retrieve a configuration by country code
    session = create_database_connection()
    config = session.query(Configuration).filter(Configuration.country_code == country_code).first()
    session.close()
    if config:
        return JSONResponse(content={"configuration": config}, media_type="application/json")
    else:
        raise HTTPException(status_code=404, detail="Configuration not found")

@app.post("/update_configuration")
async def update_configuration(request: Request, config: Configuration):
    # Update a configuration
    session = create_database_connection()
    config_to_update = session.query(Configuration).filter(Configuration.country_code == config.country_code).first()
    if config_to_update:
        config_to_update.business_name = config.business_name
        config_to_update.pan = config.pan
        config_to_update.gstin = config.gstin
        session.commit()
        session.close()
        return JSONResponse(content={"message": "Configuration updated successfully"}, media_type="application/json")
    else:
        raise HTTPException(status_code=404, detail="Configuration not found")

@app.delete("/delete_configuration/{country_code}")
async def delete_configuration(country_code: str):
    # Delete a configuration
    session = create_database_connection()
    config_to_delete = session.query(Configuration).filter(Configuration.country_code == country_code).first()
    if config_to_delete:
        session.delete(config_to_delete)
        session.commit()
        session.close()
        return JSONResponse(content={"message": "Configuration deleted successfully"}, media_type="application/json")
    else:
        raise HTTPException(status_code=404, detail="Configuration not found")


