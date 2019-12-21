from __builtin__ import reload

import maya.cmds as mc
import re
import ADUtils as au

reload(au)

class BuildTwoSide:
    def __init__(self, bsnName, eyebrowCtrlOut, eyebrowCtrlMid,
                 eyebrowCtrlIn, eyebrowCtrlInner, eyebrowCtrlSqueeze,
                 eyebrowCtrlTwist, eyebrowCtrlCurl, noseCtrl, cheekCtrl, side):

        # TWO SLIDE
        self.twoValueSlider(bsnName=bsnName, controller=eyebrowCtrlOut, side=side, slideAtribute='translateY',
                            subPrefixOne='Up', valuePosOne=2, subPrefixTwo='Down', valuePosTwo=-2, connect=True)
        self.twoValueSlider(bsnName=bsnName, controller=eyebrowCtrlMid, side=side, slideAtribute='translateY',
                            subPrefixOne='Up', valuePosOne=2, subPrefixTwo='Down', valuePosTwo=-2, connect=True)
        self.twoValueSlider(bsnName=bsnName, controller=eyebrowCtrlIn, side=side, slideAtribute='translateY',
                            subPrefixOne='Up', valuePosOne=2, subPrefixTwo='Down', valuePosTwo=-2, connect=True)
        self.twoValueSlider(bsnName=bsnName, controller=eyebrowCtrlTwist, side=side, slideAtribute='translateY',
                            subPrefixOne='In', valuePosOne=-2, subPrefixTwo='Out', valuePosTwo=2, connect=True)
        self.twoValueSlider(bsnName=bsnName, controller=noseCtrl, side=side, slideAtribute='translateX',
                            subPrefixOne='In', valuePosOne=-1, subPrefixTwo='Out', valuePosTwo=1, connect=True)

        cheekInOut = self.twoValueSlider(bsnName=bsnName, controller=cheekCtrl, side=side, slideAtribute='translateX',
                            subPrefixOne='In', valuePosOne=-2, subPrefixTwo='Out', valuePosTwo=2, connect=True)

        cheekInOutUp = self.twoValueSlider(bsnName=bsnName, controller=cheekCtrl, side=side, slideAtribute='translateY',
                                 subPrefixOne='InUp', valuePosOne=2, subPrefixTwo='OutUp', valuePosTwo=2, connect=False)

        self.combinedValueSlider(bsnName=bsnName, controller=cheekCtrl, side=side, subPrefixOne='InUp', clampDriverUpOne=cheekInOut[0],
                                 clampDriverUpTwo=cheekInOutUp[0], clampDriverDownOne=cheekInOut[1], clampDriverDownTwo=cheekInOutUp[1])


        # ONE SLIDE
        self.oneValueSlider(bsnName=bsnName, controller=eyebrowCtrlInner, side=side, slideAtribute='translateX',
                            subPrefix='', valueNode= -2)
        self.oneValueSlider(bsnName=bsnName, controller=eyebrowCtrlSqueeze, side=side, slideAtribute='translateY',
                            subPrefix='', valueNode=-2)
        self.oneValueSlider(bsnName=bsnName, controller=eyebrowCtrlCurl, side=side, slideAtribute='translateY',
                            subPrefix='', valueNode=4)

        self.oneValueSlider(bsnName=bsnName, controller=noseCtrl, side=side, slideAtribute='translateY',
                            subPrefix='Up', valueNode= 1)


    def combinedValueSlider(self, bsnName, controller, side, subPrefixOne, clampDriverUpOne, clampDriverUpTwo, clampDriverDownOne,
                            clampDriverDownTwo):
        # UP
        ctrlNew = self.replacePosLFTRGT(controller, 'BshRGT', 'BshLFT')
        # multDoubleLinearUp = mc.createNode('multDoubleLinear', n=au.prefixName(ctrlNew) + subPrefixOne + 'Bsh' + side + '_mdl')
        # mc.setAttr(multDoubleLinearUp + '.input2', 1.0/valuePosOne)
        # mc.connectAttr(controller + '.%s' % slideAtribute, multDoubleLinearUp + '.input1')
        #
        # clampUp = mc.createNode('clamp', n=au.prefixName(ctrlNew)+ subPrefixOne + 'Bsh'  + side + '_clm')
        # mc.setAttr(clampUp + '.maxR', 1)
        # mc.connectAttr(multDoubleLinearUp + '.output', clampUp + '.inputR')
        #
        # # DOWN
        # multDoubleLinearDown = mc.createNode('multDoubleLinear', n=au.prefixName(ctrlNew) + subPrefixTwo + 'Bsh'+side + '_mdl')
        # mc.setAttr(multDoubleLinearDown + '.input2', 1.0/valuePosTwo)
        # mc.connectAttr(controller + '.%s' % slideAtribute, multDoubleLinearDown + '.input1')
        #
        # clampDown = mc.createNode('clamp', n=au.prefixName(ctrlNew) + subPrefixTwo + 'Bsh' + side + '_clm')
        # mc.setAttr(clampDown + '.maxR', 1)
        # mc.connectAttr(multDoubleLinearDown + '.output', clampDown + '.inputR')

        # DRIVER VALUE
        multDoubleLinearCombinedUp = mc.createNode('multDoubleLinear', n=au.prefixName(ctrlNew) + subPrefixOne + 'BshCombined' + side + '_mdl')
        mc.connectAttr(clampDriverUpOne + '.outputR', multDoubleLinearCombinedUp + '.input1')
        mc.connectAttr(clampDriverUpTwo + '.outputR', multDoubleLinearCombinedUp + '.input2')

        multDoubleLinearCombinedDown = mc.createNode('multDoubleLinear', n=au.prefixName(ctrlNew) + subPrefixOne + 'BshCombined' + side + '_mdl')
        mc.connectAttr(clampDriverDownOne + '.outputR', multDoubleLinearCombinedDown + '.input1')
        mc.connectAttr(clampDriverDownTwo + '.outputR', multDoubleLinearCombinedDown + '.input2')

        # CONNECT TO BSH
        listWeight = mc.listAttr(bsnName+'.w', m=True)
        # UP
        self.connectNodeToBsh(listWeight, multDoubleLinearCombinedUp, 'output', bsnName=bsnName, sideRGT='BshCombinedRGT', sideLFT='BshCombinedLFT', side=side)
        self.connectNodeToBsh(listWeight, multDoubleLinearCombinedDown, 'output', bsnName=bsnName, sideRGT='BshCombinedRGT', sideLFT='BshCombinedLFT', side=side)

    def twoValueSlider(self, bsnName, controller, side, slideAtribute, subPrefixOne, valuePosOne, subPrefixTwo, valuePosTwo, connect=True):
        # UP
        ctrlNew = self.replacePosLFTRGT(controller, 'BshRGT', 'BshLFT')
        multDoubleLinearUp = mc.createNode('multDoubleLinear', n=au.prefixName(ctrlNew) + subPrefixOne + 'Bsh' + side + '_mdl')
        mc.setAttr(multDoubleLinearUp + '.input2', 1.0/valuePosOne)
        mc.connectAttr(controller + '.%s' % slideAtribute, multDoubleLinearUp + '.input1')

        clampUp = mc.createNode('clamp', n=au.prefixName(ctrlNew)+ subPrefixOne + 'Bsh'  + side + '_clm')
        mc.setAttr(clampUp + '.maxR', 1)
        mc.connectAttr(multDoubleLinearUp + '.output', clampUp + '.inputR')

        # DOWN
        multDoubleLinearDown = mc.createNode('multDoubleLinear', n=au.prefixName(ctrlNew) + subPrefixTwo + 'Bsh'+side + '_mdl')
        mc.setAttr(multDoubleLinearDown + '.input2', 1.0/valuePosTwo)
        mc.connectAttr(controller + '.%s' % slideAtribute, multDoubleLinearDown + '.input1')

        clampDown = mc.createNode('clamp', n=au.prefixName(ctrlNew) + subPrefixTwo + 'Bsh' + side + '_clm')
        mc.setAttr(clampDown + '.maxR', 1)
        mc.connectAttr(multDoubleLinearDown + '.output', clampDown + '.inputR')

        # CONNECT TO BSH
        if connect:
            listWeight = mc.listAttr(bsnName+'.w', m=True)
            self.connectNodeToBsh(listWeight, clampUp, 'outputR', bsnName=bsnName, sideRGT='BshRGT', sideLFT='BshLFT', side=side)
            self.connectNodeToBsh(listWeight, clampDown, 'outputR', bsnName=bsnName, sideRGT='BshRGT', sideLFT='BshLFT', side=side)
        else:
            return clampUp, clampDown

    def oneValueSlider(self, bsnName, controller, side, slideAtribute, subPrefix, valueNode):
        ctrlNew = self.replacePosLFTRGT(controller, 'BshRGT', 'BshLFT')
        multDoubleLinearUp = mc.createNode('multDoubleLinear', n=au.prefixName(ctrlNew) + subPrefix + 'Bsh' + side + '_mdl')
        mc.setAttr(multDoubleLinearUp + '.input2', 1.0/valueNode)
        mc.connectAttr(controller + '.%s' % slideAtribute, multDoubleLinearUp + '.input1')

        # CONNECT TO BSH
        listWeight = mc.listAttr(bsnName+'.w', m=True)

        # UP
        self.connectNodeToBsh(listWeight, multDoubleLinearUp, 'output', bsnName=bsnName, sideRGT='BshRGT', sideLFT='BshLFT', side=side)

    def replacePosLFTRGT(self, nameObj, sideRGT, sideLFT):
        if sideRGT in nameObj:
            crvNewName = nameObj.replace(sideRGT, '')
        elif sideLFT in nameObj:
            crvNewName = nameObj.replace(sideLFT, '')
        else:
            crvNewName = nameObj

        return crvNewName

    def connectNodeToBsh(self, listWeight, connectorNode, atttNode, bsnName, sideRGT, sideLFT, side):
        list = []
        for i in listWeight:
            listI = i[:-7]
            list.append(listI)

        baseName = self.replacePosLFTRGT(connectorNode, sideRGT, sideLFT)
        if re.compile('|'.join(list), re.IGNORECASE).search(connectorNode):  # re.IGNORECASE is used to ignore case
            mc.connectAttr(connectorNode+'.%s' % atttNode, bsnName+'.%s%s%s' % (au.prefixName(baseName), side, '_ply'))
        else:
            print (mc.error ('There is no weight on blendshape'))

