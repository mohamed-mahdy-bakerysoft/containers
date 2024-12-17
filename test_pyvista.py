import pyvista as pv
pv.start_xvfb()
pl=pv.Plotter(off_screen=True)
pl.add_mesh(pv.Sphere())
pl.show(screenshot='sphere.png')