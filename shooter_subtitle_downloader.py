# -*- coding: utf-8 -*-
import os
import glob
import hashlib
import math
import urllib2
import re

extensions = (".avi", ".mp4", ".mkv", ".mpg", ".mpeg", ".mov", ".rm", ".vob", ".wmv", ".flv", ".3gp")
dir_path = '/var/lib/transmission/Downloads/'


# dir_path = 'D:\\video\\movies\\test'


def get_hash(name):
    hash_val = list()
    with open(name, 'rb') as f:
        e = 4096
        f.seek(0, os.SEEK_END)
        size = f.tell()

        # first 4k
        start = min(size, 4096)
        end = min(start + e, size)
        f.seek(int(start))
        data = f.read(int(end - start))
        digest = hashlib.md5(data).hexdigest()
        hash_val.append(digest)

        # second 4k
        start = math.floor(size / 3 * 2)
        end = min(start + e, size)
        f.seek(int(start))
        data = f.read(int(end - start))
        digest = hashlib.md5(data).hexdigest()
        hash_val.append(digest)

        # third 4k
        start = math.floor(size / 3)
        end = min(start + e, size)
        f.seek(int(start))
        data = f.read(int(end - start))
        digest = hashlib.md5(data).hexdigest()
        hash_val.append(digest)

        # fourth 4k
        start = max(0, size - 8192)
        end = min(start + e, size)
        f.seek(int(start))
        data = f.read(int(end - start))
        digest = hashlib.md5(data).hexdigest()
        hash_val.append(digest)

    return hash_val


def sub_downloader(path):
    hash_val = get_hash(path)
    name = path.split('\\')[-1].split('/')[-1]  # 為了安全性著想不傳送完整路徑，只給檔名
    replace = extensions
    for content in replace:
        path = path.replace(content, "")
    headers = {'User-Agent': 'SubDB/1.0 (shooter-subtitle-downloader/1.0; '
                             'http://github.com/marksylee/shooter-subtitle-downloader)'}

    # step 1. find subtitle list
    filehash = hash_val[0] + '%3B' + hash_val[1] + '%3B' + hash_val[2] + '%3B' + hash_val[3]
    url = 'http://www.shooter.cn/api/subapi.php?filehash=' + filehash + '&format=json&pathinfo=' + name + '&lang=Chn'
    print 'get list url:', url
    req = urllib2.Request(url, '', headers)
    done = False
    response = None
    while not done:
        try:
            response = urllib2.urlopen(req).read()
            done = True
        except:
            print 'shooter api timeout, retry...'
            done = False

    # 找不到字幕，未來希望能夠加入其他網站的搜尋功能
    # http://www.opensubtitles.org/zh
    # http://www.zimuku.net/
    if response == '\xff' or response == '0xff(-1)':
        return None

    # step 2. get first 5 subtitle from subtitle list
    for index, res in enumerate(eval(response)):
        if index < 5:  # 經過測試，射手 api 似乎只會回傳三筆字幕檔，但還是以防萬一限制一下上限
            subtitle = res['Files']
            url = subtitle[0]['Link'].replace('\u0026', '&')
            print 'download file url:', url
            req = urllib2.Request(url, '', headers)
            done = False
            while not done:
                try:
                    response = urllib2.urlopen(req).read()
                    done = True
                except:
                    done = False
        with open(path + '-' + str(index) + ".zh.srt", "wb") as subtitle_file:
            subtitle_file.write(response)


# 重新命名資料夾，避免出現[]及()，glob會抓不到內容
for filename in os.listdir(dir_path):
    if re.match('^[A-Za-z0-9_.]+$', filename) is None:  # 只可包含英文大小寫及dot
        new_filename = re.sub('[^0-9a-zA-Z]+', '.', filename)
        if new_filename[-1] == '.':  # 有可能以 '.' 為結尾，修改它
            new_filename = new_filename[:-1]
        print 'rename from', filename, 'to', new_filename
        os.rename(os.path.join(dir_path, filename), os.path.join(dir_path, new_filename))

for root, subFolders, files in os.walk(dir_path):
    print 'now in folder:', root
    print 'num of srt files:', len(glob.glob(os.path.join(root, '*.srt')))
    # 檢查同資料夾底下是否已存在超過一個字幕檔 (因為可能有原生字幕檔)
    # 如果有超過一個字幕檔表示已經下載過，就可以直接跳過
    if len(glob.glob(os.path.join(root, '*.srt'))) <= 1:
        for ext in extensions:
            for f in glob.glob(os.path.join(root, '*' + ext)):
                print 'video file:', f
                sub_downloader(f)
