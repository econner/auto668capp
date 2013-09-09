"""Listens in the background for input from the mic."""


# Audio Code Source
# http://stackoverflow.com/questions/
# 4160175/detect-tap-with-pyaudio-from-live-mic

import pyaudio
import struct
import math
import os

INITIAL_TAP_THRESHOLD = 0.010
FORMAT = pyaudio.paInt16
SHORT_NORMALIZE = (1.0 / 32768.0)
CHANNELS = 2
RATE = 44100
INPUT_BLOCK_TIME = 0.05
INPUT_FRAMES_PER_BLOCK = int(RATE * INPUT_BLOCK_TIME)

OVERSENSITIVE = 15.0 / INPUT_BLOCK_TIME

# if we get this many quiet blocks in a row, decrease the threshold
UNDERSENSITIVE = 120.0 / INPUT_BLOCK_TIME

# if the noise was longer than this many blocks, it's not a 'tap'
MAX_TAP_BLOCKS = 0.15 / INPUT_BLOCK_TIME


def get_rms(block):

    # RMS amplitude is defined as the square root of the
    # mean over time of the square of the amplitude.
    # so we need to convert this string of bytes into
    # a string of 16-bit samples...

    # we will get one short out for each
    # two chars in the string.
    count = len(block) / 2
    format = "%dh" % (count)
    shorts = struct.unpack(format, block)

    # iterate over the block.
    sum_squares = 0.0
    for sample in shorts:
    # sample is a signed short in +/- 32768.
    # normalize it to 1.0
        n = sample * SHORT_NORMALIZE
        sum_squares += n * n

    return math.sqrt(sum_squares / count)

pa = pyaudio.PyAudio()

# You always use this in pyaudio...
stream = pa.open(format=FORMAT,
                 channels=CHANNELS,
                 rate=RATE,
                 input=True,
                 frames_per_buffer=INPUT_FRAMES_PER_BLOCK)

tap_threshold = INITIAL_TAP_THRESHOLD

#|---- Variables for noise detector...
noisycount = MAX_TAP_BLOCKS + 1
quietcount = 0
errorcount = 0

for i in range(1000):
    try:
        block = stream.read(INPUT_FRAMES_PER_BLOCK)
    # just in case there is an error!
    except IOError, e:
        errorcount += 1
        print("(%d) Error recording: %s" % (errorcount, e))
        noisycount = 1

    amplitude = get_rms(block)
    if amplitude > tap_threshold:  # if its to loud...
        quietcount = 0
        noisycount += 1
        if noisycount > OVERSENSITIVE:
            tap_threshold *= 1.1  # turn down the sensitivity

    else:  # if its to quiet...

        if 1 <= noisycount <= MAX_TAP_BLOCKS:
            print 'tap!'
        noisycount = 0
        quietcount += 1
        if quietcount > UNDERSENSITIVE:
            tap_threshold *= 0.9  # turn up the sensitivity
