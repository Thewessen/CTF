#!/usr/bin/python

# (from previous level)
# An example of a polyalphabetic cipher is called a Vigenre Cipher.  It works
# like this:
# 
# If we use the key(K)  'GOLD', and P = PROCEED MEETING AS AGREED, then "add"
# P to K, we get C.  When adding, if we exceed 25, then we roll to 0 (modulo 26).
# 
# 
# P     P R O C E   E D M E E   T I N G A   S A G R E   E D
# K     G O L D G   O L D G O   L D G O L   D G O L D   G O
# 
# becomes:
# 
# P     15 17 14 2  4  4  3 12  4 4  19  8 13 6  0  18 0  6 17 4 4   3
# K     6  14 11 3  6 14 11  3  6 14 11  3  6 14 11  3 6 14 11 3 6  14
# C     21 5  25 5 10 18 14 15 10 18  4 11 19 20 11 21 6 20  2 8 10 17
# 
# So, we get a ciphertext of:
# 
# VFZFK SOPKS ELTUL VGUCH KR

# (this level)
# Frequency analysis can break a known key length as well.  Lets try one
# last polyalphabetic cipher, but this time the key length is unknown.

# (great article)
# https://inventwithpython.com/hacking/chapter21.html

# found text
found1 = "SXULW GNXIO WRZJG OFLCM RHEFZ ALGSP DXBLM PWIQT XJGLA RIYRI BLPPC HMXMG CTZDL CLKRU YMYSJ TWUTX ZCMRH EFZAL OTMNL BLULV MCQMG CTZDL CPTBI AVPML NVRJN SSXWT XJGLA RIQPE FUGVP PGRLG OMDKW RSIFK TZYRM QHNXD UOWQT XJGLA RIQAV VTZVP LMAIV ZPHCX FPAVT MLBSD OIFVT PBACS EQKOL BCRSM AMULP SPPYF CXOKH LZXUO GNLID ZVRAL DOACC INREN YMLRH VXXJD XMSIN BXUGI UPVRG ESQSG YKQOK LMXRS IBZAL BAYJM AYAVB XRSIC KKPYH ULWFU YHBPG VIGNX WBIQP RGVXY SSBEL NZLVW IMQMG YGVSW GPWGG NARSP TXVKL PXWGD XRJHU SXQMI VTZYO GCTZR JYVBK MZHBX YVBIT TPVTM OOWSA IERTA SZCOI TXXLY JAZQC GKPCS LZRYE MOOVC HIEKT RSREH MGNTS KVEPN NCTUN EOFIR TPPDL YAPNO GMKGC ZRGNX ARVMY IBLXU QPYYH GNXYO ACCIN QBUQA GELNR TYQIH LANTW HAYCP RJOMO KJYTV SGVLY RRSIG NKVXI MQJEG GJOML MSGNV VERRC MRYBA GEQNP RGKLB XFLRP XRZDE JESGN XSYVB DSSZA LCXYE ICXXZ OVTPW BLEVK ZCDEA JYPCL CDXUG MARML RWVTZ LXIPL PJKKL CIREP RJYVB ITPVV ZPHCX FPCRG KVPSS CPBXW VXIRS SHYTU NWCGI ANNUN VCOEA JLLFI LECSO OLCTG CMGAT SBITP PNZBV XWUPV RIHUM IBPHG UXUQP YYHNZ MOKXD LZBAK LNTCC MBJTZ KXRSM FSKZC SSELP UMARE BCIPK GAVCY EXNOG LNLCC JVBXH XHRHI AZBLD LZWIF YXKLM PELQG RVPAF ZQNVK VZLCE MPVKP FERPM AZALV MDPKH GKKCL YOLRX TSNIB ELRYN IVMKP ECVXH BELNI OETUX SSYGV TZARE RLVEG GNOQC YXFCX YOQYO ISUKA RIQHE YRHDS REFTB LEVXH MYEAJ PLCXK TRFZX YOZCY XUKVV MOJLR RMAVC XFLHO KXUVE GOSAR RHBSS YHQUS LXSDJ INXLH PXCCV NVIPX KMFXV ZLTOW QLKRY TZDLC DTVXB ACSDE LVYOL BCWPE ERTZD TYDXF AILBR YEYEG ESIHC QMPOX UDMLZ VVMBU KPGEC EGIWO HMFXG NXPBW KPVRS XZCEE PWVTM OOIYC XURRV BHCCS SKOLX XQSEQ RTAOP WNSZK MVDLC PRTRB ZRGPZ AAGGK ZIMAP RLKVW EAZRT XXZCS DMVVZ BZRWS MNRIM ZSRYX IEOVH GLGNL FZKHX KCESE KEHDI FLZRV KVFIB XSEKB TZSPE EAZMV DLCSY ZGGYK GCELN TTUIG MXQHT BJKXG ZRFEX ABIAP MIKWA RVMFK UGGFY JRSIP NBJUI LDSSZ ALMSA VPNTX IBSMO"
found2 = "GLCYX UKFHS PEZXF AVJOW QQYYR RAYHM GIEOG ARIAZ YEYXV PXFPJ BXXUY SLELR NXHNH PLARX TADLC CSLGE NOSPR IUUML VSNPR RJMOO GMLGU JHVBE QSMFI NZDSK HEFNX KSHGE AVZAZ YQCQP BAKPC LMQGR XXTYR WQSEG FHSPH ZYETX FPVMX PBTWV XMLHM AZXYG EQLRN IAPOZ CXIAZ MVMSL RVNZN SKXCL RNJOL XXSCS HYMYK ZCWPR XNWYR ZJXUG MASQC ELRXX DKWMY PLUGL KHTPR GAKVE WRCEI KESOV JPJGH XJYRE CEGAE HDIBQ SEZAL DAMZX UKKZR EBMIR TLLDH MHRNZ MOOMP CIFVX JDMTP VBGWZ SHCOI FZBUK XGZRF ZALWM JOIJE BUCMB PSSZA LMSYN LJOMO SXQOE ZVTUN HGCXL YMYKA GEWQO LHQIC LFYKL TOPJL RQOMZ YFQNY EOMFG EQCEG NXYVM IPEYG KNOVB ZKXKG UOPKC PBXKF DLCAE FYXUQ IPDLN QBUQL GXWRR YVEXM QMGOG JREGY WBLLA BEULX NTZSO SDDLN MZFGV YATRX YSKTN TRTNT AKRBX YQJRS OKQHE FXTAR IPWMX KTSKV EPVFU KAYJB ZKGNX YOAGW POKTW KGIPX GUVHV EGDXB SHYBS UOVNC XYIIQ DMEOY ARIUP EGNXY RSJOW NTWAR IUTRQ YXACX MWIEG USOJY TVGNX ASHCH MYRLL BZCAV RZMFX MAPPL GMHLS SEXJU BUDLC LJGKK UYSLD MEHXK CMPTW UGESX SRRSG UULNX GWPAO ZODFS EMJGG AKFCO VBUFH XHYME EHXYK RBELR TUYOE IQEFZ LPBCC DWVXM OKXUL CFOKP PCMFT YKTZO WFZAP UGJYV BRIAZ ELWEL DZNRB ZOELO LBZPH DIPES PUGJY VBAYY RHMPK CYXYK FHXWZ ZSGYB UMSLN SEJRV EAGWP SOGKK JGYIF KTJYE JQMEK LPBJC EGUHT YLIPE SPUGJ YVBDX VXTIY YRELR XXUYA DZVPU GJYVB ELRIH UMSPO FRJVO KQZPV OKBUQ EJHEL YTZCM EYIQZ HHZEQ DIAMX YLCRS IZGBS KRBAE FYXUQ IPDFL ZALWE GWFRO GNKPU LCFNX HFMJJ AEGIW OHSAJ EUFOO EBESS UHADL CCSBS AHNXF PSQJB UDIPP WGLHY DLCPW GGUSS WFXIA ZHMDL CCSLG ENOSP RIGNT AKPRS SHMAI EXMYI XOGKY JKLRJ GLZOI LESTU BUDSG EEYRD PXHQL RQBTY SIRTI FUYTO RALQR UNAYJ GEGBT LLAYC YXYET UYXFP VQXTD OVYYH GCHWY VRPVF GGKCI TPVNR FHSHQ LRQZA LVELO PNJRD OVCLP YRHPD IPTRT HRHMG GOIAZ TAFEP TSHYI VSRRD SSZAL BSYOF RZPLO RRSIP UGJYV BLRQZ ALMSD QIRXH VWAFP RNMXU DPCXE AUYZS BRJJB XFHVP WOVRY LLNML LFEUP UCYGE SSIEV DLCDT EKMAI ACWPJ UKULY RGIEE PLVPI PTGCB ARPYC KRYJB KVCNY SLLHX HJLVT KYSKT QESGN XWYGI PXFVT ZCIBL PBTZV XLGDA NEMVR MQMVR GDMKW R"
found3 = "FIPJS EJXYV CYYHZ KMOYH GNEYN XSYSI PHJOM OKLYY HBTXH MLIYI RGGKK PMFHJ GMJRX GNOVT ZHCSL ZVBAL ZOVKZ RHTWL BLGDJ YGIWO HULMF ZVVKX YDXUU NNRMR AMGZX KSXQR VNBBA IELOP BTZLF MRJET GBUCX RSIYK OPDCY YHRBT UOWAP RPKHM DLCMV VYDMS VCSIU GWHQS MOPRM TUNAY DEYOM AVITL MAUYP DJMCL VYUYY ALDXB IDPXK QQMGZ XKCPC PONTW JVSQP EAJPL BIMQE SOGLD IVEYE KAPCW FZIFG GKLYA VPRYM VYXFZ YTNIS KMLHI EKMYS QFPAB XXHXS BOPVZ MSOWJ PIXIK PCTDW EKKGD SKQPX GOGNF IPJGY ULLDS FTWUK TKGLG NLJOZ PDMQE SOKIY OWSXI QCTZW EBPSS NTPBF SEAUO VOVSM VIQLT YWSPP EFZAV EKFTX JKKLC TSYJE UFMSP YXIAZ LVPWG WOBXZ SKWQS MFRBU ORRSS HMAUY XMQES OGLXI QDMAG VJYVB LRPKP PDLFT WFZHJ UMLRW JGLHC AFTXR GLARI RZTFU YARIU LZRYM OKXZC SXKNW YRRSI AKBNR FMFVV TZIOE ASSEZ ALCTC NOFUY ZKMJE LNZZS SRRPH VTMOO WSYPV MAAPE PLXFK THPEA PLNHB AEEJW CFAIW BIQDI QGGKA YGPXR JPHCW RTPYR BNRXC OYCAG KOVRS IDATP XXUTK OETWK MPZJZ UBZDF PTKUZ XFOWR SEGOM TEWRS EIKVV CXRSI VXHDX IPTRL KTYCK MYIOE LVWIN LMAYM VNVGW PGUMO OGMXT BYXKK RBCIF KKCOH CITEK LZSSL ZJGKE SCSLD FNTDO OLYOE UKTSD LWNSY UNYSR FTWPN XLUWY YHUOL MKGCE LBAZO VMLPH OUKLP IUEVN IXZYJ YYBVK MFLYR AIENT WCXFP GBTYP NILEM NRUHM LCWSE IELBO QTRGK ESCSL DFNTD DOVCA VVTVP ZEJWC BIVBZ MCOAV ZAARI ALVRY HMYXF PVCKH WVIYY HCKKO KTQDI PUGKR ELOGN XXZVM IPWRI HUNLY YHPRH ARIQN SZKXH CMJJS SLTUN SLNSZ VELDM LRLVY KLCIK MPNTV LDSYX EACAV GEQDM GZBUQ JMCLV YIVBX PLMGS KSYVP JHEUI WOHMQ JGULS OINEL RGKYS ZYWSS NBZLV CLOSG LABSS DIQNB TKRBS IFGBK DSRSI QXTDO VYDLR SHCOH FTWPN TPBXM TXVCB ZREAN SZSHK KXGZR CXXWK VCOJB XTFYY LRPNJ RDRSK LCPUF LRIPP EGGGF DMKPX BJTFC LCXEL GLRPS PXVWG KCSWJ ZVEEH YCLCX ELUGS IEQVJ BXTNO RRWIZ GGMBS KEIYR LVXWZ LRXVE LKWCE SYKMT OOLZA LKLZS VRPPY YHUCF YYOVT EVXHM YWVXR LCCCD WVXPL RETPS SZXUD MKPWG NXOYR MFVGU XUDIP EEVTR VEVEP RGRXT ORGYX UKBYD VYGIY RBUQF YNOJG KKCEL OJBXP HBHQM IGCBE DPMYH BTTUN TYCMF YBYKZ YDXQK TSYJR CEIKE SSRED MEOGA OPJDS AGGKM SKAEA ELOYY QPCRY PLKVC BYVZX HPVCY GUNHB CIYDA RREHC ELPRT RBZRS LPCRY LPBRM EQHIA PXXFP LNHBA YJQFG UZKHF IJWMA MRVEV QPPSO MOSRI DMETH AYJJL XREXH BWGEM FLBMD ICYCR GKZCM LNIJK LPXGC TGNSX SKWRQ VBSYY KRAP"
# The password for next level
krypton = "BELOS Z"

