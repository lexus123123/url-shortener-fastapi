from pathlib import Path
import logging


BASE_DIR = Path(__file__).resolve().parent.parent
SHORT_URLS_STORAGE_FILEPATH = BASE_DIR / "short_urls.json"


LOG_LEVEL = logging.INFO
LOG_FORMAT: str = (
    "[%(asctime)s.%(msecs)03d] %(module)10s:%(lineno)-3d %(levelname)-7s - %(message)s"
)


API_TOKENS = frozenset({"eD83xIM7oJMn-WmuiDJPJQ", "HDk4YMx_Lu54ETlueqxTdw"})
