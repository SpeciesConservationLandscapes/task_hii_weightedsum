import argparse
import ee
from task_base import HIITask


class HIIWeightedsum(HIITask):
    ee_driverdir = "projects/HII/v1/driver"
    scale = 300

    inputs = {
        "rail": {
            "ee_type": HIITask.IMAGECOLLECTION,
            "ee_path": f"{ee_driverdir}/railways",
            "maxage": 1,
        },
        "road": {
            "ee_type": HIITask.IMAGECOLLECTION,
            "ee_path": f"{ee_driverdir}/roads",
            "maxage": 1,
        },
        "infrastructure": {
            "ee_type": HIITask.IMAGECOLLECTION,
            "ee_path": f"{ee_driverdir}/infrastructure",
            "maxage": 1,
        },
        "landuse": {
            "ee_type": HIITask.IMAGECOLLECTION,
            "ee_path": f"{ee_driverdir}/land_use",
            "maxage": 1,
        },
        "popdens": {
            "ee_type": HIITask.IMAGECOLLECTION,
            "ee_path": f"{ee_driverdir}/population_density",
            "maxage": 1,
        },
        "power": {
            "ee_type": HIITask.IMAGECOLLECTION,
            "ee_path": f"{ee_driverdir}/power",
            "maxage": 1,
        },
        "water": {
            "ee_type": HIITask.IMAGECOLLECTION,
            "ee_path": f"{ee_driverdir}/water",
            "maxage": 1,
        },
        "watermask": {
            "ee_type": HIITask.IMAGE,
            "ee_path": "projects/HII/v1/source/phys/watermask_jrc70_cciocean",
            "static": True,
        },
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.watermask = ee.Image(self.inputs["watermask"]["ee_path"])

    def calc(self):
        rail, _ = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["rail"]["ee_path"])
        )
        road, _ = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["road"]["ee_path"])
        )
        infrastructure, _ = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["infrastructure"]["ee_path"])
        )
        landuse, _ = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["landuse"]["ee_path"])
        )
        popdens, _ = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["popdens"]["ee_path"])
        )
        power, _ = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["power"]["ee_path"])
        )
        water, _ = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["water"]["ee_path"])
        )

        weighted_hii = (
            infrastructure.addBands([landuse, popdens, power, rail, road, water])
            .reduce(ee.Reducer.sum())
            .updateMask(self.watermask)
            .rename("hii")
        )

        self.export_image_ee(weighted_hii, "hii")

    def check_inputs(self):
        super().check_inputs()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--taskdate")
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="overwrite existing outputs instead of incrementing",
    )
    options = parser.parse_args()
    weightedsum_task = HIIWeightedsum(**vars(options))
    weightedsum_task.run()
