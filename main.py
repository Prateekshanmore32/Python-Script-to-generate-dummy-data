import pandas as pd
import Temperature
import  Time

Time = Time.generate_time()
Temperature = Temperature.genetate_temp()

data = {
    "Time": Time,
    "Temperature": Temperature
}

df = pd.DataFrame(data)
dd = df.to_csv('my_dummy_data.csv',index=False)