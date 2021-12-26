import numpy as np

from AnimationPlotLines import animation_plot

data = np.load('data/edinburgh_locomotion_train.npz')

clips = data['clips']
# print("Clips: ", clips)
print("Clips: ", clips.shape)
clips = np.swapaxes(clips, 1, 2)



index = 5
seq1 = clips[index:index+1]
seq2 = clips[index+1:index+2]
seq3 = clips[index+2:index+3]

# print(seq1.shape)

# print clips.max()
# print clips.mean()
# print clips.std()

# print seq1.max()
# print seq1.mean()
# print seq1.std()
animation_plot([seq1, seq2], interval=15)
