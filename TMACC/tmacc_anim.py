from manim import *
from manim_slides import Slide

from enum import Enum

# Theme Dictionary contains all text and color formatting
THEME = {
    "default": {
        "color": "#ffffff",
        "stroke_width": 2,
        "color": [WHITE],
        "text_font": "Arial",
        "text_size": 48
    },
    "main": {
        "color": [WHITE, RED, GREEN, YELLOW, BLUE],
        "text_font": "Arial",
        "stroke_width": 4,
        "text_size": [60, 48, 36, 28]
    },
    "title": {
        "text_font": "Arial",
        "text_size": [120, 80]
    },
    "code": {
        "color": [WHITE, RED, GREEN, YELLOW, BLUE],
        "text_font": "Cascadia Code",
        "text_size": [60, 48, 36, 28]
    },
    "placeholder": {
        "stroke_width": 0
    }
}

# Current Theme takes priority over default
currentTheme = THEME["main"]


def ensure_iterable(*items):
    if len(items) == 1 and hasattr(items[0], "__iter__") and not isinstance(items[0], (str, bytes)):
        return list(items[0])
    return list(items)

# Returns property with the current themes applied
def GetThemeProp(prop:str, overrideTheme:str=""):
    themes = []
    if overrideTheme:
        themes.append(THEME[overrideTheme])
    themes += [currentTheme, THEME["default"]]

    for theme in themes:
        if prop in theme:
            return theme[prop]
    return THEME["default"][prop]

# Returns the VMobject with the current theme applied to it
# overrideTheme will take priority over the currentTheme
# Color and textSize specify which one to use since a list is returned
def ApplyTheme(mobj:VMobject, overrideTheme:str="", color:int=0, textSize:int=0):
    # Apply color
    themeColor = GetThemeProp("color", overrideTheme)[color]
    mobj.set_color(themeColor)
    mobj.set_fill(themeColor)

    
    # Apply text-specific settings
    if isinstance(mobj, Text):
        new = Text(
            mobj.original_text,
            font=GetThemeProp("text_font", overrideTheme),
            font_size=GetThemeProp("text_size", overrideTheme)[textSize],
            color=GetThemeProp("color", overrideTheme)[color],
            stroke_width=0
        )
        mobj = new
    else:
        # Apply stroke width if applicable
        if hasattr(mobj, "set_stroke"):
            mobj.set_stroke(width=GetThemeProp("stroke_width", overrideTheme))
        
    # for sub in mobj.submobjects:
    #     ApplyTheme(sub, overrideTheme, color, textSize)
    
    return mobj

# Returns a placeholder transparent rectangle
# Useful for transformations to/from nothing
def GetPlaceHolder():
    return ApplyTheme(
        Rectangle(width=0.001, height=0.001, fill_opacity=0),
        "placeholder"
    )

# Returns a Text object with the theme applied
def NewText(val, **kwargs):
    return ApplyTheme(
        # Temporarily sets font to arial to avoid missing font errors
        Text(val, font="Arial"),
        **kwargs
    )

class TextBox(VGroup):
    def __init__(self, text, max_width, **kwargs):
        super().__init__()

        words = text.split()
        lines = []
        current = ""

        # Build wrapped lines
        for w in words:
            test_line = current + (" " if current else "") + w
            test_obj = NewText(test_line, **kwargs)

            if test_obj.width > max_width:
                # Commit current line
                lines.append(current)
                current = w
            else:
                current = test_line

        # Add last line
        if current:
            lines.append(current)

        # Convert lines into mobjects
        for line in lines:
            self.add(NewText(line, **kwargs))

        # Stack vertically
        self.arrange(DOWN, aligned_edge=LEFT, buff=0.5)

class MCamera(VGroup):
    def __init__(self):
        super().__init__()
        self.frameWidth = 14
        self.originalWidth = 14
        self.scaleFactor = 1.0
        self.add(Square(100).set_opacity(0))
        self.move_to(ORIGIN)

    def cam_move_to_and_zoom(self, target, width):
        factor = width / self.frameWidth
        self.frameWidth = width
        self.scaleFactor *= 1/factor
        return self.animate.scale(1/factor).move_to(-target)
    
    def cam_set_width(self, width):
        factor = width / self.frameWidth
        self.frameWidth = width
        self.scaleFactor *= 1/factor
        return self.animate.scale(1/factor)
        
    def cam_move_to(self, target):
        return self.animate.move_to(-target)
    
    def cam_add(self, *objs):
        for mob in objs:
            mob.scale(self.scaleFactor)
            mob.move_to((mob.get_center()) * self.scaleFactor)
            mob.shift(self.get_center())
            
            self.add(mob)


