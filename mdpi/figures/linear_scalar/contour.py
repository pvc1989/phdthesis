# trace generated using paraview version 5.10.0-RC1

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

case = 'p=3_h=2^-2'
dt = '_dt=2e-3'

import os
home = os.getenv('HOME')

# create a new 'XML Partitioned Unstructured Grid Reader'
frame1pvtu = XMLPartitionedUnstructuredGridReader(registrationName='Frame1.pvtu', FileName=[home + '/CFD/output/linear_scalar/' + case + dt + '/Frame1.pvtu'])

# Properties modified on frame1pvtu
frame1pvtu.TimeArray = 'None'

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
frame1pvtuDisplay = Show(frame1pvtu, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
frame1pvtuDisplay.Representation = 'Surface'

# reset view to fit data
renderView1.ResetCamera(False)

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(frame1pvtuDisplay, ('POINTS', 'U'))

# rescale color and/or opacity maps used to include current data range
frame1pvtuDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
frame1pvtuDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'U'
uLUT = GetColorTransferFunction('U')

# get opacity transfer function/opacity map for 'U'
uPWF = GetOpacityTransferFunction('U')

# reset view to fit data
renderView1.ResetCamera(True)

# change representation type
frame1pvtuDisplay.SetRepresentationType('Surface With Edges')

# Rescale transfer function
uLUT.RescaleTransferFunction(-1.0, 1.0)

# Rescale transfer function
uPWF.RescaleTransferFunction(-1.0, 1.0)

# Rescale transfer function
uLUT.RescaleTransferFunction(-10.0, 10.0)

# Rescale transfer function
uPWF.RescaleTransferFunction(-10.0, 10.0)

# get color legend/bar for uLUT in view renderView1
uLUTColorBar = GetScalarBar(uLUT, renderView1)

# Properties modified on uLUTColorBar
uLUTColorBar.Title = '$U$'

# Properties modified on uLUTColorBar
uLUTColorBar.TitleFontSize = 32
uLUTColorBar.LabelFontSize = 20
uLUTColorBar.ScalarBarLength = 0.35

# reset view to fit data
renderView1.ResetCamera(True)

# get layout
layout1 = GetLayout()

# layout/tab size in pixels
layout1.SetSize(2560, 1280)

# current camera placement for renderView1
renderView1.CameraPosition = [7.0117601037115245, -5.013616816452548, 3.226603214192355]
renderView1.CameraFocalPoint = [2.0, 0.5, 0.25]
renderView1.CameraViewUp = [-0.2526615288641277, 0.27167094295887384, 0.9286318164826564]
renderView1.CameraParallelScale = 1.0085842125222793
renderView1.CameraParallelProjection = 1

# save screenshot
SaveScreenshot(home + '/code/manuscript/figures/linear_scalar/' + case + '.png', renderView1, ImageResolution=[2560, 1280],
    FontScaling='Do not scale fonts',
    OverrideColorPalette='WhiteBackground')

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
renderView1.CameraPosition = [7.0117601037115245, -5.013616816452548, 3.226603214192355]
renderView1.CameraFocalPoint = [2.0, 0.5, 0.25]
renderView1.CameraViewUp = [-0.2526615288641277, 0.27167094295887384, 0.9286318164826564]
renderView1.CameraParallelScale = 1.0085842125222793
renderView1.CameraParallelProjection = 1

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
