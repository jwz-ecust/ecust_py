# -*- coding: utf-8 -*-
import requests
from = requests.session()
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"}

req = r.get("http://www.ximalaya.com/29527269/album/4652398?order=desc", headers=headers)
content = req.text.encode("utf-8")

soup = BeautifulSoup(content, "html.parser")
album = soup.find(class_="album_soundlist")
 
fuck = open("cbb.sh", "w")
for i in album.find_all("li"):
    sound_id = i['sound_id']
    audio = "http://www.ximalaya.com/tracks/{}.json".format(sound_id)
    zjw = r.get(audio, headers=headers)
    audio_url = zjw.json()['play_path_32']
    name = i.text.encode("utf-8").strip()
    name = "_".join([_ for _ in name.split(" ")[:-2] if _]).strip()
    line = "wget '{}' -SO '{}.{}'\n".format(audio_url, name, "m4a")
    fuck.write(line)

f.close()



























































































































































