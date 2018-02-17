import sys, os
from pocketsphinx.pocketsphinx import *
from sphinxbase.sphinxbase import *
import pyaudio

modeldir = "/usr/local/lib/python2.7/dist-packages/pocketsphinx/model"
datadir = "/usr/local/lib/python2.7/dist-packages/pocketsphinx/test/data"

#create keyword file
#words = '''
#teriyaki /.0001/
#forward /.0001/
#'''
#open('words.txt', 'w').write(words)

# Create a decoder with certain model
config = Decoder.default_config()
config.set_string('-hmm', os.path.join(modeldir, 'en-us'))
config.set_string('-dict', os.path.join(modeldir, 'cmudict-en-us.dict'))
config.set_string('-kws', 'words.txt')
config.set_float('-kws_threshold', 1e+20)
config.set_string('-logfn', '/dev/null')

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)
stream.start_stream()

# Process audio chunk by chunk. On keyword detected perform action and restart search
decoder = Decoder(config)
decoder.start_utt()
count = 0
while True:
    buf = stream.read(1024)
    if buf:
         decoder.process_raw(buf, False, False)
    else:
         break
    if decoder.hyp() != None:
        count += 1
        print 'I HEARD THAT', count
        print 'found keyword: ', decoder.hyp().hypstr
        #print ([(seg.word, seg.prob, seg.start_frame, seg.end_frame) for seg in decoder.seg()])
        #print ("Detected keyword, restarting search")
        decoder.end_utt()
        decoder.start_utt()
        