# TMACC Animations Wrapper Class
class TMACCAnim(Slide):
    def __init__(self, FOR_SLIDESHOW=False, **kwargs):
        super().__init__(**kwargs)
        self.FOR_SLIDESHOW = FOR_SLIDESHOW
        self.LOGO_ALPHA = 0.5

    def main(self):
        pass

    # CLI runs this method
    def construct(self):
        # Set background and logo
        self.bg = ImageMobject(
            r"Assets\Images\wavydarkbackground.webp"
        ).set(height=8).set_opacity(0)
        self.logo = ImageMobject(
            r"Assets\Images\tmacc-logo-circular-inkscape.png"
        ).set(width=1.5)\
        .to_corner(DOWN+RIGHT).shift((DOWN+RIGHT)*0.25)\
        .set_opacity(self.LOGO_ALPHA)

        self.add(self.bg)
        self.play(FadeIn(self.logo))

        # Play the main animation
        self.main()

        # Play the outro
        if not self.FOR_SLIDESHOW:
            self.outro()
        
        
    def outro(self):
        self.wait()
        titleText = NewText("Follow Us", overrideTheme="title", textSize=1, color=1)\
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
        self.wait(duration=3)
        self.play(FadeOut(titleText, discord, insta, text1, text2))

class TMACCSlide:
    def __init__(self, tmaccAnim:TMACCAnim, *components):
        super().__init__()

        self.tmaccAnim = tmaccAnim
        components = ensure_iterable(*components)
        self.components = Group(*components)
        

    def play(self):
        if not self: return

        self.tmaccAnim.play(
            LaggedStart(
                AnimationGroup(
                    self.tmaccAnim.bg.animate.set_opacity(1),
                    self.tmaccAnim.logo.animate.set_opacity(self.tmaccAnim.LOGO_ALPHA),
                    FadeIn(self.components[0])
                ),
                *[FadeIn(item) for item in self.components[1:]],
                lag_ratio=0.5
            )
        )


        self.tmaccAnim.wait()
        self.tmaccAnim.next_slide()
        self.tmaccAnim.next_section()
        
        self.tmaccAnim.play(
            self.tmaccAnim.bg.animate.set_opacity(0),
            FadeOut(self.components)
        )

class AxisContainer(VGroup):
    def __init__(self, *components, componentDir=DOWN, spacing=0.5):
        super().__init__()

        components = ensure_iterable(*components)

        # Choose internal container
        if any(isinstance(c, ImageMobject) for c in components):
            self.container = Group(*components)
        else:
            self.container = VGroup(*components)

        self.add(self.container)

        if not type(spacing) is list:
            spacing = [0.5]*len(components)
        
        Pos = [item.get_center() for item in self.container]

        for i in range(len(self.container)-1):
            self.container[i+1].next_to(self.container[i], componentDir, spacing[i])

        for i in range(len(Pos)):
            if componentDir is DOWN:
                self.container[i].set_x(Pos[i][0])
            else:
                self.container[i].set_y(Pos[i][1])

        self.container.move_to(ORIGIN)

class MBulletedList(Group):
    def __init__(self, *bullets):
        super().__init__()
        bullets = ensure_iterable(*bullets)
        
        for bullet in bullets:
            text = NewText("- " + bullet, textSize=2, color=0)
            self.add(text)
        self.arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        

def MapListStr(arr):
    res = arr[:]
    for i in range(len(arr)):
        if type(arr[i]) is int:
            res[i] = str(arr[i])  
    return res

