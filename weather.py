# weather.py: Handles only the asynchronous API call and parsing. [async fetch logic]
# ---------------------------------------------------------------------------------------------------------------------------------
import python_weather

async def fetch_weather(location: str) -> tuple[float | str, str]:
    """
    Fetches temperature and condition for a given location.
    Returns a (temp, description) pair.
    """
    async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
        data = await client.get(location)
        temp = data.temperature or "N/A"
        cond = getattr(data, "condition", None) \
               or getattr(data, "description", "Unavailable")
        return temp, cond
# ---------------------------------------------------------------------------------------------------------------------------------