import logging

from astropy import units as u

from .boundary_condition import BoundaryCondition

logger = logging.getLogger(__name__)


class SunCondition(BoundaryCondition):
    def __init__(
        self,
        min_sep=0 * u.deg,
        max_sep=180 * u.deg,
        min_alt=-90 * u.deg,
        max_alt=90 * u.deg,
    ):
        """ """
        pass

    def from_string(self, string):
        pass

    def __str__(self):
        pass

    def __repr__(self):
        logger.debug("SunCondition().__repr__()")
        return str(self)

    def __call__(self, time=None, location=None, target=None):
        """ """
        pass

    def plot(self, time, location, target=None, ax=None):
        """ """
        pass
