from stellar_sdk import Server


server = Server(horizon_url="https://horizon.stellar.org")


def read_public_keys():
    with open("public_keys.txt", "r") as file:
        public_keys = [line.strip() for line in file.readlines()]
    return public_keys



def balanceOf(public_key, server):
    account = server.accounts().account_id(public_key).call()
    balances = account["balances"]
    print(f"✅ # Balances for account {public_key}:", end=": ")
    for balance in balances:
        asset_type = balance["asset_type"]
        balance_amount = balance["balance"]
        print(f"Asset Type: {asset_type}, Balance: {balance_amount}")


pub_keys_ok1 = [
    "GC5M4PD4OJARJNN24TMZIBNUBMWPFXX2UPG6V3ZAVJWU33LHM7RQUHRC",
    "GDSCDLVS2B7WWW6WVEGFESN4VD55REUSDS5BKUXQQMYVNHOVOZX3T773",
    "GBPTLZBA5AO5LM7LZZBU6G2DBULROCCFBHDQWGUFJ2YBUMBZZ7EYDAJ4",
    "GBNTK7YLWIKRVUMUEZT62R2ABN4NSKVUYBR3M5CGCPXOEL7JNW5VTDAV",
    "GDHTRMARUCLZQBW4YBKSB533T6ZTQKBKC7UXFBLEF7P4XQWUA3RJA4KU",
    "GACSU7SUHXDOZDBMFIGS4S4E655367PDZI7XKE3TQEV26SHKVGRXWPNA",
    "GDGXEL5UQA3WTBYCMTZLOCCYFG77EC26BJZGZI7B65ADNQGYQ2AAFVZ5",
    "GBTGLCUTXNZ57E4SCGCWZDYIE6WNPIQIH5ZQ6K7FTKAYEF7TC6BY5SAO",
    "GBGLJOJG3UP37ATMHDRE66YM7T6M3CNN3DGC2DXV57Y5CMG3CDWPX3C3",
    "GBKLUZCSURR44YN6J5X3MMGJQUQUEEHXTABJO2RQQM63EI33264ONWT3",
    "GCBSD5LCZLKWF7L7ADHTBZAIA7NQQMTUDXFQ5LNNWCIVPJ2UE7YJ33FL",
    "GDIT52HDBGIKLS2DOMUU3HL2D6I5D3TPD772CVGHBLOX3VYZKMTMYFU3",
    "GDQ6KY2LPOOARMW7QDR7VVATNJL3JKKHLRV7TTBL22ALRD7LEU3UZTJY",
    "GBAHLX4ZRZSM5PDPGFKENN77KGY7UEN64JZKUIDTBUVZTJDEL4VIE3WI",
    "GC5EZE7GSHXOTXIHCETXYKKCYGSDXZ5AQWYZRNCQ3BSGVYGXSTN7XH2Y",
    "GCIZTMCCH7K2PKGIFASJO6DVXJYSXX65J2YQRGUERYCSFIY2GVWWM6ZK",
    "GAO4W3XCRHL3GWR7HNTLAYWKVOWVHBTHTLQTBS2THZEV3FEGJGG3FKJW",
    "GD25GY22TP3E3K4LX7HRYTUDBINCLB725TVZFLJZ5LOHDZQQNFBWQG2X",
    "GADYTDRIN2JVHMOZK5ED6O2RKRD5UMR4MZIUBC4EQMBGF5JHOW3BO5BS",
    "GCTKLO2HQ44EPSGANXE6P2HDPUJ2EXAWTNWBUTJJFKXJKBJTSYPNZHQU",
    "GCSQM6TEBMKS4EN6WPCADRZLVOX3KYDWCLOEUE24XCIL7F4LEELEYITJ",
    "GBF7NZHSZYYUTPYVXMAGYODM66M5BYMESE2UYVWY2OAMFHAZKA7BFRNM",
    "GDGUVXC6BQVQC45PSR3QRFLATBNXKK55X47HBO4AMZ3RT7X6JQA65TXJ",
    "GBQNSLUQJSDTGW6QEUZUFIFMHVDMOU3EE7MZJOOXXMILPIYDKQWRORAM",
    "GAQ6GK3XMSKX54RX3TABYKIF3QVMI36R2CZLQ6NX24XGSKVVJ7RVDO43",
    "GCR36L2ZTD2Q2BU4JHVPBKQANRNYD7LSON7ZL2DKQQZYIWLLXOLNNWON",
    "GBGNYOXFMIT7LQ7ZHM7QIJPZEEZGC4QVUDKYKQDMJCPP7QNSHLQSUSAU",
    "GCBKAQ6YPZZ7B54QVHL5RYNVWO2ELPBOO235KKJYTD4SHBOTC5E2BBAJ",
    "GAS6QHYBYLNPRHFJG7KPRKA6PBOF54S2DCJAWETJOKBHIR2VPW5SK6CW",
    "GCSJIPUDSRXQ2FZWNJHQD3SA75XFZEZLWXM3OKT5H3LOL6VYBDMW6MNN",
    "GANJP5SGBKEHKTZLNCE64ZVNF4ACB6YAYRPEHHISMVR2MTQVXBPU6Q5K",
    "GCEWJB6XDH7FQ27NBRE5V2XKZEOZZEKY5NQ2THOIRE3OOI3IYIAOP55U",
    "GCPTP4RPNOF55SZS6QU4EBOYSUBMQWQW2ORLXUQ6B4YSCAMWFJOQDQIF",
    "GDZOBWMQ7UT5O6TB7VVQSBKFIZ2XF7HHZJYOZYXN74ADNFWJX4RE2CMN",
    "GB6ZNYEFGWM3HJDUHYVDPCUTBKKMLS45MOFPXFD5TFEAGLPHWNTYENVX",
    "GDAIUDRBFBATL7QO74S4FU5UHFPLC3TSGZBSNG7IO5NKRHD7IZB6ALAX",
    "GB56VLOCZRVWWPJRHBTA4LPPKLY5KBXFFBIQ52C5XEZ7K57PNV23G6T7",
    "GBDSBC7UJIZNHQNIM4HOYVQUAJLUFRQM475I6HCPMXWSGOXHU5IK2RSY",
    "GCWQ56MPB5YKIQJJIO4XIPBSHTLMYDKOY25IZ7JHWCAKMTWTTA6733HU",
    "GDGOCZS7WPRAENSW774BRPJSEBUPMHJV5IASJ7DEVZXSNJEVWDVWZWYC",
    "GACN3ZU64E4JGR2326YPDS4V5H45YCIXIWWHH3FBCVPWDIZV6SAWS3M2",
    "GBC7BQ72AT6NM4ZJZHRPHZME6F7LWLILTF2WBCJENOF56FGUEXB3I2NC",
    "GABA4GHFGEGNL2XGGRNT3XYCS4HSVN66GVXPOR5W5Y47YW5YESZYPMKS",
    "GA6OQUYZAVYQFXADTR3Q2BURNI5BL5BIV6DZDZWTZRMTSMT5NMYDRNQ5",
    "GB2MS3GZWO5LP4R3PIDROO5TVECOXJJSTM3E3AK727FGIVJQ56S4ZCLC",
    "GCVVXDZACYMPZOTN3NQFTBQFOM6KM2AJ4QSH2A2XD6NTR2GGN5IAN7Z2",
    "GA4WYK5DJRMVFYYC7XJQJHTJSWDESEXTTATXCUF2OQZ2Z5UVJJRYQAZU",
    "GDIIAMB2SGKY7R4AJTJDMHCZZ7Y6E7PSP6ITCQW7WHDXRURLH42JOE4N",
    "GBZXW2GB53UZFWJPJ4R4EU6Z2I4BMCJO3J6NEEBVRO3GJXHOUCGVD2VQ",
    "GDJB7NR2SBY2WN7GQ7M26IE4AZDYVV4X4L3MIWO3W4EK6ITFMJP5NEQX",
    "GCLY4JHRIQMUK4GBSJCZSMPYJILJVZAGHJNVE73X2WYON34AZDSXTU6G",
    "GDPVP4POR2VMB7ECGBGRR3PODQCSKVBSFK55RVKR7VZPYM5YDJZGTZNV",
    "GAAHX4TUAJPVWFDAEYKLT52ROZMYERWSKM7ZIYKT3JZQ6JJS73HRYHRU",
    "GBCRS6L7NTMYMTN6FWTSYXHBZVGLVHK5PFNKX4NCOXNL6733ID35JT7P",
    "GAINW2AEODHBEX5FWSL4EH2QCGPYCTD3VFADKOC7LGR4B2YDBBURBLUT",
    "GBAOXSB7EIM525KORK5Q2AATDVPNTSQMHMWDKM2AXEDHJZQDXOSVXZWM",
    "GANLRCZO4BN6V5DKJGHMTQI3E37MTDMNHDJEEE36CRHH764JEU5PDKIS",
    "GCRAVVNGNDNUVX4YGVE4P6YPXQPAQ75253D6JPTRLY6XG2NE5Q7QAJPH",
    "GCYUWXRXQ5N6Y27MNNEP66TKB2R3GDOS5GX775LW3SYV56TFRPNN34VC",
    "GBQCURFN6FI5JAOJ5UKI2QXL7MX6IFU2V2Z2SZKWSMQ4GQTJOZKBATCR",
    "GDEE7QQXP2UU42HLLE4Y3IXNYC6LG674UKK2IUBIFYBOJMT43VMQKSJN",
    "GC4M27JP6FNGUOLVWNHHPYACU6EQ5HSXSTM76F42BJ2K2H36B4UBYFDT",
    "GBUO5CPASODYD5UG6QSSJBQ6S5SHYEEEWSOFDEI533HI2LWSYAGFOQRD",
    "GALRMDOSAMU3WJVZKU4FNOTGVU44SC4YKNAMXYLZ4QQVVDWMPNJILHLD",
    "GDPN5AK3ZOKTKJMYYJNHQQQQWXRH4KF2V6GNE22DTHTHDMI7EO2IGGGN",
    "GA7DEVEAG4ZLEB5I32OFLQRRE5DBHWVHXYOY6YMP3U3GDX3DRK64VFWS",
    "GC3LUHFYEAYR4EFO67HLMUTVPHDNPRG3FHK23VCO4FMDUYW7OROMQ3QY",
    "GCODWLGMBYVQ6T37SZBMVMXSTYNAPWOUDBKYKJ2Y57CRZPBIALP5E5FL",
    "GBBIVZN5N7EMYMQHZL4ME64GWDM5REJDLFBDET7KLIIA6GQRQVJ2IQWE",
    "GCVHUYV3QH45HH3U7CUZ7VC65EWHRVIAEOCYNMSM6272IMVX4SEB3TRC",
    "GBMNR3LMWISKKMTHPUUXNQCZR3IXLAGIMMZDMDFMJBCJZ5S2UEEVMSRS",
    "GCRNDDMY5C7AECTHS3LLYLANUROL522FNN7S3IRG5IMWR4JQP4IUJVQX",
    "GA7UJRGMYAPOYMIKE5JXVVLPYGDE3YB26YJIMBARNL43KYGFIF3Y24ET",
    "GBHLXIV7WZ6VSFLTLQFTFSZ7DKTZ6K7LFXJCPJQ2MJXTQVW3FZCMVULC",
    "GBVF7TWTW3FHFIUGNIJAISGBD54V6GBSEWTIPSE7J2UBUUOJ2Y6V37JM",
    "GB4C5REQXWV3FMTRUZYFVEN2SCSTQJDG4U344HU77EH6I6VPCQ2OLNM3",
    "GDWU7KASQ6EOERJ6V56MRMWWMJTPW32U5YXLEKX2W2XVSB6PXGURSI7T",
    "GCMZNRRLF5VRE5EAYGHUENOITBC3GY5ESH5BBVLWZBFF5LV2URM5UMRH",
    "GBAU7KRKSIVNXIJYAODEFKYXS7VIUSR6XFHB4ERPSGEE7EGHA2ODY7ZY",
    "GA3E5XMZEUWWN3PT2LAV2YQKBTMXF56KPUNE46ZLN3OKXOF5ZMHUVSAN",
    "GAHOBVOXRIN2VSWA57GMJWFXDXDOMOXQJRFN33JK3II5ZXA7Y46LKCDT",
    "GD7V32ZRFQ6Y3XZLYUK43TYHI6D4P6IMZNZKHLCOSRGV6HSUWVCSQZYQ",
    "GAPUC54IAVY7QQVR2SDWWREZXLEUZERSE2PFXCP4XCQ4KI3INORFLCTN",
    "GAGYAZF2UIXHDWOOWAZZFSS4A5KAFF7S42X3CU4E7URS6VHWB5OZ67FN",
    "GA5BAAVBXPMMUZROSSFV2QTSMZ5OY2YBOMQ6URVNOK43UKF5SAA7Z2O7",
    "GDXSK5FVZEQ2KMHPMQD4VNQXBS3FLSNAIRE246CBYX5XLDTQJ4B5AEFA",
    "GDZX6UF5SRSGQBLKTPPY7TKGHHIHXM4TTPOXWBWNJOAI4UOHIUZQEAVZ",
    "GAGL327YR6JV4WUOO6TWRXB3UYWGAAOGGZAUKAJFTJDVJT6A4PASMRMS",
    "GDRD4ZEIJIA6RM6NJ6HK3NDN2YGHDLUKSPVJ4MNOJNQMG3MK7ZHPEJLB",
    "GC2CFGADUSB2USEKZA3OLTYXKGLOGS5KFT7DRLI6MH6VJUCEQMDLJQ3W",
    "GBQAAEFKHYRI4JHZCKBKABY3XYC2XT6TAXMFCGNXCGZ7NSL7XAJSC6IQ",
    "GAGMNZ5E4B2T4WMQMFKPXNUP323V6VD57LJKOHNEDZABR4WES5FBGCDC",
    "GD7D2Z6LQ5F7FDLDVCKPSGNXS6REDF3ABPM2ADKIZN4PIBWDKKQH4AS7",
    "GADYTDRIN2JVHMOZK5ED6O2RKRD5UMR4MZIUBC4EQMBGF5JHOW3BO5BS",
    "GCCKEXD4JI53RPQDLHUKLKFTCWVBLSS2RVLBCKNQEJYST3CGP3ULFE4R",
    "GB6ZNYEFGWM3HJDUHYVDPCUTBKKMLS45MOFPXFD5TFEAGLPHWNTYENVX",
    "GCMUASIHX2JBY2FJNRTXVEGDYNCWWZHI7CLE7DCYIYRGPK3Y4YBNHX65",
    "GBNZ7K5FCYNH6NI6QDGVVCSUDKWZCBOTXDVHO66WJIUDLZK4XU2P27VN",
    "GDBEGPNC6PPJSKNO3O4JWQZQQT7GD6IQOUYJV2I7NCOUZ2A4BZNBRHRO",
    "GBGBWLYRB3UDFJRQALJCXLMCV3OXFLWSX4MOZRUM3CIWZBO55YG2CCRD",
    "GABSUOAFU3UDTV6XMBT7D3O6K2H4XW3PGYSQAI5R7HP7JHUOUQHDSCVB",
    "GAREQKTGVCZIRYBGBLFOV7BM47CTPJRPPMCBQKKCW5KGPS5AVFUDOEIB",
    "GDIZIJZPT5N6GAWGUVMEZDRFR7VGHJSLXMZFX7KMNGU7X7AXRGVXBWEO",
    "GDFO7IDGWQNVHI5QHVJDXYQR3T7BZOD3ZYXA65U7TAIPKF5VKSLNQZVA",
    "GAFASLN5AWEKSDNXLRUH525N2FSNTBFLFG53EPUEOKRQCWUI2BLT5JES",
    "GAKC7ZYTIRHDNDBZXYNURIVZBPMCFHZCUSLURJRHUPAWJ5W4K6JEUYRS",
    "GD5D5EY3DOBE7P5NTWWCRBJIFIB2I23DHNKPYDLINX27DQ53H56KZPPN",
    "GAQD5WQTZ4GV5JGEMXRIPNMNOTFTC7KOOEW4KKVH4ILQVHAF2VKAEDTH",
    "GBYBAUIDYG6YR3BE52A3E6SWZR4PH5PQOXTK7BKXIUNOUEMTKS4JP5C7",
    "GDWMIUSTFBSHKXGHJOX2H6T4A2IQ2EFQO4QP25QFXCJT3HHN6ELFYSVD",
    "GBZKQVIIM4744EBCJS6DFUP273S4AQUAWIVRKF4CN26D6BNLQX36ZQE2",
    "GB3UVVNAB4NIFUWVHGWGINUW6RRIQ7Q5UGHYHFQCAKD43EUQRONWPVIL",
    "GADFNPSDVL7XSIYCUDCNI4E47NVEKY7E77BACH2I57NQTQIM2G75KUTP",
    "GB2BBGHVOHUANZOB7E3B3HOQXZOJL26JKQFFNWFCWKSNPOGXEHMBVPUQ",
    "GB4E2QRBMJR36SBXGBKYTX3KMTJRGQ6TSUGLDAPCCU5ZHVA6FU7RUXEA",
    "GDGZUETRO62IUELILU35C26BVJ6S7ULY7TGQVCNXN442KI7FIHSWIRO2",
    "GDBO5PI7NXTGX2RZBZHCBUK4LXQOLNVCQPD36WHHIP6D4TK66Y2HRV26",
    "GDX4C4ACE4AKYUWW5O5AA3ZEGD5S2SF7N56MHMFYHNOUG2IXZOOH6HUE",
    "GDKB6HGBTXUMZKZV4BTZQZT5MXENIHUL6X6F25EWKAFDLMG5F7S6HXAO",
    "GA3FPWLOAMYEXSVNMP323BF5MJQQG32BQ5PN5IJYG56D3JUOGTFHIF5N",
    "GAL6HUZAEJ54XL3O6PSAIUMROFE7ITUWKGHKMONLQ4SIVLSAIPWJ6O2Q",
    "GBYW6J26N4JELTUN6WZYAWNOKIG5YAI5O33WBLH57K4TJXPX4MHUGSZC",
    "GAS2K6ESDZUMREGMYIHAZGAGVB4443PVK5UEJYJWTVXYCUKF5TVWVSS3",
    "GDTLVGKUY2OXG43WFJYN2JAZKKER253IVQFAJZXPZMRNVYPK4CKNZ6KT",
    "GDUX5WSDQQALNJTNMZC5EMZTCUOTLC3LH4ZMMQZ3J5Y6K6RXDCW5U747",
    "GBB6IIYOJ3QHN246XTDF2ZZ2Q7JPSOJLKED6IZJD6XBEUNABGKEB6UIB",
    "GC3JS5VRNMIPPASSJGXS72UKDAHDUWLIGQ5EN467F5PUABUWSPNLF523",
    "GATXRK6LD6FK6LYEJ4ZLZPPBD2MMHTYDQ3U6BNLGBC4M3L3QCC3BJIAQ",
    "GAZ6ULLYUHOJFVHT6MY7WFAN2GBWWCWFEZWLOI5HKTAAI4MCSDYTJYWR",
    "GAEGZBKR6HYQLDJ2CF3QFE5PIA4W7Y2NR2WXM45PUPAQTNT62L3EYU4V",
    "GBMXKNM3KYHOTKRHC7WV52UB3IJH4BU3FPQYWYNQ44D2J3NSDUXW42B5",
    "GBTVUE7ACSNENGTUE3LKGN6MWQ56SGKMTMUP5GMCLUEZWYIKYFE5S357",
    "GCRMOIV5JF4CGRRQPOV6BYZAXTLEBUKCBUNYPTTNXSWRX4U7BZPGNBRS",
    "GDJTWIWTMQP4J4LIESFLBC7NAGW2HH5LWEDOLD4PYMUD3WQ7H462CEFR",
    "GAHIS47WJTR6NXH5UQESWE2E7JED52YLORRVPFHL3QFC36W67OZ3YCJ4",
    "GDW6RIWBCFLSSTVPOTOUUJ4W6QV7FZKK7MSAOROCPTPEWSKSDZ246UUL",
    "GASBS5FHTGFFMYTYYIITOTX6A4ZG3J55BJGOTSQXCRDTIRRZBA6J63MG",
    "GD6GPJCOVYCEPYM55GTEHUHXWH7BC7K3Z6QKK5Y47V5OBRBYNLNET4JB",
    "GAMFRP7LKU4SOIQKSTWGFACBHXXCIOKE3CHAFANIDU4ZZ66WR6LM6LBJ",
    "GC4C4ZIJGWKNCF6W7H7AKZ7IGAZ3ABL54FKDS25EX6MP2S3N2OSVPJUW",
    "GCOECVGLEBRZFVRFEATWT7TDCPXACUTNSPMCVE3POKHYRTBOOHNEOOZB",
    "GAJF4HIDK2SOHMCP4Y7RYW6IOOQLYAIUZYUIZBGLJA7LAFRCZQIUXCSF",
    "GD4WWUZ247STNQUIKYMUZWGIWBZ5BYLLQ2BSZEJMIJV6RQQEY25DVCHR",
    "GCNNKC4CAVK6QZ4KEA52I6EZ24566FCVDM5EUDUAQMZXBBK7GO2ZSSKU",
    "GDBFPN4BB6TK3YYHDXD5Q3LUVLX3ZNBDYN6H4NKVVHHMJLXLGE5BGLXL",
    "GBOQNUERPLE6NLXJWVIHY6ETA3T3HQMU3YBWXJUI5YLED72GJJDPSPFT",
    "GANSVIA3OR537VRFFB5S3Y3HA64FMNPJF4YNVLS7LHEBYCLXQ57J3QDS",
    "GDNDGK2YAFS4HB3JILE36VXMCQMIHF3RK45DJEFKYDAFI7CTFXFXPPRI",
    "GCSL7N3K3HNABE63MSHWZFRHJ2UGN6C7USQ7KEL3KGNX3BPZ4ZHCPRBG",
    "GDSGKFLEGCRLWEAHSX7DWECMWLSMUR7SFFP5P2RLP5FW262TOMQVWOIM",
    "GAJNOD2SBB57AMK435GAXXHJFAC2LH3J3D7TXSYKVYT5MAHJ3X33XF5I",
    "GCZIWOGOVWQHDY7J74YZGXMLQ3G6QO7GQWD2U4SIC4C37353F7CWFP7G",
    "GAZUF5J7D2BWMPBRPPO7N4LCODV5PNUMKDPLHZ2WLMGFJYKTMJBWH2ZT",
    "GCRH6EHCX2LLG2SZF6PF2TNPKD3QVZXX4JRCVJWK6JLZPP7O3Z5FSLV7",
    "GA5APZYZLAWYWOVHYGPAR77DXEU6UATLUBTALWLUSXS5T2UWM237YXG7",
    "GBV6QI4WLBWM2CTL4Q5ZG6CDYHOULCNYNRV4DLKRCCU7HIJUIPZJXF2F",
    "GB3MQUJVI3CVJKXYZLBRXMIRA4RHDIDFTP3NM4S2T4AFDNOJMWRMJKK5",
    "GBGIRYFP5JXDQ6GMYGLNJLJMVUYYD3PP44PW2BOMEIDD5JDXKPIYVVIV",
    "GDP2XH67DD2ZCTBZFRKAQGV6EM4QWE3VQCLNMM62RRYGILYZ76YWLFV2",
    "GCJCJ54OPUXXFIJ6S3QCROZP5CS2MF2GZR45LP5SK5MVBKHQ6N5AWK2P",
    "GB227MAPSVM2PJBRLHW32ZWQYFCIEJ5RIJ3KTC2AN7GRY6IHLNUO5LCG",
    "GDV5RS2MJXUBFYIVSVQEVAHXN7C2Y57PHT3A4R73R34UNIIH5CZGIBEE",
    "GCRJM6PDA65QHK47JUQONF4YBY5CM4IGM5QBKJAEMYJT4YMXOFCUMG7V",
    "GARLTYSD5YHC2HQKTEIPFBG46BGU5475LRRGP2ZSAGTAAIUIGEG3L4UK",
    "GAY4PRB2OTTLRPBE2FKKFTOXT6SOGZAEAHPIQAV7LHGXRBR6326T4LR6",
    "GAM7KUP57ZJISPSIUMB7LIQWHTAX2A4XYMZQC3DSNHNPCFMADBZDI7CQ",
    "GAAFFITODLK42PWE2SHEPUHAWMMN7IASSDQ4EHZHX7ODNGYYUNWA2FFM",
    "GBVZ5PFTBCEOJ4MM2C7TT2CBLRFR7L3GUCCBBSWRQZLP6PXAJBSZNFYI",
    "GCVFLLGZFGQYCJSD2SUWJK6HSYWJD3WUAYV4QYOAMORFF4SNW2P5RSBK",
    "GDIIB26NUDUEKVO6WGNGJ5UMAFMNAXTKJSWWB7UYRMETJ2HQCX57RSYE",
    "GDA7UGSLM4BPPI7PZ4BT7573VVY36XXH3RC3NVD4Y5GICO7Y5DYP5C2W",
    "GD6UQLYRMVPPJ7DU4HE4QFGSMGZMVKFRQHIYS2H46POMAQ3A6ZMAAFPS",
    "GDSNWT67M2H7WUSQQGA4IMIRVGYJPJ3WCFYXTOZLB5CYEXNVWALVL47L",
    "GBSW6NZ6BKDHGJFF3YVYNOXIKOUT5734QOEQZRRWGAN3OA74GOQ7EJHH",
    "GBX7PB2H4QJDTAQG5ZD3TX7EDGD7S5RDTGT4KYXFAERNWFB7FHDTBGUL",
    "GCKGOVVJPEUERQFCBVTZRC44OOZARMI7HL5N2IUNBDLQBNEBPAMEHPGC",
    "GDFXZ3QWH7ZT2X3RPRHVPTCELM2UKWWNYK7S7O4O3LPPXGIZAP7YF6RZ",
    "GCTRZJAVVU2FJMOL3DW2DCUUIEGXXVKUW6IIFFCKMVM6SIXFKNCWBBSN",
    "GBGZEA5RU4Y2MF56QL3GDDPXABBNYRI4C3DES6UTWHSBQJ7332YXOHFL",
    "GBQECXUS5XBXJYKM3NLLKO4ATSLWIZQF3D24IIOTOJA6O7U4HSU44YBK",
    "GDU7GN6TJ3XH3244X3ZWLH3E5AOWQNNGXIMEZMNGYFGKT5G5MIEGNET7",
    "GA3PDNMTSXDT7AT46GRUHUZWX5VGPIG4WQHTVH4Y6UP4QSPMOSJ3IR5L",
    "GD6LJ6MNDDTZTN7T2AXCQUCT4JG7EXTXS4FTQJ4YBYMU2KYKDXBHQILR",
    "GC3MAQPJ26S26XW5BBRDQT3SLMKIOEA53JTBBTWF25555OGXWFBPG6RX",
    "GC2MGTQNNYMF7T2FMXYOUYRIV2JH4HCWK3C6UNC56AEJOQMRXJDH6JQD",
    "GBEAL3V422IYUP5XRBRJPBBQCXE5W7MCT5JVKGM27XTYHO6ZPGNW6UDN",
    "GCNDCVIX4HUZ6EMLOCZ222N3SY47AS3P6IEW2H5RZWP4I7CCIQSVFWL6",
    "GAAFUAG5TNXPPUXHAIQSBCSOZNE6RAL6VBBXIECKERJWW3CTWV54HZSA",
    "GBSPSIAKDMBUGBIMLUWVXPHG7227OXBYFGD5CFCGVJX3IHL7YIB2NBWR",
]


# public_keys = read_public_keys()

for public_key in pub_keys_ok1:
    balanceOf(public_key, server)