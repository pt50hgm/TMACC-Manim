from manim import *

THEME = {
    "default": {
        "color": "#ffffff",
        "stroke_width": 2,
        "text_color": WHITE,
        "text_font": "Arial",
        "text_size": 48
    },
    "main": {
        "color": [WHITE, RED, GREEN, YELLOW, BLUE],
        "text_font": "Arial",
        "stroke_width": 4,
        "text_size": [60, 48, 36, 24]
    },
    "code": {
        "color": [WHITE, RED, GREEN, YELLOW, BLUE],
        "text_font": "Cascadia Code",
        "text_size": [60, 48, 36, 18]
    },
    "placeholder": {
        "stroke_width": 0
    }
}

currentTheme = THEME["main"]

def GetThemeProp(prop:str, overrideTheme:str=""):
    themes = []
    if overrideTheme:
        themes.append(THEME[overrideTheme])
    themes += [currentTheme, THEME["default"]]

    for theme in themes:
        if prop in theme:
            return theme[prop]
    return THEME["default"][prop]

def ApplyTheme(mobj:VMobject, overrideTheme:str="", color:int=0, textSize:int=0):
    # Apply color
    themeColor = GetThemeProp("color", overrideTheme)[color]
    mobj.set_color(themeColor)
    mobj.set_fill(themeColor)

    # Apply stroke width if applicable
    if hasattr(mobj, "set_stroke"):
        mobj.set_stroke(width=GetThemeProp("stroke_width", overrideTheme))

    # Apply text-specific settings
    if isinstance(mobj, Text):
        new = Text(
            mobj.original_text,
            font=GetThemeProp("text_font", overrideTheme),
            font_size=GetThemeProp("text_size", overrideTheme)[textSize],
            color=GetThemeProp("text_color", overrideTheme)
        )
        mobj = new
    
    for sub in mobj.submobjects:
        ApplyTheme(sub, overrideTheme, color)
    
    return mobj

def GetPlaceHolder():
    return ApplyTheme(
        Rectangle(width=0.001, height=0.001, fill_opacity=0),
        "placeholder"
    )

def NewText(val, **kwargs):
    return ApplyTheme(
        Text(val, font="Arial"),
        **kwargs
    )

class TMACCAnim(Scene):
    def __init__(self, FOR_SLIDESHOW=False, **kwargs):
        super().__init__(**kwargs)
        self.FOR_SLIDESHOW = FOR_SLIDESHOW

    def main(self):
        pass

    def construct(self):
        if not self.FOR_SLIDESHOW:
            logo = ImageMobject(
                r"Assets\Images\tmacc-logo-circular-inkscape.png"
            ).set(width=1.5)\
            .to_corner(DOWN+RIGHT).shift((DOWN+RIGHT)*0.25)\
            .set_opacity(0.5)
            self.add(logo)

        self.main()

        if not self.FOR_SLIDESHOW:
            self.outro()
        

    def outro(self):
        titleText = NewText("Follow Us", textSize=0, color=1)\
        .shift(UP*2.5)
        discord = ImageMobject(
            r"Assets\Images\discord.png"
        ).set(height=1.5)\
        .shift(LEFT*2)
        insta = ImageMobject(
            r"Assets\Images\instagram.png"
        ).set(height=1.5)\
        .shift(RIGHT*2)
        self.play(FadeIn(titleText, discord, insta))
        
        text1 = NewText("linktr.ee/torontometacc", textSize=3)\
        .next_to(discord, DOWN)
        text2 = NewText("tmu_acc", textSize=3)\
        .next_to(insta, DOWN)
        self.play(FadeIn(text1, text2))
        self.wait()

        

        

