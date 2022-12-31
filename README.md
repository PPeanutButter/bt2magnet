# bt2magnet
> 将bt文件转化为磁力链接, 该仓库是[花生酱的家庭流媒体](https://github.com/PPeanutButter/HomeMediaServer)的组成部分。

# usage
```shell
usage: bt2magnet.py [-h] param

positional arguments:
  param       传入一个torrent的url、一个包含torrent文件的文件夹或者一个torrent文件

optional arguments:
  -h, --help  show this help message and exit
```
# sample
```shell
// 文件夹
> bt2magnet ./
magnet:?xt=urn:btih:L43HY7TCCXURO2V6U47QOQPNRAFPS4LD
magnet:?xt=urn:btih:AULDOGL7JYDPQXREI73PM5OR53RSIYKU
magnet:?xt=urn:btih:5II7YGFGFO2UBDU4Q5O2YYEHTMZPM2SF
// url
> bt2magnet http://btbtt11.com/attach-download-fid-950-aid-5465371.htm
magnet:?xt=urn:btih:YIPTGAPCED7APSBFHHTPHY4WXU7B2OAE
// bt文件
> bt2magnet "Resident.Alien.S02E01.1080p.WEB.H264-CAKES[rarbg].torrent"
magnet:?xt=urn:btih:L43HY7TCCXURO2V6U47QOQPNRAFPS4LD
```
# build
> 编译以省去`python bt2magnet.py`

终端运行`pyinstaller -F .\bt2magnet.py`, 并将可执行文件添加到环境变量，或者下载编译好的`for Windows 64`和`for raspberry arm64 linux`
