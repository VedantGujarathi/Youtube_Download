from flask import Flask, render_template, request
from pytube import YouTube

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/download', methods=['POST'])
def download():
    if request.method == 'POST':
        video_url = request.form['url']
        resolution = request.form['resolution']
        download_video(video_url, resolution)
        return render_template('home.html', success=True)


def download_video(url, resolution='1080'):
    yt = YouTube(url)
    stream = yt.streams.filter(res=f"{resolution}p").first()
    stream.download(output_path='downloads')


if __name__ == '__main__':
    app.run(debug=True)
