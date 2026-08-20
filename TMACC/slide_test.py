from tmacc_anim import *
from manim import *


"""
To Export as .html:

manim-slides render slide_test.py SlideTest
manim-slides convert SlideTest slide_test.html
"""
class SlideTest(TMACCAnim):
    # Set FOR_SLIDESHOW to false for Instagram video format
    # Adds Logo and Outro
    def __init__(self, **kwargs):
        super().__init__(FOR_SLIDESHOW=True, **kwargs)

    # Add all animation logic here
    # Separate slides using next_section()
    def main(self):
        self.next_section(skip_animations=False)
        TMACCSlide(
            self,
            AxisContainer(
                TextBox("TMACC: Road To Leetcode!", max_width=8, overrideTheme="title", color=2),
                ImageMobject(
                    r"Assets\Images\stock-coding-graphic.png"
                ).set(width=5),
                componentDir=RIGHT,
                spacing=0
            )
        ).play()

        TMACCSlide(
            self,
            AxisContainer(
                NewText("Schedule").to_edge(LEFT),
                SBulletedList(
                    "6:10: Event Introduction + Overview",
                    "6:35: Let's start coding!",
                    "7:00: Snacks!",
                    "7:20: Event over! Time for solutions."
                ),
                spacing=[1]
            ).to_edge(UL)
        ).play()

        TMACCSlide(
            self,
            AxisContainer(
                NewText("What is Leetcode?").to_edge(LEFT),
                ImageMobject(r"Assets\Images\leetcode.png").set(width=12)
            ).to_edge(UL)
        ).play()

        TMACCSlide(
            self,
            AxisContainer(
                NewText("NeetCode Roadmap (Part 1)"),
                ImageMobject(r"Assets\Images\neetcode-roadmap1.png").set(width=6),
                NewText("Source: https://neetcode.io", textSize=1, color=1),
                spacing=[0.5,0]
            ),
        ).play()

        TMACCSlide(
            self,
            AxisContainer(
                NewText("NeetCode Roadmap (Part 2)"),
                ImageMobject(r"Assets\Images\neetcode-roadmap2.png").set(width=5),
                NewText("One problem: NeetCode is not entirely free!", textSize=2, color=1),
                NewText("Goal of LeetCode Roadmap:\nGo over each topic throughout the year.", textSize=2, color=2),
                spacing=[0.25, 0.1, 0.1]
            )
        ).play()
        
        TMACCSlide(
            self,
            AxisContainer(
                TextBox("Welcome to Road to LeetCode!", max_width=9, overrideTheme="title", textSize=1, color=2).to_edge(LEFT),
                NewText("Week 1: Arrays and Range Queries", textSize=1).to_edge(LEFT),
                spacing=2
            ).to_edge(LEFT)
        ).play()
                
        


    