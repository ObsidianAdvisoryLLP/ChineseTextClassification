from AI.cnn_model import TCNNConfig, TextCNN
from AI.data import read_category, read_vocab
from AI.preprocessing import combine_data, read_labels, shuffle_save_labeled_data
from AI.cnn import start_train, start_test

if __name__ == '__main__':
    #combine_data()
	#read_labels()
	#shuffle_save_labeled_data()
	#start_train()
	start_test()