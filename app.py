import subprocess
from datetime import datetime,timedelta

# Hàm để thực thi lệnh FFMpeg
def run_ffmpeg_command(command):
    subprocess.call(command, shell=True)

# Hàm để cắt video
def cut_video(input_file, output_file, start_time, duration):
    command = f'ffmpeg -i {input_file} -ss {start_time} -t {duration} -c copy {output_file}'
    run_ffmpeg_command(command)

# Hàm để ghép video

def concatenate_videos(video_files, output_file, start_time):
    time_run = datetime.strptime(start_time, '%H:%M:%S')
    with open('list.txt', 'w') as f:
        for file in video_files:
            duration = get_audio_duration(file)
            formatted_time = time_run.strftime('%H:%M:%S')
            f.write(f"{formatted_time} - {file}\n")
            time_run += timedelta(seconds=duration)
            
    command = f'ffmpeg -f concat -i list.txt -c copy {output_file}'
    run_ffmpeg_command(command)

# Hàm để chỉnh sửa video
def edit_video(input_file, output_file, video_filter):
    command = f'ffmpeg -i {input_file} -vf "{video_filter}" -c:a copy {output_file}'
    run_ffmpeg_command(command)

# hàm lấy ra thời lượng file
def get_audio_duration(audio_file):
    command = f'ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 {audio_file}'
    output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT).decode('utf-8')
    duration = float(output)
    return duration
# Ví dụ sử dụng
input_file = 'test1.mp3'
output_file = 'output.mp4'
output_file1 = 'output1.mp3'

# Cắt video từ 00:10 đến 00:20 giây
# cut_video(input_file, output_file, '00:00:10', '00:00:10')

# Ghép video1.mp4 và video2.mp4
video_files = ['test2.mp3','test3.mp3']
concatenate_videos(video_files, output_file1, '00:00:00')

# # Chỉnh sửa video: thay đổi kích thước thành 1280x720 pixels
# edit_video(input_file, output_file, 'scale=1280:720')