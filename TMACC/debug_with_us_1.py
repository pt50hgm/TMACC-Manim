from TMACC_ANIM import *
from manim import *

def fizzBuzz(n: int) -> list[str]:
    answer = list()
    i = 1
    while i < n:
        if i % 3 == 0:
            answer.append("Fizz")
        elif i % 5 == 0:
            answer.append("Buzz")
        elif i % 3 == 0 and i % 5 == 0:
            answer.append("FizzBuzz")
        else:
            answer.append(str(i))
        i += 1
    return answer

class MainAnim(TMACCAnim):
    # Set FOR_SLIDESHOW to false for Instagram video format
    # Adds Logo and Outro
    def __init__(self, **kwargs):
        super().__init__(FOR_SLIDESHOW=False, **kwargs)

    # Add all animation logic here
    # Separate slides using next_section()
    def main(self):
        allowSkip = False
        cam = MCamera()

        self.next_section(skip_animations=True&allowSkip)

        code = MCode(
            NewMarkupText("""
def [1]fizzBuzz[/1](n: int) -> list[str]:
    Answer = list()
    i = 1
    [1]while[/1] i < n:
        [1]if[/1] i % 3 == 0:
            answer.[1]append[/1]([2]"Fizz"[/2])
        [1]elif[/1] i % 5 == 0:
            answer.[1]append[/1]([2]"Buzz"[/2])
        [1]elif[/1] i % 3 == 0 and i % 5 == 0:
            answer.[1]append[/1]([2]"FizzBuzz"[/2])
        [1]else[/1]:
            answer.[1]append[/1](str(i))
        i += 1
    [1]return[/1] answer
            """.strip(), spacing=0.2,
                overrideTheme="code", color=0, textSize=3
            ),
            camera=cam
        )
        cam.cam_add(code)

        self.play(
            Create(code),
            run_time=1
        )


        self.wait()
        self.next_slide()
        self.next_section(skip_animations=True&allowSkip)

        caption = NewText("NameError?", textSize=1).move_to(LEFT*5)
        self.play(FadeIn(caption))

        self.play(
            Succession(
                code.highlight_line(1),
                Wait(1.5),
                code.replace_line(1, "    answer = list()"),
                Wait(1.5),
                AnimationGroup(
                    code.highlight_fade_out(),
                    FadeOut(caption)
                )
            )
        )


        self.wait()
        self.next_slide()
        self.next_section(skip_animations=True&allowSkip)

        caption = NewText("n = 1 fails?", textSize=1).move_to(LEFT*5)
        self.play(FadeIn(caption))
        self.wait(1.5)
        
        self.play(code.highlight_line(0))
        codePlay = [
            (0, 2, "def [1]fizzBuzz[/1](n = [2]1[/2]) -> list[str]:"),
            (1, 1.5, "    answer = [2][][/2]"),
            (2, 1.5, ""),
            (3, 3, "    [1]while[/1] [2]1[/2] < [2]1[/2]:"),
            (-1, 4, "    [1]return[/1] [2][][/2]")
        ]

        resolveAnims = []
        for line, duration, newText in codePlay:
            prevLine = code.codeLines[line]
            self.play(
                code.highlight_line(line, duration),
                code.replace_line(line, newText) if newText else Animation(Mobject())
            )
            if newText:
                resolveAnims.append(code.replace_line(line, prevLine))
        self.play(
            code.highlight_fade_out(),
            *resolveAnims
        )


        self.wait()
        self.next_slide()
        self.next_section(skip_animations=True&allowSkip)
        
        self.play(
            Succession(
                code.highlight_line(3),
                code.replace_line(3, "    [1]while[/1] i <= n:"),
                Wait(1.5),
                code.highlight_fade_out(),
            )
        )


        self.wait()
        self.next_slide()
        self.next_section(skip_animations=True&allowSkip)

        self.play(code.highlight_line(0))
        codePlay = [
            (0, 2, "def [1]fizzBuzz[/1](n = [2]1[/2]) -> list[str]:"),
            (1, 1.5, "    answer = [2][][/2]"),
            (2, 1.5, ""),
            (3, 3, "    [1]while[/1] [2]1[/2] <= [2]1[/2]:"),
            (4, 1, ""),
            (6, 1, ""),
            (8, 1, ""),
            (10, 1, ""),
            (11, 3, '            answer.[1]append[/1]([2]"1"[/2])'),
            (-1, 4, '    [1]return[/1] [2]["1"][/2]')
        ]

        resolveAnims = []
        for line, duration, newText in codePlay:
            prevLine = code.codeLines[line]
            self.play(
                code.highlight_line(line, duration),
                code.replace_line(line, newText) if newText else Animation(Mobject())
            )
            if newText:
                resolveAnims.append(code.replace_line(line, prevLine))
        self.play(
            FadeOut(caption),
            code.highlight_fade_out(),
            *resolveAnims
        )
        

        self.wait()
        self.next_slide()
        self.next_section(skip_animations=True&allowSkip)

        caption = NewText("i = 15?", textSize=1).move_to(LEFT*5)
        self.play(
            FadeIn(caption),
            cam.cam_move_to_and_zoom(DOWN, 14*0.85)
        )
        self.wait(1.5)

        self.play(code.highlight_line(2))
        codePlay = [
            (2, 2, "    i = [2]15[/2]"),
            (3, 1.5, ""),
            (4, 3, "        [1]if[/1] [2]15[/2] % 3 == 0:"),
            (5, 2, ""),
            (-1, 4, "")
        ]
        
        resolveAnims = []
        for line, duration, newText in codePlay:
            prevLine = code.codeLines[line]
            self.play(
                code.highlight_line(line, duration),
                code.replace_line(line, newText) if newText else Animation(Mobject())
            )
            if newText:
                resolveAnims.append(code.replace_line(line, prevLine))
        self.play(
            code.highlight_fade_out(),
            *resolveAnims
        )


        self.wait()
        self.next_slide()
        self.next_section(skip_animations=False&allowSkip)

        self.play(
            code.replace_line(4, "        [1]if[/1] i % 3 == 0 and i % 5 == 0:"),
            code.replace_line(5, '            answer.[1]append[/1]([2]"FizzBuzz"[/2])'),
            code.replace_line(8, "        [1]elif[/1] i % 3 == 0:"),
            code.replace_line(9, '            answer.[1]append[/1]([2]"Fizz"[/2])'),
        )
        self.wait(1.5)


        self.wait()
        self.next_slide()
        self.next_section(skip_animations=False&allowSkip)
        
        self.play(code.highlight_line(2))
        codePlay = [
            (2, 2, "    i = [2]15[/2]"),
            (3, 1.5, ""),
            (4, 3, "        [1]if[/1] [2]15[/2] % 3 == 0 and [2]15[/2] % 5 == 0:"),
            (5, 2, ""),
            (-1, 4, "")
        ]
        
        resolveAnims = []
        for line, duration, newText in codePlay:
            prevLine = code.codeLines[line]
            self.play(
                code.highlight_line(line, duration),
                code.replace_line(line, newText) if newText else Animation(Mobject())
            )
            if newText:
                resolveAnims.append(code.replace_line(line, prevLine))
        self.play(
            FadeOut(caption),
            code.highlight_fade_out(),
            *resolveAnims
        )


        self.wait()
        self.next_slide()
        self.next_section(skip_animations=False&allowSkip)
        self.play(
            FadeOut(code)
        )