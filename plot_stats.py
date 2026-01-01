import pandas as pd
import matplotlib.pyplot as plt

CSV_FILE = "stats.csv"

df = pd.read_csv(CSV_FILE)

ips = df['ip'].unique()

for ip in ips:
    ip_df = df[df['ip'] == ip]

    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    fig.suptitle(f"System Resource Usage - {ip}", fontsize=14)

    # ---------- CPU ----------
    axes[0].plot(ip_df.index, ip_df['cpu'])
    axes[0].set_title("CPU Usage")
    axes[0].set_xlabel("Time")
    axes[0].set_ylabel("CPU %")
    axes[0].grid(True)

    # ---------- RAM ----------
    axes[1].plot(ip_df.index, ip_df['mem'])
    axes[1].set_title("RAM Usage")
    axes[1].set_xlabel("Time")
    axes[1].set_ylabel("RAM %")
    axes[1].grid(True)

    # ---------- DISK ----------
    axes[2].plot(ip_df.index, ip_df['disk'])
    axes[2].set_title("Disk Usage")
    axes[2].set_xlabel("Time")
    axes[2].set_ylabel("Disk %")
    axes[2].grid(True)

    plt.tight_layout()
    plt.show()
