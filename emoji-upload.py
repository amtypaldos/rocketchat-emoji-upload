from pymongo import MongoClient
import gridfs
import time
import datetime
from bson.json_util import loads
import json
import yaml
import urllib2

emoji_yaml_url = raw_input("URL for YAML file?")
mongo_server = raw_input("MongoDB URI for your rocketchat deployment?")

response = urllib2.urlopen(emoji_yaml_url)
emoji_yaml = yaml.load(response.read())

# load YAML into parsable list
emojis = emoji_yaml['emojis']



# create timestamp for entry into list for DB
ts = time.time()
ts = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%dT%H:%M:%SZ')


#make connection to mongo
client = MongoClient(mongo_server)
db = client.rocketchat


# gridfs file uploader function
def gfs_fileuploader(name, content, url):
    custom_emoji = gridfs.GridFS(db, 'custom_emoji')
    opener = urllib2.build_opener()
    # change user agent to wget, for some reason CDN does not like urillib2
    opener.addheaders = [('User-Agent', 'Wget/1.19.1 (darwin16.6.0)')]
    emoji_resp = opener.open(url)
    emoji_file = emoji_resp.read()
    with custom_emoji.new_file(
        _id=name,
        filename=name  ,
        content_type=content,
        alias=None) as fp:
        fp.write(emoji_file)
    return;


# download image files and make Array for DB entries
# declare array
new_emojis = []
for emoji in emojis:
    try:
        url = emoji['src']
        filename = url.split('/')
        file = filename[len(filename)-1]
        file = file.split('.')
        name = emoji['name']
        ext = file[1]
        new_file = name + '.' + ext
        print new_file
        print emoji['src']
        gfs_fileuploader(new_file, 'image/' + ext, emoji['src'])
        item = {
                "name": name,
                "aliases": [],
                "extension": ext,
                "_updatedAt": {
                    "$date": ts }
                }
        item = json.dumps(item)
        item = loads(item)
        new_emojis.append(item)
    except:
        print "error getting image"
        pass



emoji_db = db.rocketchat_custom_emoji
result = emoji_db.insert_many(new_emojis)
