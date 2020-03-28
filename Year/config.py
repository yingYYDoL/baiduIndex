COOKIES = [#'BAIDUID=2C8B1515D6119C1FB6A42CA6A96CA968:FG=1; BIDUPSID=2C8B1515D6119C1FB6A42CA6A96CA968; PSTM=1569847469; BD_UPN=12314753; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDUSS=VHa2xwLTF1bkd3eHh3MVFuamRqMXR4LXM2VTU3T0F1YzVmbGVpQmpxS1ZkSlZlRVFBQUFBJCQAAAAAAAAAAAEAAADd3ekoY87i06K3ogAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJXnbV6V521edW; bdindexid=7sslvctfk4kh5bgdp6ank7v4u4; H_PS_PSSID=30968_1443_21090_30907_30996_30823_31085; delPer=0; BD_CK_SAM=1; PSINO=6; COOKIE_SESSION=78_2_9_7_15_21_0_0_9_4_0_2_8145275_5100746_2_0_1584281582_1576071342_1584281580%7C9%235100750_3_1576071336%7C2; BD_HOME=1; sugstore=0'\
           'PSTM=1581333715; BAIDUID=F596F7A426D1CED773943C1544CD1A1D:FG=1; BIDUPSID=DE0E1691B8D3FDAF045BD48BACFB0E4A; BD_UPN=12314753; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BD_HOME=1; sugstore=0; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; BD_CK_SAM=1; PSINO=7; BDUSS=RRYi1GLXNONjJEZ1JaQ3hhanRiZGhOSHVnWjFNTHhvS1VmaVI3bW5-T2hkWlZlRVFBQUFBJCQAAAAAAAAAAAEAAABunUmrAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKHobV6h6G1eMW; H_PS_PSSID=30963_1438_21102_30906_30998_30824_31086; COOKIE_SESSION=27_0_7_9_42_35_0_5_7_6_0_3_0_0_0_0_1584168988_0_1584261283%7C9%23301863_12_1581604129%7C3; H_PS_645EC=8976Qmsdr1bOCk0UpIs0yZ3gDPY6LtcD4Cf2aYTriOtw1ZxombNa%2FRFXXMZWrOQnUP%2F4'\
           ]
PROVINCE_CODE = {'山东': '901', '贵州': '902', '江西': '903', '重庆': '904', '内蒙古': '905', '湖北': '906', '辽宁': '907', '湖南': '908', '福建': '909', '上海': '910', '北京': '911', '广西': '912', '广东': '913', '四川': '914', '云南': '915', '江苏': '916', '浙江': '917', '青海': '918', '宁夏': '919', '河北': '920', '黑龙江': '921', '吉林': '922', '天津': '923', '陕西': '924', '甘肃': '925', '新疆': '926', '河南': '927', '安徽': '928', '山西': '929', '海南': '930', '台湾': '931', '西藏': '932', '香港': '933', '澳门': '934'}

