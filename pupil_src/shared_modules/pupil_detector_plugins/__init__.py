"""
(*)~---------------------------------------------------------------------------
Pupil - eye tracking platform
Copyright (C) 2012-2020 Pupil Labs

Distributed under the terms of the GNU
Lesser General Public License (LGPL v3.0).
See COPYING and COPYING.LESSER for license details.
---------------------------------------------------------------------------~(*)
"""
import logging
import traceback
import typing as T

from .detector_2d_plugin import Detector2DPlugin
from .detector_base_plugin import EVENT_KEY, PupilDetectorPlugin

logger = logging.getLogger(__name__)


def available_detector_plugins() -> T.List[T.Type[PupilDetectorPlugin]]:
    """Load and list available plugins

    Returns list of all detectors.
    """

    all_plugins: T.List[T.Type[PupilDetectorPlugin]] = [Detector2DPlugin]

    try:
        from .pye3d_plugin import Pye3DPlugin
    except ImportError:
        logger.info("Refraction corrected 3D pupil detector not available!")
        logger.debug(traceback.format_exc())
    else:
        logger.info("Using refraction corrected 3D pupil detector.")
        all_plugins.append(Pye3DPlugin)

    return all_plugins
