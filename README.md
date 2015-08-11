#ZH-TW Subtitle Downloader
此程式可能透過 [射手網](http://www.shooter.cn/) 的 API 下載電影的中文字幕，並轉換成繁體中文。

獲取最新的Python版本：[http://www.python.org/getit/](https://www.python.org/getit/)

###安裝:
使用前，請先執行專案內的 install_lib ( windows 執行 bat, Linux 或 Mac 執行 sh )

###用法:
指定目標資料夾，程式將會去抓取此目錄下及其子目錄下所有影片檔的字幕，並將字幕轉換為繁體中文，並保留簡體中文字幕檔
(因為很不幸地，有時候原始檔編碼本身就有問題，導致轉檔後可能產生不可修復的字幕檔，所以備份原始的簡體字幕檔，讓使用者自行決定該如何處理)

###感謝:
感謝[ttchin](https://github.com/ttchin/shooter-subtitle-downloader) 以及 [chinese-autoconvert](https://code.google.com/p/chinese-autoconvert/)