class BuildOneSide:
    def __init__(self, bsnName, mouthCtrl):

        self.twoValueSlider(bsnName=bsnName, controller=mouthCtrl, slideAtribute='translateY',
                            subPrefixOne='Up', valuePosOne=2, subPrefixTwo='Down', valuePosTwo=-2)
        self.twoValueSlider(bsnName=bsnName, controller=mouthCtrl, slideAtribute='translateX',
                            subPrefixOne='LFT', valuePosOne=2, subPrefixTwo='RGT', valuePosTwo=-2)

    def twoValueSlider(self, bsnName, controller, slideAtribute, subPrefixOne, valuePosOne, subPrefixTwo,
                       valuePosTwo):
        # UP
        # ctrlNew = self.replacePosLFTRGT(controller, 'Bsh', 'Bsh')
        multDoubleLinearUp = mc.createNode('multDoubleLinear',
                                           n=au.prefixName(controller) + subPrefixOne  + '_mdl')
        mc.setAttr(multDoubleLinearUp + '.input2', 1.0 / valuePosOne)
        mc.connectAttr(controller + '.%s' % slideAtribute, multDoubleLinearUp + '.input1')

        clampUp = mc.createNode('clamp', n=au.prefixName(controller) + subPrefixOne  + '_clm')
        mc.setAttr(clampUp + '.maxR', 1)
        mc.connectAttr(multDoubleLinearUp + '.output', clampUp + '.inputR')

        # DOWN
        multDoubleLinearDown = mc.createNode('multDoubleLinear',
                                             n=au.prefixName(controller) + subPrefixTwo + '_mdl')
        mc.setAttr(multDoubleLinearDown + '.input2', 1.0 / valuePosTwo)
        mc.connectAttr(controller + '.%s' % slideAtribute, multDoubleLinearDown + '.input1')

        clampDown = mc.createNode('clamp', n=au.prefixName(controller) + subPrefixTwo + '_clm')
        mc.setAttr(clampDown + '.maxR', 1)
        mc.connectAttr(multDoubleLinearDown + '.output', clampDown + '.inputR')

        # CONNECT TO BSH
        listWeight = mc.listAttr(bsnName + '.w', m=True)
        # UP
        self.connectNodeToBsh(listWeight, clampUp, 'outputR', bsnName)
        self.connectNodeToBsh(listWeight, clampDown, 'outputR', bsnName)

        return clampUp, clampDown

    def oneValueSlider(self, bsnName, controller, slideAtribute, subPrefix, valueNode):
        # ctrlNew = self.replacePosLFTRGT(controller, 'Bsh', 'Bsh')
        multDoubleLinearUp = mc.createNode('multDoubleLinear',
                                           n=au.prefixName(controller) + subPrefix + '_mdl')
        mc.setAttr(multDoubleLinearUp + '.input2', 1.0 / valueNode)
        mc.connectAttr(controller + '.%s' % slideAtribute, multDoubleLinearUp + '.input1')

        # CONNECT TO BSH
        listWeight = mc.listAttr(bsnName + '.w', m=True)

        # UP
        self.connectNodeToBsh(listWeight, multDoubleLinearUp, 'output', bsnName)

    def replacePosLFTRGT(self, nameObj, sideRGT, sideLFT):
        if sideRGT in nameObj:
            crvNewName = nameObj.replace(sideRGT, '')
        elif sideLFT in nameObj:
            crvNewName = nameObj.replace(sideLFT, '')
        else:
            crvNewName = nameObj

        return crvNewName

    def connectNodeToBsh(self, listWeight, connectorNode, atttNode, bsnName):
        list = []
        for i in listWeight:
            listI = i[:-7]
            list.append(listI)

        baseName = self.replacePosLFTRGT(connectorNode, 'Bsh', 'Bsh')
        if re.compile('|'.join(list), re.IGNORECASE).search(
                connectorNode):  # re.IGNORECASE is used to ignore case
            mc.connectAttr(connectorNode + '.%s' % atttNode,
                           bsnName + '.%s%s' % (au.prefixName(baseName), '_ply'))
        else:
            print(mc.error('There is no weight on blendshape'))