def group( string, number ):
    string = "".join(string.split())
    return [string[i:i+number] for i in range(0,len(string),number)]
        
def rot(char, rotate):
    nr = ord(char)
    if nr > 64 and nr < 91:
        nr -= 65
        nr += rotate
        nr %= 26
        nr += 65
    return chr(nr)

def freq( string, substr, result=[] ):
    try:
        i = string.index(substr)
    except:
        return
    if len(result) > 0:
        result.append(result[-1]+i+1)
    else:
        result.append( i )
    freq( string[i+1:], substr, result )
    return result

def block_freq( data, size=1, shift=True ):
    def do_freq( string ):
        non_white = "".join(string.split())
        diction = {}
        if shift:
            blocks = [non_white[i:i+size] for i in range(0,len(non_white)-size,1)]
        else:
            blocks = group( non_white, size )

        for sub in blocks:
            if sub not in diction:
                diction[sub] = freq( non_white, sub, [] )
        return diction

    dictio = {}
    if type( data ) is list:
        for string in data:
            temp = do_freq( string )
            for k in temp:
                if k in dictio:
                    dictio[k] += temp[k]
                    dictio[k].sort()
                else:
                    dictio[k] = temp[k]
    elif type( data ) is str:
        dictio = do_freq( data )
    return dictio

