from fastapi.routing import APIRouter

from fhirlab.web.api import echo, monitoring, redis, references

api_router = APIRouter()
api_router.include_router(monitoring.router)
api_router.include_router(echo.router, prefix="/echo", tags=["echo"])
api_router.include_router(references.router, prefix="/Observation/_references", tags=['References'])
api_router.include_router(redis.router, prefix="/redis", tags=["redis"])
