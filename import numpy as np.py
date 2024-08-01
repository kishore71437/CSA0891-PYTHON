import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sqlalchemy as sa

# Assuming your imports and database connection setup are correct as in your original code

url = "https://<your-instance>.azure.cratedb.net:4200"
user = "<your-username>"
password = "<your-password>"
db_name = "<your-db-name>"
engine = sa.create_engine(f"crate://{user}:{password}@{url}/{db_name}")

query = """
SELECT
    DATE_BIN('5 min'::INTERVAL, "timestamp", 0) AS timestamp,
    AVG(sensor_1) + 2 * STDDEV(sensor_1) AS upper_bound,
    AVG(sensor_1) - 2 * STDDEV(sensor_1) AS lower_bound
FROM vehicle_sensor_data
GROUP BY timestamp
ORDER BY timestamp ASC
"""

# Fetching data into a DataFrame
data = pd.read_sql(query, engine)

# Assuming 'timestamp' is a column in your DataFrame
# Converting 'timestamp' to datetime if it's not already
data['timestamp'] = pd.to_datetime(data['timestamp'])

# Plotting
sns.set(style="whitegrid")
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(data['timestamp'], data['sensor_1'], label="sensor_1")
ax.fill_between(data['timestamp'], data['upper_bound'], data['lower_bound'], alpha=0.2, color="gray")
ax.axhline(y=data.loc[0, 'lower_bound'], linestyle="--", label="lower_bound")
ax.axhline(y=data.loc[0, 'upper_bound'], linestyle="--", label="upper_bound")
ax.set_ylabel("Sensor value")
ax.set_xlabel("Time")
ax.legend()
plt.show()
