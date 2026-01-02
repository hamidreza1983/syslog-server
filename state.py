def get_state(cpu, mem):
    if cpu > 50 and mem > 50:
        return "critical"
    elif cpu >= 50 or mem >= 50:
        return "error"
    elif cpu >= 25 and mem >= 25:
        return "warning"
    elif cpu >= 25 or mem >= 25:
        return "caution"
    else:
        return "normal"