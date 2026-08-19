from tmacc_anim import *
from manim import *

class SlideTest(TMACCAnim):
    # Set FOR_SLIDESHOW to false for Instagram video format
    # Adds Logo and Outro
    def __init__(self, **kwargs):
        super().__init__(FOR_SLIDESHOW=True, **kwargs)

    # Add all animation logic here
    # Separate slides using next_section()
    def main(self):
        self.next_section(skip_animations=False)

        self.text_slide(
            title="Schedule",
            bullets=[
                "6:10: Event Introduction + Overview",
                "6:35: Let's start coding!",
                "7:00: Snacks!",
                "7:20: Event over! Time for solutions.",
            ]
        )
        self.text_slide(
        title="Schedule",
        bullets=[
            "6:10: Event Introduction + Overview",
            "6:35: Let's start coding!",
            "7:00: Snacks!",
            "7:20: Event over! Time for solutions.",
        ]
    )