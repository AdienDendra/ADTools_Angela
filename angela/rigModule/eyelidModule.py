from __builtin__ import reload

import maya.cmds as mc
from angela.rig import eyelid as el
import ADCtrl as ct, ADUtils as au

reload(el)
reload(ct)
reload(au)

class Eyelid:
    def __init__(self, crvUp,
                 crvDown,
                 offsetEyelidPos,
                 eyeballJnt,
                 prefixEyeball,
                 prefixEyeballAim,
                 scale,
                 side,
                 sideLFT,
                 sideRGT,
                 directionLid01,
                 directionLid02,
                 positionEyeAimCtrl,
                 eyeballAimMainCtrl,
                 headUpCtrl,
                 pupilJnt, irisJnt, prefixPupil, prefixIris,
                 eyeballSpecJnt, prefixEyeballSpec,
                 ctrlGrp, eyeballSpecTipJnt, mainJointGrp,
                 faceCtrlGrp
                 ):

        # world up object eyelid
        worldUpObject = mc.spaceLocator(n='eyeballWorldObj'+side+'_loc')[0]
        mc.delete(mc.parentConstraint(eyeballJnt, worldUpObject))
        value = mc.getAttr(worldUpObject + '.translateY')
        mc.setAttr(worldUpObject + '.translateY', value + (10 * scale))
        # mc.parentConstraint(headUpJoint, worldUpObject, mo=1)
        self.worldUpObject = worldUpObject

        # world up object eyeball aim
        worldUpAimObject = mc.duplicate(worldUpObject, n='eyeballWorldAimObj'+side+'_loc')[0]
        mc.parent(worldUpAimObject, headUpCtrl)
        mc.hide(worldUpAimObject)
        self.worldUpAimObject = worldUpAimObject

        self.eyeballMoveGrp = mc.group(em=1, n='eyeballMove'+side+'_grp')
        self.eyeballMoveOffset = mc.group(em=1, n='eyeballMoveOffset'+side+'_grp', p=self.eyeballMoveGrp)
        mc.delete(mc.parentConstraint(eyeballJnt, self.eyeballMoveGrp))

        self.eyeballMoveAll= mc.group(em=1, n='eyeballMoveAll'+side+'_grp')
        mc.parent(self.eyeballMoveAll, self.eyeballMoveOffset)


        # EYELID UP LFT
        self.eyelidUp = el.Build(crv=crvUp,
                                 worldUpObject=worldUpObject,
                                 eyeballJnt=eyeballJnt,
                                 scale=1,
                                 offsetEyelidPos=offsetEyelidPos,
                                 directionLip01=directionLid01,
                                 directionLip02=directionLid02,
                                 side=side,
                                 sideLFT=sideLFT,
                                 sideRGT=sideRGT,
                                 ctrlColor='yellow',
                                 controllerLidDown=False)

        self.eyelidDown = el.Build(crv=crvDown,
                                   worldUpObject=worldUpObject,
                                   eyeballJnt=eyeballJnt,
                                   scale=1,
                                   offsetEyelidPos=offsetEyelidPos,
                                   directionLip01=directionLid01,
                                   directionLip02=directionLid02,
                                   side=side,
                                   sideLFT=sideLFT,
                                   sideRGT=sideRGT,
                                   ctrlColor='yellow',
                                   controllerLidDown=True)

        # BLINK SETUP
        blink = self.blinkSetup(sideRGT=sideRGT, sideLFT=sideLFT,eyeballJnt=eyeballJnt, prefixEyeball=prefixEyeball,
                                prefixEyeballAim=prefixEyeballAim, crvUp=crvUp,
                                crvDown=crvDown, scale=scale, side=side, eyelidUp=self.eyelidUp,
                                eyelidDown=self.eyelidDown, positionEyeAimCtrl=positionEyeAimCtrl,
                                worldUpAimObject=worldUpAimObject,
                                eyeballAimMainCtrl=eyeballAimMainCtrl,
                                controllerBind03OffsetCtrlUp=self.eyelidUp.controllerBind03OffsetCtrl,
                                controllerBind03OffsetCtrlDown=self.eyelidDown.controllerBind03OffsetCtrl,
                                jointBind03GrpAllUp=self.eyelidUp.jointBind03GrpAll,
                                jointBind03GrpAllDown=self.eyelidDown.jointBind03GrpAll,
                                jointBind03GrpOffsetDown=self.eyelidUp.jointBind03GrpOffset,
                                jointBind03GrpOffsetUp=self.eyelidDown.jointBind03GrpOffset,
                                pupilJnt=pupilJnt, irisJnt=irisJnt, prefixPupil=prefixPupil,
                                prefixIris=prefixIris, eyeballSpecJnt=eyeballSpecJnt,
                                prefixEyeballSpec=prefixEyeballSpec,
                                ctrlGrp=ctrlGrp, headUpCtrl=headUpCtrl,
                                eyeballSpecTipJnt=eyeballSpecTipJnt,
                                mainJointGrp=mainJointGrp,
                                faceCtrlGrp=faceCtrlGrp)

        self.blink = blink

        # connect the eyeball to eyeball up grp bind
        au.connectAttrObject(self.eyeballController, self.eyelidUp.eyeballOffsetBind01[1])
        au.connectAttrObject(self.eyeballController, self.eyelidUp.eyeballOffsetBind03[1])
        au.connectAttrObject(self.eyeballController, self.eyelidUp.eyeballOffsetBind05[1])

        # connect the eyeball to eyeball down grp bind
        au.connectAttrObject(self.eyeballController, self.eyelidDown.eyeballOffsetBind01[1])
        au.connectAttrObject(self.eyeballController, self.eyelidDown.eyeballOffsetBind03[1])
        au.connectAttrObject(self.eyeballController, self.eyelidDown.eyeballOffsetBind05[1])

        # parent contraint eyeball move
        au.connectAttrTransRot(self.eyeballController, self.eyeballMoveOffset)

    # ==================================================================================================================
    #                                                  CORNER CONTROLLER
    # ==================================================================================================================
        # controller in corner
        lidCornerCtrlIn = self.cornerCtrl(matchPosOne=self.eyelidUp.jnt01,
                                          matchPosTwo=self.eyelidDown.jnt01,
                                          prefix='eyelidCornerIn',
                                          scale=scale,
                                          side=side)

        # controller in corner
        lidCornerCtrlOut = self.cornerCtrl(matchPosOne=self.eyelidUp.jnt05,
                                           matchPosTwo=self.eyelidDown.jnt05,
                                           prefix='eyelidCornerOut',
                                           scale=scale,
                                           side=side)

        pos = mc.xform(lidCornerCtrlOut[0], ws=1, q=1, t=1)[0]
        if pos > 0:
            # parent constraint corner grp bind jnt
            au.connectAttrTransRot(lidCornerCtrlIn[0], self.eyelidUp.jointBind01Grp[1])
            au.connectAttrTransRot(lidCornerCtrlIn[0], self.eyelidDown.jointBind01Grp[1])
            au.connectAttrTransRot(lidCornerCtrlOut[0], self.eyelidUp.jointBind05Grp[1])
            au.connectAttrTransRot(lidCornerCtrlOut[0], self.eyelidDown.jointBind05Grp[1])
        else:
            self.cornerReverseNode(sideRGT, sideLFT, lidCornerCtrl=lidCornerCtrlOut[0], side=side, lidCornerName='lidCornerOut',
                                   targetUp=self.eyelidUp.jointBind05Grp[1], targetDown=self.eyelidDown.jointBind05Grp[1])

            self.cornerReverseNode(sideRGT, sideLFT, lidCornerCtrl=lidCornerCtrlIn[0], side=side, lidCornerName='lidCornerIn',
                                   targetUp=self.eyelidUp.jointBind01Grp[1], targetDown=self.eyelidDown.jointBind01Grp[1])

    # ==================================================================================================================
    #                                              PARENT TO GROUP
    # ==================================================================================================================
        mc.parent(self.eyelidUp.controllerBindGrpZro01, lidCornerCtrlIn[0])
        mc.parent(self.eyelidDown.controllerBindGrpZro01, lidCornerCtrlIn[0])
        mc.parent(self.eyelidUp.controllerBindGrpZro05, lidCornerCtrlOut[0])
        mc.parent(self.eyelidDown.controllerBindGrpZro05, lidCornerCtrlOut[0])

        mc.parent(self.eyelidUp.grpDrvCtrl, self.eyelidDown.grpDrvCtrl, lidCornerCtrlIn[1],
                  lidCornerCtrlOut[1], self.eyeballCtrl.control)

        mc.parent(self.eyelidUp.jointGrp, self.eyelidUp.locatorGrp,
                  self.eyelidUp.curvesGrp, self.eyelidUp.jointGrp,
                  self.eyelidDown.jointGrp, self.eyelidDown.locatorGrp,
                  self.eyelidDown.curvesGrp, self.eyelidDown.jointGrp, self.eyeballMoveAll)

        mc.parent(self.eyelidUp.bindJntGrp, self.eyelidDown.bindJntGrp, blink)

        mc.parent(self.eyeballCtrl.parentControl[0], headUpCtrl)

    def cornerReverseNode(self, sideRGT, sideLFT, lidCornerCtrl, side, lidCornerName='', targetUp='', targetDown=''):
        if sideRGT in lidCornerName:
            newName = lidCornerName.replace(sideRGT, '')
        elif sideLFT in lidCornerName:
            newName = lidCornerName.replace(sideLFT, '')
        else:
            newName = lidCornerName

        transRev = mc.createNode('multiplyDivide', n=newName + 'Trans' + side + '_mdn')
        rotRev = mc.createNode('multiplyDivide', n=newName+ 'Rot' + side + '_mdn')
        mc.connectAttr(lidCornerCtrl + '.translate', transRev + '.input1')
        mc.setAttr(transRev + '.input2X', -1)

        mc.connectAttr(lidCornerCtrl + '.rotate', rotRev + '.input1')
        mc.setAttr(rotRev + '.input2Y', -1)
        mc.setAttr(rotRev + '.input2Z', -1)

        mc.connectAttr(transRev + '.output', targetUp + '.translate')
        mc.connectAttr(rotRev + '.output', targetUp + '.rotate')
        mc.connectAttr(transRev + '.output', targetDown + '.translate')
        mc.connectAttr(rotRev + '.output', targetDown + '.rotate')

    def cornerCtrl(self,matchPosOne, matchPosTwo, prefix, scale, side):
        cornerCtrl = ct.Control(matchPos=matchPosOne, matchPosTwo=matchPosTwo,
                                prefix=prefix,
                                shape=ct.CIRCLEPLUS, groupsCtrl=['Zro', 'Offset'],
                                ctrlSize=scale * 0.3,
                                ctrlColor='blue', lockChannels=['v', 's'], side=side)

        # check position
        pos = mc.xform(cornerCtrl.control, ws=1, q=1, t=1)[0]

        # flipping the controller
        if pos < 0:
            mc.setAttr(cornerCtrl.parentControl[0] + '.scaleX', -1)

        self.control = cornerCtrl.control
        self.parentControlZro = cornerCtrl.parentControl[0]
        self.parentControlOffset = cornerCtrl.parentControl[1]

        return cornerCtrl.control, cornerCtrl.parentControl[0]

    def blinkSetup(self, sideRGT, sideLFT, eyeballJnt, prefixEyeball, prefixEyeballAim, crvUp, crvDown, scale,
                   side, eyelidUp, eyelidDown, positionEyeAimCtrl, worldUpAimObject, eyeballAimMainCtrl,
                   controllerBind03OffsetCtrlUp, controllerBind03OffsetCtrlDown, jointBind03GrpAllUp, jointBind03GrpAllDown,
                   jointBind03GrpOffsetDown, jointBind03GrpOffsetUp, pupilJnt, irisJnt, prefixPupil, prefixIris,
                   eyeballSpecJnt, prefixEyeballSpec, ctrlGrp, headUpCtrl, faceCtrlGrp,
                   eyeballSpecTipJnt, mainJointGrp):

        # ==============================================================================================================
        #                                             EYEBALL CONTROLLER
        # ==============================================================================================================
        # # create group eye spec
        # eyeSpecDirectionGrp = mc.group(em=1, n=au.prefixName(eyeballSpecJnt) + 'Direction'+ side+'_grp')
        # eyeSpecDirectionOffsetGrp = mc.group(em=1, n=au.prefixName(eyeballSpecJnt) + 'DirectionOffset'+ side+'_grp', p=eyeSpecDirectionGrp)
        # self.eyeSpecDirectionOffsetGrp = eyeSpecDirectionOffsetGrp
        #
        #
        # mc.select(cl=1)
        # mc.delete(mc.parentConstraint(eyeballSpecJnt, eyeSpecDirectionGrp))

        eyeballGrp = au.createParentTransform(listparent=['Zro', 'Offset'], object=eyeballJnt, matchPos=eyeballJnt,
                                              prefix='eyeball',
                                              suffix='_jnt', side=side)
        irisGrp = au.createParentTransform(listparent=['Zro'], object=irisJnt, matchPos=irisJnt,
                                             prefix='iris',
                                             suffix='_jnt', side=side)
        pupilGrp = au.createParentTransform(listparent=['Zro'], object=pupilJnt, matchPos=pupilJnt,
                                             prefix='pupil',
                                             suffix='_jnt', side=side)

        eyeballSpecGrp = au.createParentTransform(listparent=['Zro'], object=eyeballSpecJnt, matchPos=eyeballSpecJnt,
                                             prefix='eyeballSpec',
                                             suffix='_jnt', side=side)
        eyeballSpecTipGrp = au.createParentTransform(listparent=['Zro'], object=eyeballSpecTipJnt, matchPos=eyeballSpecTipJnt,
                                             prefix='eyeballSpecTip',
                                             suffix='_jnt', side=side)

        self.eyeballCtrl = ct.Control(matchPos=eyeballJnt,
                                      prefix=prefixEyeball,
                                      shape=ct.JOINTPLUS, groupsCtrl=['Zro', 'Offset'],
                                      ctrlSize=scale * 2,
                                      ctrlColor='blue', lockChannels=['v'], side=side,
                                      connect=['connectMatrixAll'])

        self.irisCtrl = ct.Control(matchPos=irisJnt,
                                      prefix=prefixIris,
                                      shape=ct.CIRCLEPLUS, groupsCtrl=['Zro', 'Offset'],
                                      ctrlSize=scale * 2,
                                      ctrlColor='red', lockChannels=['v'], side=side,
                                      connect=['connectMatrixAll'])

        self.pupilCtrl = ct.Control(matchPos=pupilJnt,
                                      prefix=prefixPupil,
                                      shape=ct.CIRCLEPLUS, groupsCtrl=['Zro', 'Offset'],
                                      ctrlSize=scale * 2,
                                      ctrlColor='yellow', lockChannels=['v'], side=side,
                                      connect=['connectMatrixAll'])

        eyeballSpecCtrl = ct.Control(matchPos=eyeballSpecJnt,
                                      prefix=prefixEyeballSpec,
                                      shape=ct.CIRCLEPLUS, groupsCtrl=['', 'Global', 'Local'],
                                      ctrlSize=scale * 2,
                                      ctrlColor='yellow', lockChannels=['v', 's'], side=side,
                                     connect=['parentCons','scaleCons'])

        # ADD ATTRIBUTE EYEBALL SPEC
        self.offsetEyeballSpec = au.addAttribute(objects=[eyeballSpecCtrl.control], longName=['Offset'],
                                         attributeType="float", min=0, dv=0, k=True)

        self.sizeEyeballSpec = au.addAttribute(objects=[eyeballSpecCtrl.control], longName=['size'],
                                         attributeType="float", min=0, dv=1, k=True)


        self.eyeballController = self.eyeballCtrl.control

        self.eyeballSpecCtrl = eyeballSpecCtrl.control
        self.eyeballSpecCtrlGrp = eyeballSpecCtrl.parentControl[0]
        self.eyeballSpecCtrlGlobal = eyeballSpecCtrl.parentControl[1]
        self.eyeballSpecCtrlLocal= eyeballSpecCtrl.parentControl[2]


        # PARENT EYE SPEC DIRECTION TO EYEBALL GRP
        # mc.parent(eyeSpecDirectionGrp, eyeballGrp[1])
        mc.parent(self.pupilCtrl.parentControl[0], self.irisCtrl.control)
        mc.parent(self.irisCtrl.parentControl[0], self.eyeballController)
        mc.parent(eyeballSpecGrp[0], mainJointGrp)
        mc.parent(self.eyeballSpecCtrlGrp, faceCtrlGrp)

        # ADD ATTRIBUTE
        au.addAttribute(objects=[self.eyeballCtrl.control], longName=['eyelidDegree'], niceName=[' '], at="enum",
                        en='Eyelid Degree', cb=True)

        self.eyelidPos = au.addAttribute(objects=[self.eyeballCtrl.control], longName=['eyelidPos'],
                                         attributeType="float", min=0, max=1, dv=0.6, k=True)

        self.eyelidFollow = au.addAttribute(objects=[self.eyeballCtrl.control], longName=['eyelidFollow'],
                                         attributeType="float", min=0.001, dv=1, k=True)

        # LOCAL WORLD EYEBALL SPEC
        self.localWorld(objectName='eyeballSpec', objectCtrl=self.eyeballSpecCtrl,
                        objectParentGrp=self.eyeballSpecCtrlGrp,
                        objectParentGlobal=self.eyeballSpecCtrlGlobal,
                        objectParentLocal=self.eyeballSpecCtrlLocal,
                        localBase=headUpCtrl, worldBase=ctrlGrp, eyeAim=False, side=side)

        # CONNECT ATTRIBUTE EYEBALL SPEC
        mc.connectAttr(self.eyeballSpecCtrl+'.%s' % self.offsetEyeballSpec, eyeballSpecTipJnt+'.translateZ')
        mc.connectAttr(self.eyeballSpecCtrl+'.%s' % self.sizeEyeballSpec,eyeballSpecTipJnt+'.scaleX')
        mc.connectAttr(self.eyeballSpecCtrl+'.%s' % self.sizeEyeballSpec,eyeballSpecTipJnt+'.scaleY')
        mc.connectAttr(self.eyeballSpecCtrl+'.%s' % self.sizeEyeballSpec,eyeballSpecTipJnt+'.scaleZ')

        # SCALE CONSTRAINT
        mc.scaleConstraint(headUpCtrl, eyeballSpecCtrl.parentControl[1], mo=1)

        # # jaw reverse trans
        # self.eyeSpecReverseNode(prefixObject=prefixEyeballSpec, nodeName='ReverseTrans', eyeSpecController=self.eyeballSpecCtrl,
        #                         eyeSpecOffsetGrpCtrl=self.eyeballSpecCtrlOffset, connection='translate', side=side)
        #
        # self.eyeSpecReverseNode(prefixObject=prefixEyeballSpec, nodeName='ReverseRot', eyeSpecController=self.eyeballSpecCtrl,
        #                         eyeSpecOffsetGrpCtrl=self.eyeballSpecCtrlOffset, connection='rotate', side=side)
        #
        # au.connectAttrRot(self.eyeballSpecCtrl, eyeballSpecJnt)
        # au.connectAttrTrans(self.eyeballSpecCtrl, eyeballSpecTipJnt)


        # # connect to base joint
        # self.eyeSpecCtrlGimbalDriverJnt(prefixObject=prefixEyeballSpec, nodeName='AddTrans', eyeSpecController=head.jawCtrl.control,
        #                                 jawControllerGimbal=head.jawCtrl.controlGimbal, jawTarget=jawJoint,
        #                                 attribute='translate')
        #
        # self.eyeSpecCtrlGimbalDriverJnt(prefixObject=prefixEyeballSpec, nodeName='AddRot', eyeSpecController=head.jawCtrl.control,
        #                                 jawControllerGimbal=head.jawCtrl.controlGimbal, jawTarget=jawJoint,
        #                                 attribute='rotate')
        #
        # # connect to jaw direction offset
        # self.eyeSpecCtrlGimbalDriverJnt(prefixObject=prefixEyeballSpec, nodeName='AddTransDir', eyeSpecController=head.jawCtrl.control,
        #                                 jawControllerGimbal=head.jawCtrl.controlGimbal, jawTarget=head.jawDirectionOffsetGrp,
        #                                 attribute='translate')
        #
        # self.eyeSpecCtrlGimbalDriverJnt(prefixObject=prefixEyeballSpec, nodeName='AddRotDir', eyeSpecController=head.jawCtrl.control,
        #                                 jawControllerGimbal=head.jawCtrl.controlGimbal, jawTarget=head.jawDirectionOffsetGrp,
        #                                 attribute='rotate')

        # mc.delete(mc.parentConstraint(ctrlGrp, self.eyeballSpecCtrlOffsetMtx))
        # # connect the tip joint to parent ctrl jaw
        # dMtxEyeSpec = mc.createNode('decomposeMatrix', n=prefixEyeballSpec + side+ '_dmtx')
        # mc.connectAttr(eyeballSpecTipJnt + '.worldMatrix[0]', dMtxEyeSpec + '.inputMatrix')
        #
        # mc.connectAttr(dMtxEyeSpec + '.outputTranslate', self.eyeballSpecCtrlMtx + '.translate')
        # mc.connectAttr(dMtxEyeSpec + '.outputRotate', self.eyeballSpecCtrlMtx + '.rotate')
        # mc.connectAttr(dMtxEyeSpec + '.outputScale', self.eyeballSpecCtrlMtx + '.scale')

        # ==============================================================================================================
        #                                             EYEBALL AIM
        # ==============================================================================================================
        if mc.xform(eyeballJnt, q=1, ws=1, t=1)[0] > 0:
            ctrlColor ='red'
        else:
            ctrlColor='yellow'

        self.eyeballAimCtrl = ct.Control(matchPos=eyeballJnt,
                                      prefix=prefixEyeballAim,
                                      shape=ct.LOCATOR, groupsCtrl=['Zro', 'Offset'],
                                      ctrlSize=scale * 0.2,
                                      ctrlColor=ctrlColor, lockChannels=['v','r','s'], side=side)

        eyeballAimCtrl = self.eyeballAimCtrl.control

        getAttribute = mc.getAttr(self.eyeballAimCtrl.parentControl[0]+'.translateZ')
        mc.setAttr(self.eyeballAimCtrl.parentControl[0]+'.translateZ', getAttribute+(positionEyeAimCtrl*scale))

        mc.aimConstraint(self.eyeballAimCtrl.control, eyeballGrp[1], mo=1, weight=1, aimVector=(0, 0, 1), upVector=(0, 1, 0),
                         worldUpType="object", worldUpObject=worldUpAimObject)

        # PARENT EYE AIM TO EYEBALL AIM MAIN CTRL
        mc.parent(self.eyeballAimCtrl.parentControl[0], eyeballAimMainCtrl)

        # EXPRESSION UP AND DOWN FOLLOW EYELID CTRL
        expressionEyelidCtrl= "$range = {5}.{1}; " \
                            "$a = 20 /$range; " \
                            "$b = 30 /$range; " \
                            "$c = 80 /$range;" \
                            "{2}.translateX = {3}.translateX /$c + {0}.translateX /$c;" \
                           "{2}.translateY = {3}.translateY /$a + {0}.translateY /$a;" \
                           "{4}.translateX = {3}.translateX /$c + {0}.translateX /$c;" \
                           "{4}.translateY = -{3}.translateY /$b - {0}.translateY /$b;"\
            \
            .format(eyeballAimCtrl,  # 0
                    self.eyelidFollow,  # 1
                    controllerBind03OffsetCtrlUp,  # 2
                    eyeballAimMainCtrl,# 3
                    controllerBind03OffsetCtrlDown,
                    self.eyeballCtrl.control
                    )

        mc.expression(s=expressionEyelidCtrl, n="%s%s%s" % ('eyelidCtrl', side, '_expr'), ae=0)
        # $range = eyeballLFT_ctrl.eyelidFollow;
        # $a = 30 /$range;
        # $b = 8 /$range;
        # $d = 12 /$range;
        # $c = 60 /$range;
        # $e = 50 /$range;
        # $f = 60 /$range;
        # $g = 60 /$range;
        # $h = 25 /$range;
        #
        # if (eyeballAimLFT_ctrl.translateY >= 0)
        # {eyelidUpBindAll03LFT_grp.translateY = eyeballAimLFT_ctrl.translateY /$g;
        # eyelidDownBindAll03LFT_grp.translateY = eyeballAimLFT_ctrl.translateY /$h;}
        #
        # else if (eyeballAimLFT_ctrl.translateY < 0)
        # {eyelidUpBindAll03LFT_grp.translateY = eyeballAimLFT_ctrl.translateY /$d;
        # eyelidDownBindAll03LFT_grp.translateY = eyeballAimLFT_ctrl.translateY /$f;}
        # eyelidUpBindAll03LFT_grp.translateX = eyeballAimLFT_ctrl.translateX /$c;
        # eyelidDownBindAll03LFT_grp.translateX = eyeballAimLFT_ctrl.translateX /$c;
        #
        # if (eyeballAim_ctrl.translateY >= 0)
        # {eyelidDownBindOffset03LFT_grp.translateY = eyeballAim_ctrl.translateY /$h;
        # eyelidUpBindOffset03LFT_grp.translateY = eyeballAim_ctrl.translateY /$g;}
        #
        # else if
        # (eyeballAim_ctrl.translateY < 0)
        # {eyelidDownBindOffset03LFT_grp.translateY = eyeballAim_ctrl.translateY /$e;
        # eyelidUpBindOffset03LFT_grp.translateY = eyeballAim_ctrl.translateY /$a;}
        # eyelidDownBindOffset03LFT_grp.translateX = eyeballAim_ctrl.translateX /$c;
        # eyelidUpBindOffset03LFT_grp.translateX = eyeballAim_ctrl.translateX /$c;

        # EXPRESSION UP AND DOWN FOLLOW EYELID BIND
        expressionEyelidBind = "$range = {7}.{1}; " \
                               "$a = 30 /$range; " \
                               "$d = 12 /$range; " \
                               "$c = 60 /$range;" \
                               "$e = 50 /$range; " \
                               "$b = 25 /$range; " \
                               "if ({0}.translateY >= 0) " \
                               "{8} " \
                               "{2}.translateY = {0}.translateY /$c; " \
                               "{3}.translateY = {0}.translateY /$b;" \
                               "{9} " \
                               "else if ({0}.translateY < 0)" \
                               "{8}" \
                               "{2}.translateY = {0}.translateY /$d; " \
                               "{3}.translateY = {0}.translateY /$c;" \
                               "{9} " \
                               "{2}.translateX = {0}.translateX /$c; " \
                               "{3}.translateX = {0}.translateX /$c; " \
                               "if ({6}.translateY >= 0) " \
                               "{8}" \
                               "{4}.translateY = {6}.translateY /$b; " \
                               "{5}.translateY = {6}.translateY /$c;" \
                               "{9} " \
                               "else if ({6}.translateY < 0) " \
                               "{8}" \
                               "{4}.translateY = {6}.translateY /$e; " \
                               "{5}.translateY = {6}.translateY /$a;" \
                               "{9} " \
                               "{4}.translateX = {6}.translateX /$c; " \
                               "{5}.translateX = {6}.translateX /$c;" \
            \
            .format(eyeballAimCtrl,
                    self.eyelidFollow,
                    jointBind03GrpAllUp,
                    jointBind03GrpAllDown,
                    jointBind03GrpOffsetUp,
                    jointBind03GrpOffsetDown,
                    eyeballAimMainCtrl,
                    self.eyeballCtrl.control,
                    "{",
                    "}")

        mc.expression(s=expressionEyelidBind, n="%s%s%s" % ('eyelidBind', side, '_expr'), ae=0)

        # ==============================================================================================================
        #                                                   BLINK
        # ==============================================================================================================
        # CREATE CURVE MID BLINK
        curveBlinkBindMidOld = mc.curve(d=3, ep=[(self.eyelidUp.xformJnt01), (self.eyelidUp.xformJnt05)])
        curveBlinkBindMidReb = mc.rebuildCurve(curveBlinkBindMidOld, ch=0, rpo=1, rt=0, end=1, kr=0, kcp=0,
                                                               kep=1, kt=0, s=8, d=3, tol=0.01)

        curveBlinkBindMid = mc.rename(curveBlinkBindMidReb, ('eyelidBlink' + side + '_crv'))

        curveBlinkUp = mc.duplicate(crvUp, n='eyelidBlinkUp'+side+'_crv')[0]
        curveBlinkDown = mc.duplicate(crvDown, n='eyelidBlinkDown'+side+'_crv')[0]

        blinkBsn = mc.blendShape(eyelidUp.deformCrv, eyelidDown.deformCrv, curveBlinkBindMid, n=('eyelidBlink' +side+ '_bsn'),
                      weight=[(0, 1), (1, 0)])[0]

        mc.select(cl=1)
        if sideRGT in crvUp:
            crvUpNewName = crvUp.replace(sideRGT, '')
        elif sideLFT in crvUp:
            crvUpNewName = crvUp.replace(sideLFT, '')
        else:
            crvUpNewName = crvUp
        # wire deform up on mid curves
        stickyMidwireDefUp = mc.wire(curveBlinkUp, dds=(0, 100 * scale), wire=curveBlinkBindMid)
        stickyMidwireDefUp[0] = mc.rename(stickyMidwireDefUp[0], (au.prefixName(crvUpNewName) + 'Blink' +side+ '_wireNode'))

        # SET TO DOWN CURVE
        mc.setAttr(blinkBsn+'.%s' % eyelidUp.deformCrv, 0)
        mc.setAttr(blinkBsn+'.%s'% eyelidDown.deformCrv, 1)

        mc.select(cl=1)
        if sideRGT in crvDown:
            crvDownNewName = crvDown.replace(sideRGT, '')
        elif sideLFT in crvDown:
            crvDownNewName = crvDown.replace(sideLFT, '')
        else:
            crvDownNewName = crvDown
        # wire deform down on mid curves
        stickyMidwireDefDown = mc.wire(curveBlinkDown, dds=(0, 100 * scale), wire=curveBlinkBindMid)
        stickyMidwireDefDown[0] = mc.rename(stickyMidwireDefDown[0], (au.prefixName(crvDownNewName) + 'Blink' + side+ '_wireNode'))

        # SET SCALE WIRE 0
        mc.setAttr(stickyMidwireDefUp[0]+'.scale[0]', 0)
        mc.setAttr(stickyMidwireDefDown[0]+'.scale[0]', 0)

        # SET KEYFRAME
        mc.setDrivenKeyframe(blinkBsn +'.%s' % eyelidUp.deformCrv,
                             cd='%s.%s' % (self.eyeballCtrl.control, self.eyelidPos),
                             dv=0, v=1, itt='linear', ott='linear')

        mc.setDrivenKeyframe(blinkBsn +'.%s' % eyelidUp.deformCrv,
                             cd='%s.%s' % (self.eyeballCtrl.control, self.eyelidPos),
                             dv=1, v=0, itt='linear', ott='linear')

        mc.setDrivenKeyframe(blinkBsn + '.%s' % eyelidDown.deformCrv,
                             cd='%s.%s' % (self.eyeballCtrl.control, self.eyelidPos),
                             dv=0, v=0, itt='linear', ott='linear')

        mc.setDrivenKeyframe(blinkBsn + '.%s' % eyelidDown.deformCrv,
                             cd='%s.%s' % (self.eyeballCtrl.control, self.eyelidPos),
                             dv=1, v=1, itt='linear', ott='linear')

        # CONNECT TO BLENDSHAPE BIND CURVE
        eyelidUpBsn = mc.blendShape(curveBlinkUp, crvUp, n=('eyelidBlinkUp' +side+ '_bsn'),
                      weight=[(0, 1)])[0]

        mc.connectAttr(eyelidUp.controllerBind03Ctrl+'.%s' % eyelidUp.closeEyelid, eyelidUpBsn+'.%s'% curveBlinkUp)

        eyelidDownBsn = mc.blendShape(curveBlinkDown, crvDown, n=('eyelidBlinkDown' +side+ '_bsn'),
                      weight=[(0, 1)])[0]

        mc.connectAttr(eyelidDown.controllerBind03Ctrl+'.%s' % eyelidDown.closeEyelid, eyelidDownBsn+'.%s'% curveBlinkDown)

        # CREATE GROUP FOR EYELID STUFF
        eyelidGrp = mc.group(em=1, n='eyelid' + side + '_grp')

        return eyelidGrp

    def localWorld(self,objectName, objectCtrl, objectParentGrp,
                   objectParentGlobal, objectParentLocal, localBase, worldBase, side, eyeAim=False):
        # LOCAL WORLD HEAD
        local = mc.createNode('transform', n=objectName + 'Local'+side+'_grp')
        mc.parent(local, objectParentGrp)
        mc.setAttr(local + '.translate', 0, 0, 0, type="double3")
        mc.setAttr(local + '.rotate', 0, 0, 0, type="double3")

        world = mc.duplicate(local, n=objectName + 'World_grp')[0]

        mc.parentConstraint(localBase, local, mo=1)
        mc.parentConstraint(worldBase, world, mo=1)

        if not eyeAim:
            mc.parentConstraint(local, objectParentGlobal, mo=1)
            localWorldCons = mc.orientConstraint(local, world, objectParentLocal, mo=1)[0]
        else:
            localWorldCons = mc.parentConstraint(local, world, objectParentLocal, mo=1)[0]

        # CONNECT THE ATTRIBUTE
        headLocalWrld = au.addAttribute(objects=[objectCtrl], longName=['localWorld'],
                                             attributeType="float", min=0, max=1, dv=0, k=True)

        # CREATE REVERSE
        reverse = mc.createNode('reverse', n=objectName + 'LocalWorld'+side+'_rev')
        mc.connectAttr(objectCtrl + '.%s' % headLocalWrld, reverse + '.inputX')

        mc.connectAttr(reverse + '.outputX', localWorldCons + '.%sW0' % local)
        mc.connectAttr(objectCtrl + '.%s' % headLocalWrld, localWorldCons + '.%sW1' % world)


    def eyeSpecReverseNode(self, prefixObject, nodeName, eyeSpecController, eyeSpecOffsetGrpCtrl, side, connection):
        mdnReverseJaw = mc.createNode('multiplyDivide', n=prefixObject + nodeName +side+'_mdn')
        mc.setAttr(mdnReverseJaw + '.input2X', -1)
        mc.setAttr(mdnReverseJaw + '.input2Y', -1)
        mc.setAttr(mdnReverseJaw + '.input2Z', -1)

        mc.connectAttr(eyeSpecController + '.%s' % connection, mdnReverseJaw + '.input1')
        mc.connectAttr(mdnReverseJaw + '.output', eyeSpecOffsetGrpCtrl + '.%s' % connection)

    # def eyeSpecCtrlGimbalDriverJnt(self, prefixObject, nodeName, eyeSpecController, jawControllerGimbal, side, jawTarget, attribute):
    #     pmaJawAdd = mc.createNode('plusMinusAverage', n=prefixObject +nodeName+side+'_pma')
    #     mc.connectAttr(eyeSpecController + '.%s' % attribute, pmaJawAdd + '.input3D[0]')
    #     mc.connectAttr(jawControllerGimbal+'.%s' % attribute, pmaJawAdd+'.input3D[1]')
    #
    #     mc.connectAttr(pmaJawAdd +'.output3D', jawTarget + '.%s' % attribute)
