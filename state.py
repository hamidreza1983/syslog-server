def get_state(cpu, mem):
    if cpu > 50 or mem > 50:
        return "critical"
    elif cpu >= 25 or mem >= 25:
        return "warning"
    else:
        return "normal"