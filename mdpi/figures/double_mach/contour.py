# trace generated using paraview version 5.10.0-RC1

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

case = 'p=1_h=5e-3'

import os
home = os.getenv('HOME')

# create a new 'XML Partitioned Unstructured Grid Reader'
frame50pvtu = XMLPartitionedUnstructuredGridReader(registrationName='Frame50.pvtu', FileName=[home + '/CFD/output/double_mach/hexa/' + case + '/Frame50.pvtu'])

# Properties modified on frame50pvtu
frame50pvtu.PointArrayStatus = ['Density']
frame50pvtu.TimeArray = 'None'

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
frame50pvtuDisplay = Show(frame50pvtu, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
frame50pvtuDisplay.Representation = 'Surface'

# reset view to fit data
renderView1.ResetCamera(False)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Clip'
clip1 = Clip(registrationName='Clip1', Input=frame50pvtu)

# Properties modified on clip1.ClipType
clip1.ClipType.Origin = [3.0, 0.5, 0.0025]

# show data in view
clip1Display = Show(clip1, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
clip1Display.Representation = 'Surface'

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=clip1.ClipType)

# hide data in view
Hide(frame50pvtu, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# reset view to fit data bounds
renderView1.ResetCamera(0.0, 3.00396, 0.0, 1.0, 0.0, 0.005, True)

# set scalar coloring
ColorBy(clip1Display, ('POINTS', 'Density'))

# rescale color and/or opacity maps used to include current data range
clip1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
clip1Display.SetScalarBarVisibility(renderView1, True)


# get color transfer function/color map for 'Density'
densityLUT = GetColorTransferFunction('Density')

# Rescale transfer function
densityLUT.RescaleTransferFunction(1.4, 22.2)

# get opacity transfer function/opacity map for 'Density'
densityPWF = GetOpacityTransferFunction('Density')

# Rescale transfer function
densityPWF.RescaleTransferFunction(1.4, 22.2)

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# get layout
layout1 = GetLayout()

# layout/tab size in pixels
layout1.SetSize(2560, 1280)

# current camera placement for renderView1
renderView1.CameraPosition = [1.50198, 0.5, 6.118816982357501]
renderView1.CameraFocalPoint = [1.50198, 0.5, 0.0025]
renderView1.CameraParallelScale = 0.8341082706573666
renderView1.CameraParallelProjection = 1

# save screenshot
SaveScreenshot(home + '/code/manuscript/figures/double_mach/' + case + '.png', renderView1, ImageResolution=[2560, 1280],
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
renderView1.CameraPosition = [1.50198, 0.5, 6.118816982357501]
renderView1.CameraFocalPoint = [1.50198, 0.5, 0.0025]
renderView1.CameraParallelScale = 0.8341082706573666
renderView1.CameraParallelProjection = 1

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).