CITY_CODE = {'广州': '95', '深圳': '94', '东莞': '133', '云浮': '195', '佛山': '196', '湛江': '197', '江门': '198', '惠州': '199', '珠海': '200', '韶关': '201', '阳江': '202', '茂名': '203', '潮州': '204', '揭阳': '205', '中山': '207', '清远': '208', '肇庆': '209', '河源': '210', '梅州': '211', '汕头': '212', '汕尾': '213', '郑州': '168', '南阳': '262', '新乡': '263', '开封': '264', '焦作': '265', '平顶山': '266', '许昌': '268', '安阳': '370', '驻马店': '371', '信阳': '373', '鹤壁': '374', '周口': '375', '商丘': '376', '洛阳': '378', '漯河': '379', '濮阳': '380', '三门峡': '381', '济源': '667', '成都': '97', '宜宾': '96', '绵阳': '98', '广元': '99', '遂宁': '100', '巴中': '101', '内江': '102', '泸州': '103', '南充': '104', '德阳': '106', '乐山': '107', '广安': '108', '资阳': '109', '自贡': '111', '攀枝花': '112', '达州': '113', '雅安': '114', '眉山': '291', '甘孜': '417', '阿坝': '457', '凉山': '479', '南京': '125', '苏州': '126', '无锡': '127', '连云港': '156', '淮安': '157', '扬州': '158', '泰州': '159', '盐城': '160', '徐州': '161', '常州': '162', '南通': '163', '镇江': '169', '宿迁': '172', '武汉': '28', '黄石': '30', '荆州': '31', '襄阳': '32', '黄冈': '33', '荆门': '34', '宜昌': '35', '十堰': '36', '随州': '37', '恩施': '38', '鄂州': '39', '咸宁': '40', '孝感': '41', '仙桃': '42', '天门': '73', '潜江': '74', '神农架': '687', '杭州': '138', '丽水': '134', '金华': '135', '温州': '149', '台州': '287', '衢州': '288', '宁波': '289', '绍兴': '303', '嘉兴': '304', '湖州': '305', '舟山': '306', '福州': '50', '莆田': '51', '三明': '52', '龙岩': '53', '厦门': '54', '泉州': '55', '漳州': '56', '宁德': '87', '南平': '253', '哈尔滨': '152', '大庆': '153', '伊春': '295', '大兴安岭': '297', '黑河': '300', '鹤岗': '301', '七台河': '302', '齐齐哈尔': '319', '佳木斯': '320', '牡丹江': '322', '鸡西': '323', '绥化': '324', '双鸭山': '359', '济南': '1', '滨州': '76', '青岛': '77', '烟台': '78', '临沂': '79', '潍坊': '80', '淄博': '81', '东营': '82', '聊城': '83', '菏泽': '84', '枣庄': '85', '德州': '86', '威海': '88', '济宁': '352', '泰安': '353', '莱芜': '356', '日照': '366', '西安': '165', '铜川': '271', '安康': '272', '宝鸡': '273', '商洛': '274', '渭南': '275', '汉中': '276', '咸阳': '277', '榆林': '278', '延安': '401', '石家庄': '141', '衡水': '143', '张家口': '144', '承德': '145', '秦皇岛': '146', '廊坊': '147', '沧州': '148', '保定': '259', '唐山': '261', '邯郸': '292', '邢台': '293', '沈阳': '150', '大连': '29', '盘锦': '151', '鞍山': '215', '朝阳': '216', '锦州': '217', '铁岭': '218', '丹东': '219', '本溪': '220', '营口': '221', '抚顺': '222', '阜新': '223', '辽阳': '224', '葫芦岛': '225', '长春': '154', '四平': '155', '辽源': '191', '松原': '194', '吉林': '270', '通化': '407', '白山': '408', '白城': '410', '延边': '525', '昆明': '117', '玉溪': '123', '楚雄': '124', '大理': '334', '昭通': '335', '红河': '337', '曲靖': '339', '丽江': '342', '临沧': '350', '文山': '437', '保山': '438', '普洱': '666', '西双版纳': '668', '德宏': '669', '怒江': '671', '迪庆': '672', '乌鲁木齐': '467', '石河子': '280', '吐鲁番': '310', '昌吉': '311', '哈密': '312', '阿克苏': '315', '克拉玛依': '317', '博尔塔拉': '318', '阿勒泰': '383', '喀什': '384', '和田': '386', '巴音郭楞': '499', '伊犁': '520', '塔城': '563', '克孜勒苏柯尔克孜': '653', '五家渠': '661', '阿拉尔': '692', '图木舒克': '693', '南宁': '90', '柳州': '89', '桂林': '91', '贺州': '92', '贵港': '93', '玉林': '118', '河池': '119', '北海': '128', '钦州': '129', '防城港': '130', '百色': '131', '梧州': '132', '来宾': '506', '崇左': '665', '太原': '231', '大同': '227', '长治': '228', '忻州': '229', '晋中': '230', '临汾': '232', '运城': '233', '晋城': '234', '朔州': '235', '阳泉': '236', '吕梁': '237', '长沙': '43', '岳阳': '44', '衡阳': '45', '株洲': '46', '湘潭': '47', '益阳': '48', '郴州': '49', '湘西': '65', '娄底': '66', '怀化': '67', '常德': '68', '张家界': '226', '永州': '269', '邵阳': '405', '南昌': '5', '九江': '6', '鹰潭': '7', '抚州': '8', '上饶': '9', '赣州': '10', '吉安': '115', '萍乡': '136', '景德镇': '137', '新余': '246', '宜春': '256', '合肥': '189', '铜陵': '173', '黄山': '174', '池州': '175', '宣城': '176', '巢湖': '177', '淮南': '178', '宿州': '179', '六安': '181', '滁州': '182', '淮北': '183', '阜阳': '184', '马鞍山': '185', '安庆': '186', '蚌埠': '187', '芜湖': '188', '亳州': '391', '呼和浩特': '20', '包头': '13', '鄂尔多斯': '14', '巴彦淖尔': '15', '乌海': '16', '阿拉善盟': '17', '锡林郭勒盟': '19', '赤峰': '21', '通辽': '22', '呼伦贝尔': '25', '乌兰察布': '331', '兴安盟': '333', '兰州': '166', '庆阳': '281', '定西': '282', '武威': '283', '酒泉': '284', '张掖': '285', '嘉峪关': '286', '平凉': '307', '天水': '308', '白银': '309', '金昌': '343', '陇南': '344', '临夏': '346', '甘南': '673', '海口': '239', '万宁': '241', '琼海': '242', '三亚': '243', '儋州': '244', '东方': '456', '五指山': '582', '文昌': '670', '陵水': '674', '澄迈': '675', '乐东': '679', '临高': '680', '定安': '681', '昌江': '683', '屯昌': '684', '保亭': '686', '白沙': '689', '琼中': '690', '贵阳': '2', '黔南': '3', '六盘水': '4', '遵义': '59', '黔东南': '61', '铜仁': '422', '安顺': '424', '毕节': '426', '黔西南': '588', '银川': '140', '吴忠': '395', '固原': '396', '石嘴山': '472', '中卫': '480', '西宁': '139', '海西': '608', '海东': '652', '玉树': '659', '海南': '676', '海北': '682', '黄南': '685', '果洛': '688', '拉萨': '466', '日喀则': '516', '那曲': '655', '林芝': '656', '山南': '677', '昌都': '678', '阿里': '691'}
