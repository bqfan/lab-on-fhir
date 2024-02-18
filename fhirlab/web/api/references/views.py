from fastapi import APIRouter, status
from fastapi.param_functions import  Depends

#from redis.asyncio import ConnectionPool, Redis

# from fhirlab.services.redis.dependency import get_redis_pool
# from fhirlab.web.api.redis.schema import RedisValueDTO

router = APIRouter()



# @router.post("/",
#             summary="Returns all observation references",
#             status_code=status.HTTP_200_OK)
# # def get_references(api_key: APIKey = Depends(get_api_key)) -> dict:
# def get_references():
#     return { 'references': 'references'}


@router.get("/",
            summary="Returns all observation references",
            status_code=status.HTTP_200_OK)
# def get_references(api_key: APIKey = Depends(get_api_key)) -> dict:
async def get_references():
    return { 'references': 'references'}

@router.post("/{key}",
             summary="create reference",
             status_code=status.HTTP_201_CREATED)
async def create_reference():
    return { 'reference_keys': 'created'}


@router.get("/_keys",
            summary="Returns all observation reference keys",
            status_code=status.HTTP_200_OK)
# def get_reference_keys(api_key: APIKey = Depends(get_api_key)) -> list:
async def get_reference_keys():
    return { 'reference_keys': 'keys'}

# @router.get("/", response_model=RedisValueDTO)
# async def get_redis_value(
#     key: str,
#     redis_pool: ConnectionPool = Depends(get_redis_pool),
# ) -> RedisValueDTO:
#     """
#     Get value from redis.

#     :param key: redis key, to get data from.
#     :param redis_pool: redis connection pool.
#     :returns: information from redis.
#     """
#     async with Redis(connection_pool=redis_pool) as redis:
#         redis_value = await redis.get(key)
#     return RedisValueDTO(
#         key=key,
#         value=redis_value,
#     )


# @router.put("/")
# async def set_redis_value(
#     redis_value: RedisValueDTO,
#     redis_pool: ConnectionPool = Depends(get_redis_pool),
# ) -> None:
#     """
#     Set value in redis.

#     :param redis_value: new value data.
#     :param redis_pool: redis connection pool.
#     """
#     if redis_value.value is not None:
#         async with Redis(connection_pool=redis_pool) as redis:
#             await redis.set(name=redis_value.key, value=redis_value.value)
