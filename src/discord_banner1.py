# This code generates a stupidly simple animation of a paraboloid surface, showing it's tangent lines (1st order partial derivatives) 
# and the gradient of the function. Nothing else

from manim import *

import numpy

TEXT_POSITION = (2.5, 5, 1.5)
DEFAULT_RANGE = (-25, 25, 1)
DEFAULT_UV_RANGE = (-25, 25)

def paraboloid(u:float, v:float) -> float:
    return u**2 + v**2

# The partial derivatives are the same, only the variable changes.
def partial(u):
    return 2*u

def prepare_text(text: Text|MathTex):
    return text.scale(0.8).rotate(numpy.pi/2, RIGHT).move_to(TEXT_POSITION).rotate_about_origin(numpy.pi/3, IN)

class DiscordBanner(ThreeDScene):
    def construct(self):
        coord_system = ThreeDAxes(x_range=DEFAULT_RANGE, y_range=DEFAULT_RANGE, z_range=DEFAULT_RANGE)
        text = prepare_text(MathTex("f(x,y) = x^2 + y^2"))
        partial_text = lambda var : prepare_text(MathTex(f"\\nabla_{var}f = 2{var}"))

        par_x = partial_text("x")
        par_y = partial_text("y")
        
        nablaf = prepare_text(MathTex("\\nabla f = 2xe_1 + 2ye_2"))

        surface = coord_system.plot_surface(
            paraboloid,
            u_range=DEFAULT_UV_RANGE,
            v_range=DEFAULT_UV_RANGE,
            resolution=(32, 32),
            colorscale=[PURPLE, BLUE, PURPLE, PURPLE]
        )

        space = numpy.linspace(start=DEFAULT_UV_RANGE[0], stop=DEFAULT_UV_RANGE[1])
        nabla = lambda edge : coord_system.plot_line_graph(x_values=space if edge == 'x' else space*0, 
                                                                   y_values=space if edge == 'y' else space*0,
                                                                   z_values=partial(space))

        animation_queue = [
           Create(coord_system),
           Create(surface),
           Create(text),
           Wait(0.5),
           FadeOut(text),
           Create(nabla('x')),
           Create(par_x),
           Wait(0.5),
           FadeOut(par_x),
           Create(nabla('y')),
           Create(par_y),
           Wait(0.5),
           FadeOut(par_y),
           Create(nablaf),
           Wait(1)
        ]

        self.set_camera_orientation(phi=numpy.pi/3, theta=5*numpy.pi/4)
        for animation in animation_queue:
            self.play(animation)

