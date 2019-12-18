import maya.cmds as mc
import ADUtils as au
from angela.rig import main as mn, secondary as sc

reload(mn)
reload(sc)
reload(au)


class MainFace:
    def __init__(self,
                 ctrlGrp,
                 neckJnt,
                 headJnt,
                 headUpJnt,
                 headLowJnt,
                 jawJnt,
                 noseJnt,
                 eyebrowJnt,
                 upperTeethJnt,
                 lowerTeethJnt,
                 tongue01Jnt,
                 tongue02Jnt,
                 tongue03Jnt,
                 tongue04Jnt,
                 earLFTJnt,
                 earRGTJnt,
                 noseTipJnt,
                 chinJnt,
                 throatJnt,
                 scale,
                 nostrilLFTJnt,
                 cheekUpLFTJnt,
                 cheekUpOutLFTJnt,
                 cheekDownLFTJnt,
                 eyebrowInLFTJnt,
                 eyebrowMidLFTJnt,
                 eyebrowOutLFTJnt,
                 browInLFTJnt,
                 browMidLFTJnt,
                 browOutLFTJnt,
                 eyelidPinchLFTJnt,
                 nostrilRGTJnt,
                 cheekUpRGTJnt,
                 cheekUpOutRGTJnt,
                 cheekDownRGTJnt,
                 eyebrowInRGTJnt,
                 eyebrowMidRGTJnt,
                 eyebrowOutRGTJnt,
                 browInRGTJnt,
                 browMidRGTJnt,
                 browOutRGTJnt,
                 eyelidPinchRGTJnt,
                 sideLFT,
                 sideRGT,
                 eyeballJntLFT,
                 eyeballJntRGT,
                 prefixEyeballAim,
                 positionEyeAimCtrl,
                 objectFolMesh,
                 ):

        # BUILD CONTROLLER
        ctrlFaceGroup = mc.group(em=1, n='faceCtrl_grp')


        main = mn.Build(ctrlGrp=ctrlGrp,
                        objectFolMesh=objectFolMesh,
                        neckJnt=neckJnt,
                         headJnt=headJnt,
                        noseJnt=noseJnt,
                         headUpJnt=headUpJnt,
                         headLowJnt=headLowJnt,
                        eyebrowJnt=eyebrowJnt,
                         jawJnt=jawJnt,
                        upperTeethJnt=upperTeethJnt,
                        lowerTeethJnt=lowerTeethJnt,
                        tongue01Jnt=tongue01Jnt,
                        tongue02Jnt=tongue02Jnt,
                        tongue03Jnt=tongue03Jnt,
                        tongue04Jnt=tongue04Jnt,
                         noseTipJnt=noseTipJnt,
                         chinJnt=chinJnt,
                        throatJnt=throatJnt,
                         scale=scale,
                         eyeballJntLFT=eyeballJntLFT,
                         eyeballJntRGT=eyeballJntRGT,
                         prefixEyeballAim=prefixEyeballAim,
                         positionEyeAimCtrl=positionEyeAimCtrl,
                        )


        secLFT = sc.Build(objectFolMesh=objectFolMesh,
                          nostrilJnt=nostrilLFTJnt,
                          earJnt=earLFTJnt,
                          headCtrl=main.headCtrl,
                          headUpCtrl=main.headUpCtrl,
                          headLowCtrl=main.headLowCtrl,
                        cheekUpJnt=cheekUpLFTJnt,
                          cheekUpOutJnt=cheekUpOutLFTJnt,
                          cheekDownJnt=cheekDownLFTJnt,
                        eyebrowInJnt=eyebrowInLFTJnt,
                        eyebrowMidJnt=eyebrowMidLFTJnt,
                        eyebrowOutJnt=eyebrowOutLFTJnt,
                        browInJnt=browInLFTJnt,
                        browMidJnt=browMidLFTJnt,
                        browOutJnt=browOutLFTJnt,
                        eyelidPinchJnt=eyelidPinchLFTJnt,
                        sideRGT=sideRGT,
                        sideLFT=sideLFT,
                        scale=scale,
                        side=sideLFT)

        secRGT = sc.Build(objectFolMesh=objectFolMesh,
                          nostrilJnt=nostrilRGTJnt,
                          earJnt=earRGTJnt,
                          cheekUpJnt=cheekUpRGTJnt,
                          cheekUpOutJnt=cheekUpOutRGTJnt,
                          headCtrl=main.headCtrl,
                          headUpCtrl=main.headUpCtrl,
                          headLowCtrl=main.headLowCtrl,
                        cheekDownJnt=cheekDownRGTJnt,
                        eyebrowInJnt=eyebrowInRGTJnt,
                        eyebrowMidJnt=eyebrowMidRGTJnt,
                        eyebrowOutJnt=eyebrowOutRGTJnt,
                        browInJnt=browInRGTJnt,
                        browMidJnt=browMidRGTJnt,
                        browOutJnt=browOutRGTJnt,
                        eyelidPinchJnt=eyelidPinchRGTJnt,
                        sideRGT=sideRGT,
                        sideLFT=sideLFT,
                        scale=scale,
                        side=sideRGT)

        self.headUpCtrlGrpParent = main.headUpCtrlGrp
        self.headUpCtrl = main.headUpCtrl

        self.headLowCtrl = main.headLowCtrl
        self.jawCtrl = main.jawCtrl

        # CONSTRAINT CHEEK DOWN JNT
        mc.parentConstraint(main.headLowCtrl, main.jawCtrl, secLFT.cheekDownJntGrp, mo=1)
        mc.parentConstraint(main.headLowCtrl, main.jawCtrl, secRGT.cheekDownJntGrp, mo=1)

        mc.parent(secLFT.eyebrowCtrlGrp, secRGT.eyebrowCtrlGrp, main.headUpCtrl)
        mc.parent(secLFT.earCtrlGrp, secRGT.earCtrlGrp, main.headCtrlGimbal)
        mc.parent(secLFT.follicleTransformAll, secRGT.follicleTransformAll, main.follicleTransformAll, ctrlFaceGroup)

        self.ctrlFaceGroup = ctrlFaceGroup
        self.neckCtrlGrp = main.neckCtrlGrp
        self.eyeballAimMainCtrlGrp = main.eyeballAimMainCtrlGrp
        self.eyeballAimMainCtrl = main.eyeballAimMainCtrl
        self.headCtrlGrp = main.headCtrlGrp