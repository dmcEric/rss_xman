import os

BASE_PATH = '/media/ubuntu/45860a09-77fc-4f27-8cf3-5739e384e61d/huangw/rss_xman'
PRETRAIN_MODEL_PATH = os.path.join(BASE_PATH, 'pretrained')
# DATA_PATH = '/media/ubuntu/45860a09-77fc-4f27-8cf3-5739e384e61d/huangw/rss_xman/datasets/rssrai2019_croped'
DATA_PATH = '/media/ubuntu/45860a09-77fc-4f27-8cf3-5739e384e61d/huangw/rssai_tif_croped'
TRAIN_DATA_PATH = os.path.join(DATA_PATH,'train')
TRAIN_LABEL_PATH = os.path.join(TRAIN_DATA_PATH)
TRAIN_TXT_PATH = os.path.join(TRAIN_DATA_PATH, 'train.txt')
# TRAIN_TXT_PATH = os.path.join(TRAIN_DATA_PATH,'trainval.txt')
VAL_DATA_PATH = os.path.join(DATA_PATH,'val')
VAL_LABEL_PATH = os.path.join(VAL_DATA_PATH)
VAL_TXT_PATH = os.path.join(VAL_DATA_PATH, 'val.txt')
# VAL_TXT_PATH = os.path.join(VAL_DATA_PATH,'test.txt')
TEST_DATA_PATH = os.path.join(DATA_PATH,'test_fake')
TEST_LABEL_PATH = os.path.join(DATA_PATH)
TEST_TXT_PATH = os.path.join(TEST_DATA_PATH, 'test_fake.txt')
SAVE_PATH = BASE_PATH
SAVE_MODEL_PATH = os.path.join(BASE_PATH, 'weights')
SAVE_CKPT_PATH = os.path.join(SAVE_PATH, 'ckpt')
if not os.path.exists(SAVE_CKPT_PATH):
    os.makedirs(SAVE_CKPT_PATH)
SAVE_PRED_PATH = os.path.join(SAVE_PATH, 'prediction')
if not os.path.exists(SAVE_PRED_PATH):
    os.makedirs(SAVE_PRED_PATH)
TRAINED_LAST_MODEL = os.path.join(SAVE_MODEL_PATH, 'model20_1.pth')
INIT_LEARNING_RATE = 0.0002
DECAY = 5e-5
MOMENTUM = 0.90
MAX_ITER = 40000
BATCH_SIZE = 8
TEST_BATCH_SIZE = 1
THRESH = 0.1
THRESHS = [0.1, 0.3, 0.5]
LOSS_PARAM_CONV = 3
LOSS_PARAM_FC = 3
TRANSFROM_SCALES = (80, 80)
TEST_TRANSFORM_SCALES = (960, 960)
T0_MEAN_VALUE = (82.171, 85.481, 87.200)
T1_MEAN_VALUE = (91.536, 94.525, 97.195)
EPOCH = 50
RESUME = 0
TRAIN_LOSS = 'CE_loss'
FOCAL_LOSS_GAMMA = 2

