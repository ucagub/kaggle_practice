import requests

data = {'battery_power': 842.0, 'blue': 0.0, 'clock_speed': 2.2, 'dual_sim': 0.0, 'fc': 1.0, 'four_g': 0.0, 'int_memory': 7.0, 'm_dep': 0.6, 'mobile_wt': 188.0, 'n_cores': 2.0, 'pc': 2.0, 'px_height': 20.0, 'px_width': 756.0, 'ram': 2549.0, 'sc_h': 9.0, 'sc_w': 7.0, 'talk_time': 19.0, 'three_g': 0.0, 'touch_screen': 0.0, 'wifi': 1.0}

response = requests.post(url='http://127.0.0.1:5000/predict', json=data)
print(response.json())