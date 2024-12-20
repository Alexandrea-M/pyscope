"""telrun test docstring

This is a test docstring for the telrun module."""

# isort: skip_file

import logging

logger = logging.getLogger(__name__)

from .boundary_condition import BoundaryCondition
from .coord_condition import CoordinateCondition
from .hourangle_condition import HourAngleCondition
from .airmass_condition import AirmassCondition
from .sun_condition import SunCondition
from .moon_condition import MoonCondition
from .time_condition import TimeCondition
from .snr_condition import SNRCondition

from .field import Field
from .light_field import LightField
from .autofocus_field import AutofocusField
from .dark_field import DarkField
from .flat_field import FlatField
from .transition_field import TransitionField

from .option import Option
from .instrument_configuration import InstrumentConfiguration

from ._block import _Block
from .schedule_block import ScheduleBlock
from .calibration_block import CalibrationBlock
from .unallocated_block import UnallocatedBlock

from .observer import Observer
from .project import Project

from .prioritizer import Prioritizer
from .optimizer import Optimizer

from .queue import Queue
from .schedule import Schedule
from .scheduler import Scheduler


from .telrun_exception import TelrunException
from .exoplanet_transits import exoplanet_transits
from .init_telrun_dir import init_telrun_dir
from .mk_mosaic_schedule import mk_mosaic_schedule
from .rst import rst
from . import sch, schedtab, reports
from .schedtel import schedtel, plot_schedule_gantt, plot_schedule_sky
from .startup import start_telrun_operator
from .survey_builder import survey_builder
from .telrun_operator import TelrunOperator

__all__ = [
    "BoundaryCondition",
    "CoordinateCondition",
    "HourAngleCondition",
    "AirmassCondition",
    "SunCondition",
    "MoonCondition",
    "TimeCondition",
    "SNRCondition",
    "Field",
    "LightField",
    "AutofocusField",
    "DarkField",
    "FlatField",
    "TransitionField",
    "Option",
    "InstrumentConfiguration",
    "_Block",
    "ScheduleBlock",
    "CalibrationBlock",
    "UnallocatedBlock",
    "Observer",
    "Project",
    "Prioritizer",
    "Optimizer",
    "Queue",
    "Schedule",
    "Scheduler",
    "exoplanet_transits",
    "init_telrun_dir",
    # "mk_mosaic_schedule",
    # "rst",
    # "sch",
    # "schedtab",
    # "schedtel",
    # "reports",
    # "plot_schedule_gantt",
    # "plot_schedule_sky",
    "start_telrun_operator",
    "survey_builder",
    "TelrunOperator",
    "TelrunException",
]
