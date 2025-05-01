from manim import *
from math import cos, sin, cosh, sinh

y = FunctionGraph(cos, color=PURPLE)
dy_dx = FunctionGraph(lambda x : -sin(x), color=PURPLE_E)
d2y_dx2 = FunctionGraph(lambda x : -cos(x), color=PURPLE_E)

yh = FunctionGraph(sinh, color=PURPLE_D)
xh = FunctionGraph(cosh, color=PURPLE_D)
xh_neg = FunctionGraph(lambda x : -cosh(x), color=PURPLE_D)

ANIMATION_LIST = [
    Create(y),
    Wait(0.3),
    Create(dy_dx),
    Wait(0.3),
    Create(d2y_dx2),
    Wait(0.3),
    Create(yh),
    Wait(0.3),
    Create(xh),
    Wait(0.3),
    Create(xh_neg),
    Wait(1),
    FadeOut(d2y_dx2),
    FadeOut(dy_dx),
    FadeOut(y),
    FadeOut(yh),
    FadeOut(xh),
    FadeOut(xh_neg)
]

class WebBackground(Scene):
    def construct(self):
        for animation in ANIMATION_LIST:
            self.play(animation)

