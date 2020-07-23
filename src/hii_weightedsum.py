import argparse
import ee
from datetime import datetime, timezone
from task_base import EETask


class HIIWeightedsum(EETask):
    ee_rootdir = "projects/HII/v1/sumatra_poc"
    ee_driverdir = f"{ee_rootdir}/driver"
    scale = 300
    inputs = {
        "infrastructure": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_driverdir}/infrastructure/hii_infrastructure_driver",
            "maxage": 1,
        },
        "landuse": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_driverdir}/landuse/hii_landuse_driver",
            "maxage": 1,
        },
        "popdens": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_driverdir}/popdens/hii_popdens_driver",
            "maxage": 1,
        },
        "power": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_driverdir}/power/hii_power_driver",
            "maxage": 1,
        },
        "rail": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_driverdir}/rail/hii_rail_driver",
            "maxage": 1,
        },
        "road": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_driverdir}/road/hii_road_driver",
            "maxage": 1,
        },
        "water": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_driverdir}/water/hii_water_driver",
            "static": True,
        }

                    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_aoi_from_ee("{}/sumatra_poc_aoi".format(self.ee_rootdir))

    def calc(self):


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
        rail, _ = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["rail"]["ee_path"])
        )
        road, _ = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["road"]["ee_path"])
        )
        water, _ = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["water"]["ee_path"])
        )


        weighted_hii = infrastructure.divide(ee.Image(4))\
                        .add(landuse)\
                        .add(popdens.divide(ee.Image(3)))\
                        .add(power.divide(ee.Image(5)))\
                        .add(rail.divide(ee.Image(4)))\
                        .add(road.divide(ee.Image(4)))\
                        .add(water.multiply(ee.Image(2.5)))

        self.export_image_ee(weighted_hii, "hii")

    def check_inputs(self):
        super().check_inputs()
        # add any task-specific checks here, and set self.status = self.FAILED if any fail


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--taskdate", default=datetime.now(timezone.utc).date())
    options = parser.parse_args()
    weightedsum_task = HIIWeightedsum(**vars(options))
    weightedsum_task.run()
