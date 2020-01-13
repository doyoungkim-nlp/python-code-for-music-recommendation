EyeofSoul_200_last.xml: we downloaded 200 songs and extracted each song`s key features using jaudio. Each feature contains its path, name
, and other musical features 
EyeofSoul2.py: It shows us some basic features. 
  1.It gives us songList.txt, which is a list of songs which we extracted
  2.It gives us Euclidean.txt, which calculates Euclidean distance between two songs in a 77 dimensional space, with each vectors is a 
  feature vector extracted from jaudio.
randomshuffle_test.py: It shuffles songList.txt in a random order, which is used as a test set(not essential), which is random_test.txt.
EyeofSoul_brain: a pre-code of EyeofSoul_DUTF(dont use tensorflow), not essential. uses neural network
hate_list.txt, like_list.txt: 200*200 0 matrix. As a user implements this whole code in android, they can click each song as like/hate.
The history of each song (which is either liked or hated) will be conted in this matrix. i,j value of matrix shows how much like/hate 
the user clicked at ith song and it turned to jth song.
predict_mat.txt: It is a 200*200 matrix which is initailly set as Euclidean.txt. It will be implemented by using neural network and gradually 
be approached to the matrix which is the user`s interest(or user`s expectation probability form ith song to jth song in i,j value)
EyeofSoul_DUTF: using Neural Network, we will implement predict_mat as a weight value, and adjust it 3000 times to deduct a new matrix value,
which will be later implemented as a new weight matrix.
