import os
import argparse


def bt2magnet(torrent_file, file_name):
    import bencodepy
    import hashlib
    import base64
    if file_name and file_name[0] == '"' and file_name[-1] == '"':
        file_name = file_name[1:-1]
    with open(torrent_file, 'rb') as f:
        b32hash = base64.b32encode(hashlib.sha1(bencodepy.encode(bencodepy.decode(f.read())[b'info'])).digest()).decode(
            "utf-8")
        return f'magnet:?xt=urn:btih:{b32hash}&file={file_name}'


def get_file_name(url, headers):
    filename = ''
    from urllib.parse import unquote
    if 'Content-Disposition' in headers and headers['Content-Disposition']:
        disposition_split = headers['Content-Disposition'].split(';')
        if len(disposition_split) > 1:
            if disposition_split[1].strip().lower().startswith('filename='):
                file_name = disposition_split[1].split('=')
                if len(file_name) > 1:
                    filename = unquote(file_name[1])
    if not filename and os.path.basename(url):
        filename = os.path.basename(url).split("?")[0]
    if not filename:
        import time
        return time.time()
    return filename


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('param', type=str, help='传入一个torrent的url、一个包含torrent文件的文件夹或者一个torrent文件')
    args = parser.parse_args()
    if str(args.param).startswith('http'):
        import requests
        r = requests.request(method='GET', url=args.param)
        with open('.bt_cache', 'wb') as f:
            f.write(r.content)
        print(bt2magnet('.bt_cache', get_file_name(args.param, r.headers)))
    elif os.path.isdir(args.param):
        parent = args.param
        for name in os.listdir(parent):
            if name.endswith('.torrent') or name.endswith('.TORRENT'):
                print(bt2magnet(os.path.join(parent, name), name))
    elif os.path.isfile(args.param):
        print(bt2magnet(args.param, os.path.basename(args.param)))
