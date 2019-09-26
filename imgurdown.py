from imgur_downloader import *
imgurlink = input("imgur link: ")
downloader = ImgurDownloader(imgurlink)
print("This albums has {} images".format(downloader.num_images()))
downloader.save_images()
