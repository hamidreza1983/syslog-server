from pathlib import Path
import logging
from datetime import datetime

BASE_DIR = Path(__file__).parent

SERVER_IP = "192.168.87.1"
SERVER_PORT = 15555

logging.basicConfig(
    filename=BASE_DIR / 'server.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filemode='a',
)

logger = logging.getLogger(__name__)

CSV_FILE = "stats.csv"

all_data = []
columns = None