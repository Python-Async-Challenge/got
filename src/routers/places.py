"""Places router module."""
from fastapi import APIRouter

from src.clients.places import PlacesClient

router = APIRouter()  # pylint: disable=invalid-name

places_client = PlacesClient()

@router.get('/')
async def get_places():
    """Get places endpoint."""
    return await places_client.get_list()