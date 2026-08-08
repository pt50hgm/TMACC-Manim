from tmacc_anim import *
from manim import *

class MainAnim(TMACCAnim):
    # Set FOR_SLIDESHOW to false for Instagram video format
    # Adds Logo and Outro
    def __init__(self, **kwargs):
        super().__init__(FOR_SLIDESHOW=False, **kwargs)

    # Add all animation logic here
    # Separate slides using next_section()
    def main(self):
        nums = [2, 1, 4, 6, 3, 5]
        PSA = [0]*len(nums)

        self.next_section(skip_animations=False)
        codeText = NewText(f'{nums = }', overrideTheme="code", textSize=1).shift(DOWN*2)
        self.play(Create(codeText))
        self.wait()

        mArray = MArray(list(map(str, nums)), "nums = ").shift(UP*2)
        self.play(LaggedStart(Create(mArray.items), lag_ratio=0.5), run_time=1)
        self.play(FadeIn(mArray.label), mArray.animate.shift(RIGHT*mArray.label.width/2))
        self.wait()

        self.play(FadeOut(codeText))
        self.wait()

        codeText = NewText(f'{PSA = }', overrideTheme="code", textSize=1).shift(DOWN*2)
        self.play(Create(codeText))
        self.wait()

        mArray2 = MArray(list(map(str, PSA)), "PSA = ")
        self.play(LaggedStart(Create(mArray2.items), lag_ratio=0.5), run_time=1)
        self.play(FadeIn(mArray2.label), mArray2.animate.shift(RIGHT*mArray2.label.width/2))
        self.wait()

        self.play(FadeOut(codeText))
        self.wait()

        self.play(FadeOut(mArray, mArray2))
        self.wait()
