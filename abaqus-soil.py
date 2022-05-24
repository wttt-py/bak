# -*- coding: mbcs -*-
from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *
import os


path = '524test'
dirs = r'D:\abaqus-pytest\%s' % path
#print(dirs)
if not os.path.exists(dirs):
    os.mkdir(dirs)
    
os.chdir(dirs)

mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(0.0, 0.0), 
    point2=(60.0, 60.0))
mdb.models['Model-1'].Part(dimensionality=TWO_D_PLANAR, name='soil', type=
    DEFORMABLE_BODY)
mdb.models['Model-1'].parts['soil'].BaseShell(sketch=
    mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=4.24, name='__profile__', 
    sheetSize=169.7, transform=
    mdb.models['Model-1'].parts['soil'].MakeSketchTransform(
    sketchPlane=mdb.models['Model-1'].parts['soil'].faces[0], 
    sketchPlaneSide=SIDE1, sketchOrientation=RIGHT, origin=(30.0, 30.0, 0.0)))
mdb.models['Model-1'].parts['soil'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].offset(distance=3.0, objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[4], ), side=LEFT)
mdb.models['Model-1'].sketches['__profile__'].offset(distance=5.0, objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[6], ), side=LEFT)
mdb.models['Model-1'].sketches['__profile__'].offset(distance=10.0, objectList=
    (mdb.models['Model-1'].sketches['__profile__'].geometry[4], ), side=LEFT)
mdb.models['Model-1'].sketches['__profile__'].offset(distance=7.5, objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[8], ), side=LEFT)
mdb.models['Model-1'].sketches['__profile__'].offset(distance=30.0, objectList=
    (mdb.models['Model-1'].sketches['__profile__'].geometry[5], ), side=LEFT)
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(
    0.0, 12.5), point1=(0.0, 20.0))
mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[15], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[8])
mdb.models['Model-1'].sketches['__profile__'].EqualDistanceConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[8], entity2=
    mdb.models['Model-1'].sketches['__profile__'].vertices[9], midpoint=
    mdb.models['Model-1'].sketches['__profile__'].vertices[15])
mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[14], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[9])
mdb.models['Model-1'].sketches['__profile__'].EqualDistanceConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[10], entity2=
    mdb.models['Model-1'].sketches['__profile__'].vertices[11], midpoint=
    mdb.models['Model-1'].sketches['__profile__'].vertices[14])
mdb.models['Model-1'].sketches['__profile__'].RadialDimension(curve=
    mdb.models['Model-1'].sketches['__profile__'].geometry[11], radius=7.5, 
    textPoint=(10.2607498168945, 15.4606323242188))
mdb.models['Model-1'].sketches['__profile__'].offset(distance=9.5, objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[9], ), side=LEFT)
mdb.models['Model-1'].sketches['__profile__'].delete(objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[8], ))
mdb.models['Model-1'].sketches['__profile__'].offset(distance=15.0, objectList=
    (mdb.models['Model-1'].sketches['__profile__'].geometry[5], ), side=LEFT)
mdb.models['Model-1'].sketches['__profile__'].offset(distance=15.0, objectList=
    (mdb.models['Model-1'].sketches['__profile__'].geometry[3], ), side=LEFT)
mdb.models['Model-1'].parts['soil'].PartitionFaceBySketch(faces=
    mdb.models['Model-1'].parts['soil'].faces.getSequenceFromMask(('[#1 ]', ), 
    ), sketch=mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(
    0.0, 0.0), point1=(0.0, 10.0))
mdb.models['Model-1'].sketches['__profile__'].RadialDimension(curve=
    mdb.models['Model-1'].sketches['__profile__'].geometry[2], radius=7.5, 
    textPoint=(-13.6074447631836, 11.6666641235352))
mdb.models['Model-1'].sketches['__profile__'].offset(distance=0.25, objectList=
    (mdb.models['Model-1'].sketches['__profile__'].geometry[2], ), side=LEFT)
mdb.models['Model-1'].Part(dimensionality=TWO_D_PLANAR, name='tunnel', type=
    DEFORMABLE_BODY)
mdb.models['Model-1'].parts['tunnel'].BaseShell(sketch=
    mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=1.05, name='__profile__', 
    sheetSize=42.31, transform=
    mdb.models['Model-1'].parts['tunnel'].MakeSketchTransform(
    sketchPlane=mdb.models['Model-1'].parts['tunnel'].faces[0], 
    sketchPlaneSide=SIDE1, sketchOrientation=RIGHT, origin=(0.0, 0.0, 0.0)))
mdb.models['Model-1'].parts['tunnel'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-8.4, 0.0), point2=(
    8.4, 0.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry[4])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 8.4), point2=(
    0.0, -8.4))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=mdb.models['Model-1'].sketches['__profile__'].geometry[5])
mdb.models['Model-1'].sketches['__profile__'].autoTrimCurve(curve1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[5], point1=(
    0.0893208086490631, -1.66665387153625))
mdb.models['Model-1'].sketches['__profile__'].autoTrimCurve(curve1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[4], point1=(
    1.04378092288971, -0.077248752117157))
mdb.models['Model-1'].sketches['__profile__'].autoTrimCurve(curve1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[6], point1=(
    -0.069755882024765, 0.982355892658234))
