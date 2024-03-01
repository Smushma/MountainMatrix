from fastapi import APIRouter

router = APIRouter()


@router.get("/peaks/")
async def get_peaks():
    return [{"test": "derp"}]
