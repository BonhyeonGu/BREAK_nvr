from flask import Blueprint, session, redirect, url_for, render_template
import os
schedule = Blueprint("monitor", __name__, url_prefix="/monitor")

@schedule.route("/")
def a():
	print("a")

#모니터 추가
@schedule.route("/add", methods=['POST'])
def monitorAdd():
	os.popen('mkdir ./monitors/a')
	cmd = ''
	cmd += './ffmpeg -hwaccel cuda -rtsp_transport tcp -i'
	cmd += '"rtsp://user01:1234@10.3.129.74:12100/live.stream"'
	cmd += '-fflags flush_packets -max_delay 5 -flags -global_header -hls_time 60 -hls_list_size 10 -hls_delete_threshold 1 -hls_flags delete_segments -c:v h264_nvenc -y'
	cmd += 'monitors/a/index.m3u8'
	
    #os.popen(cmd)
	return render_template('file_setting.html', names=names, dates_edit=dates_edit, use=u.outDirByte(location))

#모니터 삭제
@schedule.route("/edit", methods=['POST'])
def b():
	print("b")