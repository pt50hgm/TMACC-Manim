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
        mArray = MArray(['0']*6, "my_array = ").shift(UP)
        self.play(
            LaggedStart(
                Create(mArray.items),
                lag_ratio=0.5
            ),
            run_time=1
        )
        self.play(
            FadeIn(mArray.label),
            mArray.animate.shift(RIGHT*mArray.label.width/2)
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
        playAnims, resolveAnims = mArray.set(1, "8")
        self.play(
            *playAnims
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
            *resolveAnims,
            Create(codeText),
        )

        self.wait()
        playAnims, resolveAnims = mArray.append("3")
        self.play(
            *playAnims
        )


        self.wait()
        self.next_slide()
        self.next_section(skip_animations=False)
        self.play(
            FadeOut(mArray),
            FadeOut(codeText)
        )
        
        caption = NewText(
            "Frequency List:",
            textSize=1,
            color=1
        ).shift(DOWN)
        numsRow = MNumberRow("3 6 1 3 4 4 1 2".split()).next_to(caption, DOWN)
        self.play(
            Succession(
                FadeIn(caption),
                Create(numsRow)
            )
        )

        self.wait()
        mArray = MArray(['0']*8, "freq = ").shift(UP)
        self.play(
            Create(mArray.items),
            FadeIn(mArray.label)
        )


        self.wait()
        self.next_slide()
        self.next_section(skip_animations=False)
        freq = [0]*8

        prevArrayResolveAnims = [Animation(Mobject())]
        for i, val in enumerate(numsRow.items):
            numsPlayAnims, numsResolveAnims = numsRow.highlight(i)
            freq[int(val)] += 1
            arrayPlayAnims, arrayResolveAnims = mArray.set(int(val), str(freq[int(val)]))
            self.play(
                *numsPlayAnims,
                numsRow.showCursor(0) if i == 0 else numsRow.moveCursor(i)
            )
            self.play(
                *prevArrayResolveAnims,
                *arrayPlayAnims,
            )
            self.wait(duration=max(0.01, 0.5-i*0.1))
            prevArrayResolveAnims = arrayResolveAnims[:]
        self.play(
            numsRow.hideCursor(),
            *prevArrayResolveAnims
        )


        self.wait()
        self.next_slide()
        self.next_section(skip_animations=False)
        self.play(
            FadeOut(mArray, numsRow, caption)
        )

