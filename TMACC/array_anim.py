from TMACC_ANIM import *
from manim import *

class ArrayAnim(TMACCAnim):
    # Set FOR_SLIDESHOW to false for Instagram video format
    # Adds Logo and Outro
    def __init__(self, **kwargs):
        super().__init__(FOR_SLIDESHOW=False, **kwargs)

    # Add all animation logic here
    # Separate slides using next_section()
    def main(self):
        self.next_section(skip_animations=False)
        codeText = NewText(
            "my_array = [0, 0, 0, 0, 0, 0]",
            overrideTheme="code",
            textSize=1
        ).shift(DOWN)
        self.play(
            Create(codeText)
        )

        self.wait()
        mArray = MArray(['0']*6).shift(UP)
        self.play(
            LaggedStart(
                Create(mArray),
                lag_ratio=0.5
            ),
            run_time=1
        )

        label = NewText("my_array = ", color=1, textSize=1)
        label.next_to(mArray.valueText, LEFT, buff=1)
        arrayGroup = VGroup(label, mArray)
        self.play(
            FadeIn(label),
            arrayGroup.animate.shift(LEFT * arrayGroup.get_x())
        )


        self.wait()
        self.next_slide()
        self.next_section(skip_animations=False)
        self.play(
            FadeOut(codeText)
        )
        codeText = NewText(
            "my_array[1] = 8",
            overrideTheme="code",
            textSize=1
        ).shift(DOWN)
        self.play(
            Create(codeText),
        )

        self.wait()
        playAnim, resolveAnim = mArray.setI(1, "8")
        self.play(
            playAnim
        )


        self.wait()
        self.next_slide()
        self.next_section(skip_animations=False)
        self.play(
            FadeOut(codeText)
        )
        codeText = NewText(
            "my_array.append(3)",
            overrideTheme="code",
            textSize=1
        ).shift(DOWN)
        self.play(
            resolveAnim,
            Create(codeText),
        )

        self.wait()
        playAnim, resolveAnim = mArray.append("3")
        self.play(
            playAnim
        )


        self.wait()
        self.next_slide()
        self.next_section(skip_animations=False)
        self.play(
            FadeOut(arrayGroup),
            FadeOut(codeText)
        )
        
        caption = NewText(
            "Frequency List:",
            textSize=1,
            color=1
        ).shift(DOWN)
        numsRow = MNumberRow(
            "3 6 1 3 4 4 1 2".split(),
            textSize=1
        ).next_to(caption, DOWN)
        self.play(
            Succession(
                FadeIn(caption),
                Create(numsRow)
            )
        )

        self.wait()
        mArray = MArray(['0']*8)
        label = NewText("freq = ", color=1, textSize=1).next_to(mArray.valueText)
        arrayGroup = AxisContainer(label, mArray, componentDir=RIGHT).shift(UP)

        self.play(
            Create(mArray),
            FadeIn(label)
        )


        self.wait()
        self.next_slide()
        self.next_section(skip_animations=False)
        freq = [0]*8

        prevArrayResolveAnim = [Animation(Mobject())]
        for i, val in enumerate(numsRow.values):
            numsPlayAnim, numsResolveAnim = numsRow.highlight(i)
            freq[int(val)] += 1
            arrayPlayAnim, arrayResolveAnim = mArray.setI(int(val), str(freq[int(val)]))
            self.play(
                numsPlayAnim,
                numsRow.showCursor(0) if i == 0 else numsRow.moveCursor(i)
            )
            self.play(
                prevArrayResolveAnim,
                arrayPlayAnim,
            )
            # self.wait(duration=max(0.04, 0.5-i*0.1))
            prevArrayResolveAnim = arrayResolveAnim
        self.play(
            numsRow.hideCursor(),
            prevArrayResolveAnim
        )


        self.wait()
        self.next_slide()
        self.next_section(skip_animations=False)
        self.play(
            FadeOut(arrayGroup, numsRow, caption)
        )

