from social_interaction_cloud.action import ActionRunner
from social_interaction_cloud.basic_connector import BasicSICConnector, RobotPosture


movement = b'{"motion":{"LShoulderPitch":{"angles":[1445,1445,1445,1445,1445,1445,1445,1445,1445,1445,1445,1445,1439,1385,1308,1177,950,486,281,279,258,252,253,265,353,482,624,980,1425,1526,1545,1546,1546,1546,1545],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680]},"LShoulderRoll":{"angles":[198,184,176,172,169,161,159,152,144,132,127,101,95,58,20,-20,-45,-38,-60,-68,-69,-68,-69,-69,-69,-68,-66,-63,6,31,17,14,14,14,12],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680]},"RShoulderRoll":{"angles":[-193,-169,-152,-132,-114,-100,-91,-81,-75,-69,-63,-48,-49,-46,-49,-48,-35,-38,-38,-37,-38,-37,-37,-38,-40,-40,-40,-40,-37,-28,-60,-58,-58,-60,-60],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680]},"LElbowYaw":{"angles":[-1178,-1177,-1178,-1178,-1177,-1177,-1178,-1178,-1178,-1177,-1178,-1177,-1175,-1174,-1174,-1174,-1174,-1174,-1174,-1174,-1174,-1174,-1174,-1174,-1175,-1175,-1175,-1175,-1175,-1178,-1178,-1178,-1178,-1178,-1178],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680]},"LWristYaw":{"angles":[113,113,113,113,113,113,113,113,113,113,113,113,117,118,120,120,118,118,117,118,118,118,117,115,115,115,115,115,115,115,115,115,115,115,115],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680]},"RWristYaw":{"angles":[298,298,298,298,298,298,298,298,298,298,298,296,291,291,290,290,290,290,290,290,290,290,290,290,290,288,288,285,287,290,293,293,293,293,293],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680]},"LHand":{"angles":[310,312,314,317,321,326,337,344,350,351,337,322,308,293,279,266,260,273,286,300,301,303,305,307,308,311,313,316,319,323,332,340,347,294,345],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680]},"LElbowRoll":{"angles":[-439,-425,-411,-394,-379,-362,-348,-334,-325,-325,-325,-331,-376,-429,-508,-609,-687,-689,-699,-726,-747,-762,-778,-775,-719,-699,-667,-650,-627,-598,-563,-545,-538,-534,-532],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680]},"RElbowRoll":{"angles":[425,414,407,394,382,368,357,347,336,327,321,338,370,425,500,545,584,641,700,741,775,802,827,836,816,830,825,822,796,752,696,680,673,672,669],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680]},"RElbowYaw":{"angles":[1207,1207,1207,1207,1207,1206,1207,1207,1207,1207,1207,1207,1213,1213,1213,1213,1213,1213,1213,1213,1213,1213,1213,1213,1212,1212,1212,1209,1209,1207,1207,1207,1207,1207,1207],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680]},"RHand":{"angles":[337,345,352,360,367,373,373,373,373,365,356,345,336,326,317,308,304,303,301,300,305,312,319,326,333,341,348,356,363,371,373,373,373,302,361],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680]},"RShoulderPitch":{"angles":[1437,1437,1437,1437,1437,1437,1437,1437,1437,1437,1437,1437,1405,1332,1221,963,680,595,469,348,272,210,199,213,279,365,473,793,1263,1566,1632,1632,1632,1634,1634],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680]}},"precision_factor_angles":1000,"precision_factor_times":100,"robot":"nao"}'
crossing_arms = b'{"motion":{"LShoulderPitch":{"angles":[1480,1480,1480,1482,1480,1482,1480,1482,1482,1480,1480,1175,722,667,626,555,522,514,512,514,494,482,719,1147,1315,1404,1410,1410,1410,1410,1410,1410,1410,1410,1410],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680]},"LShoulderRoll":{"angles":[199,179,169,159,150,140,130,120,115,110,112,-107,-314,-314,-314,-314,-314,-314,-314,-314,-311,-149,230,429,258,87,86,86,87,86,86,86,86,86,86],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680]},"RShoulderRoll":{"angles":[-199,-167,-143,-118,-101,-86,-74,-63,-55,-43,-31,21,219,314,314,314,314,314,314,314,301,-120,-315,-361,-262,-180,-130,-121,-118,-117,-115,-114,-114,-112,-112],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680]},"LElbowYaw":{"angles":[-1189,-1189,-1187,-1189,-1187,-1189,-1187,-1189,-1189,-1189,-1189,-1183,-1180,-983,-525,-385,-341,-304,-304,-304,-308,-319,-319,-319,-318,-316,-318,-318,-318,-318,-318,-318,-318,-318,-318],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680]},"LWristYaw":{"angles":[113,113,113,113,113,113,113,113,113,113,113,94,81,80,113,117,141,120,120,118,118,117,117,117,117,152,156,155,155,155,155,155,155,155,155],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680]},"RWristYaw":{"angles":[676,676,676,676,676,676,676,676,676,676,676,673,667,813,815,833,992,1017,1017,1020,950,933,933,885,880,879,880,880,880,879,879,879,880,880,880],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680]},"LHand":{"angles":[303,305,307,309,311,314,316,320,323,334,341,348,353,342,328,313,299,284,270,257,268,281,294,300,302,304,306,308,310,312,315,317,321,326,337],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680]},"LElbowRoll":{"angles":[-411,-397,-385,-370,-356,-344,-333,-324,-324,-317,-308,-437,-503,-1011,-1387,-1387,-1382,-1376,-1382,-1382,-1414,-1327,-1264,-1131,-193,-35,-35,-35,-35,-35,-35,-35,-35,-35,-35],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680]},"RElbowRoll":{"angles":[407,399,391,380,371,361,353,344,334,330,334,433,463,384,500,982,985,971,971,971,962,939,887,772,35,35,35,35,35,35,35,35,35,35,35],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680]},"RElbowYaw":{"angles":[1219,1219,1219,1219,1219,1219,1219,1219,1219,1219,1221,1213,1147,606,552,517,499,472,471,471,468,468,459,420,210,210,210,212,212,212,212,212,212,212,212],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680]},"RHand":{"angles":[312,320,327,335,342,350,357,364,371,373,373,373,369,359,350,339,330,320,311,305,303,302,300,301,308,315,323,330,338,345,353,360,368,373,373],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680]},"RShoulderPitch":{"angles":[1477,1477,1477,1477,1477,1477,1477,1477,1477,1477,1477,1364,1177,1028,1023,985,986,986,986,986,982,976,1025,1286,1376,1428,1431,1431,1431,1431,1431,1431,1431,1431,1431],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680]}},"precision_factor_angles":1000,"precision_factor_times":100,"robot":"nao"}'
left_arm_highfive = b'{"motion":{"LShoulderPitch":{"angles":[1447,1447,1447,1447,1447,1413,1353,1235,977,471,370,261,-87,-192,-322,-456,-502,-560,-598,-631,-640,-643,-646,-647,-652,-654,-652,-654,-652,-654,-652,-654,-652,-652,-652],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680]},"LShoulderRoll":{"angles":[199,181,172,169,172,253,317,400,537,643,684,706,727,745,759,758,758,756,753,753,753,753,755,753,753,753,753,752,752,750,742,738,736,735,730],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680]},"RShoulderRoll":{"angles":[-192,-166,-146,-126,-109,-97,-87,-81,-74,-64,-58,-54,-49,-40,-37,-32,-29,-26,-25,-23,-22,-20,-20,-18,-18,-18,-18,-18,-17,-17,-17,-17,-17,-17,-17],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680]},"LElbowYaw":{"angles":[-1178,-1178,-1177,-1178,-1177,-1178,-1180,-1180,-1181,-1181,-1181,-1183,-1181,-1181,-1181,-1181,-1183,-1181,-1181,-1181,-1181,-1181,-1181,-1181,-1181,-1181,-1181,-1181,-1181,-1181,-1181,-1181,-1181,-1181,-1181],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680]},"LWristYaw":{"angles":[115,115,115,115,115,117,117,118,118,129,235,399,522,523,525,541,620,638,640,640,640,640,640,640,640,640,640,640,640,638,638,638,640,638,638],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680]},"RWristYaw":{"angles":[865,865,865,865,865,865,865,865,865,865,865,865,865,865,865,865,865,865,865,865,865,865,865,865,865,865,865,865,865,865,865,865,865,865,865],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680]},"LHand":{"angles":[310,312,314,317,321,326,337,343,350,352,337,324,308,295,279,264,260,274,286,300,301,847,304,306,308,311,313,316,318,322,330,340,346,352,346],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680]},"LElbowRoll":{"angles":[-442,-425,-410,-393,-376,-411,-437,-486,-552,-555,-607,-664,-709,-756,-830,-930,-974,-1017,-1034,-1032,-1028,-1028,-1029,-1029,-1031,-1031,-1031,-1031,-1031,-1031,-1031,-1031,-1031,-1028,-1026],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680]},"RElbowRoll":{"angles":[425,416,410,399,387,373,361,350,338,325,318,307,296,288,281,275,270,264,259,255,252,249,247,244,242,241,239,238,235,233,232,230,230,229,229],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680]},"RElbowYaw":{"angles":[1207,1207,1207,1207,1207,1207,1207,1207,1207,1207,1207,1207,1207,1207,1207,1207,1207,1207,1207,1207,1207,1207,1207,1207,1207,1207,1207,1207,1207,1207,1207,1207,1207,1207,1207],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680]},"RHand":{"angles":[337,345,352,360,367,373,373,373,373,366,356,347,336,327,317,306,304,303,301,300,304,302,319,326,333,340,348,355,362,370,373,373,373,371,362],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680]},"RShoulderPitch":{"angles":[1437,1437,1437,1437,1437,1437,1437,1437,1437,1437,1437,1437,1437,1437,1437,1437,1437,1437,1437,1437,1437,1437,1437,1437,1437,1437,1437,1437,1437,1437,1437,1437,1437,1437,1437],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680]}},"precision_factor_angles":1000,"precision_factor_times":100,"robot":"nao"}'
right_arm_highfive = b'{"motion":{"LShoulderPitch":{"angles":[1445,1445,1445,1445,1445,1445,1445,1445,1445,1445,1445,1445,1445,1445,1445,1445,1445,1445,1445,1445,1445,1445,1445,1445,1445,1445,1445,1445,1445,1445,1445,1445,1445,1445,1445],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680]},"LShoulderRoll":{"angles":[199,184,173,167,163,155,147,140,132,127,118,115,112,109,104,103,97,95,94,92,92,92,92,92,90,92,92,90,90,90,92,90,90,90,92],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680]},"RShoulderRoll":{"angles":[-193,-170,-150,-130,-109,-98,-86,-71,-71,-186,-390,-680,-910,-896,-831,-830,-824,-833,-833,-844,-844,-830,-833,-831,-838,-838,-839,-838,-836,-835,-835,-836,-838,-838,-838],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680]},"LElbowYaw":{"angles":[-1178,-1178,-1177,-1178,-1178,-1178,-1178,-1178,-1178,-1177,-1178,-1178,-1178,-1177,-1178,-1178,-1178,-1178,-1177,-1177,-1177,-1178,-1178,-1177,-1178,-1178,-1178,-1178,-1178,-1178,-1177,-1177,-1177,-1177,-1178],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680]},"LWristYaw":{"angles":[115,113,113,113,115,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,115,113,113,113,113,113,113,113,113,113],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680]},"RWristYaw":{"angles":[865,865,865,865,865,865,865,865,865,850,741,502,117,-224,-440,-465,-476,-477,-479,-479,-479,-479,-479,-479,-479,-479,-479,-479,-479,-479,-479,-479,-479,-479,-479],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680]},"LHand":{"angles":[310,312,315,317,321,326,337,344,350,351,335,322,307,293,278,264,262,274,294,300,301,303,304,307,309,311,313,316,319,294,333,340,347,353,343],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680]},"LElbowRoll":{"angles":[-440,-425,-406,-393,-374,-360,-345,-331,-324,-319,-307,-291,-279,-271,-259,-245,-232,-224,-224,-224,-224,-224,-224,-224,-224,-222,-218,-212,-206,-199,-193,-192,-190,-190,-189],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680]},"RElbowRoll":{"angles":[423,414,407,397,385,373,357,353,353,373,374,399,446,509,627,756,1189,1229,1249,1252,1253,1267,1269,1282,1286,1286,1284,1286,1284,1286,1286,1284,1284,1286,1286],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680]},"RElbowYaw":{"angles":[1207,1207,1207,1207,1207,1207,1207,1207,1207,1215,1215,1215,1215,1213,1213,1212,1157,1147,1152,1166,1186,1212,1223,1229,1244,1250,1261,1262,1262,1262,1262,1262,1262,1262,1262],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680]},"RHand":{"angles":[337,345,353,360,368,373,373,373,373,365,355,345,335,326,316,306,304,303,737,300,304,312,319,326,334,341,348,356,364,756,373,373,373,370,360],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680]},"RShoulderPitch":{"angles":[1436,1437,1436,1437,1437,1437,1437,1437,1437,1399,1295,1062,506,-18,-287,-382,-406,-400,-399,-403,-408,-410,-410,-408,-408,-408,-408,-408,-408,-408,-408,-408,-408,-408,-408],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680]}},"precision_factor_angles":1000,"precision_factor_times":100,"robot":"nao"}'
big_gesture = b'{"motion":{"LShoulderPitch":{"angles":[1448,1448,1448,1448,1440,1218,1178,1152,999,429,-104,-446,-561,-580,-575,-563,-511,-387,456,709,925,1040,1149,1244,1244,1242,1242,1242,1242,1242,1244,1244,1242,1244,1242],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680]},"LShoulderRoll":{"angles":[195,184,175,166,28,-221,-189,-190,-241,-236,-100,341,831,1072,1092,1109,1134,1134,816,477,232,-64,-222,-273,-249,-222,-221,-222,-222,-222,-222,-222,-221,-222,-222],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680]},"RShoulderRoll":{"angles":[-186,-163,-118,-87,202,314,314,314,314,314,219,-184,-621,-861,-856,-861,-858,-810,-509,-365,-244,120,287,230,198,196,196,196,196,196,196,196,196,196,196],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680]},"LElbowYaw":{"angles":[-1177,-1177,-1177,-1178,-1172,-1172,-1193,-1197,-1201,-1224,-1236,-1247,-1247,-1244,-1243,-1247,-1246,-1246,-1243,-1244,-1246,-1244,-1247,-1247,-1247,-1246,-1247,-1246,-1247,-1247,-1247,-1246,-1247,-1247,-1247],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680]},"LWristYaw":{"angles":[115,115,115,117,121,126,-49,-308,-368,-502,-726,-1078,-1258,-1154,-709,-492,-486,-482,-554,-190,-8,77,109,113,113,113,113,113,113,113,113,113,113,113,113],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680]},"RWristYaw":{"angles":[356,356,356,356,350,390,442,577,635,673,920,1034,1132,1166,1098,1097,1100,1115,1126,996,853,848,709,623,624,623,623,623,623,623,623,623,623,623,623],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680]},"LHand":{"angles":[311,313,316,319,323,331,340,346,353,346,330,317,306,288,273,259,306,279,292,300,306,303,306,307,310,312,314,317,321,325,306,343,349,353,339],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680]},"LElbowRoll":{"angles":[-440,-425,-408,-394,-494,-526,-853,-1517,-1545,-1545,-1520,-1457,-1316,-807,-281,-78,-35,-35,-83,-35,-35,-35,-35,-35,-35,-35,-35,-35,-35,-35,-35,-35,-35,-35,-35],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680]},"RElbowRoll":{"angles":[423,413,408,405,477,561,838,1516,1545,1539,1517,1468,1356,974,581,489,385,328,324,308,305,299,268,230,204,201,196,195,192,190,189,189,189,189,187],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680]},"RElbowYaw":{"angles":[1207,1207,1207,1207,1212,1200,1201,1163,1117,1138,1173,1221,1227,1227,1187,1178,1178,1180,1183,1170,1161,1163,1161,1161,1164,1164,1164,1164,1164,1164,1164,1164,1164,1164,1164],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680]},"RHand":{"angles":[341,348,355,362,370,373,373,373,371,362,351,342,303,322,312,305,303,302,300,300,303,314,303,329,337,344,352,359,366,373,303,373,373,367,357],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680]},"RShoulderPitch":{"angles":[1439,1439,1445,1445,1396,1256,1180,1178,993,364,-126,-307,-333,-331,-302,-201,-86,348,808,985,1092,1192,1276,1313,1330,1330,1330,1330,1330,1330,1330,1330,1330,1330,1330],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680]}},"precision_factor_angles":1000,"precision_factor_times":100,"robot":"nao"}'
left_arm_fist= b'{"motion":{"LShoulderPitch":{"angles":[1447,1447,1447,1447,1447,1447,1447,1447,1447,1447,1447,1402,1322,1172,637,492,399,281,92,18,18,18,18,18,18,18,17,17,18,17,17,17,17,17,17,17],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680,700]},"LShoulderRoll":{"angles":[195,178,166,156,146,136,129,121,118,113,109,110,109,112,115,78,80,80,80,54,31,6,-8,-9,-12,-11,-14,-14,-12,-12,-12,-12,-12,-12,-15,-15],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680,700]},"RShoulderRoll":{"angles":[-187,-164,-146,-126,-110,-97,-87,-80,-71,-64,-58,-52,-49,-45,-38,-31,-29,-29,-29,-22,-20,-20,-18,-18,-18,-18,-17,-17,-17,-17,-17,-17,-17,-17,-17,-17],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680,700]},"LElbowYaw":{"angles":[-1178,-1178,-1178,-1178,-1178,-1178,-1178,-1178,-1177,-1178,-1177,-1172,-1174,-1172,-1172,-1170,-1161,-1147,-1094,-1074,-1074,-1074,-1074,-1074,-1074,-1074,-1074,-1074,-1074,-1074,-1074,-1074,-1074,-1074,-1074,-1074],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680,700]},"LWristYaw":{"angles":[118,118,118,118,118,118,120,118,118,118,118,166,632,1015,1028,1106,1206,1262,1285,1287,1285,1285,1285,1285,1262,1241,1230,1229,1223,1219,1216,1215,1213,1213,1212,1212],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680,700]},"RWristYaw":{"angles":[367,367,367,367,367,367,367,367,367,367,367,367,367,367,367,367,367,367,367,367,367,367,367,367,367,367,367,367,367,367,367,367,367,367,367,367],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680,700]},"LHand":{"angles":[310,313,315,318,322,328,338,345,352,347,332,318,303,290,274,261,265,277,291,300,301,303,305,307,309,311,314,317,320,324,334,294,348,354,341,328],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680,700]},"LElbowRoll":{"angles":[-439,-428,-416,-402,-394,-388,-380,-376,-376,-376,-377,-423,-439,-479,-472,-431,-377,-317,-248,-150,-92,-63,-57,-52,-52,-54,-60,-63,-63,-63,-63,-61,-63,-63,-61,-63],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680,700]},"RElbowRoll":{"angles":[422,413,408,399,390,377,364,351,341,330,321,313,304,298,290,285,276,272,264,261,259,256,255,252,249,245,242,239,235,232,227,224,221,221,219,218],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680,700]},"RElbowYaw":{"angles":[1207,1207,1207,1207,1207,1207,1207,1207,1207,1207,1207,1207,1207,1207,1207,1207,1207,1207,1207,1207,1207,1207,1207,1207,1207,1207,1207,1207,1207,1207,1207,1207,1207,1207,1207,1207],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680,700]},"RHand":{"angles":[340,347,354,362,368,373,373,373,372,363,352,343,333,324,313,306,304,302,300,300,306,313,320,328,335,343,350,358,365,373,373,302,373,369,358,349],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680,700]},"RShoulderPitch":{"angles":[1437,1437,1437,1437,1437,1437,1437,1437,1437,1437,1437,1437,1437,1437,1437,1437,1437,1437,1437,1437,1437,1437,1437,1437,1437,1437,1439,1437,1437,1439,1437,1437,1437,1437,1437,1437],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680,700]}},"precision_factor_angles":1000,"precision_factor_times":100,"robot":"nao"}'
right_arm_fist = b'{"motion":{"LShoulderPitch":{"angles":[1447,1447,1447,1447,1447,1447,1447,1447,1447,1447,1447,1447,1447,1447,1447,1447,1447,1447,1447,1447,1447,1447,1447,1447,1447,1447,1447,1447,1447,1447,1447,1447,1447,1447,1447],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680]},"LShoulderRoll":{"angles":[184,173,164,156,147,136,129,123,115,110,107,106,101,100,98,98,98,97,94,94,94,94,92,90,89,89,87,86,84,84,84,84,84,84,84],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680]},"RShoulderRoll":{"angles":[-172,-158,-150,-146,-147,-192,-290,-397,-376,-357,-339,-325,-324,-310,-305,-298,-288,-296,-313,-315,-315,-315,-315,-315,-315,-315,-315,-315,-315,-315,-313,-313,-313,-308,-310],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680]},"LElbowYaw":{"angles":[-1177,-1178,-1178,-1177,-1178,-1178,-1178,-1177,-1177,-1178,-1177,-1178,-1178,-1177,-1178,-1177,-1178,-1177,-1177,-1177,-1178,-1177,-1177,-1177,-1177,-1178,-1178,-1178,-1177,-1177,-1177,-1177,-1177,-1177,-1178],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680]},"LWristYaw":{"angles":[113,115,113,113,113,113,113,113,113,113,115,113,113,113,113,113,113,115,115,113,113,115,113,113,115,115,113,113,113,113,113,113,113,115,113],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680]},"RWristYaw":{"angles":[367,367,367,367,350,265,204,152,64,-75,-153,-166,-175,-175,-175,-175,-175,-166,-164,-164,-164,-164,-164,-164,-164,-166,-164,-164,-164,-164,-164,-164,-164,-164,-164],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680]},"LHand":{"angles":[312,314,317,321,326,337,344,350,351,337,322,308,293,279,264,260,274,286,300,301,303,304,306,308,311,313,316,319,322,332,340,347,352,346,331],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680]},"LElbowRoll":{"angles":[-429,-414,-396,-379,-362,-350,-333,-324,-313,-299,-285,-275,-265,-255,-247,-242,-241,-241,-242,-242,-241,-241,-241,-241,-241,-238,-236,-232,-229,-224,-221,-219,-219,-219,-218],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680]},"RElbowRoll":{"angles":[414,410,403,399,426,465,486,473,477,492,491,460,442,426,419,417,416,391,354,347,347,345,345,342,341,341,338,330,324,321,321,321,321,321,321],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680]},"RElbowYaw":{"angles":[1206,1206,1206,1206,1209,1155,1055,612,176,141,120,110,11,-14,-15,-15,-15,-6,25,32,32,32,32,32,32,32,32,32,32,32,32,31,32,32,31],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680]},"RHand":{"angles":[345,352,360,367,373,373,373,373,365,356,345,336,326,317,306,304,303,301,300,304,312,319,326,333,340,348,355,363,370,373,373,373,371,362,352],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680]},"RShoulderPitch":{"angles":[1439,1439,1437,1439,1399,1275,1092,678,295,192,57,-37,-72,-63,-52,-52,-51,-44,-44,-44,-44,-44,-44,-44,-44,-44,-35,-21,-21,-21,-21,-21,-20,-21,-20],"times":[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680]}},"precision_factor_angles":1000,"precision_factor_times":100,"robot":"nao"}'


