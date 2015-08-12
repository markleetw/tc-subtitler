#ZH-TW Subtitle Downloader
此程式可能透過 [射手網](http://www.shooter.cn/) 的 API 下載電影的中文字幕，並轉換成繁體中文。

獲取最新的Python版本：[http://www.python.org/getit/](https://www.python.org/getit/)

###安裝:
使用前，請先執行專案內的 install_lib ( windows 執行 bat, Linux 或 Mac 執行 sh )

###用法:
修改 subtitle_downloader.py 內的 dir_path 指定目標資料夾，程式將會去抓取此目錄下及其子目錄下所有影片檔的字幕，並將字幕轉換為繁體中文，並保留簡體中文字幕檔，因為很不幸地，有時候原始檔編碼本身就有問題，導致轉檔後可能產生不可修復的字幕檔，所以備份原始的簡體字幕檔，讓使用者自行決定該如何處理。

###舉例：
資料夾底下有影片 「The.Avengers.2012.1080p.mp4」，執行過後資料夾會出現三份轉換過的繁體版字幕「The.Avengers.2012.1080p-0.zh.srt」、「The.Avengers.2012.1080p-1.zh.srt」、「The.Avengers.2012.1080p-2.zh.srt」 和三份簡體版備份字幕、「The.Avengers.2012.1080p-0.zh.bak.srt」、「The.Avengers.2012.1080p-1.zh.bak.srt」、「The.Avengers.2012.1080p-2.zh.bak.srt」

###Future Work：
因應射手字幕資料量逐漸減少，有機會會再增加其他字幕來源，希望其他字幕網站未來能夠提供 API 方便開發，否則就得用土法煉鋼爬蟲大法了。

###感謝:
感謝 [ttchin](https://github.com/ttchin/shooter-subtitle-downloader) 以及 [chinese-autoconvert](https://code.google.com/p/chinese-autoconvert/)