mdb.models['Model-1'].sketches['__profile__'].autoTrimCurve(curve1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[8], point1=(
    -1.55447232723236, 0.0287120938301086))
mdb.models['Model-1'].sketches['__profile__'].autoTrimCurve(curve1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[11], point1=(
    -8.07661914825439, 0.0287120938301086))
mdb.models['Model-1'].sketches['__profile__'].autoTrimCurve(curve1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[10], point1=(
    0.0893208086490631, 7.97574043273926))
mdb.models['Model-1'].sketches['__profile__'].autoTrimCurve(curve1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[9], point1=(
    8.20223236083984, 0.0287120938301086))
mdb.models['Model-1'].sketches['__profile__'].autoTrimCurve(curve1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[7], point1=(
    0.0362946093082428, -8.07725715637207))
mdb.models['Model-1'].parts['tunnel'].PartitionFaceBySketch(faces=
    mdb.models['Model-1'].parts['tunnel'].faces.getSequenceFromMask(('[#1 ]', 
    ), ), sketch=mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].Material(name='soil1')
mdb.models['Model-1'].materials['soil1'].Density(table=((1.7, ), ))
mdb.models['Model-1'].materials['soil1'].Elastic(table=((4000.0, 0.2), ))
mdb.models['Model-1'].materials['soil1'].MohrCoulombPlasticity(table=((15.0, 
    0.1), ))
mdb.models['Model-1'].materials['soil1'].mohrCoulombPlasticity.MohrCoulombHardening(
    table=((2.0, 0.0), ))
mdb.models['Model-1'].materials['soil1'].mohrCoulombPlasticity.TensionCutOff(
    dependencies=0, table=((0.0, 0.0), ), temperatureDependency=OFF)
mdb.models['Model-1'].Material(name='soil2')
mdb.models['Model-1'].materials['soil2'].Density(table=((2.0, ), ))
mdb.models['Model-1'].materials['soil2'].Elastic(table=((6000.0, 0.2), ))
mdb.models['Model-1'].materials['soil2'].MohrCoulombPlasticity(table=((24.0, 
    0.0), ))
mdb.models['Model-1'].materials['soil2'].mohrCoulombPlasticity.MohrCoulombHardening(
    table=((3.0, 0.0), ))
mdb.models['Model-1'].materials['soil2'].mohrCoulombPlasticity.TensionCutOff(
    dependencies=0, table=((0.0, 0.0), ), temperatureDependency=OFF)
mdb.models['Model-1'].Material(name='soil3')
mdb.models['Model-1'].materials['soil3'].Density(table=((2.7, ), ))
mdb.models['Model-1'].materials['soil3'].Elastic(table=((400000.0, 0.23), ))
mdb.models['Model-1'].materials['soil3'].MohrCoulombPlasticity(table=((45.0, 
    0.1), ))
mdb.models['Model-1'].materials['soil3'].mohrCoulombPlasticity.MohrCoulombHardening(
    table=((400.0, 0.0), ))
mdb.models['Model-1'].materials['soil3'].mohrCoulombPlasticity.TensionCutOff(
    dependencies=0, table=((0.0, 0.0), ), temperatureDependency=OFF)
mdb.models['Model-1'].Material(name='tunnel')
mdb.models['Model-1'].materials['tunnel'].Density(table=((2.5, ), ))
mdb.models['Model-1'].materials['tunnel'].Elastic(table=((30000000.0, 0.2), ))
mdb.models['Model-1'].HomogeneousSolidSection(material='soil1', name='soil1', 
    thickness=None)
mdb.models['Model-1'].HomogeneousSolidSection(material='soil2', name='soil2', 
    thickness=None)
mdb.models['Model-1'].HomogeneousSolidSection(material='soil3', name='soil3', 
    thickness=None)
mdb.models['Model-1'].HomogeneousSolidSection(material='tunnel', name='tunnel', 
    thickness=None)
mdb.models['Model-1'].parts['soil'].Set(faces=
    mdb.models['Model-1'].parts['soil'].faces.getSequenceFromMask((
    '[#460800 ]', ), ), name='Set-1')
