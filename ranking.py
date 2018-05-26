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

    posts = {}
    with open('./AI/data/ubs/UBS Weibo Data/weibo/Status_Data9_with_city_code.json', "rb") as infile:
            data = json.load(infile)
            for status in data:
                posts[status['sid']] = cnn_model.predict(status['s_text'])

    china_data = {}
    with open('./AI/data/ubs/UBS Weibo Data/weibo/weibo-china-province-city.json', "rb") as infile:
            data = json.load(infile)
            for entry in data:
                province = entry['province']
                province_en = entry['province_en']
                province_tc = entry['province_tc']
                province_sc = entry['province_sc']
                city = entry['city']
                city_en = entry['city_en']
                city_tc = entry['city_tc']
                city_sc = entry['city_sc']
                ref_id = entry['ref_id']
                if province not in china_data:
                    china_data[province] = {
                        'name':{
                            'en': province_en,
                            'tc': province_tc,
                            'sc': province_sc
                        },
                        'cities':{
                        }
                    }
                china_data[province]['cities'][city] = {
                    'name':{
                        'en':city_en,
                        'tc':city_tc,
                        'sc':city_sc
                    },
                    'ref_id':ref_id
                }
    province_data = {}
    with open('./AI/data/ubs/UBS Weibo Data/weibo/Status_Data9_Comment_Data_with_city_code.json', "rb") as infile:
            data = json.load(infile)
            for comment in data:
                if comment['u_province'] not in province_data:
                    if comment['u_province'] in china_data:
                        province_data[comment['u_province']] = {'name':china_data[comment['u_province']]['name']}
                    else:
                        province_data[comment['u_province']] = {}
                if 'comment_count' not in province_data[comment['u_province']]:
                    province_data[comment['u_province']]['comment_count'] = {
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
                province_data[comment['u_province']]['comment_count'][posts[comment['cid']]] += 1

    with open('province_data.json', 'w') as f:
        json.dump(province_data, f, ensure_ascii=False)

    city_data = {}
    with open('./AI/data/ubs/UBS Weibo Data/weibo/Status_Data9_Comment_Data_with_city_code.json', "rb") as infile:
            data = json.load(infile)
            for comment in data:
                if comment['u_city'] not in city_data:
                    if comment['u_province'] in china_data and comment['u_city'] in china_data[comment['u_province']]['cities']:
                        city_data[comment['u_city']] = {
                            'name': china_data[comment['u_province']]['cities'][comment['u_city']]['name'],
                            'ref_id': china_data[comment['u_province']]['cities'][comment['u_city']]['ref_id'],
                            'province':{
                                'id':comment['u_province'],
                                'name':china_data[comment['u_province']]['name']
                            }
                        }
                    else:
                        city_data[comment['u_city']] = {}
                if 'comment_count' not in city_data[comment['u_city']]:
                    city_data[comment['u_city']]['comment_count'] = {
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
                city_data[comment['u_city']]['comment_count'][posts[comment['cid']]] += 1
    
    with open('city_data.json', 'w') as f:
        json.dump(city_data, f, ensure_ascii=False)








