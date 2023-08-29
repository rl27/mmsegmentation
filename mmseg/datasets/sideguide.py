# Copyright (c) OpenMMLab. All rights reserved.
from mmseg.registry import DATASETS
from .basesegdataset import BaseSegDataset


@DATASETS.register_module()
class SideGuide(BaseSegDataset):
    METAINFO = dict(
        classes=('background',  'sidewalk_blocks', 'sidewalk_cement', 'sidewalk_urethane', 'sidewalk_asphalt', 'sidewalk_soil_stone', 'sidewalk_damaged', 'sidewalk_other', 'braille_guide_blocks_normal', 'braille_guide_blocks_damaged', 'roadway_normal', 'roadway_crosswalk', 'alley_normal', 'alley_crosswalk', 'alley_speed_bump', 'alley_damaged', 'bike_lane_normal', 'caution_zone_stairs', 'caution_zone_manhole', 'caution_zone_tree_zone', 'caution_zone_grating', 'caution_zone_repair_zone'),
        palette=[[0, 0, 0], [0, 0, 255], [217, 217, 217], [198, 89, 17], [128, 128, 128], [255, 230, 153], [55, 86, 35], [110, 168, 70], [255, 255, 0], [128, 96, 0], [255, 128, 255], [255, 0, 255], [230, 170, 255], [208, 88, 255], [138, 60, 200], [88, 38, 128], [255, 155, 155], [255, 192, 0], [255, 0, 0], [0, 255, 0], [255, 128, 0], [105, 105, 255]]
    )

    def __init__(self,
                 img_suffix='.jpg',
                 seg_map_suffix='.png',
                 **kwargs) -> None:
        super().__init__(
            img_suffix=img_suffix, seg_map_suffix=seg_map_suffix, **kwargs)




