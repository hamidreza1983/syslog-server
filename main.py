from state import get_state
from pathlib import Path
import socket
import logging
import json
from datetime import datetime
from dataset import create_dataframe

BASE_DIR = Path(__file__).parent

logging.basicConfig(
    filename=BASE_DIR / 'server.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filemode='a',
)

logger = logging.getLogger(__name__)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('192.168.140.20', 15555))

logger.info("UDP Server started on port 15555")

all_data = []
columns = None

while True:
    data, addr = s.recvfrom(1024)
    message = data.decode('utf-8')

    try:
        stats = json.loads(message)

        cpu = stats.get('cpu')
        mem = stats.get('mem')
        disk = stats.get('disk')

        state = get_state(cpu, mem)

        row = {
            "ip": addr[0],
            "cpu": cpu,
            "mem": mem,
            "disk": disk,
            "state": state
        }

        if columns is None:
            columns = list(row.keys())

        all_data.append(list(row.values()))

        df = create_dataframe(all_data, columns)
        df.to_csv(BASE_DIR / 'stats.csv', index=False)

        print(df.tail(5))
        logger.info(f"{addr[0]} | {row}")

    except json.JSONDecodeError:
        logger.error(f"Invalid JSON from {addr}")

    except Exception as e:
        logger.exception("Unexpected error")

