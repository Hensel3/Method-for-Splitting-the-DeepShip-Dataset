import os
from scipy.io import wavfile

# 文件路径
train_list = r"C:\Users\A\Desktop\复现\数据集\DeepShip-dataset-segmentation-main\train.txt"
test_list = r"C:\Users\A\Desktop\复现\数据集\DeepShip-dataset-segmentation-main\test.txt"
audio_path = r"C:\Users\A\Desktop\复现\数据集"

# 读取文件列表
train_lines = open(train_list).read().splitlines()
test_lines = open(test_list).read().splitlines()

# 定义音频长度和步长
audlen = 32000 * 3
audstr = 32000 * 1

for idx_train, file_train in enumerate(train_lines):
    file_train = os.path.join(audio_path, file_train)
    file_train = file_train.replace('/', '\\')  # 将路径分隔符统一为反斜杠
    fs_train, aud_train = wavfile.read(file_train)
    writedir_train = file_train.replace('\\DeepShip\\', '\\DeepShip_train\\')
    print(writedir_train)
    directory_train = os.path.dirname(writedir_train)  # 获取目录部分
    os.makedirs(directory_train, exist_ok=True)  # 创建目录，若目录存在则不会抛出异常
    for st_train in range(0, len(aud_train) - audlen, audstr):
        output_file = os.path.join(directory_train, '%05d.wav' % (st_train // fs_train))
        wavfile.write(output_file, fs_train, aud_train[st_train:st_train + audlen])
    print(idx_train, file_train)

for idx_test, file_test in enumerate(test_lines):
    file_test = os.path.join(audio_path, file_test)
    file_test = file_test.replace('/', '\\')  # 将路径分隔符统一为反斜杠
    fs_test, aud_test = wavfile.read(file_test)
    writedir_test = file_test.replace('\\DeepShip\\', '\\DeepShip_test\\')
    directory_test = os.path.dirname(writedir_test)  # 获取目录部分
    os.makedirs(directory_test, exist_ok=True)  # 创建目录，若目录存在则不会抛出异常
    for st_test in range(0, len(aud_test) - audlen, audstr):
        output_file = os.path.join(directory_test, '%05d.wav' % (st_test // fs_test))
        wavfile.write(output_file, fs_test, aud_test[st_test:st_test + audlen])
    print(idx_test, file_test)
