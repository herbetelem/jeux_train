# import winsound
# frequency = 2500  # Set Frequency To 2500 Hertz
# frequency2 = 5000  # Set Frequency To 2500 Hertz
# duration = 1  # Set Duration To 1000 ms == 1 second
# winsound.Beep(frequency2, 50)
# winsound.Beep(frequency, 100)
# winsound.Beep(frequency2, 50)
# winsound.Beep(frequency, 100)
# winsound.Beep(frequency2, 50)
# winsound.Beep(frequency, 100)
# winsound.Beep(frequency2, 50)
# winsound.Beep(frequency, 100)


import platform
try:
    import winsound
    beep = winsound.Beep
except ImportError:
    def beep(f, d):
        s = 8000
        hp = int(s/f/2)
        b = chr(255)*hp+chr(0)*hp
        b *= int(d*f)
        a = file('/dev/audio', 'wb')
        a.write(b)
        a.close()    

c = [
	(880, 700),
	(587, 1000),
	(698, 500),
	(880, 500),
	(587, 1000),
	(698, 500),
	(880, 250),
	(1046, 250),
	(988, 500),
	(784, 500),
	(699, 230),
	(784, 250),
	(880, 500),
	(587, 500),
	(523, 250),
	(659, 250),
	(587, 750)
]

s = c + c

for f, d in s:
	beep(f, d)