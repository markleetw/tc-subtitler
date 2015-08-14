__author__ = 'marklee'

import os
import glob
from g2butf8 import g2butf8

dir_path = 'C:\\Users\\marklee\\Downloads\\test'
extensions = ['.ass', '.srt']

for root, subFolders, files in os.walk(dir_path):
    for ext in extensions:
        for f in glob.glob(os.path.join(root, '*' + ext)):
            print 'subtitle file:', f
            g2butf8.translate(os.path.join(root, f))
