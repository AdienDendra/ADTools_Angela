import maya.cmds as mc
import ADUtils as au
reload (au)


class listFaceSkeletonDuplicate:
    # HEAD PART AND FACE
    def __init__(self, objDuplicate,
                 valuePrefix,
                 keyPrefix,
                 suffix,
                 oriPrefix='',
                 ):

        hide = mc.ls(type='joint')
        mc.hide(hide)

        # DUPLICATE SKELETON
        sj = au.listSkeletonDic(objDuplicate=objDuplicate,
                                valuePrefix=valuePrefix,
                                keyPrefix=keyPrefix,
                                oriPrefix=oriPrefix,
                                suffix=suffix)

        # NECK AND HEAD
        self.neck       = sj['%s%s%s_%s' % ('neck01', oriPrefix, keyPrefix, suffix)]
        self.head01     = sj['%s%s%s_%s' % ('head01', oriPrefix, keyPrefix, suffix)]
        self.head02     = sj['%s%s%s_%s' % ('head02', oriPrefix, keyPrefix, suffix)]


        self.headUp01      = sj['%s%s%s_%s' % ('headUp01', oriPrefix, keyPrefix, suffix)]
        self.headLow01     = sj['%s%s%s_%s' % ('headLow01', oriPrefix, keyPrefix, suffix)]
        self.jaw01     = sj['%s%s%s_%s' % ('jaw01', oriPrefix, keyPrefix, suffix)]
        self.chin     = sj['%s%s%s_%s' % ('chin', oriPrefix, keyPrefix, suffix)]
        self.throat     = sj['%s%s%s_%s' % ('throat', oriPrefix, keyPrefix, suffix)]
        self.eyebrow    = sj['%s%s%s_%s' % ('eyebrow', oriPrefix, keyPrefix, suffix)]


        # EYELIDS LFT
        self.eyebrowInLFT    = sj['%s%s%s%s_%s' % ('eyebrowIn', oriPrefix, keyPrefix, 'LFT', suffix)]
        self.eyebrowMidLFT    = sj['%s%s%s%s_%s' % ('eyebrowMid', oriPrefix, keyPrefix, 'LFT', suffix)]
        self.eyebrowOutLFT    = sj['%s%s%s%s_%s' % ('eyebrowOut', oriPrefix, keyPrefix, 'LFT', suffix)]
        self.eyelidPinchInLFT    = sj['%s%s%s%s_%s' % ('eyelidPinchIn', oriPrefix, keyPrefix, 'LFT', suffix)]
        self.eyelidPinchOutLFT    = sj['%s%s%s%s_%s' % ('eyelidPinchOut', oriPrefix, keyPrefix, 'LFT', suffix)]

        # BROW LFT
        self.browInUpLFT    = sj['%s%s%s%s_%s' % ('browInUp', oriPrefix, keyPrefix, 'LFT', suffix)]
        self.browMidUpLFT    = sj['%s%s%s%s_%s' % ('browMidUp', oriPrefix, keyPrefix, 'LFT', suffix)]
        self.browOutUpLFT    = sj['%s%s%s%s_%s' % ('browOutUp', oriPrefix, keyPrefix, 'LFT', suffix)]
        self.browInDownLFT    = sj['%s%s%s%s_%s' % ('browInDown', oriPrefix, keyPrefix, 'LFT', suffix)]
        self.browMidDownLFT    = sj['%s%s%s%s_%s' % ('browMidDown', oriPrefix, keyPrefix, 'LFT', suffix)]
        self.browOutDownLFT    = sj['%s%s%s%s_%s' % ('browOutDown', oriPrefix, keyPrefix, 'LFT', suffix)]

        # CHEEK MID LFT SIDE
        self.cheekUpLFT     = sj['%s%s%s%s_%s' % ('cheekUp', oriPrefix, keyPrefix, 'LFT', suffix)]
        self.cheekUpOutLFT     = sj['%s%s%s%s_%s' % ('cheekUpOut', oriPrefix, keyPrefix, 'LFT', suffix)]
        self.cheekDownLFT   = sj['%s%s%s%s_%s' % ('cheekDown', oriPrefix, keyPrefix, 'LFT', suffix)]

        # NOSE LFT
        self.nose    = sj['%s%s%s_%s' % ('nose', oriPrefix, keyPrefix, suffix)]
        self.noseTip    = sj['%s%s%s_%s' % ('noseTip', oriPrefix, keyPrefix, suffix)]
        self.nostrilLFT = sj['%s%s%s%s_%s' % ('nostril', oriPrefix, keyPrefix, 'LFT', suffix)]

        # LIP
        self.lipMidUp    = sj['%s%s%s_%s' % ('lipMidUp', oriPrefix, keyPrefix, suffix)]
        self.lipMidDown  = sj['%s%s%s_%s' % ('lipMidDown', oriPrefix, keyPrefix, suffix)]

        # LIP LFT
        self.lipUp01LFT    = sj['%s%s%s%s_%s' % ('lipUp01', oriPrefix, keyPrefix, 'LFT', suffix)]
        self.lipUp02LFT    = sj['%s%s%s%s_%s' % ('lipUp02', oriPrefix, keyPrefix, 'LFT', suffix)]
        self.lipDown01LFT  = sj['%s%s%s%s_%s' % ('lipDown01', oriPrefix, keyPrefix, 'LFT', suffix)]
        self.lipDown02LFT  = sj['%s%s%s%s_%s' % ('lipDown02', oriPrefix, keyPrefix, 'LFT', suffix)]

        self.lipCornerLFT    = sj['%s%s%s%s_%s' % ('lipCorner', oriPrefix, keyPrefix, 'LFT', suffix)]

        # EYELIDS RGT
        self.eyebrowInRGT    = sj['%s%s%s%s_%s' % ('eyebrowIn', oriPrefix, keyPrefix, 'RGT', suffix)]
        self.eyebrowMidRGT    = sj['%s%s%s%s_%s' % ('eyebrowMid', oriPrefix, keyPrefix, 'RGT', suffix)]
        self.eyebrowOutRGT    = sj['%s%s%s%s_%s' % ('eyebrowOut', oriPrefix, keyPrefix, 'RGT', suffix)]
        self.eyelidPinchInRGT    = sj['%s%s%s%s_%s' % ('eyelidPinchIn', oriPrefix, keyPrefix, 'RGT', suffix)]
        self.eyelidPinchOutRGT    = sj['%s%s%s%s_%s' % ('eyelidPinchOut', oriPrefix, keyPrefix, 'RGT', suffix)]

        # BROW RGT
        self.browInUpRGT    = sj['%s%s%s%s_%s' % ('browInUp', oriPrefix, keyPrefix, 'RGT', suffix)]
        self.browMidUpRGT    = sj['%s%s%s%s_%s' % ('browMidUp', oriPrefix, keyPrefix, 'RGT', suffix)]
        self.browOutUpRGT    = sj['%s%s%s%s_%s' % ('browOutUp', oriPrefix, keyPrefix, 'RGT', suffix)]
        self.browInDownRGT    = sj['%s%s%s%s_%s' % ('browInDown', oriPrefix, keyPrefix, 'RGT', suffix)]
        self.browMidDownRGT    = sj['%s%s%s%s_%s' % ('browMidDown', oriPrefix, keyPrefix, 'RGT', suffix)]
        self.browOutDownRGT    = sj['%s%s%s%s_%s' % ('browOutDown', oriPrefix, keyPrefix, 'RGT', suffix)]

        # CHEEK MID RGT SIDE
        self.cheekUpRGT     = sj['%s%s%s%s_%s' % ('cheekUp', oriPrefix, keyPrefix, 'RGT', suffix)]
        self.cheekUpOutRGT     = sj['%s%s%s%s_%s' % ('cheekUpOut', oriPrefix, keyPrefix, 'RGT', suffix)]
        self.cheekDownRGT   = sj['%s%s%s%s_%s' % ('cheekDown', oriPrefix, keyPrefix, 'RGT', suffix)]

        # NOSE RGT
        self.nostrilRGT = sj['%s%s%s%s_%s' % ('nostril', oriPrefix, keyPrefix, 'RGT', suffix)]

        # LIP RGT
        self.lipUp01RGT    = sj['%s%s%s%s_%s' % ('lipUp01', oriPrefix, keyPrefix, 'RGT', suffix)]
        self.lipUp02RGT    = sj['%s%s%s%s_%s' % ('lipUp02', oriPrefix, keyPrefix, 'RGT', suffix)]
        self.lipDown01RGT  = sj['%s%s%s%s_%s' % ('lipDown01', oriPrefix, keyPrefix, 'RGT', suffix)]
        self.lipDown02RGT  = sj['%s%s%s%s_%s' % ('lipDown02', oriPrefix, keyPrefix, 'RGT', suffix)]

        self.lipCornerRGT    = sj['%s%s%s%s_%s' % ('lipCorner', oriPrefix, keyPrefix, 'RGT', suffix)]

        # EYEBALL
        self.eyeballLFT = sj['%s%s%s%s_%s' % ('eyeball', oriPrefix, keyPrefix, 'LFT', suffix)]
        self.eyeballSpecLFT = sj['%s%s%s%s_%s' % ('eyeballSpec', oriPrefix, keyPrefix, 'LFT', suffix)]
        self.eyeballSpecTipLFT = sj['%s%s%s%s_%s' % ('eyeballSpecTip', oriPrefix, keyPrefix, 'LFT', suffix)]
        self.pupilLFT = sj['%s%s%s%s_%s' % ('pupil', oriPrefix, keyPrefix, 'LFT', suffix)]
        self.irisLFT = sj['%s%s%s%s_%s' % ('iris', oriPrefix, keyPrefix, 'LFT', suffix)]

        self.eyeballRGT = sj['%s%s%s%s_%s' % ('eyeball', oriPrefix, keyPrefix, 'RGT', suffix)]
        self.eyeballSpecRGT = sj['%s%s%s%s_%s' % ('eyeballSpec', oriPrefix, keyPrefix, 'RGT', suffix)]
        self.eyeballSpecTipRGT = sj['%s%s%s%s_%s' % ('eyeballSpecTip', oriPrefix, keyPrefix, 'RGT', suffix)]
        self.pupilRGT = sj['%s%s%s%s_%s' % ('pupil', oriPrefix, keyPrefix, 'RGT', suffix)]
        self.irisRGT = sj['%s%s%s%s_%s' % ('iris', oriPrefix, keyPrefix, 'RGT', suffix)]

        # EAR
        self.earLFT = sj['%s%s%s%s_%s' % ('ear', oriPrefix, keyPrefix, 'LFT', suffix)]
        self.earRGT = sj['%s%s%s%s_%s' % ('ear', oriPrefix, keyPrefix, 'RGT', suffix)]

        # TEETH
        self.upperTeeth = sj['%s%s%s_%s' % ('upperTeeth', oriPrefix, keyPrefix, suffix)]
        self.lowerTeeth = sj['%s%s%s_%s' % ('lowerTeeth', oriPrefix, keyPrefix, suffix)]

        # TOUNGE
        self.tongue01 = sj['%s%s%s_%s' % ('tongue01', oriPrefix, keyPrefix, suffix)]
        self.tongue02 = sj['%s%s%s_%s' % ('tongue02', oriPrefix, keyPrefix, suffix)]
        self.tongue03 = sj['%s%s%s_%s' % ('tongue03', oriPrefix, keyPrefix, suffix)]
        self.tongue04 = sj['%s%s%s_%s' % ('tongue04', oriPrefix, keyPrefix, suffix)]

        # mc.parent(self.neck, 'tmpJnt_grp')