# Manim Array Class
# set, append, pop methods return [playAnimation, resolveAnimation]
# eg. use self.play(playAnimation)
class MArray(VGroup):
    def __init__(self, init:list[str], **kwargs):
        super().__init__()
        self.length = len(init)
        self.textArgs = kwargs
        self.numberRow = MNumberRow(init, spacing=0.75, **self.textArgs)
        self.valueText = self.numberRow.valueText
        self.indexText = VGroup()
        self.squares = VGroup()
        self.add(self.squares, self.indexText, self.numberRow)

        for i in range(self.length):
            value = self.valueText[i]
            square = ApplyTheme(Square(side_length=1))\
                .move_to(value)
            self.squares.add(square)

            indexText = NewText(str(i), color=2, textSize=2)\
                .move_to(value).shift(UP)
            self.indexText.add(indexText)

        self.move_to(ORIGIN)
    
    def setI(self, i:int, val:str):
        return self.numberRow.setI(i, val)

    def append(self, val:str):
        self.length += 1
        i = self.length-1

        valueTextPlayAnim, valueTextResolveAnim = self.numberRow.append(val)
        valueText = self.numberRow.valueText[-1]

        square = ApplyTheme(
            Square(side_length=1)\
                .move_to(self.valueText[-1]),
            color=1
        )
        
        
        indexText = NewText(str(i), color=2, textSize=2)\
            .move_to(valueText).shift(UP)

        self.squares.add(square)
        self.indexText.add(indexText)

        return [
            AnimationGroup(
                Create(square), 
                Create(indexText),
                valueTextPlayAnim
            ),
            AnimationGroup(
                square.animate.set_color(GetThemeProp("color")[0]),
                valueTextResolveAnim
            )
        ]

    def pop(self):
        i = self.length-1
        self.length -= 1
        anims = [
            AnimationGroup(
                Uncreate(self.squares[i]), 
                Uncreate(self.valueText[i]),
                Uncreate(self.indexText[i])
            ),
            Animation(Mobject())
        ]
        self.squares.remove(self.squares[i])
        self.valueText.remove(self.valueText[i])
        self.indexText.remove(self.indexText[i])
        return anims

# Manim Row of Numbers Class
# set, highlight, show/hide/move cursor methods return [playAnimations, resolveAnimations]
# eg. use self.play(*playAnimations)
class MNumberRow(VGroup):
    def __init__(self, init:list[str], spacing=0.5, **kwargs):
        super().__init__()
        init = MapListStr(init)
        self.buff = spacing
        self.textArgs = kwargs

        self.values = init[:]
        self.valueText = VGroup()
        for num in init:
            self.valueText.add(
                NewText(num,
                    **self.textArgs,
                )
            )
        self.valueText.arrange(RIGHT, buff=self.buff)
        self.add(self.valueText)
        self.valueText.arrange(RIGHT, buff=self.buff)
        self.valueText.move_to(ORIGIN)

        self.cursor = ApplyTheme(
            Rectangle(height=0.08, width=0.6, fill_opacity=1),
            color=2
        )
        
    def setI(self, i:int, val:str):
        text = NewText(val, **self.textArgs)\
                .move_to(self.valueText[i])\
                .set_color(GetThemeProp("color")[1])\
                    if val else GetPlaceHolder()
        
        self.values[i] = val
        anims = [
            ReplacementTransform(
                self.valueText[i],
                text
            ),
            text.animate.set_color(GetThemeProp("color")[0])
        ]
        return anims
    def append(self, val:str):
        valueText = NewText(val, **self.textArgs)
        if len(self.values) > 1:
            valueText.next_to(self.valueText[-1], RIGHT, buff=self.buff)
        self.values.append(val)
        self.valueText.add(valueText)
        
        return [
            Create(valueText),
            valueText.animate.set_color(GetThemeProp("color")[0])
        ]
    def remove(self, i):
        return AnimationGroup(
            ReplacementTransform(
                self.valueText[i],
                GetPlaceHolder()
            ),
            self.animate.arrange(RIGHT, buff=self.buff)
        )

    def highlight(self, i):
        playAnims, resolveAnims = self.setI(i, self.values[i])
        return [playAnims, resolveAnims]

    def showCursor(self, i):
        return FadeIn(self.cursor.next_to(self.valueText[i], DOWN))
    def hideCursor(self):
        return FadeOut(self.cursor)
    def moveCursor(self, i):
        return self.cursor.animate.next_to(self.valueText[i], DOWN)

class MSet(AxisContainer):
    def __init__(self, init:list[str], **kwargs):
        self.vals = set(init)
        init = list(self.vals)
        self.valueText = MNumberRow(init)
        self.bracket1 = NewText("{", **kwargs)
        self.bracket2 = NewText("}", **kwargs)

        super().__init__(self.bracket1, self.valueText, self.bracket2, componentDir=RIGHT, **kwargs)

    def Create(self):
        return Succession(
            FadeIn(self.bracket1),
            Create(self.valueText),
            FadeIn(self.bracket2),
        )

    def append(num):
        pass
    