import os
#import glob
from pydub import AudioSegment
import sys
import csv
from csv_indices_to_global_conditioning_names import INDICES_to_GC_NAME
import pickle

#### get passed in directory name
### go through each line of csv
### pass line to get_global_category_ids
### pass to save_as_wav

gc_id_utter_num = pickle.load(open('gc_id_utter_num.pkl')) 
GC_NAME_to_GC_ID = pickle.load(open('groups_dict.pkl'))

curr_file = sys.argv[1]
print(sys.argv[1])

csv_filename = "annotations_final.csv"

def get_gc_filenames(description_list):
	gc_ids = get_gc_ids(description_list)
	mp3_filenames = []
	for gc_id in gc_ids:
		utter_num = gc_id_utter_num[gc_id]
		gc_id_utter_num[gc_id] = gc_id_utter_num[gc_id] + 1
		filename = './wav_files/p' + str(gc_id) + '_' + str(utter_num) + '.wav'
		mp3_filenames.append(filename)
	return mp3_filenames

def get_gc_ids(description_list):
	gc_ids_out = []
	#print(description_list)
	indices = [i for i, x in enumerate(description_list) if x == '1']	
	#print(indices)
	gc_ids_seen = set([])
	for ind in indices:
		gc_name = INDICES_to_GC_NAME[ind]
		if gc_name not in GC_NAME_to_GC_ID:
			continue
		gc_id = GC_NAME_to_GC_ID[gc_name]
		if gc_id not in gc_ids_seen:
			gc_ids_out.append(gc_id)
			gc_ids_seen.add(gc_id)
	return gc_ids_out 

def save_as_wavs(video, mp3_filenames):
	for filename in mp3_filenames:
		AudioSegment.from_file(video).export(filename, format='wav')

with open(csv_filename, 'rb') as csvfile:
	reader = csv.reader(csvfile, delimiter='\t', quotechar='\"')
	i = 0
	for row in reader:
		if i == 0:
			i+= 1
			continue
		i+= 1
		path = row[-1]
		if path[0] != curr_file:
			continue
		if(i % 1000 == 0):
			print(path)
		filenames = get_gc_filenames(row[1:-1])
		save_as_wavs(path, filenames)
print(gc_id_utter_num)
pickle.dump(gc_id_utter_num, open('gc_id_utter_num.pkl', 'wb'))

'''
i = 0
extension = '*.mp3'
for video in glob.glob(extension):
	mp3_filename = '../wav_files/' + os.path.splitext(os.path.basename(video))[0] + '.wav'
	if (i%1000) == 0:
		print (os.path.splitext(os.path.basename(video))[0])
	i+=1
	AudioSegment.from_file(video).export(mp3_filename, format='wav')	
'''
