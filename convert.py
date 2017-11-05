import os
import glob
from pydub import AudioSegment

i = 0
extension = '*.mp3'
for video in glob.glob(extension):
	mp3_filename = '../wav_files/' + os.path.splitext(os.path.basename(video))[0] + '.wav'
	if (i%1000) == 0:
		print (os.path.splitext(os.path.basename(video))[0])
	i+=1
	AudioSegment.from_file(video).export(mp3_filename, format='wav')	
