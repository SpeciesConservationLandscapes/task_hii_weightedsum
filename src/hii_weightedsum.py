import argparse
import ee
from datetime import datetime, timezone
from task_base import HIITask


class HIIWeightedsum(HIITask):
    ee_rootdir = "projects/HII/v1"
    ee_driverdir = f"{ee_rootdir}/driver"
    scale = 300


    inputs = {
        "infrastructure_afrotropic": {
            "ee_type": HIITask.IMAGECOLLECTION,
            "ee_path": f"{ee_driverdir}/infrastructure/aois/Afrotropic",
            "maxage": 1,
        },
        "infrastructure_australasia": {
            "ee_type": HIITask.IMAGECOLLECTION,
            "ee_path": f"{ee_driverdir}/infrastructure/aois/Australasia",
            "maxage": 1,
        },
        "infrastructure_indomalayan": {
            "ee_type": HIITask.IMAGECOLLECTION,
            "ee_path": f"{ee_driverdir}/infrastructure/aois/Indomalayan",
            "maxage": 1,
        },
        "infrastructure_nearctic": {
            "ee_type": HIITask.IMAGECOLLECTION,
            "ee_path": f"{ee_driverdir}/infrastructure/aois/Nearctic",
            "maxage": 1,
        },
        "infrastructure_neotropic": {
            "ee_type": HIITask.IMAGECOLLECTION,
            "ee_path": f"{ee_driverdir}/infrastructure/aois/Neotropic",
            "maxage": 1,
        },
        "infrastructure_oceania": {
            "ee_type": HIITask.IMAGECOLLECTION,
            "ee_path": f"{ee_driverdir}/infrastructure/aois/Oceania",
            "maxage": 1,
        },
        "infrastructure_palearctic": {
            "ee_type": HIITask.IMAGECOLLECTION,
            "ee_path": f"{ee_driverdir}/infrastructure/aois/Palearctic",
            "maxage": 1,
        },
        "infrastructure_higharctic": {
            "ee_type": HIITask.IMAGECOLLECTION,
            "ee_path": f"{ee_driverdir}/infrastructure/aois/HighArctic",
            "maxage": 1,
        },



        "landuse_afrotropic": {
            "ee_type": HIITask.IMAGECOLLECTION,
            "ee_path": f"{ee_driverdir}/landuse/aois/Afrotropic",
            "maxage": 1,
        },
        "landuse_australasia": {
            "ee_type": HIITask.IMAGECOLLECTION,
            "ee_path": f"{ee_driverdir}/landuse/aois/Australasia",
            "maxage": 1,
        },
        "landuse_indomalayan": {
            "ee_type": HIITask.IMAGECOLLECTION,
            "ee_path": f"{ee_driverdir}/landuse/aois/Indomalayan",
            "maxage": 1,
        },
        "landuse_nearctic": {
            "ee_type": HIITask.IMAGECOLLECTION,
            "ee_path": f"{ee_driverdir}/landuse/aois/Nearctic",
            "maxage": 1,
        },
        "landuse_neotropic": {
            "ee_type": HIITask.IMAGECOLLECTION,
            "ee_path": f"{ee_driverdir}/landuse/aois/Neotropic",
            "maxage": 1,
        },
        "landuse_oceania": {
            "ee_type": HIITask.IMAGECOLLECTION,
            "ee_path": f"{ee_driverdir}/landuse/aois/Oceania",
            "maxage": 1,
        },
        "landuse_palearctic": {
            "ee_type": HIITask.IMAGECOLLECTION,
            "ee_path": f"{ee_driverdir}/landuse/aois/Palearctic",
            "maxage": 1,
        },
        "landuse_higharctic": {
            "ee_type": HIITask.IMAGECOLLECTION,
            "ee_path": f"{ee_driverdir}/landuse/aois/HighArctic",
            "maxage": 1,
        },



        "popdens_afrotropic": {
            "ee_type": HIITask.IMAGECOLLECTION,
            "ee_path": f"{ee_driverdir}/popdens/aois/Afrotropic",
            "maxage": 3,
        },
        "popdens_australasia": {
            "ee_type": HIITask.IMAGECOLLECTION,
            "ee_path": f"{ee_driverdir}/popdens/aois/Australasia",
            "maxage": 3,
        },
        "popdens_indomalayan": {
            "ee_type": HIITask.IMAGECOLLECTION,
            "ee_path": f"{ee_driverdir}/popdens/aois/Indomalayan",
            "maxage": 3,
        },
        "popdens_nearctic": {
            "ee_type": HIITask.IMAGECOLLECTION,
            "ee_path": f"{ee_driverdir}/popdens/aois/Nearctic",
            "maxage": 3,
        },
        "popdens_neotropic": {
            "ee_type": HIITask.IMAGECOLLECTION,
            "ee_path": f"{ee_driverdir}/popdens/aois/Neotropic",
            "maxage": 3,
        },
        "popdens_oceania": {
            "ee_type": HIITask.IMAGECOLLECTION,
            "ee_path": f"{ee_driverdir}/popdens/aois/Oceania",
            "maxage": 3,
        },
        "popdens_palearctic": {
            "ee_type": HIITask.IMAGECOLLECTION,
            "ee_path": f"{ee_driverdir}/popdens/aois/Palearctic",
            "maxage": 3,
        },
        "popdens_higharctic": {
            "ee_type": HIITask.IMAGECOLLECTION,
            "ee_path": f"{ee_driverdir}/popdens/aois/HighArctic",
            "maxage": 3,
        },





        "power_afrotropic": {
            "ee_type": HIITask.IMAGECOLLECTION,
            "ee_path": f"{ee_driverdir}/power/aois/Afrotropic",
            "maxage": 1,
        },
        "power_australasia": {
            "ee_type": HIITask.IMAGECOLLECTION,
            "ee_path": f"{ee_driverdir}/power/aois/Australasia",
            "maxage": 1,
        },
        "power_indomalayan": {
            "ee_type": HIITask.IMAGECOLLECTION,
            "ee_path": f"{ee_driverdir}/power/aois/Indomalayan",
            "maxage": 1,
        },
        "power_nearctic": {
            "ee_type": HIITask.IMAGECOLLECTION,
            "ee_path": f"{ee_driverdir}/power/aois/Nearctic",
            "maxage": 1,
        },
        "power_neotropic": {
            "ee_type": HIITask.IMAGECOLLECTION,
            "ee_path": f"{ee_driverdir}/power/aois/Neotropic",
            "maxage": 1,
        },
        "power_oceania": {
            "ee_type": HIITask.IMAGECOLLECTION,
            "ee_path": f"{ee_driverdir}/power/aois/Oceania",
            "maxage": 1,
        },
        "power_palearctic": {
            "ee_type": HIITask.IMAGECOLLECTION,
            "ee_path": f"{ee_driverdir}/power/aois/Palearctic",
            "maxage": 1,
        },
        "power_higharctic": {
            "ee_type": HIITask.IMAGECOLLECTION,
            "ee_path": f"{ee_driverdir}/power/aois/HighArctic",
            "maxage": 1,
        },




        "rail_afrotropic": {
            "ee_type": HIITask.IMAGECOLLECTION,
            "ee_path": f"{ee_driverdir}/rail/aois/Afrotropic",
            "maxage": 1,
        },
        "rail_australasia": {
            "ee_type": HIITask.IMAGECOLLECTION,
            "ee_path": f"{ee_driverdir}/rail/aois/Australasia",
            "maxage": 1,
        },
        "rail_indomalayan": {
            "ee_type": HIITask.IMAGECOLLECTION,
            "ee_path": f"{ee_driverdir}/rail/aois/Indomalayan",
            "maxage": 1,
        },
        "rail_nearctic": {
            "ee_type": HIITask.IMAGECOLLECTION,
            "ee_path": f"{ee_driverdir}/rail/aois/Nearctic",
            "maxage": 1,
        },
        "rail_neotropic": {
            "ee_type": HIITask.IMAGECOLLECTION,
            "ee_path": f"{ee_driverdir}/rail/aois/Neotropic",
            "maxage": 1,
        },
        "rail_oceania": {
            "ee_type": HIITask.IMAGECOLLECTION,
            "ee_path": f"{ee_driverdir}/rail/aois/Oceania",
            "maxage": 1,
        },
        "rail_palearctic": {
            "ee_type": HIITask.IMAGECOLLECTION,
            "ee_path": f"{ee_driverdir}/rail/aois/Palearctic",
            "maxage": 1,
        },
        "rail_higharctic": {
            "ee_type": HIITask.IMAGECOLLECTION,
            "ee_path": f"{ee_driverdir}/rail/aois/HighArctic",
            "maxage": 1,
        },




        "road_afrotropic": {
            "ee_type": HIITask.IMAGECOLLECTION,
            "ee_path": f"{ee_driverdir}/road/aois/Afrotropic",
            "maxage": 1,
        },
        "road_australasia": {
            "ee_type": HIITask.IMAGECOLLECTION,
            "ee_path": f"{ee_driverdir}/road/aois/Australasia",
            "maxage": 1,
        },
        "road_indomalayan": {
            "ee_type": HIITask.IMAGECOLLECTION,
            "ee_path": f"{ee_driverdir}/road/aois/Indomalayan",
            "maxage": 1,
        },
        "road_nearctic": {
            "ee_type": HIITask.IMAGECOLLECTION,
            "ee_path": f"{ee_driverdir}/road/aois/Nearctic",
            "maxage": 1,
        },
        "road_neotropic": {
            "ee_type": HIITask.IMAGECOLLECTION,
            "ee_path": f"{ee_driverdir}/road/aois/Neotropic",
            "maxage": 1,
        },
        "road_oceania": {
            "ee_type": HIITask.IMAGECOLLECTION,
            "ee_path": f"{ee_driverdir}/road/aois/Oceania",
            "maxage": 1,
        },
        "road_palearctic": {
            "ee_type": HIITask.IMAGECOLLECTION,
            "ee_path": f"{ee_driverdir}/road/aois/Palearctic",
            "maxage": 1,
        },

        "road_higharctic": {
            "ee_type": HIITask.IMAGECOLLECTION,
            "ee_path": f"{ee_driverdir}/road/aois/HighArctic",
            "maxage": 1,
        },



    "water_afrotropic": {
        "ee_type": HIITask.IMAGECOLLECTION,
        "ee_path": f"{ee_driverdir}/water/aois/Afrotropic",
        "maxage": 3,
    },
    "water_australasia": {
        "ee_type": HIITask.IMAGECOLLECTION,
        "ee_path": f"{ee_driverdir}/water/aois/Australasia",
        "maxage": 3,
    },
    "water_indomalayan": {
        "ee_type": HIITask.IMAGECOLLECTION,
        "ee_path": f"{ee_driverdir}/water/aois/Indomalayan",
        "maxage": 3,
    },
    "water_nearctic": {
        "ee_type": HIITask.IMAGECOLLECTION,
        "ee_path": f"{ee_driverdir}/water/aois/Nearctic",
        "maxage": 3,
    },
    "water_neotropic": {
        "ee_type": HIITask.IMAGECOLLECTION,
        "ee_path": f"{ee_driverdir}/water/aois/Neotropic",
        "maxage": 3,
    },
    "water_oceania": {
        "ee_type": HIITask.IMAGECOLLECTION,
        "ee_path": f"{ee_driverdir}/water/aois/Oceania",
        "maxage": 3,
    },
    "water_palearctic": {
        "ee_type": HIITask.IMAGECOLLECTION,
        "ee_path": f"{ee_driverdir}/water/aois/Palearctic",
        "maxage": 3,
    }
    
                    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_aoi_from_ee("{}/earth_aoi".format(self.ee_rootdir))

    def calc(self):

        '''
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
        '''
        infrastructure_afrotropic, _ = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["infrastructure_afrotropic"]["ee_path"])
        )
        infrastructure_australasia, _ = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["infrastructure_australasia"]["ee_path"])
        )
        infrastructure_indomalayan, _ = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["infrastructure_indomalayan"]["ee_path"])
        )
        infrastructure_nearctic, _ = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["infrastructure_nearctic"]["ee_path"])
        )
        infrastructure_neotropic, _ = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["infrastructure_neotropic"]["ee_path"])
        )
        infrastructure_oceania, _ = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["infrastructure_oceania"]["ee_path"])
        )
        infrastructure_palearctic, _ = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["infrastructure_palearctic"]["ee_path"])
        )
        infrastructure_higharctic, _ = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["infrastructure_higharctic"]["ee_path"])
        )

        infrastructure = ee.ImageCollection([infrastructure_afrotropic,\
                                infrastructure_australasia,\
                                infrastructure_indomalayan,\
                                infrastructure_nearctic,\
                                infrastructure_neotropic,\
                                infrastructure_oceania,\
                                infrastructure_palearctic,\
                                infrastructure_higharctic]).max()



        landuse_afrotropic, _ = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["landuse_afrotropic"]["ee_path"])
        )
        landuse_australasia, _ = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["landuse_australasia"]["ee_path"])
        )
        landuse_indomalayan, _ = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["landuse_indomalayan"]["ee_path"])
        )
        landuse_nearctic, _ = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["landuse_nearctic"]["ee_path"])
        )
        landuse_neotropic, _ = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["landuse_neotropic"]["ee_path"])
        )
        landuse_oceania, _ = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["landuse_oceania"]["ee_path"])
        )
        landuse_palearctic, _ = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["landuse_palearctic"]["ee_path"])
        )
        landuse_higharctic, _ = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["landuse_higharctic"]["ee_path"])
        )
        landuse = ee.ImageCollection([landuse_afrotropic,\
                                landuse_australasia,\
                                landuse_indomalayan,\
                                landuse_nearctic,\
                                landuse_neotropic,\
                                landuse_oceania,\
                                landuse_palearctic,\
                                landuse_higharctic]).max()



        popdens_afrotropic, _ = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["popdens_afrotropic"]["ee_path"])
        )
        popdens_australasia, _ = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["popdens_australasia"]["ee_path"])
        )
        popdens_indomalayan, _ = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["popdens_indomalayan"]["ee_path"])
        )
        popdens_nearctic, _ = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["popdens_nearctic"]["ee_path"])
        )
        popdens_neotropic, _ = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["popdens_neotropic"]["ee_path"])
        )
        popdens_oceania, _ = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["popdens_oceania"]["ee_path"])
        )
        popdens_palearctic, _ = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["popdens_palearctic"]["ee_path"])
        )
        popdens_higharctic, _ = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["popdens_higharctic"]["ee_path"])
        )

        popdens = ee.ImageCollection([popdens_afrotropic,\
                                popdens_australasia,\
                                popdens_indomalayan,\
                                popdens_nearctic,\
                                popdens_neotropic,\
                                popdens_oceania,\
                                popdens_palearctic,\
                                popdens_higharctic]).max()


        power_afrotropic, _ = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["power_afrotropic"]["ee_path"])
        )
        power_australasia, _ = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["power_australasia"]["ee_path"])
        )
        power_indomalayan, _ = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["power_indomalayan"]["ee_path"])
        )
        power_nearctic, _ = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["power_nearctic"]["ee_path"])
        )
        power_neotropic, _ = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["power_neotropic"]["ee_path"])
        )
        power_oceania, _ = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["power_oceania"]["ee_path"])
        )
        power_palearctic, _ = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["power_palearctic"]["ee_path"])
        )
        power_higharctic, _ = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["power_higharctic"]["ee_path"])
        )

        power = ee.ImageCollection([power_afrotropic,\
                                power_australasia,\
                                power_indomalayan,\
                                power_nearctic,\
                                power_neotropic,\
                                power_oceania,\
                                power_palearctic,\
                                power_higharctic]).max()




        rail_afrotropic, _ = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["rail_afrotropic"]["ee_path"])
        )
        rail_australasia, _ = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["rail_australasia"]["ee_path"])
        )
        rail_indomalayan, _ = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["rail_indomalayan"]["ee_path"])
        )
        rail_nearctic, _ = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["rail_nearctic"]["ee_path"])
        )
        rail_neotropic, _ = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["rail_neotropic"]["ee_path"])
        )
        rail_oceania, _ = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["rail_oceania"]["ee_path"])
        )
        rail_palearctic, _ = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["rail_palearctic"]["ee_path"])
        )
        rail_higharctic, _ = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["rail_higharctic"]["ee_path"])
        )

        rail = ee.ImageCollection([rail_afrotropic,\
                                rail_australasia,\
                                rail_indomalayan,\
                                rail_nearctic,\
                                rail_neotropic,\
                                rail_oceania,\
                                rail_palearctic,\
                                rail_higharctic]).max()




        road_afrotropic, _ = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["road_afrotropic"]["ee_path"])
        )
        road_australasia, _ = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["road_australasia"]["ee_path"])
        )
        road_indomalayan, _ = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["road_indomalayan"]["ee_path"])
        )
        road_nearctic, _ = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["road_nearctic"]["ee_path"])
        )
        road_neotropic, _ = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["road_neotropic"]["ee_path"])
        )
        road_oceania, _ = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["road_oceania"]["ee_path"])
        )
        road_palearctic, _ = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["road_palearctic"]["ee_path"])
        )
        road_higharctic, _ = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["road_higharctic"]["ee_path"])
        )

        road = ee.ImageCollection([road_afrotropic,\
                                road_australasia,\
                                road_indomalayan,\
                                road_nearctic,\
                                road_neotropic,\
                                road_oceania,\
                                road_palearctic,\
                                road_higharctic]).max()



        
        water_afrotropic, _ = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["water_afrotropic"]["ee_path"])
        )
        water_australasia, _ = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["water_australasia"]["ee_path"])
        )
        water_indomalayan, _ = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["water_indomalayan"]["ee_path"])
        )
        water_nearctic, _ = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["water_nearctic"]["ee_path"])
        )
        water_neotropic, _ = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["water_neotropic"]["ee_path"])
        )
        water_oceania, _ = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["water_oceania"]["ee_path"])
        )
        water_palearctic, _ = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["water_palearctic"]["ee_path"])
        )
        water_higharctic, _ = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["water_palearctic"]["ee_path"])
        )

        water = ee.ImageCollection([water_afrotropic,\
                                water_australasia,\
                                water_indomalayan,\
                                water_nearctic,\
                                water_neotropic,\
                                water_oceania,\
                                water_palearctic,\
                                water_higharctic\
                                ]).max()




        weighted_hii = infrastructure\
                        .add(landuse)\
                        .add(popdens)\
                        .add(power)\
                        .add(rail)\
                        .add(road)\
                        .add(water)



        self.export_image_ee(weighted_hii, "hii")
        self.export_image_ee(infrastructure, "infrastructure/hii_infrastructure_driver")
        self.export_image_ee(landuse, "landuse/hii_landuse_driver")
        self.export_image_ee(popdens, "popdens/hii_popdens_driver")
        self.export_image_ee(power, "power/hii_power_driver")
        self.export_image_ee(rail, "rail/hii_rail_driver")
        self.export_image_ee(road, "road/hii_road_driver")
        self.export_image_ee(water, "water/hii_water_driver")

    def check_inputs(self):
        super().check_inputs()
        # add any task-specific checks here, and set self.status = self.FAILED if any fail


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--taskdate", default=datetime.now(timezone.utc).date())
    options = parser.parse_args()
    weightedsum_task = HIIWeightedsum(**vars(options))
    weightedsum_task.run()
