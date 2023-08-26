from lib6300.audio import wav_read, wav_write, wav_file_play
from math import cos, pi, ceil, sin, e
import numpy as np
import matplotlib.pyplot as plt


# the example tune for this lab, with each note encoded as a pair of
# (frequency, duration) with frequency in Hz and duration in seconds
tune = [
    (392.0, 0.6),
    (523.26, 0.45),
    (392.0, 0.15),
    (440.0, 0.3),
    (349.22, 0.3),
    (293.66, 0.6),
    (392.0 , 0.45),
    (329.62, 0.15),
    (261.62, 0.3),
    (329.62, 0.3),
    (293.66, 1.2),
    (392.0, 0.6),
    (523.26, 0.45),
    (392.0, 0.15),
    (440.0, 0.3),
    (349.22, 0.3),
    (293.66, 0.6),
    (392.0, 0.45),
    (329.62, 0.15),
    (349.22, 0.3),
    (246.94, 0.3),
    (261.62, 1.2),
]


##########
# part a #
##########

sampling_rate = 44100  # samples/second
sine_samples = []  # empty array to hold the output samples
for frequency, duration in tune:
    # TODO: duration is in seconds.  convert it to a number of samples.
    num_samples = int(duration*sampling_rate) 
    for n in range(num_samples):
        # TODO: compute the appropriate sample value
        Omega = 2 * pi * frequency / sampling_rate
        sample_value = sin(Omega*n)
        sine_samples.append(sample_value)
# save the file to disk
#wav_write(sine_samples, sampling_rate, "sine_tune.wav")

##########
# part b #
##########

def idtfs(x, omega, numSamples):
    nlist = []
    for n in range(numSamples):
        function = 0
        for k in range(-5,5,1):
            if (k in x):
                function += (x[k]*e**(1j*omega*k*n)).real
        nlist.append(function)

    return nlist

timbre_samples = []
for frequency, duration in tune: 
    num_samples = int(duration*sampling_rate) 
    omega = 2*pi*frequency / sampling_rate
    x = {
        -1: 1j/4,
        1: -1j/4,
        2: 1/10,
        -2: 1/10,
        -4: (3/20)*e**(1j*pi/4),
         4: (3/20)*e**(-1j*pi/4),
    }
    timbre_samples.extend(idtfs(x, omega, num_samples))
wav_write(timbre_samples, sampling_rate, "sine_tunepartb5.wav")
#wav_file_play("sine_tunepartb5.wav")




##########
# part c #
##########

# example of loading a file
example_note, example_sampling_rate = wav_read("oboe_C4.wav")
xbracketn = len(example_note)
listx = [1,2,3,4,5,6,7,8,9,10]
listyoboe=[]
for k in range(1,11,1):
    analysis = 0
    for n in range(example_sampling_rate):
        analysis += example_note[n]*e**(-1j*2*pi*n*k/example_sampling_rate)
    analysis = analysis/example_sampling_rate
    listyoboe.append(abs(analysis))
plt.plot(listx,listyoboe,'o', color='blue')
plt.show()

listxchange = []
example_note, example_sampling_rate = wav_read("sax_C4.wav")
listysax=[]
for k in range(1,11,1):
    analysis = 0
    for n in range(example_sampling_rate):
        analysis += example_note[n]*e**(-1j*2*pi*n*k/example_sampling_rate)
    analysis = analysis/example_sampling_rate
    listysax.append(abs(analysis))
plt.plot(listx,listysax,'o', color='black')
plt.show()


##########
# part d #
##########

def idtfs2(x, omega, numSamples):
    nlist = []
    for n in range(numSamples):
        function = 0
        for k in range(-9,10,1):
            if (k in x):
                function += (x[k]*e**(1j*omega*k*n)).real
        nlist.append(function)
    return nlist


example_note, example_sampling_rate = wav_read("trumpet_C4.wav")
bigN = example_sampling_rate/261.6

listofkstrumpet = {}
for k in range(1,10,1):
    analysis = 0
    for n in range(bigN):
        analysis += example_note[n]*e**(-1j*2*pi*n*k/bigN)
    analysis = analysis/bigN
    listofkstrumpet[k] = analysis

for k in range (1, 10, 1):
    listofkstrumpet[-k] = np.conjugate(listofkstrumpet[k])

timbre_samples = []
duration = 1
num_samples = int(duration*example_sampling_rate) 
omega = 2*pi / bigN
timbre_samples.extend(idtfs2(listofkstrumpet, omega, num_samples))
wav_write(timbre_samples, example_sampling_rate, "trumpettryc41.wav")
wav_file_play("trumpettryc41.wav")


##########
# part e #
##########
