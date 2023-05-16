import argparse
import ee
from task_base import HIITask


class HIIWeightedsum(HIITask):
    ee_driverdir = "projects/HII/v1/driver"

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
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.export_path = None
        self.noosm = kwargs.get("noosm", False)

    def calc(self):
        if self.noosm is False:
            rail, _ = self.get_most_recent_image(
                ee.ImageCollection(self.inputs["rail"]["ee_path"])
            )
            road, _ = self.get_most_recent_image(
                ee.ImageCollection(self.inputs["road"]["ee_path"])
            )
            infrastructure, _ = self.get_most_recent_image(
                ee.ImageCollection(self.inputs["infrastructure"]["ee_path"])
            )
        else:
            rail, _ = self.get_most_recent_image(
                ee.ImageCollection(self.inputs["rail"]["ee_path"] + "_no_osm")
            )
            road, _ = self.get_most_recent_image(
                ee.ImageCollection(self.inputs["road"]["ee_path"] + "_no_osm")
            )
            infrastructure, _ = self.get_most_recent_image(
                ee.ImageCollection(self.inputs["infrastructure"]["ee_path"] + "_no_osm")
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

        if self.noosm is False:
            self.export_path = f"hii"
        else:
            self.export_path = f"hii_no_osm"

        self.export_image_ee(weighted_hii, self.export_path)

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
    parser.add_argument(
        "-n",
        "--noosm",
        action="store_true",
        help="do not include osm in driver calculation",
    )
    options = parser.parse_args()
    weightedsum_task = HIIWeightedsum(**vars(options))
    weightedsum_task.run()