class Example:

    def __init__(self, server_ip: str):
        self.sic = BasicSICConnector(server_ip)
        self.action_runner = ActionRunner(self.sic)

    def run(self) -> None:
        self.sic.start()

        #Wakes the nao robot and setup the language + breathing state
        self.action_runner.run_waiting_action('wake_up')
        self.action_runner.run_waiting_action('set_language', 'en-US')
        self.action_runner.run_waiting_action('set_breathing', True)
        self.action_runner.run_loaded_actions()

        #This line plays an audio file
        # action_runner.load_waiting_action('play_audio', "cartoon-birds-2_daniel-simion.wav")

        #Activates the sensor on his head as an emergency exit. To execute the stop function
        self.sic.subscribe_touch_listener('MiddleTactilTouched', self.stop)

        #Speech line
        self.action_runner.load_waiting_action('say', 'I\'m going to crouch now.')

        #Posture Line
        self.action_runner.load_waiting_action('go_to_posture', RobotPosture.STAND,
                                        additional_callback=self.posture_callback)

        #SET Color of the LED Eyes
        self.action_runner.load_waiting_action('set_eye_color', 'green')

        #Do a specific motion. This is a predefined one
        self.action_runner.load_waiting_action('say', 'no no no no')
        self.action_runner.load_waiting_action('do_gesture', 'animations/Stand/Gestures/Desperate_2')

        #Do a motion that we prerecorderd
        self.action_runner.load_waiting_action('do_gesture', crossing_arms)

        self.action_runner.run_loaded_actions()

        self.action_runner.load_waiting_action('set_eye_color', 'blue')
        self.action_runner.load_waiting_action('say', 'I\'m going to stand now.')

        self.action_runner.load_waiting_action('go_to_posture', RobotPosture.STAND,
                                          additional_callback=self.posture_callback)
        self.action_runner.run_loaded_actions()

        self.action_runner.run_waiting_action('rest')

        self.sic.stop()

    @staticmethod
    def posture_callback(success: bool) -> None:
        print('It worked!' if success else 'It failed...')

    def stop(self):
        print('start')
        self.sic.unsubscribe_touch_listener('MiddleTactilTouched')
        self.action_runner.run_action('say', 'Im going back to sleep now.')
        self.action_runner.run_action('set_eye_color', 'white')
        #self.action_runner.run_loaded_actions()
        print('stop')
        self.sic.rest()
        self.sic.stop()


example = Example('127.0.0.1')
example.run()