mdb.models['Model-1'].parts['soil'].SectionAssignment(offset=0.0, offsetField=
    '', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['soil'].sets['Set-1'], sectionName='soil1', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['soil'].Set(faces=
    mdb.models['Model-1'].parts['soil'].faces.getSequenceFromMask((
    '[#a81000 ]', ), ), name='Set-2')
mdb.models['Model-1'].parts['soil'].SectionAssignment(offset=0.0, offsetField=
    '', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['soil'].sets['Set-2'], sectionName='soil2', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['soil'].Set(faces=
    mdb.models['Model-1'].parts['soil'].faces.getSequenceFromMask((
    '[#11e7ff ]', ), ), name='Set-3')
mdb.models['Model-1'].parts['soil'].SectionAssignment(offset=0.0, offsetField=
    '', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['soil'].sets['Set-3'], sectionName='soil3', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['tunnel'].Set(faces=
    mdb.models['Model-1'].parts['tunnel'].faces.getSequenceFromMask(('[#f ]', 
    ), ), name='Set-1')
mdb.models['Model-1'].parts['tunnel'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['tunnel'].sets['Set-1'], sectionName='tunnel', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].rootAssembly.DatumCsysByDefault(CARTESIAN)
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='soil-1', part=
    mdb.models['Model-1'].parts['soil'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='tunnel-1', 
    part=mdb.models['Model-1'].parts['tunnel'])
mdb.models['Model-1'].rootAssembly.translate(instanceList=('tunnel-1', ), 
    vector=(30.0, 42.5, 0.0))
mdb.models['Model-1'].GeostaticStep(initialInc=0.1, matrixSolver=DIRECT, 
    matrixStorage=UNSYMMETRIC, maxInc=1.0, minInc=1e-05, name='geo', previous=
    'Initial', timeIncrementationMethod=AUTOMATIC, utol=0.001)
mdb.models['Model-1'].StaticStep(initialInc=0.1, matrixSolver=DIRECT, 
    matrixStorage=UNSYMMETRIC, name='add tunnel', previous='geo')
mdb.models['Model-1'].rootAssembly.Set(faces=
    mdb.models['Model-1'].rootAssembly.instances['soil-1'].faces.getSequenceFromMask(
    ('[#40c4 ]', ), ), name='remove')
mdb.models['Model-1'].ModelChange(activeInStep=False, createStepName=
    'add tunnel', includeStrain=False, name='Int-1', region=
    mdb.models['Model-1'].rootAssembly.sets['remove'])
mdb.models['Model-1'].rootAssembly.Set(faces=
    mdb.models['Model-1'].rootAssembly.instances['tunnel-1'].faces.getSequenceFromMask(
    ('[#f ]', ), ), name='tunnel')
mdb.models['Model-1'].ModelChange(activeInStep=False, createStepName='geo', 
    includeStrain=False, name='Int-2', region=
    mdb.models['Model-1'].rootAssembly.sets['tunnel'])
mdb.models['Model-1'].interactions['Int-2'].setValuesInStep(activeInStep=True, 
    stepName='add tunnel')
mdb.models['Model-1'].ContactProperty('IntProp-1')
mdb.models['Model-1'].interactionProperties['IntProp-1'].TangentialBehavior(
    dependencies=0, directionality=ISOTROPIC, elasticSlipStiffness=None, 
    formulation=PENALTY, fraction=0.005, maximumElasticSlip=FRACTION, 
    pressureDependency=OFF, shearStressLimit=None, slipRateDependency=OFF, 
    table=((0.5, ), ), temperatureDependency=OFF)
mdb.models['Model-1'].interactionProperties['IntProp-1'].NormalBehavior(
    allowSeparation=ON, constraintEnforcementMethod=DEFAULT, 
    pressureOverclosure=HARD)
mdb.models['Model-1'].rootAssembly.Surface(name='tunnel', side1Edges=
    mdb.models['Model-1'].rootAssembly.instances['tunnel-1'].edges.getSequenceFromMask(
    ('[#642 ]', ), ))
mdb.models['Model-1'].rootAssembly.Surface(name='soil-Y', side1Edges=
    mdb.models['Model-1'].rootAssembly.instances['soil-1'].edges.getSequenceFromMask(
    ('[#600200 #80 ]', ), ))
mdb.models['Model-1'].SurfaceToSurfaceContactStd(adjustMethod=NONE, 
    clearanceRegion=None, createStepName='add tunnel', datumAxis=None, 
    initialClearance=OMIT, interactionProperty='IntProp-1', master=
    mdb.models['Model-1'].rootAssembly.surfaces['tunnel'], name='Int-3', slave=
    mdb.models['Model-1'].rootAssembly.surfaces['soil-Y'], sliding=FINITE, 
    thickness=ON)
mdb.models['Model-1'].rootAssembly.Set(edges=
    mdb.models['Model-1'].rootAssembly.instances['soil-1'].edges.getSequenceFromMask(
    ('[#40024044 #420809 ]', ), ), name='Set-3', vertices=
    mdb.models['Model-1'].rootAssembly.instances['soil-1'].vertices.getSequenceFromMask(
    ('[#8d0b01c #3 ]', ), ))
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', 
    distributionType=UNIFORM, fieldName='', localCsys=None, name='BC-1', 
    region=mdb.models['Model-1'].rootAssembly.sets['Set-3'], u1=SET, u2=UNSET, 
    ur3=UNSET)
mdb.models['Model-1'].rootAssembly.Set(edges=
    mdb.models['Model-1'].rootAssembly.instances['soil-1'].edges.getSequenceFromMask(
    ('[#4008802 ]', ), ), name='Set-4', vertices=
    mdb.models['Model-1'].rootAssembly.instances['soil-1'].vertices.getSequenceFromMask(
    ('[#6406 ]', ), ))
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', 
    distributionType=UNIFORM, fieldName='', localCsys=None, name='BC-2', 
    region=mdb.models['Model-1'].rootAssembly.sets['Set-4'], u1=SET, u2=SET, 
    ur3=UNSET)
mdb.models['Model-1'].rootAssembly.Set(faces=
    mdb.models['Model-1'].rootAssembly.instances['soil-1'].faces.getSequenceFromMask(
    ('[#ffffff ]', ), ), name='Set-5')
mdb.models['Model-1'].Gravity(comp2=-10.0, createStepName='geo', 
    distributionType=UNIFORM, field='', name='Load-1', region=
    mdb.models['Model-1'].rootAssembly.sets['Set-5'])
mdb.models['Model-1'].parts['soil'].seedPart(deviationFactor=0.1, 
    minSizeFactor=0.1, size=2.0)
mdb.models['Model-1'].parts['soil'].seedEdgeByNumber(constraint=FINER, edges=
    mdb.models['Model-1'].parts['soil'].edges.getSequenceFromMask((
    '[#600200 #80 ]', ), ), number=6)
mdb.models['Model-1'].parts['soil'].setMeshControls(algorithm=MEDIAL_AXIS, 
    elemShape=QUAD, regions=
    mdb.models['Model-1'].parts['soil'].faces.getSequenceFromMask((
    '[#10e1c4 ]', ), ))
mdb.models['Model-1'].parts['soil'].setMeshControls(elemShape=QUAD, regions=
    mdb.models['Model-1'].parts['soil'].faces.getSequenceFromMask((
    '[#ef1e3b ]', ), ), technique=STRUCTURED)
mdb.models['Model-1'].parts['soil'].generateMesh()
mdb.models['Model-1'].parts['soil'].setElementType(elemTypes=(ElemType(
    elemCode=CPE4R, elemLibrary=STANDARD, secondOrderAccuracy=OFF, 
    hourglassControl=DEFAULT, distortionControl=DEFAULT), ElemType(
    elemCode=CPE3, elemLibrary=STANDARD)), regions=(
    mdb.models['Model-1'].parts['soil'].faces.getSequenceFromMask((
    '[#ffffff ]', ), ), ))
mdb.models['Model-1'].parts['tunnel'].seedEdgeByNumber(constraint=FINER, edges=
    mdb.models['Model-1'].parts['tunnel'].edges.getSequenceFromMask(('[#fdb ]', 
    ), ), number=6)
mdb.models['Model-1'].parts['tunnel'].seedEdgeByNumber(constraint=FINER, edges=
    mdb.models['Model-1'].parts['tunnel'].edges.getSequenceFromMask(('[#a5 ]', 
    ), ), number=3)
mdb.models['Model-1'].parts['tunnel'].setMeshControls(algorithm=MEDIAL_AXIS, 
    elemShape=QUAD, regions=
    mdb.models['Model-1'].parts['tunnel'].faces.getSequenceFromMask(('[#f ]', 
    ), ))
mdb.models['Model-1'].parts['tunnel'].generateMesh()
mdb.models['Model-1'].parts['tunnel'].setElementType(elemTypes=(ElemType(
    elemCode=CPE4I, elemLibrary=STANDARD), ElemType(elemCode=CPE3, 
    elemLibrary=STANDARD)), regions=(
    mdb.models['Model-1'].parts['tunnel'].faces.getSequenceFromMask(('[#f ]', 
    ), ), ))
mdb.models['Model-1'].rootAssembly.regenerate()
mdb.Job(atTime=None, contactPrint=OFF, description='', echoPrint=OFF, 
    explicitPrecision=SINGLE, getMemoryFromAnalysis=True, historyPrint=OFF, 
    memory=90, memoryUnits=PERCENTAGE, model='Model-1', modelPrint=OFF, 
    multiprocessingMode=DEFAULT, name='4#', nodalOutputPrecision=SINGLE, 
    numCpus=4, numDomains=4, numGPUs=0, queue=None, resultsFormat=ODB, scratch=
    '', type=ANALYSIS, userSubroutine='', waitHours=0, waitMinutes=0)
mdb.jobs['4#'].submit(consistencyChecking=OFF)
# mdb.jobs['4#']._Message(STARTED, {'phase': BATCHPRE_PHASE,
#     'clientHost': 'Whaoo', 'handle': 0, 'jobName': '4#'})
# mdb.jobs['4#']._Message(WARNING, {'phase': BATCHPRE_PHASE,
#     'message': 'THE DILATION ANGLE IS SMALL OR ZERO. THE VALUE WILL BE SET TO 0.10000',
#     'jobName': '4#'})
# mdb.jobs['4#']._Message(WARNING, {'phase': BATCHPRE_PHASE,
#     'message': 'THERE ARE 32 FACETS THAT ARE FOUND TO BE FACING IN THE WRONG DIRECTION WITH RESPECT TO THE MASTER SURFACE FOR THE CONTACT PAIR (ASSEMBLY_SOIL-Y,ASSEMBLY_TUNNEL).  PLEASE CHECK THE ORIENTATION OF THE SURFACES RELATIVE TO EACH OTHER.',
#     'jobName': '4#'})
# mdb.jobs['4#']._Message(WARNING, {'phase': BATCHPRE_PHASE,
#     'message': 'A GEOSTATIC PROCEDURE WITH MAXIMUM DISPLACEMENT TOLERANCES IS SUPPORTED ONLY FOR THE FOLLOWING MATERIALS: ELASTIC, POROUS ELASTIC, EXTENDED CAM-CLAY PLASTICITY MODEL, DRUCKER PRAGER  AND MOHR-COULOMB PLASTICITY MODEL. IN GENERAL, THE USE OF OTHER MATERIALS WITH THIS PROCEDURE MAY LEAD TO POOR CONVERGENCE OR NO CONVERGENCE OF THE ANALYSIS.',
#     'jobName': '4#'})
# mdb.jobs['4#']._Message(WARNING, {'phase': BATCHPRE_PHASE,
#     'message': 'A GEOSTATIC PROCEDURE WITH MAXIMUM DISPLACEMENT TOLERANCES IS SUPPORTED ONLY FOR CONTINUUM ELEMENTS WITH PORE PRESSURE DEGREE OF FREEDOM AND THE CORRESPONDING STRESS/DISPLACEMENT CONTINUUM ELEMENTS. IN GENERAL, THE USE OF OTHER ELEMENTS WITH THIS PROCEDURE MAY LEAD TO POOR CONVERGENCE OR NO CONVERGENCE OF THE ANALYSIS.',
#     'jobName': '4#'})
# mdb.jobs['4#']._Message(ODB_FILE, {'phase': BATCHPRE_PHASE,
#     'file': 'F:\\ABAQUS\\temp\\LX\\2022.4.13\\4#.odb', 'jobName': '4#'})
# mdb.jobs['4#']._Message(COMPLETED, {'phase': BATCHPRE_PHASE,
#     'message': 'Analysis phase complete', 'jobName': '4#'})
# mdb.jobs['4#']._Message(STARTED, {'phase': STANDARD_PHASE,
#     'clientHost': 'Whaoo', 'handle': 1896, 'jobName': '4#'})
# mdb.jobs['4#']._Message(STEP, {'phase': STANDARD_PHASE, 'stepId': 1,
#     'jobName': '4#'})
# mdb.jobs['4#']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
#     'frame': 0, 'jobName': '4#'})
# mdb.jobs['4#']._Message(MEMORY_ESTIMATE, {'phase': STANDARD_PHASE,
#     'jobName': '4#', 'memory': 32.0})
# mdb.jobs['4#']._Message(PHYSICAL_MEMORY, {'phase': STANDARD_PHASE,
#     'physical_memory': 16297.0, 'jobName': '4#'})
# mdb.jobs['4#']._Message(MINIMUM_MEMORY, {'minimum_memory': 23.0,
#     'phase': STANDARD_PHASE, 'jobName': '4#'})
# mdb.jobs['4#']._Message(STATUS, {'totalTime': 0.1, 'attempts': 1,
#     'timeIncrement': 0.1, 'increment': 1, 'stepTime': 0.1, 'step': 1,
#     'jobName': '4#', 'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE,
#     'equilibrium': 2})
# mdb.jobs['4#']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
#     'frame': 1, 'jobName': '4#'})
# mdb.jobs['4#']._Message(STATUS, {'totalTime': 0.2, 'attempts': 1,
#     'timeIncrement': 0.1, 'increment': 2, 'stepTime': 0.2, 'step': 1,
#     'jobName': '4#', 'severe': 0, 'iterations': 3, 'phase': STANDARD_PHASE,
#     'equilibrium': 3})
# mdb.jobs['4#']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
#     'frame': 2, 'jobName': '4#'})
# mdb.jobs['4#']._Message(STATUS, {'totalTime': 0.35, 'attempts': 1,
#     'timeIncrement': 0.15, 'increment': 3, 'stepTime': 0.35, 'step': 1,
#     'jobName': '4#', 'severe': 0, 'iterations': 3, 'phase': STANDARD_PHASE,
#     'equilibrium': 3})
# mdb.jobs['4#']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
#     'frame': 3, 'jobName': '4#'})
# mdb.jobs['4#']._Message(STATUS, {'totalTime': 0.575, 'attempts': 1,
#     'timeIncrement': 0.225, 'increment': 4, 'stepTime': 0.575, 'step': 1,
#     'jobName': '4#', 'severe': 0, 'iterations': 4, 'phase': STANDARD_PHASE,
#     'equilibrium': 4})
# mdb.jobs['4#']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
#     'frame': 4, 'jobName': '4#'})
# mdb.jobs['4#']._Message(STATUS, {'totalTime': 0.9125, 'attempts': 1,
#     'timeIncrement': 0.3375, 'increment': 5, 'stepTime': 0.9125, 'step': 1,
#     'jobName': '4#', 'severe': 0, 'iterations': 7, 'phase': STANDARD_PHASE,
#     'equilibrium': 7})
# mdb.jobs['4#']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
#     'frame': 5, 'jobName': '4#'})
# mdb.jobs['4#']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
#     'frame': 6, 'jobName': '4#'})
# mdb.jobs['4#']._Message(STATUS, {'totalTime': 1.0, 'attempts': 1,
#     'timeIncrement': 0.0874999999999999, 'increment': 6, 'stepTime': 1.0,
#     'step': 1, 'jobName': '4#', 'severe': 0, 'iterations': 3,
#     'phase': STANDARD_PHASE, 'equilibrium': 3})
# mdb.jobs['4#']._Message(END_STEP, {'phase': STANDARD_PHASE, 'stepId': 1,
#     'jobName': '4#'})
# mdb.jobs['4#']._Message(STEP, {'phase': STANDARD_PHASE, 'stepId': 2,
#     'jobName': '4#'})
# mdb.jobs['4#']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 1,
#     'frame': 0, 'jobName': '4#'})
# mdb.jobs['4#']._Message(WARNING, {'phase': STANDARD_PHASE,
#     'message': 'THERE ARE 2 UNCONNECTED REGIONS IN THE MODEL.',
#     'jobName': '4#'})
# mdb.jobs['4#']._Message(MEMORY_ESTIMATE, {'phase': STANDARD_PHASE,
#     'jobName': '4#', 'memory': 32.0})
# mdb.jobs['4#']._Message(PHYSICAL_MEMORY, {'phase': STANDARD_PHASE,
#     'physical_memory': 16297.0, 'jobName': '4#'})
# mdb.jobs['4#']._Message(MINIMUM_MEMORY, {'minimum_memory': 23.0,
#     'phase': STANDARD_PHASE, 'jobName': '4#'})
# mdb.jobs['4#']._Message(WARNING, {'phase': STANDARD_PHASE,
#     'message': 'Solver problem. Numerical singularity when processing node TUNNEL-1.79 D.O.F. 2 ratio = 23.9586E+09 .',
#     'jobName': '4#'})
# mdb.jobs['4#']._Message(WARNING, {'phase': STANDARD_PHASE,
#     'message': 'Solver problem. Numerical singularity when processing node TUNNEL-1.80 D.O.F. 1 ratio = 5.76974E+15.',
#     'jobName': '4#'})
# mdb.jobs['4#']._Message(WARNING, {'phase': STANDARD_PHASE,
#     'message': 'Solver problem. Numerical singularity when processing node TUNNEL-1.80 D.O.F. 2 ratio = 358.306E+12  .',
#     'jobName': '4#'})
# mdb.jobs['4#']._Message(WARNING, {'phase': STANDARD_PHASE,
#     'message': 'Solver problem. Numerical singularity when processing node TUNNEL-1.79 D.O.F. 2 ratio = 23.9586E+09 .',
#     'jobName': '4#'})
# mdb.jobs['4#']._Message(WARNING, {'phase': STANDARD_PHASE,
#     'message': 'Solver problem. Numerical singularity when processing node TUNNEL-1.80 D.O.F. 1 ratio = 5.76974E+15.',
#     'jobName': '4#'})
# mdb.jobs['4#']._Message(WARNING, {'phase': STANDARD_PHASE,
#     'message': 'Solver problem. Numerical singularity when processing node TUNNEL-1.80 D.O.F. 2 ratio = 358.306E+12  .',
#     'jobName': '4#'})
# mdb.jobs['4#']._Message(WARNING, {'phase': STANDARD_PHASE,
#     'message': 'Solver problem. Numerical singularity when processing node TUNNEL-1.79 D.O.F. 2 ratio = 23.9586E+09 .',
#     'jobName': '4#'})
# mdb.jobs['4#']._Message(WARNING, {'phase': STANDARD_PHASE,
#     'message': 'Solver problem. Numerical singularity when processing node TUNNEL-1.80 D.O.F. 1 ratio = 5.76974E+15.',
#     'jobName': '4#'})
# mdb.jobs['4#']._Message(WARNING, {'phase': STANDARD_PHASE,
#     'message': 'Solver problem. Numerical singularity when processing node TUNNEL-1.80 D.O.F. 2 ratio = 358.306E+12  .',
#     'jobName': '4#'})
# mdb.jobs['4#']._Message(STATUS, {'totalTime': 1.1, 'attempts': 1,
#     'timeIncrement': 0.1, 'increment': 1, 'stepTime': 0.1, 'step': 2,
#     'jobName': '4#', 'severe': 0, 'iterations': 3, 'phase': STANDARD_PHASE,
#     'equilibrium': 3})
# mdb.jobs['4#']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 1,
#     'frame': 1, 'jobName': '4#'})
# mdb.jobs['4#']._Message(WARNING, {'phase': STANDARD_PHASE,
#     'message': 'Solver problem. Numerical singularity when processing node TUNNEL-1.79 D.O.F. 2 ratio = 23.9586E+09 .',
#     'jobName': '4#'})
# mdb.jobs['4#']._Message(WARNING, {'phase': STANDARD_PHASE,
#     'message': 'Solver problem. Numerical singularity when processing node TUNNEL-1.80 D.O.F. 1 ratio = 5.76974E+15.',
#     'jobName': '4#'})
# mdb.jobs['4#']._Message(WARNING, {'phase': STANDARD_PHASE,
#     'message': 'Solver problem. Numerical singularity when processing node TUNNEL-1.80 D.O.F. 2 ratio = 358.306E+12  .',
#     'jobName': '4#'})
# mdb.jobs['4#']._Message(WARNING, {'phase': STANDARD_PHASE,
#     'message': 'Solver problem. Numerical singularity when processing node TUNNEL-1.79 D.O.F. 2 ratio = 23.9586E+09 .',
#     'jobName': '4#'})
# mdb.jobs['4#']._Message(WARNING, {'phase': STANDARD_PHASE,
#     'message': 'Solver problem. Numerical singularity when processing node TUNNEL-1.80 D.O.F. 1 ratio = 5.76974E+15.',
#     'jobName': '4#'})
# mdb.jobs['4#']._Message(WARNING, {'phase': STANDARD_PHASE,
#     'message': 'Solver problem. Numerical singularity when processing node TUNNEL-1.80 D.O.F. 2 ratio = 358.306E+12  .',
#     'jobName': '4#'})
# mdb.jobs['4#']._Message(STATUS, {'totalTime': 1.2, 'attempts': 1,
#     'timeIncrement': 0.1, 'increment': 2, 'stepTime': 0.2, 'step': 2,
#     'jobName': '4#', 'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE,
#     'equilibrium': 2})
# mdb.jobs['4#']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 1,
#     'frame': 2, 'jobName': '4#'})
# mdb.jobs['4#']._Message(WARNING, {'phase': STANDARD_PHASE,
#     'message': 'Solver problem. Numerical singularity when processing node TUNNEL-1.79 D.O.F. 2 ratio = 23.9586E+09 .',
#     'jobName': '4#'})
# mdb.jobs['4#']._Message(WARNING, {'phase': STANDARD_PHASE,
#     'message': 'Solver problem. Numerical singularity when processing node TUNNEL-1.80 D.O.F. 1 ratio = 5.76974E+15.',
#     'jobName': '4#'})
# mdb.jobs['4#']._Message(WARNING, {'phase': STANDARD_PHASE,
#     'message': 'Solver problem. Numerical singularity when processing node TUNNEL-1.80 D.O.F. 2 ratio = 358.306E+12  .',
#     'jobName': '4#'})
# mdb.jobs['4#']._Message(STATUS, {'totalTime': 1.35, 'attempts': 1,
#     'timeIncrement': 0.15, 'increment': 3, 'stepTime': 0.35, 'step': 2,
#     'jobName': '4#', 'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE,
#     'equilibrium': 1})
# mdb.jobs['4#']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 1,
#     'frame': 3, 'jobName': '4#'})
# mdb.jobs['4#']._Message(WARNING, {'phase': STANDARD_PHASE,
#     'message': 'Solver problem. Numerical singularity when processing node TUNNEL-1.79 D.O.F. 2 ratio = 23.9586E+09 .',
#     'jobName': '4#'})
# mdb.jobs['4#']._Message(WARNING, {'phase': STANDARD_PHASE,
#     'message': 'Solver problem. Numerical singularity when processing node TUNNEL-1.80 D.O.F. 1 ratio = 5.76974E+15.',
#     'jobName': '4#'})
# mdb.jobs['4#']._Message(WARNING, {'phase': STANDARD_PHASE,
#     'message': 'Solver problem. Numerical singularity when processing node TUNNEL-1.80 D.O.F. 2 ratio = 358.306E+12  .',
#     'jobName': '4#'})
# mdb.jobs['4#']._Message(STATUS, {'totalTime': 1.575, 'attempts': 1,
#     'timeIncrement': 0.225, 'increment': 4, 'stepTime': 0.575, 'step': 2,
#     'jobName': '4#', 'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE,
#     'equilibrium': 1})
# mdb.jobs['4#']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 1,
#     'frame': 4, 'jobName': '4#'})
# mdb.jobs['4#']._Message(WARNING, {'phase': STANDARD_PHASE,
#     'message': 'Solver problem. Numerical singularity when processing node TUNNEL-1.79 D.O.F. 2 ratio = 23.9586E+09 .',
#     'jobName': '4#'})
# mdb.jobs['4#']._Message(WARNING, {'phase': STANDARD_PHASE,
#     'message': 'Solver problem. Numerical singularity when processing node TUNNEL-1.80 D.O.F. 1 ratio = 5.76974E+15.',
#     'jobName': '4#'})
# mdb.jobs['4#']._Message(WARNING, {'phase': STANDARD_PHASE,
#     'message': 'Solver problem. Numerical singularity when processing node TUNNEL-1.80 D.O.F. 2 ratio = 358.306E+12  .',
#     'jobName': '4#'})
# mdb.jobs['4#']._Message(STATUS, {'totalTime': 1.9125, 'attempts': 1,
#     'timeIncrement': 0.3375, 'increment': 5, 'stepTime': 0.9125, 'step': 2,
#     'jobName': '4#', 'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE,
#     'equilibrium': 1})
# mdb.jobs['4#']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 1,
#     'frame': 5, 'jobName': '4#'})
# mdb.jobs['4#']._Message(WARNING, {'phase': STANDARD_PHASE,
#     'message': 'Solver problem. Numerical singularity when processing node TUNNEL-1.79 D.O.F. 2 ratio = 23.9586E+09 .',
#     'jobName': '4#'})
# mdb.jobs['4#']._Message(WARNING, {'phase': STANDARD_PHASE,
#     'message': 'Solver problem. Numerical singularity when processing node TUNNEL-1.80 D.O.F. 1 ratio = 5.76974E+15.',
#     'jobName': '4#'})
# mdb.jobs['4#']._Message(WARNING, {'phase': STANDARD_PHASE,
#     'message': 'Solver problem. Numerical singularity when processing node TUNNEL-1.80 D.O.F. 2 ratio = 358.306E+12  .',
#     'jobName': '4#'})
# mdb.jobs['4#']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 1,
#     'frame': 6, 'jobName': '4#'})
# mdb.jobs['4#']._Message(STATUS, {'totalTime': 2.0, 'attempts': 1,
#     'timeIncrement': 0.0874999999999999, 'increment': 6, 'stepTime': 1.0,
#     'step': 2, 'jobName': '4#', 'severe': 0, 'iterations': 1,
#     'phase': STANDARD_PHASE, 'equilibrium': 1})
# mdb.jobs['4#']._Message(END_STEP, {'phase': STANDARD_PHASE, 'stepId': 2,
#     'jobName': '4#'})
# mdb.jobs['4#']._Message(COMPLETED, {'phase': STANDARD_PHASE,
#     'message': 'Analysis phase complete', 'jobName': '4#'})
# mdb.jobs['4#']._Message(JOB_COMPLETED, {'time': 'Wed Apr 13 18:34:36 2022',
#     'jobName': '4#'})
# Save by 0000 on 2022_04_13-18.37.08; build 2020 2019_09_14-01.49.31 163176
# Save by 0000 on 2022_04_13-18.37.22; build 2020 2019_09_14-01.49.31 163176

#等待job结束
mdb.jobs['4#'].waitForCompletion()
# with open('%s/wttest.txt' % dirs ,'w') as f:
#     f.write('wtt')
#     f.write(a)
# import time
# time.sleep(60)


# 绘制云图
from abaqus import *
from abaqusConstants import *
o3 = session.openOdb(name='D:/abaqus-pytest/%s/4#.odb' % path)
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(deformationScaling=UNIFORM, uniformScaleFactor=1)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(CONTOURS_ON_DEF, ))