class MArray(VGroup):
    def __init__(self, init:list[str], label=""):
        super().__init__()
        self.length = len(init)

        self.label = ApplyTheme(Text(label), color=1, textSize=1) if label else GetPlaceHolder()
        self.valueText = VGroup()
        self.indexText = VGroup()
        self.squares = VGroup()
        self.items = VGroup(self.squares, self.valueText, self.indexText)
        self.add(self.label, self.items)

        for i in range(self.length):
            square = ApplyTheme(Square(side_length=1))
            self.squares.add(square)
        self.squares.arrange(RIGHT, buff=0)
        self.squares.move_to(ORIGIN)

        for i in range(self.length):
            square = self.squares[i]
            valueText = NewText(init[i], textSize=1).move_to(square)
            indexText = NewText(str(i), color=2, textSize=2)\
                .move_to(square).shift(UP)
            self.valueText.add(valueText)
            self.indexText.add(indexText)
        
        self.label.next_to(self.squares[0], LEFT*self.label.width/2)

    def set(self, i:int, val:str):
        text = NewText(val, textSize=1, color=1)\
                .move_to(self.squares[i])\
                    if val else GetPlaceHolder()
        return [
            [
                ReplacementTransform(
                    self.valueText[i],
                    text
                )
            ],
            [text.animate.set_color(GetThemeProp("color")[0])]
        ]

    def append(self, val:str):
        self.length += 1
        i = self.length-1
        square = ApplyTheme(
            Square(side_length=1)\
                .move_to(self.squares[i-1])\
                .shift(RIGHT),
            color=1
        )
        valueText = NewText(val, textSize=1).move_to(square)
        indexText = NewText(str(i), color=2, textSize=2)\
            .move_to(square).shift(UP)
        self.squares.add(square)
        self.valueText.add(valueText)
        self.indexText.add(indexText)
        return [
            [
                Create(square), 
                Create(valueText),
                Create(indexText)
            ],
            [square.animate.set_color(GetThemeProp("color")[0])]
        ]

    def pop(self):
        i = self.length-1
        self.length -= 1
        playAnims = [
            Uncreate(self.squares[i]), 
            Uncreate(self.valueText[i]),
            Uncreate(self.indexText[i])
        ]
        self.squares.remove(self.squares[i])
        self.valueText.remove(self.valueText[i])
        self.indexText.remove(self.indexText[i])
        return playAnims

class MNumberRow(VGroup):
    def __init__(self, init:list[str]):
        super().__init__()
        self.items = init[:]
        for num in init:
            self.add(
                NewText(num,
                    textSize=1,
                ).shift(DOWN*2)
            )
        self.arrange(RIGHT, buff=0.5)
        self.move_to(ORIGIN)
        self.cursor = ApplyTheme(
            Rectangle(height=0.08, width=0.6, fill_opacity=1),
            color=2
        )
    
    def set(self, i:int, val:str):
        text = NewText(val, textSize=1, color=1)\
                .move_to(self[i])\
                    if val else GetPlaceHolder()
        return [
            [
                ReplacementTransform(
                    self[i],
                    text
                )
            ],
            [text.animate.set_color(GetThemeProp("color")[0])]
        ]

    def highlight(self, i):
        playAnims, resolveAnims = self.set(i, self.items[i])
        return [playAnims, resolveAnims]

    def showCursor(self, i):
        return [FadeIn(self.cursor.next_to(self[i], DOWN))]
    def hideCursor(self):
        return [FadeOut(self.cursor)]
    def moveCursor(self, i):
        return [self.cursor.animate.next_to(self[i], DOWN)]

class DefaultTemplate(TMACCAnim):
    def __init__(self, **kwargs):
        super().__init__(FOR_SLIDESHOW=False, **kwargs)
    
    def main(self):
        self.next_section(skip_animations=True)
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
        self.play(
            FadeOut(codeText)
        )


        self.next_section(skip_animations=True)
        self.wait()
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
        self.play(
            FadeOut(codeText)
        )


        self.next_section(skip_animations=True)
        self.wait()

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


        self.next_section(skip_animations=True)
        self.wait()
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


        self.next_section(skip_animations=True)
        self.wait()
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
            self.wait(duration=0.5)
            prevArrayResolveAnims = arrayResolveAnims[:]
        self.play(
            numsRow.hideCursor(),
            *prevArrayResolveAnims
        )

        self.next_section(skip_animations=False)
        self.wait()
        self.play(
            FadeOut(mArray, numsRow, caption)
        )

