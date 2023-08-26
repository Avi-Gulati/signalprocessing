from lib6300.audio import wav_read, wav_write, wav_file_play
from math import cos, pi, ceil, sin, e
import numpy as np
import matplotlib.pyplot as plt



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

#analysis
def idtfs2(x, omega, numSamples):
    nlist = []
    for n in range(numSamples):
        function = 0
        for k in range(-29,30,1):
            if (k in x):
                function += (x[k]*e**(1j*omega*k*n)).real
        nlist.append(function)
    return nlist


example_note, example_sampling_rate = wav_read("trumpet_C4.wav")
bigN = int(example_sampling_rate/261.6)

lengthexample = len(example_note)

listofkstrumpet = {}
for k in range(0,30,1):
    analysis = 0
    for n in range(lengthexample//2, lengthexample//2 + bigN):
        analysis += example_note[n]*e**(-1j*2*pi*n*k/bigN)
    analysis = analysis/bigN
    listofkstrumpet[k] = analysis

for k in range (1, 30, 1):
    listofkstrumpet[-k] = listofkstrumpet[k].conjugate()

timbre_samples = []
duration = 1
num_samples = int(duration*example_sampling_rate) 
omega = 2*pi / bigN
timbre_samples.extend(idtfs2(listofkstrumpet, omega, num_samples))
wav_write(timbre_samples, example_sampling_rate, "partdtrumpet.wav")
wav_file_play("trumpettryc41jan.wav")

timbre_samples = []
for frequency, duration in tune: 
    num_samples = int(duration*example_sampling_rate) 
    omega = 2*pi*frequency / example_sampling_rate
    timbre_samples.extend(idtfs2(listofkstrumpet, omega, num_samples))
wav_write(timbre_samples, example_sampling_rate, "parte_trumpet.wav")
wav_file_play("parte_trumpet.wav")




example_note, example_sampling_rate = wav_read("oboe_C4.wav")
bigN = int(example_sampling_rate/261.6)

lengthexample = len(example_note)

listofkstrumpet = {}
for k in range(0,30,1):
    analysis = 0
    for n in range(lengthexample//2, lengthexample//2 + bigN):
        analysis += example_note[n]*e**(-1j*2*pi*n*k/bigN)
    analysis = analysis/bigN
    listofkstrumpet[k] = analysis

for k in range (1, 30, 1):
    listofkstrumpet[-k] = listofkstrumpet[k].conjugate()

timbre_samples = []
duration = 1
num_samples = int(duration*example_sampling_rate) 
omega = 2*pi / bigN
timbre_samples.extend(idtfs2(listofkstrumpet, omega, num_samples))
wav_write(timbre_samples, example_sampling_rate, "partdoboe.wav")
wav_file_play("partdoboe.wav")

timbre_samples = []
for frequency, duration in tune: 
    num_samples = int(duration*example_sampling_rate) 
    omega = 2*pi*frequency / example_sampling_rate
    timbre_samples.extend(idtfs2(listofkstrumpet, omega, num_samples))
wav_write(timbre_samples, example_sampling_rate, "parte_oboe.wav")
wav_file_play("parte_oboe.wav")


example_note, example_sampling_rate = wav_read("violin_C4.wav")
bigN = int(example_sampling_rate/261.6)

lengthexample = len(example_note)

listofkstrumpet = {}
for k in range(0,30,1):
    analysis = 0
    for n in range(lengthexample//2, lengthexample//2 + bigN):
        analysis += example_note[n]*e**(-1j*2*pi*n*k/bigN)
    analysis = analysis/bigN
    listofkstrumpet[k] = analysis

for k in range (1, 30, 1):
    listofkstrumpet[-k] = listofkstrumpet[k].conjugate()

timbre_samples = []
duration = 1
num_samples = int(duration*example_sampling_rate) 
omega = 2*pi / bigN
timbre_samples.extend(idtfs2(listofkstrumpet, omega, num_samples))
wav_write(timbre_samples, example_sampling_rate, "partdviolin.wav")
wav_file_play("partdviolin.wav")

timbre_samples = []
for frequency, duration in tune: 
    num_samples = int(duration*example_sampling_rate) 
    omega = 2*pi*frequency / example_sampling_rate
    timbre_samples.extend(idtfs2(listofkstrumpet, omega, num_samples))
wav_write(timbre_samples, example_sampling_rate, "parte_violin.wav")
wav_file_play("parte_violin.wav")

example_note, example_sampling_rate = wav_read("sax_C4.wav")
bigN = int(example_sampling_rate/261.6)

lengthexample = len(example_note)

listofkstrumpet = {}
for k in range(0,30,1):
    analysis = 0
    for n in range(lengthexample//2, lengthexample//2 + bigN):
        analysis += example_note[n]*e**(-1j*2*pi*n*k/bigN)
    analysis = analysis/bigN
    listofkstrumpet[k] = analysis

for k in range (1, 30, 1):
    listofkstrumpet[-k] = listofkstrumpet[k].conjugate()

timbre_samples = []
duration = 1
num_samples = int(duration*example_sampling_rate) 
omega = 2*pi / bigN
timbre_samples.extend(idtfs2(listofkstrumpet, omega, num_samples))
wav_write(timbre_samples, example_sampling_rate, "partdsax.wav")
wav_file_play("partdsax.wav")




timbre_samples = []
for frequency, duration in tune: 
    num_samples = int(duration*example_sampling_rate) 
    omega = 2*pi*frequency / example_sampling_rate
    timbre_samples.extend(idtfs2(listofkstrumpet, omega, num_samples))
wav_write(timbre_samples, example_sampling_rate, "parte_sax.wav")
wav_file_play("parte_sax.wav")