#通用调成1，把上方凹陷的去掉,这里需提前调整，否则不会生效
# session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(deformationScaling=UNIFORM, uniformScaleFactor=1)


# 调u，u2对应位移的变化
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT,'Magnitude'),)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U2'), )


# # # 绘制曲线(定义路劲，绘制)
# import xyPlot
# session.Path(name='Path-1', type=NODE_LIST, expression=(('SOIL-1', (33,
#     '334:328:-1', 32, '369:363:-1', 29, '318:312:-1', 25, '272:266:-1', 24, )),
#     ))
# xyp = session.XYPlot('XYPlot-1')
#
# chartName = xyp.charts.keys()[0]
# chart = xyp.charts[chartName]
# pth = session.paths['Path-1']
# xy1 = xyPlot.XYDataFromPath(path=pth, includeIntersections=False,
#     projectOntoMesh=False, pathStyle=PATH_POINTS, numIntervals=10,
#     projectionTolerance=0, shape=DEFORMED, labelType=TRUE_DISTANCE,
#     removeDuplicateXYPairs=True, includeAllElements=False)
# c1 = session.Curve(xyData=xy1)
# chart.setValues(curvesToPlot=(c1, ), )
# session.charts[chartName].autoColor(lines=True, symbols=True)
# session.viewports['Viewport: 1'].setValues(displayedObject=xyp)
# ##保存
# session.printToFile(fileName='D:/abaqus-pytest/%s/xy' % path, format=PNG,
#     canvasObjects=(session.viewports['Viewport: 1'], ))




