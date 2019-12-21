from __builtin__ import reload

import ADUtils as au
from angela import  blendShape as bsh

reload(bsh)
reload(au)



def blendshape():
    leftSide = bsh.BuildTwoSide(bsnName='face_bsn', eyebrowCtrlOut='eyebrowOutBshLFT_ctrl',
                                eyebrowCtrlMid='eyebrowMidBshLFT_ctrl',
                                eyebrowCtrlIn='eyebrowInBshLFT_ctrl', eyebrowCtrlInner='eyebrowInnerBshLFT_ctrl',
                                eyebrowCtrlSqueeze='eyebrowSqueezeBshRGT_ctrl', eyebrowCtrlTwist='eyebrowTwistBshLFT_ctrl',
                                eyebrowCtrlCurl='eyebrowCurlBshLFT_ctrl', noseCtrl='noseBshLFT_ctrl', cheekCtrl='cheekBshLFT_ctrl',
                                side='LFT')

    rightSide = bsh.BuildTwoSide(bsnName='face_bsn', eyebrowCtrlOut='eyebrowOutBshRGT_ctrl',
                                 eyebrowCtrlMid='eyebrowMidBshRGT_ctrl',
                                 eyebrowCtrlIn='eyebrowInBshRGT_ctrl', eyebrowCtrlInner='eyebrowInnerBshRGT_ctrl',
                                 eyebrowCtrlSqueeze='eyebrowSqueezeBshRGT_ctrl', eyebrowCtrlTwist='eyebrowTwistBshRGT_ctrl',
                                 eyebrowCtrlCurl='eyebrowCurlBshRGT_ctrl', noseCtrl='noseBshRGT_ctrl', cheekCtrl='cheekBshRGT_ctrl',
                                 side='RGT')

    center = bsh.BuildOneSide(bsnName='face_bsn', mouthCtrl='mouthBsh_ctrl')