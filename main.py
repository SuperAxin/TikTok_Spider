from Lizard import Catch


# 手動進行機器人驗證後按下Enter即可下載影片

if __name__ == '__main__':
    Creator = 'wdz_pet' # 可自行輸入創作者名稱
    Downloader = Catch(Creator)
    Downloader.FireFox()
    Downloader.VideoDownload()
