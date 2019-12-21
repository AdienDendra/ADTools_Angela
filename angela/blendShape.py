from __builtin__ import reload

import maya.cmds as mc
import re
import ADUtils as au

reload(au)

class BuildTwoSide:
    def __init__(self, bsnName, eyebrowCtrlOut, eyebrowCtrlMid,
                 eyebrowCtrlIn, eyebrowCtrlInner, eyebrowCtrlSqueeze,
                 eyebrowCtrlTwist, eyebrowCtrlCurl, noseCtrl, cheekCtrl, upperLipRollCtrl, lowerLipRollCtrl,
                 upperLipCtrl, lowerLipCtrl,
                 side):

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

        self.combinedValueSlider(bsnName=bsnName, controller=cheekCtrl, side=side, subPrefixOne='InUp', subPrefixTwo='OutUp',
                                 clampDriverInOne=cheekInOut[0], clampDriverInTwo=cheekInOutUp[0],
                                 clampDriverOutOne=cheekInOut[1], clampDriverOutTwo=cheekInOutUp[1])

        self.twoValueSlider(bsnName=bsnName, controller=upperLipRollCtrl, side=side, slideAtribute='translateY',
                            subPrefixOne='Up', valuePosOne=1, subPrefixTwo='Down', valuePosTwo=-1, connect=True)

        self.twoValueSlider(bsnName=bsnName, controller=lowerLipRollCtrl, side=side, slideAtribute='translateY',
                            subPrefixOne='Up', valuePosOne=-1, subPrefixTwo='Down', valuePosTwo=1, connect=True)

        self.twoValueSlider(bsnName=bsnName, controller=upperLipCtrl, side=side, slideAtribute='translateY',
                            subPrefixOne='Up', valuePosOne=1, subPrefixTwo='Down', valuePosTwo=-1, connect=True)

        self.twoValueSlider(bsnName=bsnName, controller=lowerLipCtrl, side=side, slideAtribute='translateY',
                            subPrefixOne='Up', valuePosOne=1, subPrefixTwo='Down', valuePosTwo=-1, connect=True)

        # ONE SLIDE
        self.oneValueSlider(bsnName=bsnName, controller=eyebrowCtrlInner, side=side, slideAtribute='translateX',
                            subPrefix='', valueNode= -2)
        self.oneValueSlider(bsnName=bsnName, controller=eyebrowCtrlSqueeze, side=side, slideAtribute='translateY',
                            subPrefix='', valueNode=-2)
        self.oneValueSlider(bsnName=bsnName, controller=eyebrowCtrlCurl, side=side, slideAtribute='translateY',
                            subPrefix='', valueNode=4)

        self.oneValueSlider(bsnName=bsnName, controller=noseCtrl, side=side, slideAtribute='translateY',
                            subPrefix='Up', valueNode= 1)


    def combinedValueSlider(self, bsnName, controller, side, subPrefixOne, subPrefixTwo, clampDriverInOne,
                            clampDriverInTwo, clampDriverOutOne, clampDriverOutTwo):

        ctrlNew = self.replacePosLFTRGT(controller, 'BshRGT', 'BshLFT')
        # DRIVER VALUE
        multDoubleLinearCombinedOne = mc.createNode('multDoubleLinear', n=au.prefixName(ctrlNew) + subPrefixOne + 'BshCombined' + side + '_mdl')
        mc.connectAttr(clampDriverInOne + '.outputR', multDoubleLinearCombinedOne + '.input1')
        mc.connectAttr(clampDriverInTwo + '.outputR', multDoubleLinearCombinedOne + '.input2')

        multDoubleLinearCombinedTwo = mc.createNode('multDoubleLinear', n=au.prefixName(ctrlNew) + subPrefixTwo + 'BshCombined' + side + '_mdl')
        mc.connectAttr(clampDriverOutOne + '.outputR', multDoubleLinearCombinedTwo + '.input1')
        mc.connectAttr(clampDriverOutTwo + '.outputR', multDoubleLinearCombinedTwo + '.input2')

        # CONNECT TO BSH
        listWeight = mc.listAttr(bsnName+'.w', m=True)
        self.connectNodeToBsh(listWeight, multDoubleLinearCombinedOne, 'output', bsnName=bsnName, sideRGT='BshCombinedRGT', sideLFT='BshCombinedLFT', side=side)
        self.connectNodeToBsh(listWeight, multDoubleLinearCombinedTwo, 'output', bsnName=bsnName, sideRGT='BshCombinedRGT', sideLFT='BshCombinedLFT', side=side)

    def twoValueSlider(self, bsnName, controller, side, slideAtribute, subPrefixOne, valuePosOne, subPrefixTwo, valuePosTwo,
                       sideRGT='BshRGT', sideLFT='BshLFT', connect=True):
        # UP
        ctrlNew = self.replacePosLFTRGT(controller, sideRGT, sideLFT)
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
        print (clampDown)

        # CONNECT TO BSH
        if connect:
            listWeight = mc.listAttr(bsnName+'.w', m=True)
            self.connectNodeToBsh(listWeight, clampUp, 'outputR', bsnName=bsnName, sideRGT=sideRGT, sideLFT=sideLFT, side=side)
            self.connectNodeToBsh(listWeight, clampDown, 'outputR', bsnName=bsnName, sideRGT=sideRGT, sideLFT=sideLFT, side=side)
        # else:
        return clampUp, clampDown

    def oneValueSlider(self, bsnName, controller, side, slideAtribute, subPrefix, valueNode, sideRGT='BshRGT', sideLFT='BshLFT'):
        ctrlNew = self.replacePosLFTRGT(controller, sideRGT, sideLFT)
        multDoubleLinearUp = mc.createNode('multDoubleLinear', n=au.prefixName(ctrlNew) + subPrefix + 'Bsh' + side + '_mdl')
        mc.setAttr(multDoubleLinearUp + '.input2', 1.0/valueNode)
        mc.connectAttr(controller + '.%s' % slideAtribute, multDoubleLinearUp + '.input1')

        # CONNECT TO BSH
        listWeight = mc.listAttr(bsnName+'.w', m=True)

        # UP
        self.connectNodeToBsh(listWeight, multDoubleLinearUp, 'output', bsnName=bsnName, sideRGT=sideRGT, sideLFT=sideLFT, side=side)

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
    def __init__(self, bsnName, mouthCtrl, upperLipRollCtrl, lowerLipRollCtrl, upperLipCtrl, lowerLipCtrl):

        self.twoValueSlider(bsnName=bsnName, controller=mouthCtrl, slideAtribute='translateY',
                            subPrefixOne='Up', valuePosOne=2, subPrefixTwo='Down', valuePosTwo=-2)
        self.twoValueSlider(bsnName=bsnName, controller=mouthCtrl, slideAtribute='translateX',
                            subPrefixOne='LFT', valuePosOne=2, subPrefixTwo='RGT', valuePosTwo=-2)

        self.twoValueSlider(bsnName=bsnName, controller=upperLipRollCtrl, slideAtribute='translateY',
                            subPrefixOne='Up', valuePosOne=1, subPrefixTwo='Down', valuePosTwo=-1, addPrefix='MID',
                            sideRGT='BshMID', sideLFT='BshMID')

        self.twoValueSlider(bsnName=bsnName, controller=lowerLipRollCtrl, slideAtribute='translateY',
                            subPrefixOne='Up', valuePosOne=-1, subPrefixTwo='Down', valuePosTwo=1, addPrefix='MID',
                            sideRGT='BshMID', sideLFT='BshMID')

        self.twoValueSlider(bsnName=bsnName, controller=upperLipCtrl, slideAtribute='translateY',
                            subPrefixOne='Up', valuePosOne=1, subPrefixTwo='Down', valuePosTwo=-1, addPrefix='MID',
                            sideRGT='BshMID', sideLFT='BshMID')

        self.twoValueSlider(bsnName=bsnName, controller=lowerLipCtrl, slideAtribute='translateY',
                            subPrefixOne='Up', valuePosOne=1, subPrefixTwo='Down', valuePosTwo=-1, addPrefix='MID',
                            sideRGT='BshMID', sideLFT='BshMID')

    def twoValueSlider(self, bsnName, controller, slideAtribute, subPrefixOne, valuePosOne, subPrefixTwo,
                       valuePosTwo, addPrefix='', sideRGT='Bsh', sideLFT='Bsh'):
        # UP
        ctrlNew = self.replacePosLFTRGT(controller, sideRGT, sideLFT)
        multDoubleLinearUp = mc.createNode('multDoubleLinear',
                                           n=au.prefixName(ctrlNew) + subPrefixOne  + '_mdl')
        mc.setAttr(multDoubleLinearUp + '.input2', 1.0 / valuePosOne)
        mc.connectAttr(controller + '.%s' % slideAtribute, multDoubleLinearUp + '.input1')

        clampUp = mc.createNode('clamp', n=au.prefixName(ctrlNew) + subPrefixOne  + '_clm')
        mc.setAttr(clampUp + '.maxR', 1)
        mc.connectAttr(multDoubleLinearUp + '.output', clampUp + '.inputR')

        # DOWN
        multDoubleLinearDown = mc.createNode('multDoubleLinear',
                                             n=au.prefixName(ctrlNew) + subPrefixTwo + '_mdl')
        mc.setAttr(multDoubleLinearDown + '.input2', 1.0 / valuePosTwo)
        mc.connectAttr(controller + '.%s' % slideAtribute, multDoubleLinearDown + '.input1')

        clampDown = mc.createNode('clamp', n=au.prefixName(ctrlNew) + subPrefixTwo + '_clm')
        mc.setAttr(clampDown + '.maxR', 1)
        mc.connectAttr(multDoubleLinearDown + '.output', clampDown + '.inputR')

        # CONNECT TO BSH
        listWeight = mc.listAttr(bsnName + '.w', m=True)
        # UP
        self.connectNodeToBsh(listWeight, clampUp, 'outputR', bsnName, addPrefix, sideRGT=sideRGT, sideLFT=sideLFT)
        self.connectNodeToBsh(listWeight, clampDown, 'outputR', bsnName, addPrefix, sideRGT=sideRGT, sideLFT=sideLFT)

        return clampUp, clampDown

    def oneValueSlider(self, bsnName, controller, slideAtribute, subPrefix, valueNode, addPrefix, sideRGT='Bsh', sideLFT='Bsh'):
        ctrlNew = self.replacePosLFTRGT(controller, sideRGT, sideLFT)
        multDoubleLinearUp = mc.createNode('multDoubleLinear',
                                           n=au.prefixName(ctrlNew) + subPrefix + '_mdl')
        mc.setAttr(multDoubleLinearUp + '.input2', 1.0 / valueNode)
        mc.connectAttr(controller + '.%s' % slideAtribute, multDoubleLinearUp + '.input1')

        # CONNECT TO BSH
        listWeight = mc.listAttr(bsnName + '.w', m=True)

        # UP
        self.connectNodeToBsh(listWeight, multDoubleLinearUp, 'output', bsnName, addPrefix, sideRGT=sideRGT, sideLFT=sideLFT)

    def replacePosLFTRGT(self, nameObj, sideRGT, sideLFT):
        if sideRGT in nameObj:
            crvNewName = nameObj.replace(sideRGT, '')
        elif sideLFT in nameObj:
            crvNewName = nameObj.replace(sideLFT, '')
        else:
            crvNewName = nameObj

        return crvNewName

    def connectNodeToBsh(self, listWeight, connectorNode, atttNode, bsnName, addPrefix, sideRGT, sideLFT):
        list = []
        for i in listWeight:
            listI = i[:-7]
            list.append(listI)

        baseName = self.replacePosLFTRGT(connectorNode, sideRGT, sideLFT)
        if re.compile('|'.join(list), re.IGNORECASE).search(
                connectorNode):  # re.IGNORECASE is used to ignore case
            mc.connectAttr(connectorNode + '.%s' % atttNode,
                           bsnName + '.%s%s%s' % (au.prefixName(baseName), addPrefix, '_ply'))
        else:
            print(mc.error('There is no weight on blendshape'))

