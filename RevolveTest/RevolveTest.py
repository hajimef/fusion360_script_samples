#Author-
#Description-

import adsk.core, adsk.fusion, adsk.cam, traceback, math

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        product = app.activeProduct
        design = adsk.fusion.Design.cast(product)
        rootComp = design.rootComponent
        sketches = rootComp.sketches
        xyPlane = rootComp.xYConstructionPlane
        sketch = sketches.add(xyPlane)
        points = adsk.core.ObjectCollection.create()
        for i in range(101):
            x = i / 100
            z = x ** 2
            points.add(adsk.core.Point3D.create(x * 5, 0, z * 5))
        splines = sketch.sketchCurves.sketchFittedSplines
        splines.add(points)
        lines = sketch.sketchCurves.sketchLines
        lines.addByTwoPoints(adsk.core.Point3D.create(0, 0, 0), adsk.core.Point3D.create(0, 0, 5))
        lines.addByTwoPoints(adsk.core.Point3D.create(0, 0, 5), adsk.core.Point3D.create(5, 0, 5))
        prof = sketch.profiles.item(0)
        revs = rootComp.features.revolveFeatures
        zAxis = rootComp.zConstructionAxis
        revInput = revs.createInput(prof, zAxis, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        revInput.setAngleExtent(False, adsk.core.ValueInput.createByReal(math.pi * 2))
        revs.add(revInput)

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
