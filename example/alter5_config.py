import torch
from models.model_utils import (
    get_available_gpus,
)
from models.delta_pretrain import MainModel
from functools import partial
import os

EL = 10000
W = [
    11,
    11,
    11,
    11,
    19,
    19,
    19,
    19,
    25,
    25,
    25,
    25,
    33,
    33,
    33,
    33,
    43,
    43,
    85,
    85,
    85,
    85,
    85,
    85,
]
AR = [
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    2,
    2,
    2,
    2,
    8,
    8,
    8,
    8,
    16,
    16,
    16,
    16,
    16,
    16,
    32,
    32,
]


optimizer = partial(torch.optim.Adam, lr=1e-3)
model = MainModel(64, W, AR, 0.3, EL=EL, optimizer=optimizer, scheduler=partial(torch.optim.lr_scheduler.StepLR, step_size=1, gamma=0.5))


class config:
    log_path = "TestResultWCons/mut_train.log"
    save_path = "TestResultWCons/"
    seed = 321
    EL = EL
    batch_size = 16 * get_available_gpus()
    withcons = False

    # for training, can be ignored in test process, except the path to test data
    trainjsonfile = None
    validjsonfile = None
    testjsonfile = None
    mut_data = [os.path.join("/temp/xuchencheng/eSplicedata/Species_37_ProcessedData/Alter5/", x) for x in os.listdir("/temp/xuchencheng/eSplicedata/Species_37_ProcessedData/Alter5/")]
    model = model
    epoch_num = 1
    num_workers = 5  # number of dataloader workers

    model_path = ["tasks/Pretrain_withoutcons_rep{}/models/model.ckpt-2".format(i) for i in range(5)]
    print_summary = True
    save_files = True
    is_train = False
