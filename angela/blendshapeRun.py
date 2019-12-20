import maya.cmds as mc

import ADUtils as au, blendShape as bsh
reload(bsh)
reload(au)



def blendshape():
    leftSide = bsh.Blendshape(bsnName='face_bsn', eyebrowCtrlOut='eyebrowOutBshLFT_ctrl',
                              eyebrowCtrlMid='eyebrowMidBshLFT_ctrl',
                              eyebrowCtrlIn='eyebrowInBshLFT_ctrl', eyebrowCtrlInner='eyebrowInnerBshLFT_ctrl',
                              eyebrowCtrlSqueeze='eyebrowSqueezeBshRGT_ctrl', eyebrowCtrlTwist='eyebrowTwistBshLFT_ctrl',
                              eyebrowCtrlCurl='eyebrowCurlBshLFT_ctrl',
                              side='LFT')

    rightSide = bsh.Blendshape(bsnName='face_bsn', eyebrowCtrlOut='eyebrowOutBshRGT_ctrl',
                              eyebrowCtrlMid='eyebrowMidBshRGT_ctrl',
                              eyebrowCtrlIn='eyebrowInBshRGT_ctrl', eyebrowCtrlInner='eyebrowInnerBshRGT_ctrl',
                               eyebrowCtrlSqueeze='eyebrowSqueezeBshRGT_ctrl', eyebrowCtrlTwist='eyebrowTwistBshRGT_ctrl',
                               eyebrowCtrlCurl='eyebrowCurlBshRGT_ctrl',
                               side='RGT')