class BuildFree:
    def __init__(self, bsnName, rollCtrl, upperWeightBsnMID,
                 upperWeightBsnLFT, upperWeightBsnRGT,
                 lowerWeightBsnMID, lowerWeightBsnLFT,
                 lowerWeightBsnRGT):

        self.oneValueSlider(bsnName, controller=rollCtrl, slideAtribute='translateY',
                            valueNode=3, weightBsnName=upperWeightBsnMID)

        self.oneValueSlider(bsnName, controller=rollCtrl, slideAtribute='translateY',
                            valueNode=3, weightBsnName=upperWeightBsnLFT)

        self.oneValueSlider(bsnName, controller=rollCtrl, slideAtribute='translateY',
                            valueNode=3, weightBsnName=upperWeightBsnRGT)

        self.oneValueSlider(bsnName, controller=rollCtrl, slideAtribute='translateY',
                            valueNode=3, weightBsnName=lowerWeightBsnMID)

        self.oneValueSlider(bsnName, controller=rollCtrl, slideAtribute='translateY',
                            valueNode=3, weightBsnName=lowerWeightBsnLFT)

        self.oneValueSlider(bsnName, controller=rollCtrl, slideAtribute='translateY',
                            valueNode=3, weightBsnName=lowerWeightBsnRGT)

    def twoValueSlider(self, bsnName, controller, slideAtribute, subPrefixOne, valuePosOne, subPrefixTwo,
                       valuePosTwo, weightBsnName,
                     connect=True):
        # UP
        # ctrlNew = self.replacePosLFTRGT(weightBsnName, sideRGT=sideRGT, sideLFT=sideLFT)
        weightNames = au.prefixName(weightBsnName)
        weightName = weightNames.replace(subPrefixOne,'').replace(subPrefixTwo,'')

        multDoubleLinearUp = mc.createNode('multDoubleLinear',
                                           n=weightName[:-3]+ subPrefixOne+ weightName[-3:] +'_mdl')
        mc.setAttr(multDoubleLinearUp + '.input2', 1.0 / valuePosOne)
        mc.connectAttr(controller + '.%s' % slideAtribute, multDoubleLinearUp + '.input1')

        clampUp = mc.createNode('clamp', n=weightName[:-3]+ subPrefixOne+ weightName[-3:] +'_clm')
        mc.setAttr(clampUp + '.maxR', 1)
        mc.connectAttr(multDoubleLinearUp + '.output', clampUp + '.inputR')

        # DOWN
        multDoubleLinearDown = mc.createNode('multDoubleLinear',
                                             n=weightName[:-3]+ subPrefixTwo+ weightName[-3:] + '_mdl')
        mc.setAttr(multDoubleLinearDown + '.input2', 1.0 / valuePosTwo)
        mc.connectAttr(controller + '.%s' % slideAtribute, multDoubleLinearDown + '.input1')

        clampDown = mc.createNode('clamp', n=weightName[:-3]+ subPrefixTwo+ weightName[-3:] + '_clm')
        mc.setAttr(clampDown + '.maxR', 1)
        mc.connectAttr(multDoubleLinearDown + '.output', clampDown + '.inputR')
        print(clampDown)

        # CONNECT TO BSH
        if connect:
            listWeight = mc.listAttr(bsnName + '.w', m=True)
            self.connectNodeToBsh(listWeight, clampUp, 'outputR', bsnName=bsnName)
            self.connectNodeToBsh(listWeight, clampDown, 'outputR', bsnName=bsnName)
        return clampUp, clampDown

    def oneValueSlider(self, bsnName, controller, slideAtribute, valueNode, weightBsnName):
        # ctrlNew = self.replacePosLFTRGT(controller, sideRGT, sideLFT)
        weightName = au.prefixName(weightBsnName)
        multDoubleLinearUp = mc.createNode('multDoubleLinear',
                                           n=weightName[:-3]+ weightName[-3:] + '_mdl')
        mc.setAttr(multDoubleLinearUp + '.input2', 1.0 / valueNode)
        mc.connectAttr(controller + '.%s' % slideAtribute, multDoubleLinearUp + '.input1')

        # CONNECT TO BSH
        listWeight = mc.listAttr(bsnName + '.w', m=True)

        # UP
        self.connectNodeToBsh(listWeight, multDoubleLinearUp, 'output', bsnName=bsnName)

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

        # baseName = self.replacePosLFTRGT(connectorNode, sideRGT=sideRGT, sideLFT=sideLFT)
        if re.compile('|'.join(list), re.IGNORECASE).search(connectorNode):  # re.IGNORECASE is used to ignore case
            mc.connectAttr(connectorNode + '.%s' % atttNode,
                           bsnName + '.%s%s' % (au.prefixName(connectorNode) ,'_ply'))
        else:
            print(mc.error('There is no weight on blendshape'))