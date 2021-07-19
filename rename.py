import os

os.chdir('C:/Users/zeus/Desktop/Python/automation/videos')

for i in os.listdir():
	f_name, f_ext = os.path.splitext(i)
	f_title, f_playlist, f_num = f_name.split('-')

	f_title = f_title.strip()
	f_playlist = f_playlist.strip()
	f_num = f_num.strip()[1:].zfill(2)
	
	new_name = f"{f_num}-{f_title}-{f_playlist}{f_ext}"

	os.rename(i,new_name )


# print(os.getcwd())

# Earth - Our Solar System - #4.pdf

# 4-Earth-Our Solar System.pdf