def freq_analyses( data, size=1, shift=True ):
    diction = block_freq( data, size, shift )
    total = 0
    data = []
    sortdict = sorted(diction.items(),key=lambda kv: len(kv[1]),reverse=True)
    for a in sortdict:
        data.append([str(a[0]),str(len(a[1])),str(a[1])])
        total += len(a[1])
    return data

def calc_factors( integer ):
    fract = []
    if integer < 2:
        return fract
    for i in range(2,integer/2+1):
        if( integer % i == 0 ):
            fract.append( i )
    return fract

def calc_poss_keylength( strings, substrs ):
    diffs = []
    factors = []
    result = []
    for string in strings:
        for substr in substrs:
            f = freq( "".join(string.split()), substr )
            diffs += [f[i+1] - f[i] - 1 for i in range(0,len(f)-1,2)]
        for d in diffs:
            factors += calc_factors( d )

    result = sorted( set(factors), 
                     key=lambda k: factors.count(k),
                     reverse=True )
    return result

def compare_english( string ):
    ENG_ALPH = 'ETAOINSRHLDCUMFPGWYBVKXJQZ'
    string = "".join(string.split())
    orderd = sorted( set( string ),
                     key=lambda k: string.count(k),
                     reverse=True )
    print orderd
    score = 0
    for i in range(len(orderd)):
        if orderd[i] == ENG_ALPH[i]:
            score += 1
    return score

