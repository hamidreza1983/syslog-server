from pathlib import Path
from config import BASE_DIR, CSV_FILE, SERVER_IP, SERVER_PORT, all_data, columns

def test_server_ip():
    assert SERVER_IP == "192.168.87.1"

def test_server_port():
    assert SERVER_PORT == 15555

def test_csv_file():
    assert CSV_FILE == "stats.csv"

def test_base_dir():
    assert BASE_DIR == Path(__file__).parent

def test_read_csv():
    import pandas as pd
    df = pd.read_csv(CSV_FILE)
    assert isinstance(df, pd.DataFrame)

def test_write_csv():
    import pandas as pd
    df = pd.DataFrame(all_data, columns=columns)
    df.to_csv(CSV_FILE, index=False)
    assert Path(CSV_FILE).exists()

def test_all_data():
    assert isinstance(all_data, list)
    assert all_data == []

def test_columns():
    assert columns == None