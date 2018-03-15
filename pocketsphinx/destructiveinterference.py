from pydub import AudioSegment
from pydub.playback import play

#Load an audio file
droneFile = "./recordings/16bit/sample-drone-noise.wav"
droneSound = AudioSegment.from_file(droneFile, format="wav")
droneWithSpeakingFile = "./recordings/16bit/cut-off-no-windscreen-drone-noise1.wav"
droneWithSpeakingSound = AudioSegment.from_file(droneWithSpeakingFile, format="wav")

#Invert phase of audio file
inverted = droneSound.invert_phase()

#Merge two audio files
combined = droneWithSpeakingSound.overlay(inverted)

#Export merged audio file
combined.export("outAudio.wav", format="wav")

#Play audio file :
mergedAudio = AudioSegment.from_wav("outAudio.wav")
play(mergedAudio)