def column_print( data, head=[], nr_of_rows=10 ):
    if len(head) != 0:
        data = [head] + data
    column_width = max(len(attr) for row in data for attr in row[:-1]) + 2
    for row in data[:nr_of_rows+1]:
        print "".join(attr.ljust(column_width) for attr in row)

def block_analyses( string, number ):
    blocks = group( string, number )
    letters = {}
    for i in range(number):
        letters[i] = []
    for block in blocks:
        for i in range(len(block)):
            letters[i].append(block[i])
    return letters

def vineger_decipher( string, key):
    string = "".join(string.split())
    result = ''
    for i in range( len(string) ):
        k = key[i % len(key)]
        if k == '-':
            result += '-'
        else:
            result += rot( string[i], 26 - (ord(k) - 65) )
    return result

# lettrs = block_analyses( found1, 4 )
# for n in lettrs:
#     chars = lettrs[n]
#     analyses = freq_analyses( "".join(chars) )
#     print "letter" + str(int(n) + 1) + " in block"
#     print column_print( analyses, ["letter","occur","indice"], 5 )

# head = [ "substring", "occurence", "indices" ]
# print "found1:"
# data1 = freq_analyses( found1, 3 ) 
# column_print( data1, head )
# print "found2:"
# data2 = freq_analyses( found2, 3 ) 
# column_print( data2, head )
# print "found3:"
# data3 = freq_analyses( found3, 3 )
# column_print( data3, head )
# print "total:"
# total = freq_analyses( [found1,found2,found3], 3 )
# column_print( total, head, 10 )

