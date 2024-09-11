from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse
from sqlalchemy.sql import func

from config.database import session
from models.vinyls import Vinyls as VinylsModel
from request import VinylRequest
from typing import List

# Setting API router
router = APIRouter()


@router.get('/all', tags=['Vinyl'], response_model=List[VinylRequest])
async def get_all() -> JSONResponse:
    """
    Get all the vinyls in the database.
    """
    db = session()
    result = db.query(VinylsModel).all()
    return JSONResponse(content=jsonable_encoder(result), status_code=200)


@router.get('/get_vinyl/{id}', tags=['Vinyl'], response_model=VinylRequest)
async def get_vinyl(id: int) -> JSONResponse:
    """
    Get a specific vinyl using the id.
    """
    db = session()
    result = db.query(VinylsModel).filter(VinylsModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={'message': 'ID not found in the database'})
    return JSONResponse(content=jsonable_encoder(result), status_code=200)


@router.get('/get_vinyl_by_label/{label}', tags=['Vinyl'], response_model=VinylRequest)
async def get_vinyl_by_label(label: str) -> JSONResponse:
    """
    Get a specific vinyl using the name of the label
    """
    db = session()
    result = db.query(VinylsModel).filter(func.lower(VinylsModel.label) == func.lower(label)).all()
    if not result:
        return JSONResponse(status_code=404, content={'message': 'Label not founded'})
    return JSONResponse(content=jsonable_encoder(result), status_code=200)


@router.post('/add_vinyl', tags=['Vinyl'], response_model=VinylRequest)
async def add_vinyl(vinyl: VinylRequest) -> JSONResponse:
    """
    Add a vinyl to the database
    """
    db = session()
    new_vinyl = VinylsModel(**vinyl.dict())
    db.add(new_vinyl)
    db.commit()
    return JSONResponse(content=vinyl.dict(), status_code=200)


@router.put('/update_vinyl/', tags=['Vinyl'], response_model=VinylRequest)
async def update_vinyl(vinyl: VinylRequest) -> JSONResponse:
    """
    Update a vinyl in the database
    """
    db = session()
    db_vinyl = db.query(VinylsModel).filter(VinylsModel.id == vinyl.id).first()
    if not db_vinyl:
        raise HTTPException(status_code=404, detail='Vinyl not found')

    db_vinyl.name = vinyl.name
    db_vinyl.artist = vinyl.artist
    db_vinyl.label = vinyl.label
    db_vinyl.release_year = vinyl.release_year

    db.commit()
    db.refresh(db_vinyl)

    return JSONResponse(content=jsonable_encoder(db_vinyl), status_code=200)
