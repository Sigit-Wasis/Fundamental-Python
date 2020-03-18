# Download youtube Videos with Python

import webbrowser

# enter the url of the video to be downloaded
url = "https://www.youtube.com/watch?v=yWlpCdoXTpY"
download = url[:12] + "ss" + url[12:]

webbrowser.open(download)
