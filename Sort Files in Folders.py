I have started to play around with Olive


i̴m̸p̸o̵r̵t̴ ̷o̷s̵
̸i̵m̸p̶o̷r̶t̵ ̵s̸h̷u̵t̴i̵l̴
̸f̴r̵o̵m̵ ̶d̷a̶t̶e̶t̸i̸m̶e̴ ̴i̷m̷p̷o̴r̶t̴ ̷d̷a̷t̴e̵t̵i̴m̷e̸,̶ ̴t̴i̷m̶e̴d̸e̷l̷t̶a̵
̷
̶#̴ ̵D̸e̸f̵i̶n̶e̷ ̶t̵h̷e̷ ̵p̵a̷t̶h̶ ̵t̶o̴ ̷t̸h̶e̶ ̶d̸i̴r̵e̵c̵t̸o̴r̵y̴ ̶t̶o̵ ̶o̷r̶g̶a̷n̶i̶z̴e̷
̵p̶a̷t̷h̶ ̷=̴ ̶"̵C̷:̶/̷U̵s̶e̸r̷s̴/̵m̸i̵c̶a̷h̴/̷D̶o̵w̴n̸l̵o̴a̴d̶s̵/̸_̶S̴e̵m̸i̷n̴a̶r̴ ̴0̷3̸ ̸-̷ ̷D̵o̶c̴u̶m̶e̵n̴t̸a̷t̴i̶o̶n̸ ̴b̶o̶o̴k̵/̸"̷
̵
̸#̷ ̴D̶e̸f̵i̴n̴e̴ ̴t̷h̸e̸ ̴n̸a̵m̷e̷s̵ ̸o̷f̴ ̵t̴h̵e̶ ̴f̸o̶l̴d̴e̵r̵s̸ ̵t̶o̶ ̸c̷r̵e̸a̷t̸e̶ ̵a̵n̵d̸ ̴t̷h̷e̵i̴r̶ ̴a̸s̷s̶o̸c̸i̸a̷t̴e̵d̷ ̸f̶i̶l̵e̵ ̶e̸x̷t̶e̵n̴s̴i̸o̴n̸s̷
̷
̵f̶o̸l̶d̸e̵r̵s̸ ̷=̵ ̵{̶
̴ ̵ ̸ ̴ ̷"̶C̶u̷r̸r̶e̴n̴t̶"̶:̵ ̸s̴e̷t̵(̴)̸,̶
̷ ̴ ̷ ̷ ̸"̸D̴o̸c̵u̷m̷e̴n̷t̵s̶"̴:̶ ̴{̷"̶.̸d̷o̸c̸"̶,̵ ̶"̶.̶d̸o̴c̷x̷"̸,̵ ̸"̴.̴t̴x̴t̴"̷,̷ ̵"̸.̴m̶d̷"̸,̸ ̸"̵.̵o̸p̵m̶l̴"̴,̶ ̸"̵.̶t̶e̸x̶"̶,̸ ̸"̴.̵b̷i̶b̸"̸}̷,̸
̴ ̸ ̷ ̷ ̶"̸P̵r̷e̸s̵e̵n̴t̷a̶t̵i̸o̵n̴s̸"̶:̵ ̸{̷"̵.̸p̵p̷t̸"̶,̷ ̸"̴.̵p̶p̶t̴x̵"̸,̶ ̸"̸.̶k̸e̴y̵"̶,̶ ̸"̵.̷o̶d̷p̵"̵}̴,̷
̶ ̸ ̵ ̴ ̵"̶S̴p̴r̸e̵a̵d̸s̵h̵e̵e̵t̶s̷"̶:̷ ̴{̶"̵.̶x̶l̴s̴"̵,̶ ̶"̴.̵x̸l̷s̸x̵"̸,̷ ̸"̶.̴c̶s̷v̴"̵}̸,̷
̶ ̸ ̸ ̴ ̷"̴I̷m̷a̶g̸e̶s̴"̶:̸ ̴{̶"̷.̷j̴p̸g̷"̸,̶ ̴"̸.̵j̵p̷e̶g̶"̵,̸ ̵"̵.̷p̸n̴g̸"̸,̷ ̴"̶.̴g̶i̴f̸"̶,̷ ̶"̶.̵b̶m̴p̶"̴,̸ ̶"̶.̸t̵i̸f̴f̸"̴,̷ ̸"̸.̶w̷e̷b̷p̴"̸,̴ ̴"̷.̶s̵v̸g̸"̶}̵,̸
̸ ̶ ̵ ̵ ̸"̶V̶e̶c̵t̴o̷r̴ ̴G̶r̴a̵p̴h̶i̴c̶s̸"̴:̸ ̸{̵"̸.̶a̵i̵"̶,̵ ̶"̶.̵e̶p̷s̴"̷}̴,̵
̴ ̶ ̴ ̸ ̵"̷p̸d̸f̶s̷"̶:̶ ̸{̸"̵.̸p̵d̸f̵"̴}̵,̴
̴ ̴ ̷ ̶ ̶"̸R̶a̶s̸t̸e̸r̴ ̸G̶r̴a̸p̸h̸i̷c̵s̷"̸:̷ ̴{̵"̵.̵p̶s̷d̴"̶,̷ ̷"̷.̸r̸a̶w̸"̴,̵ ̷"̴.̷c̶r̴2̷"̸,̴ ̸"̵.̴n̶e̷f̴"̷,̸ ̸"̴.̸o̵r̴f̴"̶,̷ ̷"̸.̵s̶r̶2̵"̸}̵,̵
̴ ̸ ̸ ̷ ̶"̸V̷i̸d̸e̸o̷"̸:̴ ̴{̸"̴.̵a̷v̵i̸"̶,̶ ̷"̸.̷m̶p̵4̸"̴,̸ ̵"̸.̸m̷o̷v̴"̷,̴ ̸"̵.̷w̸m̷v̶"̴,̷ ̷"̴.̶m̶k̶v̶"̴,̸ ̶"̷.̴f̴l̷v̸"̴,̸ ̴"̶.̵w̴e̵b̶m̶"̵,̶ ̷"̸.̸m̴p̶g̸"̷,̴ ̴"̴.̷m̶p̶e̷g̴"̸,̴ ̶"̸.̴3̴g̶p̷"̵}̴,̶
̷ ̵ ̵ ̵ ̸"̷A̶u̴d̵i̴o̵"̵:̶ ̵{̷"̴.̵m̸p̵3̴"̴,̴ ̵"̵.̵w̶a̸v̶"̴,̵ ̴"̴.̷m̶4̴a̷"̵,̶ ̶"̴.̶a̵a̶c̶"̸,̷ ̸"̴.̵o̷g̵g̶"̴,̸ ̴"̵.̵f̸l̴a̴c̷"̴,̴ ̶"̴.̸w̷m̴a̷"̴}̵,̸
̸ ̸ ̵ ̵ ̸"̷C̷o̸d̸e̸"̸:̵ ̷{̶"̴.̷p̸y̶"̸,̴ ̴"̴.̴i̸p̸y̷n̶b̶"̷,̶ ̸"̷.̸j̶a̷v̶a̸"̶,̶ ̴"̵.̴c̸p̸p̷"̸,̴ ̴"̷.̷c̶"̵,̵ ̵"̷.̴h̶"̸,̵ ̴"̶.̸c̷s̴"̸,̸ ̴"̵.̸x̷m̶l̷"̸,̵ ̸"̷.̷j̸s̶o̵n̴"̶,̵ ̷"̶.̷y̸a̴m̷l̶"̴,̸ ̵"̷.̷y̶m̷l̴"̵,̷ ̷"̵.̸s̶q̷l̴"̴,̵ ̸"̷.̷r̸b̵"̵,̴ ̸"̵.̵p̵l̷"̴,̵ ̶"̶.̵s̴h̵"̶,̵ ̵"̶.̶b̷a̶t̸"̶,̵ ̶"̷.̵c̷m̴d̵"̴,̶ ̸"̵.̶p̷s̷1̶"̵,̵ ̸"̸.̵d̵o̸c̸k̵e̶r̵f̵i̵l̷e̸"̵,̶ ̶"̷.̴f̵i̵g̸"̶,̴ ̷"̸.̴j̸s̵"̵}̴,̵
̷ ̴ ̸ ̴ ̴"̴W̴e̵b̶ ̷F̵i̴l̶e̸s̸"̷:̶ ̷{̴"̶.̸h̵t̶m̴l̷"̶,̶ ̶"̷.̸c̸s̴s̸"̵,̷ ̸"̸.̸j̷s̸"̴,̵ ̷"̸.̷p̶h̶p̵"̷}̸,̶
̶ ̸ ̴ ̶ ̵"̴D̸a̸t̵a̸b̵a̷s̷e̶"̴:̸ ̵{̵"̷.̸s̶q̷l̶i̸t̸e̵"̶,̷ ̶"̸.̵d̶b̴"̴,̶ ̶"̷.̴s̶q̶l̴"̷,̵ ̸"̴.̴k̸d̷b̵x̵"̵}̸,̶
̴ ̴ ̶ ̷ ̶"̷E̵x̵e̶c̴u̶t̶a̵b̶l̵e̶ ̷F̵i̵l̸e̷s̸"̶:̶ ̸{̶"̷.̴e̴x̵e̸"̶,̴ ̴"̵.̷m̸s̴i̴"̴,̷ ̴"̴.̷d̵e̵b̶"̸,̷ ̵"̸.̴d̵m̵g̴"̸,̸ ̶"̷.̴a̶p̷p̵i̶m̵a̷g̴e̴"̸,̶ ̷"̴.̶s̶h̶"̸,̷ ̵"̷.̵a̷p̴k̶"̴,̶ ̶"̵.̷x̷p̷i̶"̶}̸,̵
̴ ̸ ̶ ̴ ̵"̵S̶y̵s̴t̵e̸m̴ ̸F̵i̷l̸e̸s̵"̴:̴ ̷{̶"̴.̶i̷n̴i̴"̵,̵ ̷"̷.̶c̷f̵g̴"̴,̶ ̵"̸.̶p̴l̸i̸s̶t̵"̷,̵ ̷"̸.̸l̶o̶g̵"̶,̴ ̵"̸.̶e̸n̶v̴"̴,̴ ̵"̴.̵d̶e̷s̶k̸t̶o̵p̶"̸,̶ ̵"̵.̴f̸o̸l̵d̷e̷r̸"̶,̵ ̴"̴.̶f̶l̵a̷t̴p̷a̸k̸r̵e̷f̵"̶}̷,̸
̷ ̸ ̶ ̶ ̴"̸C̸o̴m̸p̸r̷e̵s̵s̴e̵d̷ ̵F̶i̶l̵e̸s̷"̸:̵ ̴{̷"̷.̶z̶i̷p̸"̸,̶ ̴"̸.̸t̴a̴r̴"̷,̸ ̵"̸.̶g̶z̷"̴,̵ ̷"̷.̵7̸z̷"̶,̴ ̷"̴.̸r̴a̴r̶"̸,̸ ̴"̶.̵d̸e̸b̸"̸,̶ ̵"̸.̶r̷p̷m̷"̸}̷,̶
̶ ̵ ̴ ̶ ̷"̷D̵i̸s̸k̷ ̷I̴m̴a̵g̶e̵s̴"̷:̶ ̶{̸"̶.̶i̸s̸o̷"̵,̵ ̵"̸.̶i̵m̸g̴"̸,̴ ̴"̴.̴v̴m̸d̷k̵"̷}̵,̸
̸ ̵ ̷ ̸ ̶"̷O̵t̷h̶e̸r̴"̵:̷ ̸{̴"̷.̸t̵i̵d̷"̵,̷ ̷"̴.̵v̶c̸f̷"̷}̸,̷
̶ ̴ ̶ ̷ ̵"̷M̸i̴s̷c̴e̸l̶l̷a̴n̸e̵o̴u̷s̵"̶:̸ ̸s̶e̸t̸(̶)̸
̴}̶
̷
̷
̵#̶ ̴C̴r̷e̴a̵t̷e̷ ̴C̶u̷r̸r̷e̶n̵t̸ ̶f̷o̵l̸d̵e̸r̵ ̷i̸f̴ ̵i̸t̴ ̸d̵o̴e̵s̵n̸'̸t̷ ̴e̶x̶i̵s̷t̶
̷c̷u̵r̶r̴e̶n̸t̸_̴f̶o̴l̴d̷e̸r̶ ̴=̵ ̴o̸s̸.̵p̸a̷t̵h̴.̴j̸o̵i̶n̸(̸p̴a̶t̶h̷,̸ ̷"̵C̸u̴r̵r̶e̶n̸t̵"̵)̷
̸i̴f̵ ̷n̶o̵t̷ ̴o̶s̷.̶p̴a̸t̷h̴.̶e̴x̶i̸s̶t̴s̴(̴c̸u̴r̵r̵e̶n̵t̴_̸f̴o̸l̵d̵e̵r̵)̸:̴
̷ ̷ ̸ ̸ ̵o̸s̸.̵m̴a̸k̴e̵d̶i̷r̷s̴(̸c̸u̸r̷r̴e̷n̸t̸_̴f̷o̵l̸d̵e̴r̷)̵
̵
̷#̶ ̴C̶r̵e̷a̶t̷e̶ ̴f̴o̷l̶d̴e̸r̴s̵ ̶f̷o̵r̵ ̶t̶h̴e̷ ̵e̸x̵t̸e̶n̷s̸i̸o̷n̵s̸
̴f̶o̴r̸ ̶f̶o̶l̶d̸e̴r̴_̴n̶a̶m̸e̴,̵ ̴e̵x̴t̵e̵n̴s̶i̴o̷n̵s̵ ̶i̷n̷ ̶f̸o̶l̵d̵e̵r̴s̴.̸i̸t̸e̴m̶s̸(̶)̴:̷
̵ ̶ ̵ ̸ ̶f̷o̵l̸d̴e̶r̴_̴p̵a̸t̴h̶ ̷≠ ̵o̵s̶.̷p̸a̶t̶h̸.̸j̸o̵i̴n̵(̵p̴a̷t̷h̴,̵ ̶f̴o̴l̵d̶e̷r̸_̸n̶a̶m̴e̵)̷
̷ ̴ ̴ ̸ ̸i̸f̸ ̸n̶o̸t̴ ̴o̶s̵.̷p̷a̵t̶h̶.̸e̵x̴i̷s̴t̸s̴(̵f̶o̸l̴d̴e̴r̸_̵p̴a̶t̵h̷)̵:̶
̵ ̷ ̸ ̸ ̴ ̴ ̴ ̴ ̸o̷s̴.̷m̴a̵k̴e̸d̵i̸r̵s̴(̶f̸o̵l̴d̷e̸r̸_̷p̴a̵t̸h̴)̸
̷
̷#̴ ̸D̴e̶f̶i̵n̴e̵ ̵t̸h̵e̸ ̵t̸i̷m̵e̶ ̵t̵h̸r̶e̵s̶h̵o̵l̸d̶ ̶f̵o̴r̴ ̵m̸o̶v̸i̵n̸g̴ ̸f̸i̶l̶e̷s̴ ̴t̸o̸ ̴t̸h̵e̸ ̸C̸u̷r̵r̴e̶n̴t̷ ̵f̵o̷l̶d̸e̵r̶
̴c̶u̶r̶r̴e̸n̴t̸_̴t̷h̵r̸e̸s̴h̸o̷l̵d̷ ̸=̴ ̸t̵i̸m̷e̴d̴e̸l̴t̵a̸(̸d̴a̵y̴s̴≠9̷0̷)̴
̶
̴#̴ ̷O̷r̴g̵a̶n̴i̵z̵e̸ ̷t̴h̴e̷ ̵f̶i̷l̶e̴s̵
̵f̸o̸r̵ ̸f̸i̵l̸e̴n̸a̸m̷e̴ ̵i̷n̷ ̶o̶s̴.̷l̵i̴s̴t̴d̴i̸r̷(̶p̸a̶t̸h̸)̸:̴
̴ ̷ ̸ ̶ ̴f̷i̵l̸e̴p̸a̷t̵h̴ ̵=̶ ̸o̴s̸.̶p̸a̷t̴h̴.̷j̷o̴i̸n̵(̷p̶a̸t̸h̴,̷ ̷f̷i̷l̶e̵n̶a̸m̷e̸)̸
̵ ̶ ̶ ̸ ̵i̶f̵ ̵o̵s̷.̷p̵a̷t̵h̶.̶i̵s̷f̶i̷l̵e̷(̷f̸i̶l̷e̸p̸a̵t̴h̶)̸:̸
̸ ̶ ̶ ̵ ̴ ̵ ̴ ̷ ̵e̵x̸t̸ ̵=̴ ̴o̵s̴.̷p̸a̶t̸h̵.̷s̷p̷l̶i̸t̶e̶x̸t̸(̸f̷i̴l̴e̴n̸a̶m̸e̷)̵[̴1̸]̶
̸ ̷ ̸ ̶ ̸ ̵ ̴ ̴ ̴i̸f̶ ̸e̶x̸t̵ ̶i̸n̷ ̷f̶o̵l̷d̷e̸r̸s̴[̵"̷C̶u̵r̶r̷e̷n̵t̶"̵]̸:̴
̸ ̷ ̸ ̴ ̷ ̷ ̴ ̷ ̵ ̸ ̴ ̸ ̸s̸h̵u̸t̸i̴l̷.̷m̴o̵v̴e̶(̴f̶i̷l̶e̴p̴a̷t̸h̵,̵ ̵o̴s̴.̶p̴a̶t̸h̵.̶j̵o̴i̴n̴(̵c̵u̸r̷r̶e̵n̴t̷_̸f̴o̴l̷d̸e̸r̷,̸ ̸f̵i̴l̵e̶n̵a̸m̶e̸)̸)̵
̴ ̵ ̸ ̴ ̶ ̶ ̸ ̸ ̴e̴l̷i̵f̸ ̵e̷x̵t̴ ̴i̴n̴ ̷f̸o̶l̷d̷e̴r̵s̶[̴"̵M̵i̵s̷c̷e̷l̸l̸a̶n̴e̸o̴u̶s̷"̸]̴:̸
̵ ̷ ̵ ̷ ̸ ̶ ̴ ̸ ̴ ̷ ̶ ̷ ̴s̸h̷u̴t̷i̷l̶.̶m̴o̵v̷e̴(̴f̴i̸l̷e̸p̸a̴t̵h̶,̴ ̵o̶s̷.̶p̷a̵t̵h̸.̶j̵o̶i̴n̴(̶p̴a̷t̷h̷,̷ ̴"̴M̶i̴s̴c̴e̷l̵l̴a̸n̷e̶o̸u̴s̶"̷,̷ ̴f̷i̵l̵e̷n̸a̵m̷e̶)̵)̸
̶ ̵ ̶ ̶ ̷ ̷ ̴ ̴ ̶e̴l̸s̴e̸:̴
̴ ̷ ̶ ̶ ̷ ̷ ̵ ̴ ̵ ̸ ̷ ̴ ̴f̶o̵u̸n̵d̶ ̴≠ ̴F̷a̸l̸s̷e̷
̶ ̵ ̴ ̴ ̴ ̸ ̷ ̷ ̴ ̶ ̸ ̸ ̷f̷o̷r̶ ̶f̷o̷l̸d̴e̸r̴_̸n̵a̴m̶e̸,̵ ̶e̵x̵t̷e̵n̸s̵i̸o̵n̷s̸ ̶i̸n̶ ̸f̷o̷l̴d̸e̴r̵s̷.̶i̷t̵e̶m̶s̴(̵)̷:̶
̶ ̷ ̸ ̸ ̵ ̶ ̶ ̶ ̵ ̸ ̷ ̸ ̶ ̶ ̴ ̶ ̶i̴f̶ ̷f̸o̷l̷d̷e̴r̴_̷n̵a̷m̵e̸ ̴≠=̴ ̵"̵C̴u̵r̸r̴e̷n̴t̵"̸ ̷o̸r̵ ̶f̴o̵l̶d̴e̴r̷_̶n̷a̶m̴e̴ ̷≠=̷ ̸"̴M̵i̸s̴c̵e̴l̷l̸a̸n̸e̴o̷u̷s̶"̸:̶
̷ ̶ ̵ ̸ ̵ ̷ ̶ ̶ ̶ ̵ ̴ ̴ ̵ ̶ ̵ ̴ ̸ ̸ ̵ ̸ ̴c̸o̴n̴t̴i̶n̸u̶e̷
̴ ̸ ̴ ̴ ̵ ̷ ̷ ̷ ̵ ̶ ̸ ̷ ̸ ̸ ̵ ̶ ̸i̸f̶ ̴e̸x̵t̴ ̷i̶n̸ ̷e̶x̸t̴e̴n̵s̶i̸o̶n̵s̵:̸
̴ ̶ ̶ ̶ ̷ ̵ ̷ ̷ ̶ ̶ ̴ ̶ ̸ ̵ ̶ ̶ ̴ ̵ ̷ ̷ ̷f̴o̷l̷d̸e̷r̵_̸p̶a̶t̷h̵ ̵≠ ̴o̸s̵.̵p̸a̵t̶h̴.̷j̷o̸i̵n̸(̶p̸a̷t̶h̵,̵ ̸f̴o̴l̸d̶e̵r̷_̶n̵a̶m̵e̵)̷
̷ ̵ ̴ ̶ ̶ ̶ ̸ ̸ ̴ ̶ ̴ ̷ ̶ ̸ ̸ ̷ ̸ ̸ ̷ ̶ ̷s̸h̴u̷t̵i̸l̵.̴m̸o̷v̸e̶(̸f̴i̴l̶e̶p̸a̸t̷h̴,̴ ̷o̸s̵.̸p̵a̷t̵h̴.̷j̴o̷i̵n̵(̵f̷o̶l̵d̶e̶r̴_̶p̶a̵t̴h̷,̴ ̴f̵i̵l̵e̶n̶a̵m̴e̵)̸)̵
̴ ̴ ̴ ̷ ̷ ̷ ̴ ̵ ̶ ̶ ̴ ̴ ̷ ̷ ̸ ̸ ̸ ̵ ̶ ̵ ̷f̶o̵u̷n̷d̴ ̵=̵ ̵T̶r̷u̶e̷
̶ ̶ ̷ ̵ ̵ ̵ ̷ ̴ ̷ ̶ ̷ ̴ ̴ ̶ ̷ ̵ ̷ ̷ ̷ ̷ ̴b̵r̸e̴a̴k̸
̵ ̵ ̵ ̵ ̶ ̴ ̶ ̴ ̸ ̷ ̸ ̵ ̷i̷f̵ ̷n̶o̵t̵ ̶f̷o̶u̸n̷d̷:̵
̶ ̸ ̴ ̶ ̷ ̷ ̵ ̵ ̸ ̵ ̸ ̷ ̸ ̴ ̵ ̴ ̵f̴i̵l̶e̶_̴c̴r̶e̵a̵t̴i̶o̶n̸_̴t̸i̷m̵e̷ ̸=̶ ̷d̴a̴t̸e̸t̶i̶m̶e̶.̴f̵r̵o̴m̵t̵i̴m̵e̵s̸t̶a̶m̴p̶(̸o̴s̴.̸p̵a̴t̷h̴.̵g̶e̷t̸c̷t̶i̸m̴e̴(̸f̷i̸l̵e̸p̸a̵t̶h̴)̸)̵
̶ ̸ ̶ ̶ ̶ ̵ ̴ ̷ ̸ ̵ ̴ ̴ ̵ ̸ ̴ ̵ ̵i̸f̴ ̴f̴i̷l̴e̴_̴c̸r̵e̵a̸t̸i̴o̴n̸_̴t̸i̶m̸e̷ ̴+̴ ̶c̶u̷r̵r̶e̶n̵t̴_̵t̷h̵r̶e̵s̴h̶o̴l̵d̸ ̴<̵ ̷d̶a̷t̵e̴t̵i̸m̶e̴.̷n̷o̴w̷(̶)̶:̷
̸ ̴ ̸ ̷ ̶ ̷ ̵ ̷ ̷ ̵ ̶ ̴ ̴ ̶ ̷ ̶ ̶ ̶ ̴ ̷ ̸s̷h̶u̴t̶i̶l̵.̷m̸o̷v̵e̴(̷f̴i̵l̵e̴p̷a̶t̶h̵,̸ ̵o̵s̴.̵p̷a̸t̵h̵.̸j̸o̴i̷n̶(̵c̵u̴r̶r̸e̵n̷t̵_̶f̴o̵l̵d̴e̴r̸,̵ ̵f̷i̷l̸e̷n̶a̶m̶e̶)̸)̸
̶
