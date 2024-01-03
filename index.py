import subprocess
from datetime import datetime, timedelta

# Hàm để thực thi lệnh FFmpeg
def run_ffmpeg_command(command):
    subprocess.call(command, shell=True)

# Hàm để ghép các bài nhạc lại với nhau và tạo file MP3 và file TXT
def concatenate_music_files(music_files, output_file):
    time_run = datetime.strptime('00:00:00', '%H:%M:%S')
    with open('list.txt', 'w') as f:
        for file in music_files:
            duration = get_audio_duration(file)
            formatted_time = time_run.strftime('%H:%M:%S')
            f.write(f"{formatted_time} - {file}\n")
            time_run += timedelta(seconds=duration)
            
    command = f'ffmpeg -f concat -i list.txt -c copy {output_file}'
    run_ffmpeg_command(command)

# Hàm để lấy thời lượng của file âm thanh
def get_audio_duration(audio_file):
    try:
        command = f'ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "{audio_file}"'
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT).decode('utf-8')
        duration = float(output)
        return duration
    except (subprocess.CalledProcessError, ValueError):
        print(f"Failed to retrieve duration for {audio_file}. Defaulting to 0.")
        return 0

# Ví dụ sử dụng
music_files = ['test1.mp3', 'test2.mp3', 'test3.mp3']
output_file = 'merged.mp3'

# Ghép các bài nhạc và tạo file MP3 và file TXT
concatenate_music_files(music_files, output_file)