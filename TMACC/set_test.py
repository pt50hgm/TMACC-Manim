from TMACC_ANIM import *
from manim import *

class MainAnim(TMACCAnim):
    # Set FOR_SLIDESHOW to false for Instagram video format
    # Adds Logo and Outro
    def __init__(self, **kwargs):
        super().__init__(FOR_SLIDESHOW=False, **kwargs)

    # Add all animation logic here
    # Separate slides using next_section()
    def main(self):
        mSet = MSet([1, 2, 4, 2, 4]).shift(UP)
        
        label = NewText("my_set = ", color=1, textSize=1).next_to(mSet.valueText)
        setGroup = AxisContainer(label, mSet, componentDir=RIGHT)
        self.play(
            mSet.Create(),
            FadeIn(label),
            run_time=1
        )

        self.wait()
        self.next_slide()
        self.next_section(skip_animations=False)
        codeText = NewText(
            "my_set = 8",
            overrideTheme="code",
            textSize=1
        ).shift(DOWN)
        self.play(
            Create(codeText),
        )

        # self.wait()
        # playAnim, resolveAnim = mArray.set(1, "8")
        # self.play(
        #     playAnim
        # )