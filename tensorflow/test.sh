cd speech_commands

python label_wav.py \
--graph=trainedGraph.pb \
--labels=conv_labels.txt \
--wav=test.wav 


