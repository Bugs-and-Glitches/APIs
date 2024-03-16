from fastapi import APIRouter ,Request
from pydantic import BaseModel
from information.list_of_companies.list import list_companies
from static import *


router = APIRouter()

@router.get("/v1/listCompanies")
async def read_users():
    return list_companies

@router.get("/no")
async def read_users():
    return 'no'
