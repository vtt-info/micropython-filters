# Filter coeffs for network analyser. Frozen.
from array import array
# http://t-filter.engineerjs.com/
# t-filter parameters based on 2KHz sampling

# FIR filter designed with
# http://t-filter.engineerjs.com/ http://t-filter.appspot.com

# sampling frequency: 2000 Hz

# 0 Hz - 160 Hz
# gain = 0
# desired attenuation = -50 dB
# actual attenuation = -58.773432260359314 dB

# 245 Hz - 255 Hz
# gain = 1
# desired ripple = 3 dB
# actual ripple = 0.4395212955083323 dB

# 340 Hz - 1000 Hz
# gain = 0
# desired attenuation = -50 dB
# actual attenuation = -58.773432260359314 dB

coeffs_8a = array('f', (
  -0.0008646866700221276,
  -0.00007789338800231479,
  0.0014455418248231421,
  0.00324942874567572,
  0.0034335420218244736,
  0.0003696228529220283,
  -0.005386758741411639,
  -0.010286980700035711,
  -0.009476857566307942,
  -0.0005716445337012121,
  0.013060616663050698,
  0.02267306167010209,
  0.019259785517254543,
  0.000723376637842406,
  -0.024191733749048327,
  -0.03938769356521361,
  -0.0315583525496071,
  -0.0007302161019150122,
  0.036810191640485275,
  0.05697731369689379,
  0.043521415665204635,
  0.0005472992042452829,
  -0.04758718282764343,
  -0.07050099792957325,
  -0.051611335733147364,
  -0.0002035216105500873,
  0.05314581450454528,
  0.07558936092565023,
  0.05314581450454528,
  -0.0002035216105500873,
  -0.051611335733147364,
  -0.07050099792957325,
  -0.04758718282764343,
  0.0005472992042452829,
  0.043521415665204635,
  0.05697731369689379,
  0.036810191640485275,
  -0.0007302161019150122,
  -0.0315583525496071,
  -0.03938769356521361,
  -0.024191733749048327,
  0.000723376637842406,
  0.019259785517254543,
  0.02267306167010209,
  0.013060616663050698,
  -0.0005716445337012121,
  -0.009476857566307942,
  -0.010286980700035711,
  -0.005386758741411639,
  0.0003696228529220283,
  0.0034335420218244736,
  0.00324942874567572,
  0.0014455418248231421,
  -0.00007789338800231479,
  -0.0008646866700221276))

# Pass 0-50Hz Stop 100-1000Hz
# Stop band rejection -50dB specified, got -66dB
# Passband ripple 5dB specified, got 0.6dB

coeffs_0 = array('f', (
 -0.0000722153288409739,
  0.0003137058058630565,
  0.00038569220273319,
  0.0005749003425041003,
  0.0008280425734109133,
  0.0011346221296965157,
  0.0014887378298292999,
  0.0018814765248971652,
  0.002299518125800201,
  0.0027248838317960747,
  0.003134965231304449,
  0.0035031351253230567,
  0.0037996986161231254,
  0.003993157175022867,
  0.004051893948396048,
  0.003946112840593105,
  0.003649969034869255,
  0.0031437941879818064,
  0.002416242838343031,
  0.0014662999820256536,
  0.000305034184804234,
  -0.0010430492122074377,
  -0.0025392466792292555,
  -0.004130678277876215,
  -0.005751049775881588,
  -0.007322155703621066,
  -0.008756130180246412,
  -0.009958330410979013,
  -0.010831073488386338,
  -0.011278072334255495,
  -0.011208838308213781,
  -0.01054327350041362,
  -0.009216350964953384,
  -0.007181670621633992,
  -0.00441622494402543,
  -0.0009234713204266227,
  0.003267606213602425,
  0.008097703551613553,
  0.013480668331577402,
  0.01930425810934074,
  0.02543307750077006,
  0.03171306481322245,
  0.03797652147310733,
  0.04404809796449255,
  0.04975147197554726,
  0.05491606886755329,
  0.059383735186375505,
  0.0630151042478662,
  0.06569528478024036,
  0.0673386481774585,
  0.06789238429813454,
  0.0673386481774585,
  0.06569528478024036,
  0.0630151042478662,
  0.059383735186375505,
  0.05491606886755329,
  0.04975147197554726,
  0.04404809796449255,
  0.03797652147310733,
  0.03171306481322245,
  0.02543307750077006,
  0.01930425810934074,
  0.013480668331577402,
  0.008097703551613553,
  0.003267606213602425,
  -0.0009234713204266227,
  -0.00441622494402543,
  -0.007181670621633992,
  -0.009216350964953384,
  -0.01054327350041362,
  -0.011208838308213781,
  -0.011278072334255495,
  -0.010831073488386338,
  -0.009958330410979013,
  -0.008756130180246412,
  -0.007322155703621066,
  -0.005751049775881588,
  -0.004130678277876215,
  -0.0025392466792292555,
  -0.0010430492122074377,
  0.000305034184804234,
  0.0014662999820256536,
  0.002416242838343031,
  0.0031437941879818064,
  0.003649969034869255,
  0.003946112840593105,
  0.004051893948396048,
  0.003993157175022867,
  0.0037996986161231254,
  0.0035031351253230567,
  0.003134965231304449,
  0.0027248838317960747,
  0.002299518125800201,
  0.0018814765248971652,
  0.0014887378298292999,
  0.0011346221296965157,
  0.0008280425734109133,
  0.0005749003425041003,
  0.00038569220273319,
  0.0003137058058630565,
  -0.0000722153288409739))