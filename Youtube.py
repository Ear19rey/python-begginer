#! C:\Users\gameb\AppData\Local\Programs\Python\Python38\Python

from pytube import YouTube
import argparse

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('url',help='指定YOUTUBE網址')
    parser.add_argument('-sd',action='store_true',help='480p')
    parser.add_argument('-hd',action='store_true',help='720p')
    parser.add_argument('-fhd',action='store_true',help='1080p')
    parser.add_argument('-a',action='store_true',help='僅下載聲音')

    args = parser.parse_args()
    global yt
    yt = YouTube(args.url,on_progress_callback=progress)

    try:
        download_video(yt,args)
    except IndexError:
        print('只有以下解析度')
        for i,res in enumerate(video_res(yt)):
            print(f'{i+1}){res}')

def progress(chunk, file_handle, bytes_remaining):
    contentSize = yt.streams.first().filesize
    size = contentSize - bytes_remaining

    print('\r' + '[Download progress]:[%s%s]%.2f%%;' % (
        '█' * int(size*20/contentSize), ' '*(20-int(size*20/contentSize)), float(size/contentSize*100)), end='')

def download_video(yt, args):
    filter = yt.streams.filter
    if args.sd:
        target=filter(type='video',res='480p')[0]
    elif args.hd:
        target=filter(type='video',res='720p')[0]
    elif args.fhd:
        target=filter(type='video',res='1080p')[0]
    elif args.a:
        target=filter(type='audio')[0]
    else:
        target=filter(type='video')[0]

    target.download(output_path=pyTube_folder())

def pyTube_folder():
    return 'D:\python project\程式設計\PYTUBE_YOUTUBE'

def video_res(yt):
    res_set = set()
    video_list = yt.streams.filter(type='video')

    for v in video_list:
        res_set.add(v.resolution)
    return sorted(res_set, reverse=True, key=lambda s:int(s[:-1]))


if __name__=="__main__":
    main()
