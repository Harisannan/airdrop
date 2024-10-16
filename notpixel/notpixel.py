import random
import time
import os
import requests
import json
import cv2
import numpy as np
from PIL import Image

init_data = input('masukkan init data ==>> ')
manual_template = input('bawa template sendiri mas ? [y/n]==>> ')



headers = {
  'Accept': 'application/json, text/plain, */*',
  'Accept-Encoding': 'gzip, deflate, br, zstd',
  'Accept-Language': 'en-US,en;q=0.9',
  'Authorization': init_data,
  'Origin': 'https://app.notpx.app',
  'Priority': 'u=1, i',
  'Referer': 'https://app.notpx.app/',
  'Sec-Ch-Ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
  'Sec-Ch-Ua-Mobile': '?0',
  'Sec-Ch-Ua-Platform': '"Windows"',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-site',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
}



def select_template(headers):


  if manual_template == 'y' :
    tmplt_id = int(input('masukkan id template ==>> '))
    template_id = tmplt_id
    template_url = f'https://static.notpx.app/templates/{tmplt_id}.png'
  else :
    list_number = [12,24,36,48,60,72,84,96]
    url = f'https://notpx.app/api/v1/image/template/list?limit=12&offset={random.choice(list_number)}'
    response = requests.get(url, headers=headers).json()
    random_pick_number = random.randint(0,11)
    template_id = pick_random_template = response[random_pick_number]['templateId']
    template_url = pick_random_template = response[random_pick_number]['url']


  select_template_url = f'https://notpx.app/api/v1/image/template/subscribe/{template_id}'
  select_template = requests.put(select_template_url, headers=headers)



  selected_template_url = select_template_url = f'https://notpx.app/api/v1/image/template/{template_id}'
  response2 = requests.get(select_template_url, headers=headers).json()
  x_position = response2['x']
  y_position = response2['y']


  return template_id, template_url, x_position, y_position

def rgb_to_hex(rgb):
  """Converts RGB values (tuple or list of 3 integers) to a hex string."""
  if len(rgb) != 3:
    raise ValueError("Input must be a tuple or list of 3 integers (RGB values).")
  return '#%02x%02x%02x' % tuple(rgb)




id, template_image, x, y = select_template(headers)

print(f'''
id : {id}
image_url : {template_image}
x : {x}
y : {y}
''')


while True :
  random_x = random.randint(x, x+127)
  random_y = random.randint(y, y+127)

  pixel_target = int(f'{random_y}{random_x+1}')




  response = requests.get(template_image, stream=True)
  img_pil = Image.open(response.raw)
  img = np.array(img_pil)

  # Akses pixel dengan koordinat yang ditentukan
  pixel_value = img[random_x-x, random_y-y]
  pixel_value = [pixel_value[0], pixel_value[1], pixel_value[2]]
  hex_color = rgb_to_hex(pixel_value).upper()


  url_cek_color_target = f'https://notpx.app/api/v1/image/get/{pixel_target}'
  get_color_target = requests.get(url_cek_color_target, headers=headers).json()
  color_target = get_color_target['pixel']['color']

  print(f''''
  koordinat : {random_x},{random_y}
  koordinat gambar : {random_x-x},{random_y-y}
  warna target : {color_target}
  warna seharusnya : {hex_color}
  
  ''')
  if color_target == hex_color:
    print('ini sama')
    os.system('cls')
  else :
    print(f"ndak sama mas, wong ini warnanya {color_target} sedangkan ini warna aslinya {hex_color}")


    start_url = 'https://notpx.app/api/v1/repaint/start'
    payload = {
      'newColor' : hex_color,
      'pixelId' : pixel_target
    }

    paint_response = requests.post(start_url, headers=headers, json=payload)
    if 'insufficient' in paint_response.text :
      requests.get('https://notpx.app/api/v1/mining/claim', headers=headers)
      requests.get('https://notpx.app/api/v1/mining/boost/check/reChargeSpeed', headers=headers)
      requests.get('https://notpx.app/api/v1/mining/claim', headers=headers)
    else :
      print(f"balance : {paint_response.json()['balance']}")
      time.sleep(3)