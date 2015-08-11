__author__ = 'marklee'

import os
import glob

dir_path = 'C:\\Users\\marklee\\Downloads\\test'
extensions = ['.ass', '.srt']

for root, subFolders, files in os.walk(dir_path):
    for ext in extensions:
        for f in glob.glob(os.path.join(root, '*' + ext)):
            print 'subtitle file:', f
            os.system('python ' + os.path.dirname(os.path.abspath(__file__)) +
                      '/g2butf8/g2butf8.py ' + os.path.join(root, f))
