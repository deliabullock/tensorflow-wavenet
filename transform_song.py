from pydub import AudioSegment
from generate import main
import time

second_unit = 1000.0
output_song_path = 'transform/generated.wav'
seed_song_path = 'transform/seed.wav'
new_song_path = 'transform/in_progress.wav'
input_song_path = 'transform/input.wav'
# 10 seconds for wavenet = 160000

def transform_song(input_song):
	output_song = None
	song = AudioSegment.from_file(input_song, format="wav")
	#leng = len(song)
	#last_mark = 12.5*second_unit#0
	#for i in range(1):#while last_mark < leng - 500:
#		next_mark = min(leng, last_mark + 500)
#		print(next_mark)
#		print(last_mark)
	song.export(seed_song_path, format="wav")
#		
	main(seed_song_path, new_song_path, 2, True)
		
	new_song = AudioSegment.from_file(new_song_path, format="wav")
		#if output_song == None:
	#		output_song = new_clip
#		else:
#			output_song = output_song + new_clip
#		last_mark = next_mark
#		print('yay!')
#		time.sleep(3)
		
		
	
	#output_song = new_song.fade_out()
	new_song.export(output_song_path, format="wav")
	print('DONE')
		
		
transform_song(input_song_path)
