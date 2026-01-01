import psutil
import json

def send():
    data = {
        "cpu": psutil.cpu_percent(interval=1),
        "mem": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage('/').percent
    }
    return json.dumps(data)