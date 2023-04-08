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
        extrudes = rootComp.features.extrudeFeatures
        d = math.pi / 180
        hs = [ 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII' ]
        sketch = sketches.add(xyPlane)
        texts = sketch.sketchTexts
        input = texts.createInput2("Fusion 360\nSketch Text", 0.8)
        input.fontName = 'Times New Roman'
        cornerPoint = adsk.core.Point3D.create(-5, 3, 0)
        diagonalPoint = adsk.core.Point3D.create(5, -3, 0)
        horizontalAlignment = adsk.core.HorizontalAlignments.CenterHorizontalAlignment
        verticalAlignment = adsk.core.VerticalAlignments.MiddleVerticalAlignment
        input.setAsMultiLine(cornerPoint, diagonalPoint, horizontalAlignment, verticalAlignment, 0)
        text = texts.add(input)
        extInput = extrudes.createInput(text, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        distance = adsk.core.ValueInput.createByReal(0.2)
        extInput.setDistanceExtent(False, distance)
        extInput.isSolid = True
        extrudes.add(extInput)
        for i in range(1, 13):
            sketch = sketches.add(xyPlane)
            lines = sketch.sketchCurves.sketchLines
            texts = sketch.sketchTexts
            sx = math.cos((85 - i * 30) * d) * 5
            sy = math.sin((85 - i * 30) * d) * 5
            ex = math.cos((95 - i * 30) * d) * 5
            ey = math.sin((95 - i * 30) * d) * 5
            sp = adsk.core.Point3D.create(sx, sy, 0)
            ep = adsk.core.Point3D.create(ex, ey, 0)
            line = lines.addByTwoPoints(sp, ep)
            input = texts.createInput2(hs[i - 1], 0.5)
            input.fontName = 'Times New Roman'
            isAbove = True if i >= 3 and i < 9 else False
            input.setAsAlongPath(line, isAbove, adsk.core.HorizontalAlignments.CenterHorizontalAlignment, 0)
            if i >= 3 and i < 9:
                input.isHorizontalFlip = True
                input.isVerticalFlip = True
            text = texts.add(input)
            extInput = extrudes.createInput(text, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
            distance = adsk.core.ValueInput.createByReal(0.2)
            extInput.setDistanceExtent(False, distance)
            extInput.isSolid = True
            extrudes.add(extInput)
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))