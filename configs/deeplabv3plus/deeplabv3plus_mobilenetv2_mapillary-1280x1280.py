_base_ = [
    '../deeplabv3plus/deeplabv3plus_r50-d8_4xb2-300k_mapillay_v1_65-1280x1280.py',
]

model = dict(
    pretrained='mmcls://mobilenet_v2',
    backbone=dict(
        _delete_=True,
        type='MobileNetV2',
        widen_factor=1.,
        strides=(1, 2, 2, 1, 1, 1, 1),
        dilations=(1, 1, 1, 2, 2, 4, 4),
        out_indices=(1, 2, 4, 6),
        norm_cfg=dict(type='SyncBN', requires_grad=True)),
    decode_head=dict(in_channels=320, c1_in_channels=24),
    auxiliary_head=dict(in_channels=96))
