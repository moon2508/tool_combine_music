from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/merge', methods=['POST'])
def merge_music():
    music_files = request.form.getlist('music_files')
    output_file = 'merged.mp3'
    merge_command = f'ffmpeg -f concat -i list.txt -c copy {output_file}'

    with open('list.txt', 'w') as f:
        for file in music_files:
            f.write(f"file '{file}'\n")

    subprocess.call(merge_command, shell=True)

    return f"Merge complete! <a href='{output_file}'>Download</a>"

if __name__ == '__main__':
    app.run(debug=True)