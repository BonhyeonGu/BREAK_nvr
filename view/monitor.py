from flask import Blueprint, session, redirect, url_for, render_template
import os
import subprocess

monitor = Blueprint("monitor", __name__, url_prefix="/monitor")

@monitor.route("/")
def a():
	print("a")

#모니터 추가
@monitor.route("/add")
def monitorAdd():
	#os.popen('mkdir ./monitors/a')
	cmd = ''
	cmd += 'ffmpeg -hwaccel cuda -rtsp_transport tcp -i '
	cmd += '"rtsp://user01:1234@10.3.129.74:12100/live.stream" '
	cmd += '-fflags flush_packets -max_delay 5 -flags -global_header -hls_time 60 -hls_list_size 10 -hls_delete_threshold 1 -hls_flags delete_segments -c:v copy -y '
	cmd += '/var/www/html/index.m3u8 '
	proc = subprocess.Popen(cmd, shell=True)
	return redirect(url_for('index'))
