from __builtin__ import reload

import ADUtils as au
from angela import  blendShape as bsh

reload(bsh)
reload(au)



def blendshape():
    leftSide = bsh.BuildTwoSide(bsnName='face_bsn', eyebrowCtrlOut='eyebrowOutBshLFT_ctrl',
                                eyebrowCtrlMid='eyebrowMidBshLFT_ctrl',
                                eyebrowCtrlIn='eyebrowInBshLFT_ctrl', eyebrowCtrlInner='eyebrowInnerBshLFT_ctrl',
                                eyebrowCtrlSqueeze='eyebrowSqueezeBshLFT_ctrl', eyebrowCtrlTwist='eyebrowTwistBshLFT_ctrl',
                                eyebrowCtrlCurl='eyebrowCurlBshLFT_ctrl', noseCtrl='noseBshLFT_ctrl',
                                cheekInOutCtrl='cheekBshLFT_ctrl', cheekInUp='cheekInUpBshLFT_ctrl', cheekOutUp='cheekOutUpBshLFT_ctrl',
                                upperLipRollCtrl='upperLipRollBshLFT_ctrl', lowerLipRollCtrl='lowerLipRollBshLFT_ctrl',
                                upperLipCtrl='upperLipBshLFT_ctrl', lowerLipCtrl='lowerLipBshLFT_ctrl',
                                upperLipCtrlOut='upperLipOutBshLFT_ctrl', lowerLipCtrlOut='lowerLipOutBshLFT_ctrl',
                                mouthCtrl='mouthBshLFT_ctrl',
                                side='LFT')

    rightSide = bsh.BuildTwoSide(bsnName='face_bsn', eyebrowCtrlOut='eyebrowOutBshRGT_ctrl',
                                 eyebrowCtrlMid='eyebrowMidBshRGT_ctrl',
                                 eyebrowCtrlIn='eyebrowInBshRGT_ctrl', eyebrowCtrlInner='eyebrowInnerBshRGT_ctrl',
                                 eyebrowCtrlSqueeze='eyebrowSqueezeBshRGT_ctrl', eyebrowCtrlTwist='eyebrowTwistBshRGT_ctrl',
                                 eyebrowCtrlCurl='eyebrowCurlBshRGT_ctrl', noseCtrl='noseBshRGT_ctrl',
                                 cheekInOutCtrl='cheekBshRGT_ctrl', cheekInUp='cheekInUpBshRGT_ctrl', cheekOutUp='cheekOutUpBshRGT_ctrl',
                                 upperLipRollCtrl='upperLipRollBshRGT_ctrl', lowerLipRollCtrl='lowerLipRollBshRGT_ctrl',
                                 upperLipCtrl='upperLipBshRGT_ctrl', lowerLipCtrl='lowerLipBshRGT_ctrl',
                                 upperLipCtrlOut='upperLipOutBshRGT_ctrl', lowerLipCtrlOut='lowerLipOutBshRGT_ctrl',
                                 mouthCtrl='mouthBshRGT_ctrl',
                                 side='RGT')

    center = bsh.BuildOneSide(bsnName='face_bsn', mouthCtrl='mouthBsh_ctrl',
                              upperLipRollCtrl='upperLipRollBshMID_ctrl',lowerLipRollCtrl='lowerLipRollBshMID_ctrl',
                              upperLipCtrl='upperLipBshMID_ctrl', lowerLipCtrl='lowerLipBshMID_ctrl',
                              upperLipCtrlOut='upperLipOutBshMID_ctrl', lowerLipCtrlOut='lowerLipOutBshMID_ctrl',
                              mouthTwistCtrl='mouthTwistBsh_ctrl', ACtrl='ABsh_ctrl', AhCtrl='AhBsh_ctrl',
                              ECtrl='EBsh_ctrl', FVCtrl='FVBsh_ctrl', LCtrl='LBsh_ctrl', MBPCtrl='MBPBsh_ctrl',
                              OhCtrl='OhBsh_ctrl', OOOCtrl='OOOBsh_ctrl', RCtrl='RBsh_ctrl', TKGCtrl='TKGBsh_ctrl',
                              ThCtrl='ThBsh_ctrl', UhCtrl='UhBsh_ctrl', YCtrl='YBsh_ctrl', NCtrl='NBsh_ctrl'
                              )


    # independent = bsh.BuildFree(bsnName='face_bsn', rollCtrl='rollLipBsh_ctrl',
    #                             upperWeightBsnMID='upperLipRollHalfDownMID_ply',
    #                             upperWeightBsnLFT='upperLipRollHalfDownLFT_ply',
    #                             upperWeightBsnRGT='upperLipRollHalfDownRGT_ply',
    #                             lowerWeightBsnMID='lowerLipRollHalfUpMID_ply',
    #                             lowerWeightBsnLFT='lowerLipRollHalfUpLFT_ply',
    #                             lowerWeightBsnRGT='lowerLipRollHalfUpRGT_ply', )