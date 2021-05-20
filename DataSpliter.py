import os, shutil

base_dir = 'D:/dataset/images/train/'
train_dir = 'D:/dataset/images/kaggle/train/'
test_dir = 'D:/dataset/images/kaggle/test/'
valid_dir = 'D:/dataset/images/kaggle/validation/'

# train = 0.7
# test = 0.15
# validation = 0.15

parent_list = [
    {
        "name": 'Black-grass',
        'count': 263,
        'train': 184,
        'test': 38,
        'validation': 38
    },
    {
        "name": 'Charlock',
        'count': 390,
        'train': 273,
        'test': 54,
        'validation': 54
    }, {
        "name": 'Cleavers',
        'count': 287,
        'train': 200,
        'test': 41,
        'validation': 41
    },
    {
        "name": 'Common Chickweed',
        'count': 611,
        'train': 425,
        'test': 88,
        'validation': 88
    }, {
        "name": 'Common wheat',
        'count': 221,
        'train': 154,
        'test': 31,
        'validation': 31
    }, {
        "name": 'Fat Hen',
        'count': 475,
        'train': 330,
        'test': 69,
        'validation': 69
    },
    {
        "name": 'Loose Silky-bent',
        'count': 654,
        'train': 455,
        'test': 94,
        'validation': 94
    }, {
        "name": 'Maize',
        'count': 221,
        'train': 154,
        'test': 32,
        'validation': 32
    }, {
        "name": 'Scentless Mayweed',
        'count': 516,
        'train': 361,
        'test': 76,
        'validation': 76
    },
    {
        "name": 'Shepherds Purse',
        'count': 231,
        'train': 161,
        'test': 34,
        'validation': 34
    }, {
        "name": 'Small-flowered Cranesbill',
        'count': 496,
        'train': 347,
        'test': 73,
        'validation': 73
    }, {
        "name": 'Sugar beet',
        'count': 385,
        'train': 269,
        'test': 56,
        'validation': 56
    },
]

for item in parent_list:
    files = os.listdir(base_dir + item['name'])
    for i in range(0, item['train'] - 1):
        shutil.move(base_dir + item['name'] + '/' + files[i], train_dir + item['name'] + '/' + str(i) + files[i])
    for i in range(item['train'], item['train'] + item['test'] - 1):
        shutil.move(base_dir + item['name'] + '/' + files[i], test_dir + item['name'] + '/' + str(i) + files[i])
    for i in range(item['train'] + item['test'], item['train'] + item['test'] + item['validation'] - 1):
        shutil.move(base_dir + item['name'] + '/' + files[i], valid_dir + item['name'] + '/' + str(i) + files[i])

print('JoB DonE')
