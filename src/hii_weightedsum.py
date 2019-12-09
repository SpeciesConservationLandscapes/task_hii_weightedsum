import ee
from task_base import EETask


class HIIWeightedsum(EETask):
    ee_rootdir = "projects/HII/v1/sumatra_poc"
    ee_driverdir = 'final'
    # if input lives in ee, it should have an "ee_path" pointing to an ImageCollection/FeatureCollection
    inputs = {

                    }
    

    gpw_cadence = 5

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_aoi_from_ee("{}/sumatra_poc_aoi".format(self.ee_rootdir))



    def calc(self):
        
        hii_infrastructure_driver = ee.ImageCollection("projects/HII/v1/sumatra_poc/driver/infrastructure/hii_infrastructure_driver").sort('system:index',False).first()
        hii_landuse_driver = ee.ImageCollection("projects/HII/v1/sumatra_poc/driver/landuse/hii_landuse_driver").sort('system:index',False).first()
        hii_popdens_driver = ee.ImageCollection("projects/HII/v1/sumatra_poc/driver/popdens/hii_popdens_driver").sort('system:index',False).first()
        hii_power_driver = ee.ImageCollection("projects/HII/v1/sumatra_poc/driver/power/hii_power_driver").sort('system:index',False).first()
        hii_water_driver = ee.ImageCollection("projects/HII/v1/sumatra_poc/driver/water/hii_water_driver").sort('system:index',False).first()



        hii = hii_infrastructure_driver\
                  .add(hii_landuse_driver)\
                  .add(hii_popdens_driver)\
                  .add(hii_power_driver)\
                  .add(hii_water_driver)

        

                                          

        self.export_image_ee(ee.Image(hii), '{}/{}'.format(self.ee_driverdir, 'weighted_hii'))

    def check_inputs(self):
        super().check_inputs()
        # add any task-specific checks here, and set self.status = self.FAILED if any fail


if __name__ == "__main__":
    weightedsum_task = HIIWeightedsum()
    weightedsum_task.run()
