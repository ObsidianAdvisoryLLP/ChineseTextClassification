import json
import locale
locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' ) 

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

    posts = {}
    views_by_topic = {
        '0':0,
        '1':0,
        '2':0,
        '3':0,
        '4':0,
        '5':0,
        '6':0,
        '7':0,
        '8':0,
        '9':0,
        '10':0,
        '11':0,
        '12':0
    }
    with open('./translated_records.json', "rb") as infile:
            data = json.load(infile)
            for record in data:
                label = cnn_model.predict(record["translated"])
                views_by_topic[label] += locale.atoi(record["UniqueVistors"])
    print(views_by_topic)

    import matplotlib.pyplot as plt

    labels_start = ['Stock','Bond','Oil','Gold','Artefact','Chinese PDC','English PDC','Jewellery','Real Estate','Golf','Car','Oversea Education','Yong Children Education']
    values_start = list(views_by_topic.values())
    labels = []
    values = []

    for i in range(len(values_start)):
        if values_start[i] != 0:
            labels.append(labels_start[i])
            values.append(values_start[i])
    plt.pie(values, labels=labels,autopct='%1.1f%%')
     
    plt.axis('equal')
    plt.show()
