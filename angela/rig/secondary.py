import maya.cmds as mc
import ADCtrl as ac, ADUtils as au

reload(ac)

class Build:
    def __init__(self,
                 nostrilJnt,
                 earJnt,
                 cheekUpJnt,
                 cheekUpOutJnt,
                 cheekDownJnt,
                 eyebrowInJnt,
                 eyebrowMidJnt,
                 eyebrowOutJnt,
                 browInUpJnt,
                 browMidUpJnt,
                 browOutUpJnt,
                 eyelidPinchInJnt,
                 browInDownJnt,
                 browMidDownJnt,
                 browOutDownJnt,
                 eyelidPinchOutJnt,
                 scale,
                 objectFolMesh,
                 sideRGT,
                 sideLFT,
                 side,
                 headCtrl,
                 headUpCtrl,
                 headLowCtrl
                 ):

        # check position
        pos = mc.xform(nostrilJnt, ws=1, q=1, t=1)[0]

        nostrilCtrl = ac.Control(matchPos=nostrilJnt,
                                      prefix='nostril',
                                      shape=ac.JOINT, groupsCtrl=['','Offset'],
                                      ctrlSize=scale * 0.5,
                                      ctrlColor='yellow', lockChannels=['v'], side=side)

        cheekUpCtrl = ac.Control(matchPos=cheekUpJnt,
                                      prefix='cheekUp',
                                      shape=ac.JOINT, groupsCtrl=[''],
                                      ctrlSize=scale * 1.0,
                                      ctrlColor='yellow', lockChannels=['v'], side=side)

        cheekUpOutCtrl = ac.Control(matchPos=cheekUpOutJnt,
                                      prefix='cheekUpOut',
                                      shape=ac.JOINT, groupsCtrl=[''],
                                      ctrlSize=scale * 1.0,
                                      ctrlColor='yellow', lockChannels=['v'], side=side)

        cheekDownCtrl = ac.Control(matchPos=cheekDownJnt,
                                        prefix='cheekDown',
                                        shape=ac.JOINT, groupsCtrl=[''],
                                        ctrlSize=scale * 1.0,
                                        ctrlColor='yellow', lockChannels=['v'], side=side)

        eyebrowInCtrl = ac.Control(matchPos=eyebrowInJnt,
                                        prefix='eyebrowIn',
                                        shape=ac.CUBE, groupsCtrl=[''],
                                        ctrlSize=scale * 0.5,
                                        ctrlColor='blue', lockChannels=['v'], side=side)

        eyebrowMidCtrl = ac.Control(matchPos=eyebrowMidJnt,
                                         prefix='eyebrowMid',
                                         shape=ac.CUBE, groupsCtrl=[''],
                                         ctrlSize=scale * 0.5,
                                         ctrlColor='blue', lockChannels=['v'], side=side)

        eyebrowOutCtrl = ac.Control(matchPos=eyebrowOutJnt,
                                         prefix='eyebrowOut',
                                         shape=ac.CUBE, groupsCtrl=[''],
                                         ctrlSize=scale * 0.5,
                                         ctrlColor='blue', lockChannels=['v'], side=side)

        eyebrowCtrl = ac.Control(matchPos=eyebrowInJnt,
                                 matchPosTwo=eyebrowOutJnt,
                                 prefix='eyebrows',
                                 shape=ac.SQUAREPLUS, groupsCtrl=[''],
                                 ctrlSize=scale * 3.0,
                                 ctrlColor='yellow', lockChannels=['v'], side=side)

        browInUpCtrl = ac.Control(matchPos=browInUpJnt,
                                  prefix='browInUp',
                                  shape=ac.JOINT, groupsCtrl=[''],
                                  ctrlSize=scale * 0.4,
                                  ctrlColor='red', lockChannels=['v'], side=side)

        browMidUpCtrl = ac.Control(matchPos=browMidUpJnt,
                                   prefix='browMidUp',
                                   shape=ac.JOINT, groupsCtrl=[''],
                                   ctrlSize=scale * 0.4,
                                   ctrlColor='red', lockChannels=['v'], side=side)

        browOutUpCtrl = ac.Control(matchPos=browOutUpJnt,
                                   prefix='browOutUp',
                                   shape=ac.JOINT, groupsCtrl=[''],
                                   ctrlSize=scale * 0.4,
                                   ctrlColor='red', lockChannels=['v'], side=side)

        eyelidPinchInCtrl = ac.Control(matchPos=eyelidPinchInJnt,
                                       prefix='eyelidPinchIn',
                                       shape=ac.JOINT, groupsCtrl=[''],
                                       ctrlSize=scale * 1.0,
                                       ctrlColor='blue', lockChannels=['v'], side=side)

        browInDownCtrl = ac.Control(matchPos=browInDownJnt,
                                    prefix='browInDown',
                                    shape=ac.JOINT, groupsCtrl=[''],
                                    ctrlSize=scale * 0.4,
                                    ctrlColor='red', lockChannels=['v'], side=side)

        browMidDownCtrl = ac.Control(matchPos=browMidDownJnt,
                                     prefix='browMidDown',
                                     shape=ac.JOINT, groupsCtrl=[''],
                                     ctrlSize=scale * 0.4,
                                     ctrlColor='red', lockChannels=['v'], side=side)

        browOutDownCtrl = ac.Control(matchPos=browOutDownJnt,
                                     prefix='browOutDown',
                                     shape=ac.JOINT, groupsCtrl=[''],
                                     ctrlSize=scale * 0.4,
                                     ctrlColor='red', lockChannels=['v'], side=side)

        eyelidPinchOutCtrl = ac.Control(matchPos=eyelidPinchOutJnt,
                                        prefix='eyelidPinchOut',
                                        shape=ac.JOINT, groupsCtrl=[''],
                                        ctrlSize=scale * 1.0,
                                        ctrlColor='blue', lockChannels=['v'], side=side)

        earCtrl = ac.Control(matchPos=earJnt,
                                      prefix='ear',
                                      shape=ac.CUBE, groupsCtrl=[''],
                                      ctrlSize=scale * 1.0,
                                      ctrlColor='blue', lockChannels=['v'], side=side)


    # ==================================================================================================================
    #                                            ASSIGNING THE INSTANCE NAME
    # ==================================================================================================================

        self.nostrilCtrl = nostrilCtrl.control
        self.nostrilCtrlGrp = nostrilCtrl.parentControl[0]
        self.nostrilCtrlOffset = nostrilCtrl.parentControl[1]

        self.cheekUpCtrl = cheekUpCtrl.control
        self.cheekUpCtrlGrp = cheekUpCtrl.parentControl[0]

        self.cheekUpOutCtrl = cheekUpOutCtrl.control
        self.cheekUpOutCtrlGrp = cheekUpOutCtrl.parentControl[0]

        self.cheekDownCtrl = cheekDownCtrl.control
        self.cheekDownCtrlGrp = cheekDownCtrl.parentControl[0]

        self.eyebrowInCtrl = eyebrowInCtrl.control
        self.eyebrowInCtrlGrp = eyebrowInCtrl.parentControl[0]

        self.eyebrowMidCtrl = eyebrowMidCtrl.control
        self.eyebrowMidCtrlGrp = eyebrowMidCtrl.parentControl[0]

        self.eyebrowOutCtrl = eyebrowOutCtrl.control
        self.eyebrowOutCtrlGrp = eyebrowOutCtrl.parentControl[0]

        self.eyebrowCtrl = eyebrowCtrl.control
        self.eyebrowCtrlGrp = eyebrowCtrl.parentControl[0]

        self.browInUpCtrl = browInUpCtrl.control
        self.browInUpCtrlGrp = browInUpCtrl.parentControl[0]

        self.browMidUpCtrl = browMidUpCtrl.control
        self.browMidUpCtrlGrp = browMidUpCtrl.parentControl[0]

        self.browOutUpCtrl = browOutUpCtrl.control
        self.browOutUpCtrlGrp = browOutUpCtrl.parentControl[0]

        self.eyelidPinchInCtrl = eyelidPinchInCtrl.control
        self.eyelidPinchInCtrlGrp = eyelidPinchInCtrl.parentControl[0]

        self.browInDownCtrl = browInDownCtrl.control
        self.browInDownCtrlGrp = browInDownCtrl.parentControl[0]

        self.browMidDownCtrl = browMidDownCtrl.control
        self.browMidDownCtrlGrp = browMidDownCtrl.parentControl[0]

        self.browOutDownCtrl = browOutDownCtrl.control
        self.browOutDownCtrlGrp = browOutDownCtrl.parentControl[0]

        self.eyelidPinchOutCtrl = eyelidPinchOutCtrl.control
        self.eyelidPinchOutCtrlGrp = eyelidPinchOutCtrl.parentControl[0]

        self.earCtrl = earCtrl.control
        self.earCtrlGrp = earCtrl.parentControl[0]

    # ==================================================================================================================
    #                                           EYEBROW CONTROLLER SETUP
    # ==================================================================================================================
        mc.parent(self.eyebrowInCtrlGrp, self.eyebrowMidCtrlGrp, self.eyebrowOutCtrlGrp,
                  self.eyebrowCtrl)

    # GROUPING FOR OFFSET
        mc.select(cl=1)
        self.ctrlGrpEyebrowInCenter = mc.group(em=1, n='eyebrowInCtrlCenter' + side + '_grp')
        self.ctrlOffsetGrpEyebrowInCenter = mc.group(em=1, n='eyebrowInCtrlOffsetCenter' + side + '_grp')
        mc.parent(self.ctrlOffsetGrpEyebrowInCenter, self.ctrlGrpEyebrowInCenter)

        mc.select(cl=1)
        self.ctrlGrpEyebrowMidCenter = mc.group(em=1, n='eyebrowMidCtrlCenter' + side + '_grp')
        self.ctrlOffsetGrpEyebrowMidCenter = mc.group(em=1, n='eyebrowMidCtrlOffsetCenter' + side + '_grp')
        mc.parent(self.ctrlOffsetGrpEyebrowMidCenter, self.ctrlGrpEyebrowMidCenter)

        mc.select(cl=1)
        self.ctrlGrpEyebrowOutCenter = mc.group(em=1, n='eyebrowOutCtrlCenter' + side + '_grp')
        self.ctrlOffsetGrpEyebrowOutCenter = mc.group(em=1, n='eyebrowOutCtrlOffsetCenter' + side + '_grp')
        mc.parent(self.ctrlOffsetGrpEyebrowOutCenter, self.ctrlGrpEyebrowOutCenter)

    # CREATE GROUP CORESPONDENT THE JOINTS
        au.createParentTransform(listparent=['', 'Offset'], object=nostrilJnt, matchPos=nostrilJnt, prefix='nostril', suffix='_jnt', side=side)
        au.createParentTransform(listparent=[''], object=cheekUpJnt, matchPos=cheekUpJnt, prefix='cheekUp', suffix='_jnt', side=side)
        au.createParentTransform(listparent=[''], object=cheekUpOutJnt, matchPos=cheekUpOutJnt, prefix='cheekUpOut', suffix='_jnt', side=side)
        self.cheekDownJntGrp = au.createParentTransform(listparent=[''], object=cheekDownJnt, matchPos=cheekDownJnt, prefix='cheekDown', suffix='_jnt', side=side)
        eyebrowInGrp = au.createParentTransform(listparent=['', 'Offset'], object=eyebrowInJnt, matchPos=eyebrowInJnt, prefix='eyebrowIn', suffix='_jnt', side=side)
        eyebrowMidGrp = au.createParentTransform(listparent=['', 'Offset'], object=eyebrowMidJnt, matchPos=eyebrowMidJnt, prefix='eyebrowMid', suffix='_jnt', side=side)
        eyebrowOutGrp = au.createParentTransform(listparent=['', 'Offset'], object=eyebrowOutJnt, matchPos=eyebrowOutJnt, prefix='eyebrowOut', suffix='_jnt', side=side)

        au.createParentTransform(listparent=[''], object=browInUpJnt, matchPos=browInUpJnt, prefix='browInUp', suffix='_jnt', side=side)
        au.createParentTransform(listparent=[''], object=browMidUpJnt, matchPos=browMidUpJnt, prefix='browMidUp', suffix='_jnt', side=side)
        au.createParentTransform(listparent=[''], object=browOutUpJnt, matchPos=browOutUpJnt, prefix='browOutUp', suffix='_jnt', side=side)
        au.createParentTransform(listparent=[''], object=eyelidPinchInJnt, matchPos=eyelidPinchInJnt, prefix='eyelidPinchIn', suffix='_jnt', side=side)

        au.createParentTransform(listparent=[''], object=browInDownJnt, matchPos=browInDownJnt, prefix='browInDown', suffix='_jnt', side=side)
        au.createParentTransform(listparent=[''], object=browMidDownJnt, matchPos=browMidDownJnt, prefix='browMidDown', suffix='_jnt', side=side)
        au.createParentTransform(listparent=[''], object=browOutDownJnt, matchPos=browOutDownJnt, prefix='browOutDown', suffix='_jnt', side=side)
        au.createParentTransform(listparent=[''], object=eyelidPinchOutJnt, matchPos=eyelidPinchOutJnt, prefix='eyelidPinchOut', suffix='_jnt', side=side)

    # EYBROW MAIN OFFSET GRP JOINT TRANSFORM
        eyebrowInMain = self.mainGroupBindConnection(name='eyebrowIn', side=side, objectParent=eyebrowInGrp[0])
        eyebrowMidMain = self.mainGroupBindConnection(name='eyebrowMid', side=side, objectParent=eyebrowMidGrp[0])
        eyebrowOutMain = self.mainGroupBindConnection(name='eyebrowOut', side=side, objectParent=eyebrowOutGrp[0])

    # SHIFTING PARENT JOINT TO MAIN OFFSET GRP EYEBROW
        mc.parent(eyebrowInGrp[1], eyebrowInMain)
        mc.parent(eyebrowMidGrp[1], eyebrowMidMain)
        mc.parent(eyebrowOutGrp[1], eyebrowOutMain)

    # CONTROLLER ACCORDING THE FOLLICLE
        object = [self.nostrilCtrlGrp, self.cheekDownCtrlGrp, self.cheekUpCtrlGrp,
                  self.eyebrowInCtrlGrp, self.eyebrowMidCtrlGrp,
                  self.eyebrowOutCtrlGrp, self.browInUpCtrlGrp, self.browMidUpCtrlGrp, self.browOutUpCtrlGrp,
                  self.browInDownCtrlGrp, self.browMidDownCtrlGrp, self.browOutDownCtrlGrp,
                  self.eyelidPinchInCtrlGrp, self.eyelidPinchOutCtrlGrp, self.cheekUpOutCtrlGrp]

        self.follicleTransformAll=[]
        for i in object:
            follicleTransform = au.createFollicleSel(objSel=i, objMesh=objectFolMesh, connectFol=['transConn', 'rotateConn'])[0]
            mc.parent(i, follicleTransform)
            self.follicleTransformAll.append(follicleTransform)

    # SCALE CONSTRAINT
        mc.scaleConstraint(headCtrl,  self.follicleTransformAll[0])
        mc.scaleConstraint(headLowCtrl, self.follicleTransformAll[1])
        for b in self.follicleTransformAll[2:]:
            mc.scaleConstraint(headUpCtrl, b)


    # FLIPPING THE CONTROLLER
        if pos <0:
            mc.setAttr(self.nostrilCtrlGrp+ '.scaleX', -1)
            mc.setAttr(self.cheekUpCtrlGrp + '.scaleX', -1)
            mc.setAttr(self.cheekUpOutCtrlGrp + '.scaleX', -1)
            mc.setAttr(self.cheekDownCtrlGrp + '.scaleX', -1)
            mc.setAttr(self.eyebrowInCtrlGrp + '.scaleX', -1)
            mc.setAttr(self.eyebrowMidCtrlGrp + '.scaleX', -1)
            mc.setAttr(self.eyebrowOutCtrlGrp + '.scaleX', -1)

            mc.setAttr(self.browInUpCtrlGrp + '.scaleX', -1)
            mc.setAttr(self.browMidUpCtrlGrp + '.scaleX', -1)
            mc.setAttr(self.browOutUpCtrlGrp + '.scaleX', -1)
            mc.setAttr(self.eyelidPinchInCtrlGrp + '.scaleX', -1)

            mc.setAttr(self.browInDownCtrlGrp + '.scaleX', -1)
            mc.setAttr(self.browMidDownCtrlGrp + '.scaleX', -1)
            mc.setAttr(self.browOutDownCtrlGrp + '.scaleX', -1)
            mc.setAttr(self.eyelidPinchOutCtrlGrp + '.scaleX', -1)

            mc.setAttr(self.browInDownCtrlGrp + '.scaleY', -1)
            mc.setAttr(self.browMidDownCtrlGrp + '.scaleY', -1)
            mc.setAttr(self.browOutDownCtrlGrp + '.scaleY', -1)
            mc.setAttr(self.eyelidPinchOutCtrlGrp + '.scaleY', -1)

            mc.setAttr(self.ctrlGrpEyebrowInCenter+ '.scaleX', -1)
            mc.setAttr(self.ctrlGrpEyebrowMidCenter+ '.scaleX', -1)
            mc.setAttr(self.ctrlGrpEyebrowOutCenter+ '.scaleX', -1)
            mc.setAttr(self.earCtrlGrp+ '.scaleX', -1)
            mc.setAttr(self.eyebrowCtrlGrp+ '.scaleX', -1)

            self.reverseNode(self.nostrilCtrl, nostrilJnt, sideRGT, sideLFT, side)
            self.reverseNode(self.cheekUpCtrl, cheekUpJnt, sideRGT, sideLFT, side)
            self.reverseNode(self.cheekUpOutCtrl, cheekUpOutJnt, sideRGT, sideLFT, side)
            self.reverseNode(self.cheekDownCtrl, cheekDownJnt, sideRGT, sideLFT, side)
            self.reverseNode(self.eyebrowInCtrl, eyebrowInJnt, sideRGT, sideLFT, side)
            self.reverseNode(self.eyebrowMidCtrl, eyebrowMidJnt, sideRGT, sideLFT, side)
            self.reverseNode(self.eyebrowOutCtrl, eyebrowOutJnt, sideRGT, sideLFT, side)

            self.reverseNode(self.browInUpCtrl, browInUpJnt, sideRGT, sideLFT, side)
            self.reverseNode(self.browMidUpCtrl, browMidUpJnt, sideRGT, sideLFT, side)
            self.reverseNode(self.browOutUpCtrl, browOutUpJnt, sideRGT, sideLFT, side)
            self.reverseNode(self.eyelidPinchInCtrl, eyelidPinchInJnt, sideRGT, sideLFT, side)

            self.reverseNode(self.browInDownCtrl, browInDownJnt, sideRGT, sideLFT, side, inputTrans2Y=-1, inputRot2X=-1, inputRot2Z=1)
            self.reverseNode(self.browMidDownCtrl, browMidDownJnt, sideRGT, sideLFT, side, inputTrans2Y=-1, inputRot2X=-1, inputRot2Z=1)
            self.reverseNode(self.browOutDownCtrl, browOutDownJnt, sideRGT, sideLFT, side, inputTrans2Y=-1, inputRot2X=-1, inputRot2Z=1)
            self.reverseNode(self.eyelidPinchOutCtrl, eyelidPinchOutJnt, sideRGT, sideLFT, side, inputTrans2X=1, inputRot2Y=1, inputRot2Z=1)

            self.reverseNode(self.eyebrowCtrl, eyebrowInMain, sideRGT, sideLFT, side)
            self.reverseNode(self.eyebrowCtrl, eyebrowMidMain, sideRGT, sideLFT, side)
            self.reverseNode(self.eyebrowCtrl, eyebrowOutMain, sideRGT, sideLFT, side)

            au.connectAttrScale(self.nostrilCtrl, nostrilJnt)
            au.connectAttrScale(self.cheekUpCtrl, cheekUpJnt)
            au.connectAttrScale(self.cheekUpOutCtrl, cheekUpOutJnt)
            au.connectAttrScale(self.cheekDownCtrl, cheekDownJnt)
            au.connectAttrScale(self.eyebrowInCtrl, eyebrowInJnt)
            au.connectAttrScale(self.eyebrowMidCtrl, eyebrowMidJnt)
            au.connectAttrScale(self.eyebrowOutCtrl, eyebrowOutJnt)

            au.connectAttrScale(self.browInUpCtrl, browInUpJnt)
            au.connectAttrScale(self.browMidUpCtrl, browMidUpJnt)
            au.connectAttrScale(self.browOutUpCtrl, browOutUpJnt)
            au.connectAttrScale(self.eyelidPinchInCtrl, eyelidPinchInJnt)

            au.connectAttrScale(self.browInDownCtrl, browInDownJnt)
            au.connectAttrScale(self.browMidDownCtrl, browMidDownJnt)
            au.connectAttrScale(self.browOutDownCtrl, browOutDownJnt)
            au.connectAttrScale(self.eyelidPinchOutCtrl, eyelidPinchOutJnt)

            au.connectAttrScale(self.eyebrowCtrl, eyebrowInMain)
            au.connectAttrScale(self.eyebrowCtrl, eyebrowMidMain)
            au.connectAttrScale(self.eyebrowCtrl, eyebrowOutMain)

        else:
            au.connectAttrObject(self.nostrilCtrl, nostrilJnt)
            au.connectAttrObject(self.cheekUpCtrl, cheekUpJnt)
            au.connectAttrObject(self.cheekUpOutCtrl, cheekUpOutJnt)
            au.connectAttrObject(self.cheekDownCtrl, cheekDownJnt)
            au.connectAttrObject(self.eyebrowInCtrl, eyebrowInJnt)
            au.connectAttrObject(self.eyebrowMidCtrl, eyebrowMidJnt)
            au.connectAttrObject(self.eyebrowOutCtrl, eyebrowOutJnt)

            au.connectAttrObject(self.browInUpCtrl, browInUpJnt)
            au.connectAttrObject(self.browMidUpCtrl, browMidUpJnt)
            au.connectAttrObject(self.browOutUpCtrl, browOutUpJnt)
            au.connectAttrObject(self.eyelidPinchInCtrl, eyelidPinchInJnt)

            au.connectAttrObject(self.eyebrowCtrl, eyebrowInMain)
            au.connectAttrObject(self.eyebrowCtrl, eyebrowMidMain)
            au.connectAttrObject(self.eyebrowCtrl, eyebrowOutMain)

            mc.setAttr(self.browInDownCtrlGrp + '.scaleY', -1)
            mc.setAttr(self.browMidDownCtrlGrp + '.scaleY', -1)
            mc.setAttr(self.browOutDownCtrlGrp + '.scaleY', -1)
            mc.setAttr(self.eyelidPinchOutCtrlGrp + '.scaleX', -1)

            self.reverseNode(self.browInDownCtrl, browInDownJnt, sideRGT, sideLFT, side, inputTrans2X=1, inputTrans2Y=-1, inputRot2X=-1, inputRot2Y=1)
            self.reverseNode(self.browMidDownCtrl, browMidDownJnt, sideRGT, sideLFT, side, inputTrans2X=1, inputTrans2Y=-1,inputRot2X=-1,  inputRot2Y=1)
            self.reverseNode(self.browOutDownCtrl, browOutDownJnt, sideRGT, sideLFT, side, inputTrans2X=1, inputTrans2Y=-1, inputRot2X=-1, inputRot2Y=1)
            self.reverseNode(self.eyelidPinchOutCtrl, eyelidPinchOutJnt, sideRGT, sideLFT, side)

    # CONSTRAINT EARS
        mc.parentConstraint(self.earCtrl, earJnt, mo=1)
        mc.scaleConstraint(self.earCtrl, earJnt, mo=1)

    # EYEBROW EXCEPTION PARENTING CTRL
        mc.delete(mc.pointConstraint(self.eyebrowCtrl, self.ctrlGrpEyebrowInCenter))
        mc.delete(mc.pointConstraint(self.eyebrowCtrl, self.ctrlGrpEyebrowMidCenter))
        mc.delete(mc.pointConstraint(self.eyebrowCtrl, self.ctrlGrpEyebrowOutCenter))

        # grouping to follicle
        mc.parent(self.ctrlGrpEyebrowInCenter,  self.follicleTransformAll[3])
        mc.parent(self.ctrlGrpEyebrowMidCenter,  self.follicleTransformAll[4])
        mc.parent(self.ctrlGrpEyebrowOutCenter,  self.follicleTransformAll[5])

        # regrouping to offset grp
        mc.parent(self.eyebrowInCtrlGrp, self.ctrlOffsetGrpEyebrowInCenter)
        mc.parent(self.eyebrowMidCtrlGrp, self.ctrlOffsetGrpEyebrowMidCenter)
        mc.parent(self.eyebrowOutCtrlGrp, self.ctrlOffsetGrpEyebrowOutCenter)

        # connect attr
        au.connectAttrObject(self.eyebrowCtrl, self.ctrlOffsetGrpEyebrowInCenter)
        au.connectAttrObject(self.eyebrowCtrl, self.ctrlOffsetGrpEyebrowMidCenter)
        au.connectAttrObject(self.eyebrowCtrl, self.ctrlOffsetGrpEyebrowOutCenter)

    def reverseNode(self, object, targetJnt, sideRGT, sideLFT, side, inputTrans2X=-1, inputTrans2Y=1, inputTrans2Z=1,
                    inputRot2X=1, inputRot2Y=-1, inputRot2Z=-1):
        if sideRGT in targetJnt:
            newName = targetJnt.replace(sideRGT, '')
        elif sideLFT in targetJnt:
            newName = targetJnt.replace(sideLFT, '')
        else:
            newName = targetJnt

        transMdn = mc.createNode('multiplyDivide', n=au.prefixName(newName)+'Trans'+ side+ '_mdn')
        mc.connectAttr(object+'.translate', transMdn+'.input1')
        mc.setAttr(transMdn+'.input2X', inputTrans2X)
        mc.setAttr(transMdn+'.input2Y', inputTrans2Y)
        mc.setAttr(transMdn+'.input2Z', inputTrans2Z)

        mc.connectAttr(transMdn+'.output', targetJnt +'.translate')

        rotMdn = mc.createNode('multiplyDivide', n=au.prefixName(newName)+'Rot' + side+'_mdn')
        mc.connectAttr(object+'.rotate', rotMdn+'.input1')
        mc.setAttr(rotMdn + '.input2X', inputRot2X)
        mc.setAttr(rotMdn+'.input2Y', inputRot2Y)
        mc.setAttr(rotMdn+'.input2Z', inputRot2Z)
        mc.connectAttr(rotMdn+'.output', targetJnt+'.rotate')

    def mainGroupBindConnection(self, name, side, objectParent):
        # EYBROW MAIN OFFSET GRP JOINT TRANSFORM
        eyebrowMainBindGrp = mc.group(em=1, n=name+'Main' + side + '_grp')
        eyebrowMainBindOffset = mc.group(em=1, n=name+'MainOffset' + side + '_grp', p=eyebrowMainBindGrp)
        mc.delete(mc.parentConstraint(self.eyebrowCtrl, eyebrowMainBindGrp))

        mc.parent(eyebrowMainBindGrp, objectParent)

        return eyebrowMainBindOffset