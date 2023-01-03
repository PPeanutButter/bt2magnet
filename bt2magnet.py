import os
import sys


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


def print_copy(magnet):
    print(magnet)
    results.append(magnet)


def copy():
    import clipboard
    clipboard.copy(os.linesep.join(results))


results = []
if __name__ == '__main__':
    param = sys.argv
    if len(param) < 2:
        param = "./"
    else:
        param = param[1]
    if str(param).startswith('http'):
        import requests
        r = requests.request(method='GET', url=param)
        with open('.bt_cache', 'wb') as f:
            f.write(r.content)
        print_copy(bt2magnet('.bt_cache', get_file_name(param, r.headers)))
    elif os.path.isdir(param):
        parent = param
        for name in os.listdir(parent):
            if name.endswith('.torrent') or name.endswith('.TORRENT'):
                print_copy(bt2magnet(os.path.join(parent, name), name))
    elif os.path.isfile(param):
        print_copy(bt2magnet(param, os.path.basename(param)))
    copy()
