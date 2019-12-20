import maya.cmds as mc
import re
import ADUtils as au

reload(au)

class Blendshape:
    def __init__(self, bsnName, eyebrowCtrlOut,  eyebrowCtrlMid,
                 eyebrowCtrlIn, eyebrowCtrlInner, eyebrowCtrlSqueeze,
                 eyebrowCtrlTwist, eyebrowCtrlCurl, side):

        # EYEBROW LEFT AND RIGHT
        self.eyebrowTwoValue(bsnName, eyebrowCtrlOut, side, posOne='UpBsh', valuePosOne=0.5, poseTwo='DownBsh', valuePosTwo=-0.5)
        self.eyebrowTwoValue(bsnName, eyebrowCtrlMid, side, posOne='UpBsh', valuePosOne=0.5, poseTwo='DownBsh', valuePosTwo=-0.5)
        self.eyebrowTwoValue(bsnName, eyebrowCtrlIn, side, posOne='UpBsh', valuePosOne=0.5, poseTwo='DownBsh', valuePosTwo=-0.5)
        self.eyebrowTwoValue(bsnName, eyebrowCtrlTwist, side, posOne='InBsh', valuePosOne=-0.5, poseTwo='OutBsh', valuePosTwo=0.5)

        self.eyebrowOneValue(bsnName, eyebrowCtrlInner, side, 'translateX', -0.5)
        self.eyebrowOneValue(bsnName, eyebrowCtrlSqueeze, side, 'translateY', -0.5)
        self.eyebrowOneValue(bsnName, eyebrowCtrlCurl, side, 'translateY', 0.25)



    def eyebrowTwoValue(self, bsnName, eyebrowCtrl, side, posOne, valuePosOne, poseTwo, valuePosTwo):
        # UP
        eyebrowCtrlNew = self.replacePosLFTRGT(eyebrowCtrl, 'BshRGT', 'BshLFT')
        multDoubleLinearUp = mc.createNode('multDoubleLinear', n=au.prefixName(eyebrowCtrlNew) + posOne + side + '_mdl')
        mc.setAttr(multDoubleLinearUp + '.input2', valuePosOne)
        mc.connectAttr(eyebrowCtrl +'.translateY', multDoubleLinearUp + '.input1')

        clampUp = mc.createNode('clamp', n=au.prefixName(eyebrowCtrlNew) + posOne + side + '_clm')
        mc.setAttr(clampUp + '.maxR', 1)
        mc.connectAttr(multDoubleLinearUp + '.output', clampUp + '.inputR')

        # DOWN
        multDoubleLinearDown = mc.createNode('multDoubleLinear', n=au.prefixName(eyebrowCtrlNew) + poseTwo + side + '_mdl')
        mc.setAttr(multDoubleLinearDown + '.input2', valuePosTwo)
        mc.connectAttr(eyebrowCtrl +'.translateY', multDoubleLinearDown + '.input1')

        clampDown = mc.createNode('clamp', n=au.prefixName(eyebrowCtrlNew) + poseTwo + side + '_clm')
        mc.setAttr(clampDown + '.maxR', 1)
        mc.connectAttr(multDoubleLinearDown + '.output', clampDown + '.inputR')

        # CONNECT TO BSH
        listWeight = mc.listAttr(bsnName+'.w', m=True)
        # UP
        self.connectNodeToBsh(listWeight, clampUp, 'outputR', bsnName, side)
        self.connectNodeToBsh(listWeight, clampDown, 'outputR', bsnName, side)

        return clampUp, clampDown

    def eyebrowOneValue(self, bsnName, eyebrowCtrlIn, side, slideAtribute, valueNode):
        eyebrowInCtrlNew = self.replacePosLFTRGT(eyebrowCtrlIn, 'BshRGT', 'BshLFT')
        multDoubleLinearUp = mc.createNode('multDoubleLinear', n=au.prefixName(eyebrowInCtrlNew) + 'Bsh' + side + '_mdl')
        mc.setAttr(multDoubleLinearUp + '.input2', valueNode)
        mc.connectAttr(eyebrowCtrlIn + '.%s' % slideAtribute, multDoubleLinearUp + '.input1')

        # CONNECT TO BSH
        listWeight = mc.listAttr(bsnName+'.w', m=True)

        # UP
        self.connectNodeToBsh(listWeight, multDoubleLinearUp, 'output', bsnName, side)

    def replacePosLFTRGT(self, nameObj, sideRGT, sideLFT):
        if sideRGT in nameObj:
            crvNewName = nameObj.replace(sideRGT, '')
        elif sideLFT in nameObj:
            crvNewName = nameObj.replace(sideLFT, '')
        else:
            crvNewName = nameObj

        return crvNewName

    def connectNodeToBsh(self, listWeight, connectorNode, atttNode, bsnName, side):
        list = []
        for i in listWeight:
            listI = i[:-7]
            list.append(listI)

        searchList = list
        longString = connectorNode
        baseName = self.replacePosLFTRGT(connectorNode, 'BshRGT', 'BshLFT')
        if re.compile('|'.join(searchList), re.IGNORECASE).search(longString):  # re.IGNORECASE is used to ignore case
            mc.connectAttr(connectorNode+'.%s' % atttNode, bsnName+'.%s%s%s' % (au.prefixName(baseName), side, '_ply'))
        else:
            print mc.error ('There is no weight on blendshape')