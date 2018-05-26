import json

from AI.cnn_model import TCNNConfig, TextCNN
from AI.predict import CnnModel
from AI.preprocessing import get_labeled_unlabeled_data

if __name__ == '__main__':
    cnn_model = CnnModel()

    print('\n\nTesting Start\n\n')
    test_demo = ['三星ST550以全新的拍摄方式超越了以往任何一款数码相机',
                 '热火vs骑士前瞻：皇帝回乡二番战 东部次席唾手可得新浪体育讯北京时间3月30日7:00']
    for i in test_demo:
        print(cnn_model.predict(i))
    print('\n\nTesting Finished\n\n')

    labeled_data, unlabeled_data = get_labeled_unlabeled_data()
    for i in range(len(unlabeled_data)):
    	unlabeled_data[i]['label'] = cnn_model.predict(unlabeled_data[i]['text'])
    with open('all_data.json', 'w') as f:
        json.dump(labeled_data + unlabeled_data, f, ensure_ascii=False)