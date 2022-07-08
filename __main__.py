import asyncio,tts,os,video,requests
from distutils.log import error
from tkinter.tix import Tree
import imp
from scraper import scrape
from utils import config

async def main():
    # Fetching posts from r/AskReddit
    headers = { 'user-agent':'py-reddit-scraping:0:1.0 (by u/ur_name)' }
    posts = requests.get('https://www.reddit.com/r/AskReddit/hot.json?t=day&limit=30', headers=headers).json()['data']['children']
    for post in posts:
        try:
            list1 = []
            list = []
            a = False
            num = 0

            # Avoid getting banned, no NSFW posts
            if 'nsfw' in post['data']['whitelist_status']:
                continue
            url = post['data']['url']
            name = url.split('/')[-2]
            name = name.replace("_", " ")
            print(f"⏱ Processing post: {name}")
            with open (r"C:/Users/Erin Tomorri/Desktop/Youtube/Upload/videos.txt", "r") as f: #opens file
                contents = f.read()

                while num !=(len(contents)):
                    if contents[num] == ";": #fix this
                        list.append(num)# append all the spaces
                    num+=1

                try:
                    for y in range(len(list)):
                        x = y+1
                        list1.append(contents[list[y]+1:list[x]]) 
                except IndexError:#upon a index error it will pass 
                    pass
                f.close()

            if name in list1:
                print("❌ Video already on your tiktok or made already")
                a = True

            if a == True:
                continue

            # Clean 'temporary' files from last video
            for file in os.listdir('output'):
                os.remove(f'output/{file}')

            # Scraping the post, screenshotting, etc
            print("📸 Screenshotting post...")
            data = scrape(url)
            if not data:
                print("❌ Failed to screenshot post!")
                continue

            # Generate TTS clips for each comment
            print("\n📢 Generating voice clips...",end="",flush=True)
            voice = await tts.get_voice()
            for key in data.keys():
                print('.',end="",flush=True)
                await tts.generate(data[key], key, voice)

            # Render & Upload
            if video.render(name):
                # Upload video if rendered
                print("\n🎥 Rendering video...")
            list1.append(name)
            with open("C:/Users/Erin Tomorri/Desktop/Youtube/Upload/videos.txt", "w") as w:
                for num in range(len(list1)):
                    if num == 0:
                        w.write(";")
                    w.write(list1[num]+";")

        except Exception as e:
            try:
                print ("error")
                list1.append(name)
                with open("C:/Users/Erin Tomorri/Desktop/Youtube/Upload/videos.txt", "w") as w:
                    for num in range(len(list1)):
                        if num == 0:
                            w.write(";")
                        w.write(list1[num]+";")
            except Exception as e:
                continue
            
if __name__ == '__main__':
    while True:
        [os.mkdir(dir) for dir in ['output','render','backgrounds'] if not os.path.exists(dir)]
        asyncio.run(main())
