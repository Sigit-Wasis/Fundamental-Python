# Download youtube Videos with Python

import webbrowser

url = "https://www.youtube.com/watch?v=yWlpCdoXTpY"
download = url[:12] + "ss" + url[12:]

webbrowser.open(download)