def print_poss_keylengths():
    print "possible key-lengths:" 
    keylengths = calc_poss_keylength( [found1, found2, found3], [t[0] for t in total[1:4]])
    print keylengths

def score_english( string ):
    # f = open("dictionary.txt")
    # words = f.read()
    # words = words.split('\n')
    # f.close()
    words = ['THE','AND','THA','ENT','ION','TIO','FOR','NDE','HAS','NCE','EDT','TIS','OFT','STH','MEN']
    score = 0
    # multiple = len(string) / (len(string) - string.count('-')) 
    for word in words:
        if word in string:
            score+=string.count(word)
    return score
    # return score * multiple

def convert_to_key( data, ii, oo, length ):
    blocks = []
    keys = []
    for string in data:
        blocks += group( string, length )
    for b in blocks:
        if ii in b:
            key = ''
            start = b.index(ii)
            for i in range(start):
                key += '-'
            for j in range(len(ii)):
                key += chr((ord(oo[j]) - ord(ii[j]) - 1) % 26 + 65)
            for k in range(start+len(ii),length):
                key += '-'
            if key not in keys:
                keys.append(key)
    return keys

def try_find_key( data ):
    # Find frequent occuring 3-blocks
    freq_an = freq_analyses( data, 3 )
    common_encr = [e[0] for e in freq_an[:15]]
    keylengths = calc_poss_keylength( data, [t[0] for t in freq_an[1:4]])
    common_words = ['THE','AND','THA','ENT','ION','TIO','FOR','NDE','HAS','NCE','EDT','TIS','OFT','STH','MEN']
    poss_keys = []
    for n in keylengths[:4]:
        for e in common_encr:
            for w in common_words:
                poss_keys += convert_to_key( data, e, w, n )
    keys = set(poss_keys)
    for k in keys:
        score1 = score_english( vineger_decipher( found1, k ) )
        score2 = score_english( vineger_decipher( found2, k ) )
        score3 = score_english( vineger_decipher( found3, k ) )
        tsc = score1 + score2 + score3
        if tsc > 9:
            print "'%s' total score: " % k + str(tsc)
            print "found1 score: %s -------------------" % str(score1)
            print vineger_decipher( found1, k ) 
            # print "found2 score: " + str(score2)
            print vineger_decipher( found2, k ) 
            # print "found3 score: " + str(score3)
            print vineger_decipher( found3, k ) 

print vineger_decipher( krypton, "KEYLENGTH" )
# print "".join(found2.split())
# try_find_key( [found1,found2,found3] )
# ZAL -> THE => TGS
# DLC -> THE => PVB * 8-length
# blocks = group( found3, 4)
# for b in blocks:
#     if "ZAL" in b:
#         print b

# print_three_block_freq()
# key = "TGSPVD"
# print vineger_decipher( found1, key)
# print vineger_decipher( found2, key)
