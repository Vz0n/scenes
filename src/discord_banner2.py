# This code generates a simple animation of a conic section and its first derivative.
# I made it because I can't use the paraboloid in HD resolution as banner because exceeds Discord's file size limits.

from manim import *

DEFAULT_RANGE = [-25, 25, 1]
TEXT_POSITION = (2.5, 1, 0)

def parabola(x):
    return x**2 + 2*x + 1

def dy(x):
    return 2*x + 2

class DiscordBanner(Scene):
    def construct(self):
        cart_plane = Axes(x_range=DEFAULT_RANGE, y_range=DEFAULT_RANGE)

        func_text = MathTex("y = (x+1)^2").move_to(TEXT_POSITION).scale(0.8)
        dydx_text = MathTex("\\frac{dy}{dx} = 2(x+1)").move_to(TEXT_POSITION).scale(0.8)

        ANIMATIONS = [
            Create(cart_plane),
            Create(cart_plane.plot(parabola, color=PURPLE)),
            Wait(0.5),
            Create(func_text),
            Wait(0.5),
            FadeOut(func_text),
            Create(cart_plane.plot(dy, color=PURPLE)),
            Create(dydx_text),
            Wait(2)
        ]

        for anim in ANIMATIONS:
            self.play(anim)