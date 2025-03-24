from manim import *

import numpy

TEXT_POSITION = (2.5, 5, 1.5)
DEFAULT_RANGE = (-25, 25, 1)
DEFAULT_UV_RANGE = (-25, 25)

def tangent_plane(u: float, v:float):
    return 2*(u+v) - 2

def paraboloid(u:float, v:float) -> float:
    return u**2 + v**2

def partial(u):
    return 2*u

def prepare_text(text: Text|MathTex):
    return text.scale(0.7).rotate(numpy.pi/2, RIGHT).move_to(TEXT_POSITION).rotate_about_origin(numpy.pi/3, IN)

class DiscordBanner(ThreeDScene):
    def construct(self):
        coord_system = ThreeDAxes(x_range=DEFAULT_RANGE, y_range=DEFAULT_RANGE, z_range=DEFAULT_RANGE)
        text = prepare_text(MathTex("r(u,v) = (u, v, u^2 + v^2)"))        
        partial_text = lambda var : prepare_text(MathTex(f"\\fracRB\\partialRBrLBLBRB\\partialRB{var}LBLB = ({int(var == 'u')},{int(var == 'v')},2{var})".replace("RB", "{").replace("LB", "}")))

        par_u = partial_text("u")
        par_v = partial_text("v")
        
        tsurface_eq = prepare_text(MathTex("2x + 2y - z = 2"))

        surface = coord_system.plot_surface(
            paraboloid,
            u_range=DEFAULT_UV_RANGE,
            v_range=DEFAULT_UV_RANGE,
            resolution=(32, 32),
            colorscale=[PURPLE, BLUE, PURPLE, PURPLE]
        )

        # A tangent plane to (1, 1, r(1,1))
        tangent_surface = coord_system.plot_surface(
            tangent_plane,
            u_range=DEFAULT_UV_RANGE,
            v_range=DEFAULT_UV_RANGE,
            resolution=(32, 32),
            colorscale=[PURPLE, BLUE]
        )

        space = numpy.linspace(start=DEFAULT_UV_RANGE[0], stop=DEFAULT_UV_RANGE[1])
        partial_delta = lambda edge : coord_system.plot_line_graph(x_values=space if edge == 'u' else space*0, 
                                                                   y_values=space if edge == 'v' else space*0,
                                                                   z_values=partial(space))

        animation_queue = [
           Create(coord_system),
           Create(surface),
           Create(text),
           Wait(0.5),
           FadeOut(text),
           Create(partial_delta('u')),
           Create(par_u),
           Wait(0.5),
           FadeOut(par_u),
           Create(partial_delta('v')),
           Create(par_v),
           Wait(0.5),
           FadeOut(par_v),
           Create(tangent_surface),
           Rotate(tangent_surface, angle=numpy.pi/2),
           Create(tsurface_eq),
           Wait(1)
        ]

        self.set_camera_orientation(phi=numpy.pi/3, theta=5*numpy.pi/4)
        for animation in animation_queue:
            self.play(animation)

