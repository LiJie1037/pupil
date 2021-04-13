"""
(*)~---------------------------------------------------------------------------
Pupil - eye tracking platform
Copyright (C) 2012-2021 Pupil Labs

Distributed under the terms of the GNU
Lesser General Public License (LGPL v3.0).
See COPYING and COPYING.LESSER for license details.
---------------------------------------------------------------------------~(*)
"""

from plugin import System_Plugin_Base
from pyglui.cygl.utils import draw_points_norm, RGBA
from gl_utils import draw_circle_filled
from methods import denormalize


class Display_Recent_Gaze(System_Plugin_Base):
    """
    DisplayGaze shows the three most
    recent gaze position on the screen
    """

    def __init__(self, g_pool):
        super().__init__(g_pool)
        self.order = 0.8
        self.pupil_display_list = []

    def recent_events(self, events):
        frame = events.get("frame", None)
        if not frame:
            return
        frame_size = frame.width, frame.height
        for pt in events.get("gaze", []):
            point = denormalize(pt["norm_pos"], frame_size, flip_y=True)
            self.pupil_display_list.append((point, pt["confidence"] * 0.8))
        self.pupil_display_list[:-3] = []

    def gl_display(self):
        for pt, a in self.pupil_display_list:
            # This could be faster if there would be a method to also add multiple colors per point
            draw_circle_filled(
                tuple(pt),
                size=35 / 2,
                color=RGBA(1.0, 0.2, 0.4, a),
            )

    def get_init_dict(self):
        return {}