#保存动画到指定路劲，并调整参数，1帧1秒
#: AVI Codec设置为:无 - 24 比特/像素
session.aviOptions.setValues(compressionMethod=CODEC,
    codecOptions='[12]:aaaaaaaabiaaaaaaaaaaaaaa')
session.imageAnimationOptions.setValues(vpDecorations=ON, vpBackground=ON,
    compass=ON, timeScale=1, frameRate=1)
session.writeImageAnimation(fileName='D:/abaqus-pytest/%s/video1' % path,
    format=AVI, canvasObjects=(session.viewports['Viewport: 1'], ))

#打开缩放系数，只有在装管片的
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=SCALE_FACTOR)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)

#参数保持第一次到处默认的，然后也导出
session.imageAnimationOptions.setValues(vpDecorations=ON, vpBackground=ON,
    compass=ON)
session.writeImageAnimation(fileName='D:/abaqus-pytest/%s/video2' % path,
    format=AVI, canvasObjects=(session.viewports['Viewport: 1'], ))


#打开时间历程（对应所有的过程，即为完整的过程TIME_HISTORY），然后导出
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.imageAnimationOptions.setValues(vpDecorations=ON, vpBackground=ON,
    compass=ON)
session.writeImageAnimation(fileName='D:/abaqus-pytest/%s/video3' % path,
    format=AVI, canvasObjects=(session.viewports['Viewport: 1'], ))

# # 绘制曲线(定义路劲，绘制)
import xyPlot
session.Path(name='Path-1', type=NODE_LIST, expression=(('SOIL-1', (33,
    '334:328:-1', 32, '369:363:-1', 29, '318:312:-1', 25, '272:266:-1', 24, )),
    ))
xyp = session.XYPlot('XYPlot-1')

chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
pth = session.paths['Path-1']
xy1 = xyPlot.XYDataFromPath(path=pth, includeIntersections=False,
    projectOntoMesh=False, pathStyle=PATH_POINTS, numIntervals=10,
    projectionTolerance=0, shape=DEFORMED, labelType=TRUE_DISTANCE,
    removeDuplicateXYPairs=True, includeAllElements=False)
c1 = session.Curve(xyData=xy1)
chart.setValues(curvesToPlot=(c1, ), )
session.charts[chartName].autoColor(lines=True, symbols=True)
session.viewports['Viewport: 1'].setValues(displayedObject=xyp)
##保存
session.printToFile(fileName='D:/abaqus-pytest/%s/xy' % path, format=PNG,
    canvasObjects=(session.viewports['Viewport: 1'], ))


#sava
mdb.saveAs(pathName='%s/%s' % (dirs, path))
import sys
sys.exit(0)
