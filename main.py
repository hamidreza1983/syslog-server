from pathlib import Path
import socket
import logging
import json

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
s.bind(('192.168.87.1', 15555))

logger.info("UDP Server started on port 5555")

while True:
    data, addr = s.recvfrom(1024)
    message = data.decode('utf-8')

    stats = json.loads(message)

    print(f"{addr} | CPU: {stats['cpu']}% | RAM: {stats['mem']}% | DISK: {stats['disk']}%")
    logger.info(f"{addr} | {stats}")
