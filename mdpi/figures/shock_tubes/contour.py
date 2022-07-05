# trace generated using paraview version 5.10.0-RC1

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

case = 'vacuum'
mesh = 'tetra'
pvtu = 'Frame16.pvtu'

import os
home = os.getenv('HOME')

# create a new 'XML Partitioned Unstructured Grid Reader'
frame10pvtu = XMLPartitionedUnstructuredGridReader(registrationName=pvtu, FileName=[home + '/CFD/output/shock_tubes/' + case + '/' + mesh + '/p=3_h=1e-1/' + pvtu])

# Properties modified on frame10pvtu
frame10pvtu.PointArrayStatus = ['Density']
frame10pvtu.TimeArray = 'None'

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
frame10pvtuDisplay = Show(frame10pvtu, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
frame10pvtuDisplay.Representation = 'Surface'

# reset view to fit data
renderView1.ResetCamera(False)

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(frame10pvtuDisplay, ('POINTS', 'Density'))

# rescale color and/or opacity maps used to include current data range
frame10pvtuDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
frame10pvtuDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'Density'
densityLUT = GetColorTransferFunction('Density')

# get opacity transfer function/opacity map for 'Density'
densityPWF = GetOpacityTransferFunction('Density')

# change representation type
frame10pvtuDisplay.SetRepresentationType('Surface With Edges')

# get color legend/bar for densityLUT in view renderView1
densityLUTColorBar = GetScalarBar(densityLUT, renderView1)

# Properties modified on densityLUTColorBar
densityLUTColorBar.Title = '$\\rho$'

# reset view to fit data bounds
renderView1.ResetCamera(0.0, 5.0, 0.0, 1.0, 0.0, 0.5, True)

# get layout
layout1 = GetLayout()

# layout/tab size in pixels
layout1.SetSize(2560, 1280)

# reset view to fit data
renderView1.ResetCamera(True)

# current camera placement for renderView1
renderView1.CameraPosition = [8.708842073880625, 2.6835545804139915, 7.642476120667951]
renderView1.CameraFocalPoint = [2.5, 0.5, 0.25]
renderView1.CameraViewUp = [-0.14404073131221004, 0.9753581791561353, -0.16711879031476917]
renderView1.CameraParallelScale = 1.1552280648689262
renderView1.CameraParallelProjection = 1

# save screenshot
# SaveScreenshot(home + '/code/manuscript/figures/shock_tubes/' + case + '/contour_' + mesh + '.png', renderView1, ImageResolution=[2560, 1280],
#     FontScaling='Do not scale fonts',
#     OverrideColorPalette='WhiteBackground')

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(2560, 1280)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.CameraPosition = [8.708842073880625, 2.6835545804139915, 7.642476120667951]
renderView1.CameraFocalPoint = [2.5, 0.5, 0.25]
renderView1.CameraViewUp = [-0.14404073131221004, 0.9753581791561353, -0.16711879031476917]
renderView1.CameraParallelScale = 1.1552280648689262
renderView1.CameraParallelProjection = 1

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).