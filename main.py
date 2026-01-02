from state import get_state
import socket
import json
from dataset import create_dataframe
from config import BASE_DIR, SERVER_IP, SERVER_PORT, logger, all_data, columns


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((SERVER_IP, SERVER_PORT))

logger.info("UDP Server started on port 15555")



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

