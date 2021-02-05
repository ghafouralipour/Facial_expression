import os
from matplotlib.image import imread
import csv
import random


def create_dictionary(start_address, is_train, start_k):

    # create last_col
    usage = 'Testing'
    if is_train == 1:
        usage = 'Training'
    emotion_dict = {0: 'angry', 1: 'disgust', 2: 'fear', 3: 'happy', 4: 'neutral', 5: 'sad', 6: 'surprise'}

    dataset_dict = {}
    k = start_k
    for x in emotion_dict.items():
        image_addresses = start_address + x[1] + '/ca/'
        arr3 = os.listdir(image_addresses)
        for i in range(len(arr3)):
            filename = image_addresses + arr3[i]
            image = imread(filename)
            image2 = image.reshape(image.shape[0] * image.shape[1])
            print('################ Image {0} is readed.'.format(k + 1))
            dataset_dict[k] = {'emotion': x[0], 'pixels': image2, 'Usage': usage}
            k = k + 1
    return dataset_dict


def create_dataset(dict_train, dict_test):
    with open('image_dataset_file.csv', mode='w', newline='') as csv_file:
        fieldnames = ['emotion', 'pixels', 'Usage']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(len(dict_train)):
            pixel = " ".join([str(a) for a in dict_train[i][1]['pixels']])
            writer.writerow({'emotion': dict_train[i][1]['emotion'],
                             'pixels': pixel, 'Usage': dict_train[i][1]['Usage']})
            print('################ Image {0} is writed to dataset.'.format(i + 1))

        for i in range(len(dict_test)):
            pixel = " ".join([str(a) for a in dict_test[i][1]['pixels']])
            writer.writerow({'emotion': dict_test[i][1]['emotion'],
                             'pixels': pixel, 'Usage': dict_test[i][1]['Usage']})
            print('################ Image {0} is writed to dataset.'.format(i + 1))


def shuffle_dict(input_dict):
    l = list(input_dict.items())
    random.shuffle(l)
    return l


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start_train_address = './train/'
    start_test_address = './public_test/'

    dict_train = create_dictionary(start_train_address, 1, 0)
    print('############################ End Train Images ################################')

    dict_test = create_dictionary(start_test_address, 0, len(dict_train) + 1)
    print('############################ End Test Images ################################')

    # shuffle the dictionaries
    dict_train = shuffle_dict(dict_train)
    dict_test = shuffle_dict(dict_test)
    # Create dataset
    create_dataset(dict_train, dict_test)
    print('############################ End Creation Dataset ################################')
