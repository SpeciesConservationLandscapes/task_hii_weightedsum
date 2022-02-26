HII WEIGHTED SUM TASK
---------------------

This task adds the most recent Human Impact drivers for the specified date together, producing the final 
synthetic index dataset representing anthropogenic impact on the Earth's terrestrial surface: 
the Human Impact Index (HII). For more information, see [citation TBD].

## HII value ranges

Each of the drivers have a minimum value of 0 and a maximum value of 10 
(though note the data is multiplied by 100 and stored as an integer to optimize precision and storage; 
actual values are thus 0-1000 for each driver). This task adds them together without weighting them 
(despite the task name), because the drivers themselves already have weights built in -- i.e. each driver's
theoretical 0-10 range is absolute, not normalized, so that a value can be compared across drivers; thus the actual
maximum weight from a driver (e.g. navigable water) can be less than 10. 

Similarly, this task does not normalize. Therefore, the theoretical minimum and maximum values for HII on a 
given date are 0 and (10 * [number of drivers, currently 7]) respectively. In practice, however, because no single cell has 
a maximum value from all drivers, and because drivers are not normalized and so do not all have a maximum of 10, 
the actual maximum value will be more like 64.

## Drivers and output

The output HII from this task is stored in the Earth Engine ImageCollection at `projects/HII/v1/hii`. 
Like all Earth Engine images output from tasks based on 
[`task_base`](https://github.com/SpeciesConservationLandscapes/task_base), 
HII images are assigned a `system:time_start` based on the task's `self.taskdate`, 
which can be used for temporal selection and comparison.

### Drivers

| Driver | EE output path | Code |
| ------ | -------------- | ---- |
| infrastructure | projects/HII/v1/driver/infrastructure | https://github.com/SpeciesConservationLandscapes/task_hii_infrastructure |
| land use | projects/HII/v1/driver/land_use | https://github.com/SpeciesConservationLandscapes/task_hii_landuse |
| population density | projects/HII/v1/driver/population_density | https://github.com/SpeciesConservationLandscapes/task_hii_popdens |
| power | projects/HII/v1/driver/power | https://github.com/SpeciesConservationLandscapes/task_hii_power |
| railways | projects/HII/v1/driver/railways | https://github.com/SpeciesConservationLandscapes/task_hii_rail |
| roads | projects/HII/v1/driver/roads | https://github.com/SpeciesConservationLandscapes/task_hii_road |
| navigable waterways | projects/HII/v1/driver/water | https://github.com/SpeciesConservationLandscapes/task_hii_water |

## Variables and Defaults

### Environment variables
```
SERVICE_ACCOUNT_KEY=<GOOGLE SERVICE ACCOUNT KEY>
```

### Class constants

```
scale=300
```

## Usage

*All parameters may be specified in the environment as well as the command line.*

```
/app # python task.py --help
usage: task.py [-h] [-d TASKDATE] [--overwrite]

optional arguments:
  -h, --help            show this help message and exit
  -d TASKDATE, --taskdate TASKDATE
  --overwrite           overwrite existing outputs instead of incrementing
```

### License
Copyright (C) 2022 Wildlife Conservation Society
The files in this repository  are part of the task framework for calculating 
Human Impact Index and Species Conservation Landscapes (https://github.com/SpeciesConservationLandscapes) 
and are released under the GPL license:
https://www.gnu.org/licenses/#GPL
See [LICENSE](./LICENSE) for details.
