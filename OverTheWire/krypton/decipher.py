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

import string as st
# .ascii_uppercase
import numpy as np
# .mean
# .std (standard deviation)

# found text
found1 = "SXULW GNXIO WRZJG OFLCM RHEFZ ALGSP DXBLM PWIQT XJGLA RIYRI BLPPC HMXMG CTZDL CLKRU YMYSJ TWUTX ZCMRH EFZAL OTMNL BLULV MCQMG CTZDL CPTBI AVPML NVRJN SSXWT XJGLA RIQPE FUGVP PGRLG OMDKW RSIFK TZYRM QHNXD UOWQT XJGLA RIQAV VTZVP LMAIV ZPHCX FPAVT MLBSD OIFVT PBACS EQKOL BCRSM AMULP SPPYF CXOKH LZXUO GNLID ZVRAL DOACC INREN YMLRH VXXJD XMSIN BXUGI UPVRG ESQSG YKQOK LMXRS IBZAL BAYJM AYAVB XRSIC KKPYH ULWFU YHBPG VIGNX WBIQP RGVXY SSBEL NZLVW IMQMG YGVSW GPWGG NARSP TXVKL PXWGD XRJHU SXQMI VTZYO GCTZR JYVBK MZHBX YVBIT TPVTM OOWSA IERTA SZCOI TXXLY JAZQC GKPCS LZRYE MOOVC HIEKT RSREH MGNTS KVEPN NCTUN EOFIR TPPDL YAPNO GMKGC ZRGNX ARVMY IBLXU QPYYH GNXYO ACCIN QBUQA GELNR TYQIH LANTW HAYCP RJOMO KJYTV SGVLY RRSIG NKVXI MQJEG GJOML MSGNV VERRC MRYBA GEQNP RGKLB XFLRP XRZDE JESGN XSYVB DSSZA LCXYE ICXXZ OVTPW BLEVK ZCDEA JYPCL CDXUG MARML RWVTZ LXIPL PJKKL CIREP RJYVB ITPVV ZPHCX FPCRG KVPSS CPBXW VXIRS SHYTU NWCGI ANNUN VCOEA JLLFI LECSO OLCTG CMGAT SBITP PNZBV XWUPV RIHUM IBPHG UXUQP YYHNZ MOKXD LZBAK LNTCC MBJTZ KXRSM FSKZC SSELP UMARE BCIPK GAVCY EXNOG LNLCC JVBXH XHRHI AZBLD LZWIF YXKLM PELQG RVPAF ZQNVK VZLCE MPVKP FERPM AZALV MDPKH GKKCL YOLRX TSNIB ELRYN IVMKP ECVXH BELNI OETUX SSYGV TZARE RLVEG GNOQC YXFCX YOQYO ISUKA RIQHE YRHDS REFTB LEVXH MYEAJ PLCXK TRFZX YOZCY XUKVV MOJLR RMAVC XFLHO KXUVE GOSAR RHBSS YHQUS LXSDJ INXLH PXCCV NVIPX KMFXV ZLTOW QLKRY TZDLC DTVXB ACSDE LVYOL BCWPE ERTZD TYDXF AILBR YEYEG ESIHC QMPOX UDMLZ VVMBU KPGEC EGIWO HMFXG NXPBW KPVRS XZCEE PWVTM OOIYC XURRV BHCCS SKOLX XQSEQ RTAOP WNSZK MVDLC PRTRB ZRGPZ AAGGK ZIMAP RLKVW EAZRT XXZCS DMVVZ BZRWS MNRIM ZSRYX IEOVH GLGNL FZKHX KCESE KEHDI FLZRV KVFIB XSEKB TZSPE EAZMV DLCSY ZGGYK GCELN TTUIG MXQHT BJKXG ZRFEX ABIAP MIKWA RVMFK UGGFY JRSIP NBJUI LDSSZ ALMSA VPNTX IBSMO"
found2 = "GLCYX UKFHS PEZXF AVJOW QQYYR RAYHM GIEOG ARIAZ YEYXV PXFPJ BXXUY SLELR NXHNH PLARX TADLC CSLGE NOSPR IUUML VSNPR RJMOO GMLGU JHVBE QSMFI NZDSK HEFNX KSHGE AVZAZ YQCQP BAKPC LMQGR XXTYR WQSEG FHSPH ZYETX FPVMX PBTWV XMLHM AZXYG EQLRN IAPOZ CXIAZ MVMSL RVNZN SKXCL RNJOL XXSCS HYMYK ZCWPR XNWYR ZJXUG MASQC ELRXX DKWMY PLUGL KHTPR GAKVE WRCEI KESOV JPJGH XJYRE CEGAE HDIBQ SEZAL DAMZX UKKZR EBMIR TLLDH MHRNZ MOOMP CIFVX JDMTP VBGWZ SHCOI FZBUK XGZRF ZALWM JOIJE BUCMB PSSZA LMSYN LJOMO SXQOE ZVTUN HGCXL YMYKA GEWQO LHQIC LFYKL TOPJL RQOMZ YFQNY EOMFG EQCEG NXYVM IPEYG KNOVB ZKXKG UOPKC PBXKF DLCAE FYXUQ IPDLN QBUQL GXWRR YVEXM QMGOG JREGY WBLLA BEULX NTZSO SDDLN MZFGV YATRX YSKTN TRTNT AKRBX YQJRS OKQHE FXTAR IPWMX KTSKV EPVFU KAYJB ZKGNX YOAGW POKTW KGIPX GUVHV EGDXB SHYBS UOVNC XYIIQ DMEOY ARIUP EGNXY RSJOW NTWAR IUTRQ YXACX MWIEG USOJY TVGNX ASHCH MYRLL BZCAV RZMFX MAPPL GMHLS SEXJU BUDLC LJGKK UYSLD MEHXK CMPTW UGESX SRRSG UULNX GWPAO ZODFS EMJGG AKFCO VBUFH XHYME EHXYK RBELR TUYOE IQEFZ LPBCC DWVXM OKXUL CFOKP PCMFT YKTZO WFZAP UGJYV BRIAZ ELWEL DZNRB ZOELO LBZPH DIPES PUGJY VBAYY RHMPK CYXYK FHXWZ ZSGYB UMSLN SEJRV EAGWP SOGKK JGYIF KTJYE JQMEK LPBJC EGUHT YLIPE SPUGJ YVBDX VXTIY YRELR XXUYA DZVPU GJYVB ELRIH UMSPO FRJVO KQZPV OKBUQ EJHEL YTZCM EYIQZ HHZEQ DIAMX YLCRS IZGBS KRBAE FYXUQ IPDFL ZALWE GWFRO GNKPU LCFNX HFMJJ AEGIW OHSAJ EUFOO EBESS UHADL CCSBS AHNXF PSQJB UDIPP WGLHY DLCPW GGUSS WFXIA ZHMDL CCSLG ENOSP RIGNT AKPRS SHMAI EXMYI XOGKY JKLRJ GLZOI LESTU BUDSG EEYRD PXHQL RQBTY SIRTI FUYTO RALQR UNAYJ GEGBT LLAYC YXYET UYXFP VQXTD OVYYH GCHWY VRPVF GGKCI TPVNR FHSHQ LRQZA LVELO PNJRD OVCLP YRHPD IPTRT HRHMG GOIAZ TAFEP TSHYI VSRRD SSZAL BSYOF RZPLO RRSIP UGJYV BLRQZ ALMSD QIRXH VWAFP RNMXU DPCXE AUYZS BRJJB XFHVP WOVRY LLNML LFEUP UCYGE SSIEV DLCDT EKMAI ACWPJ UKULY RGIEE PLVPI PTGCB ARPYC KRYJB KVCNY SLLHX HJLVT KYSKT QESGN XWYGI PXFVT ZCIBL PBTZV XLGDA NEMVR MQMVR GDMKW R"
found3 = "FIPJS EJXYV CYYHZ KMOYH GNEYN XSYSI PHJOM OKLYY HBTXH MLIYI RGGKK PMFHJ GMJRX GNOVT ZHCSL ZVBAL ZOVKZ RHTWL BLGDJ YGIWO HULMF ZVVKX YDXUU NNRMR AMGZX KSXQR VNBBA IELOP BTZLF MRJET GBUCX RSIYK OPDCY YHRBT UOWAP RPKHM DLCMV VYDMS VCSIU GWHQS MOPRM TUNAY DEYOM AVITL MAUYP DJMCL VYUYY ALDXB IDPXK QQMGZ XKCPC PONTW JVSQP EAJPL BIMQE SOGLD IVEYE KAPCW FZIFG GKLYA VPRYM VYXFZ YTNIS KMLHI EKMYS QFPAB XXHXS BOPVZ MSOWJ PIXIK PCTDW EKKGD SKQPX GOGNF IPJGY ULLDS FTWUK TKGLG NLJOZ PDMQE SOKIY OWSXI QCTZW EBPSS NTPBF SEAUO VOVSM VIQLT YWSPP EFZAV EKFTX JKKLC TSYJE UFMSP YXIAZ LVPWG WOBXZ SKWQS MFRBU ORRSS HMAUY XMQES OGLXI QDMAG VJYVB LRPKP PDLFT WFZHJ UMLRW JGLHC AFTXR GLARI RZTFU YARIU LZRYM OKXZC SXKNW YRRSI AKBNR FMFVV TZIOE ASSEZ ALCTC NOFUY ZKMJE LNZZS SRRPH VTMOO WSYPV MAAPE PLXFK THPEA PLNHB AEEJW CFAIW BIQDI QGGKA YGPXR JPHCW RTPYR BNRXC OYCAG KOVRS IDATP XXUTK OETWK MPZJZ UBZDF PTKUZ XFOWR SEGOM TEWRS EIKVV CXRSI VXHDX IPTRL KTYCK MYIOE LVWIN LMAYM VNVGW PGUMO OGMXT BYXKK RBCIF KKCOH CITEK LZSSL ZJGKE SCSLD FNTDO OLYOE UKTSD LWNSY UNYSR FTWPN XLUWY YHUOL MKGCE LBAZO VMLPH OUKLP IUEVN IXZYJ YYBVK MFLYR AIENT WCXFP GBTYP NILEM NRUHM LCWSE IELBO QTRGK ESCSL DFNTD DOVCA VVTVP ZEJWC BIVBZ MCOAV ZAARI ALVRY HMYXF PVCKH WVIYY HCKKO KTQDI PUGKR ELOGN XXZVM IPWRI HUNLY YHPRH ARIQN SZKXH CMJJS SLTUN SLNSZ VELDM LRLVY KLCIK MPNTV LDSYX EACAV GEQDM GZBUQ JMCLV YIVBX PLMGS KSYVP JHEUI WOHMQ JGULS OINEL RGKYS ZYWSS NBZLV CLOSG LABSS DIQNB TKRBS IFGBK DSRSI QXTDO VYDLR SHCOH FTWPN TPBXM TXVCB ZREAN SZSHK KXGZR CXXWK VCOJB XTFYY LRPNJ RDRSK LCPUF LRIPP EGGGF DMKPX BJTFC LCXEL GLRPS PXVWG KCSWJ ZVEEH YCLCX ELUGS IEQVJ BXTNO RRWIZ GGMBS KEIYR LVXWZ LRXVE LKWCE SYKMT OOLZA LKLZS VRPPY YHUCF YYOVT EVXHM YWVXR LCCCD WVXPL RETPS SZXUD MKPWG NXOYR MFVGU XUDIP EEVTR VEVEP RGRXT ORGYX UKBYD VYGIY RBUQF YNOJG KKCEL OJBXP HBHQM IGCBE DPMYH BTTUN TYCMF YBYKZ YDXQK TSYJR CEIKE SSRED MEOGA OPJDS AGGKM SKAEA ELOYY QPCRY PLKVC BYVZX HPVCY GUNHB CIYDA RREHC ELPRT RBZRS LPCRY LPBRM EQHIA PXXFP LNHBA YJQFG UZKHF IJWMA MRVEV QPPSO MOSRI DMETH AYJJL XREXH BWGEM FLBMD ICYCR GKZCM LNIJK LPXGC TGNSX SKWRQ VBSYY KRAP"
# The password for next level
krypton = "BELOS Z"

# TOOLS
# ---------------------------------------------------------
# Index of Coincidence
def IC( datastr ):
    # Make sure the datastr is all upper and nonblank
    datastr = "".join(datastr.split())
    datastr = datastr.upper()

    # Formula: IC = (n  * (n - 1))/(N * (N - 1))
    # With
    # n: occurence of letter from alphabet in string
    # N: total number of letters in string
    n = 0.0
    r = 0.0
    t = float(len(datastr))
    t = t * (t - 1)
    for c in st.ascii_uppercase:
        o = float(datastr.count(c))
        n += o * (o - 1)
    r = n / t
    return r

# Calculate the factors of any integer greater than 2
def calc_factors( integer ):
    fact = []
    if integer < 2:
        return fact
    for i in range(2,integer + 1):
        if( integer % i == 0 ):
            fact.append( i )
    return fact

# Make sure datastring is all uppercase 
# and contains no blank chars
def clean_datastr( datastr ):
    if datastr.find(' ') or datastr.find('\n') or datastr.find('\r'):
        datastr = "".join(datastr.split())
    if not datastr.isupper():
        datastr = datastr.upper()
    return datastr

# Create block-groups of characters
def block_group( datastr, blksize ):
    datastr = clean_datastr( datastr )
    return [datastr[i:i+blksize] for i in range(0,len(datastr),blksize)]

# Create shift-groups of characters
def shift_group( datastr, blksize ):
    datastr = clean_datastr( datastr )
    return [datastr[i:i+blksize] for i in range(len(datastr)-blksize)]

# Simple Caesar Cipher per character
def rot(char, rotate):
    nr = ord(char)
    if nr > 64 and nr < 91:
        nr -= 65
        nr += rotate
        nr %= 26
        nr += 65
    return chr(nr)

# Indices of given substring in datastring
def find_indc( datastr, substr, indices=[] ):
    try:
        indx = datastr.index(substr)
    except:
        return
    if len(indices) > 0:
        indices.append(indices[-1]+indx+1)
    else:
        indices.append( indx )
    find_indc( datastr[indx+1:], substr, indices )
    return indices

# Print two dimensional list in nice columns
def column_print( data, head=[], nr_of_rows=0 ):
    # print out all the data
    if nr_of_rows == 0:
        nr_of_rows = len(data)
    # print out the head first
    if len(head) != 0:
        data = [head] + data
    # calculate the column width
    column_width = max(len(str(attr)) for row in data for attr in row[:-1]) + 2
    # print
    for row in data[:nr_of_rows+1]:
        print "".join(str(attr).ljust(column_width) for attr in row)

# Try to detect if the text is English
def score_english( text ):
    # Get all the words from the dictionare.txt file
    f = open("./dictionary.txt")
    eng_words = f.read()
    f.close()
    # Make list of dictionary and sort largest word first
    eng_words = eng_words.split()
    eng_words.sort(key = lambda s: len(s),reverse=True)
    # Calculate a score based on the remaining text
    t = float(len(text))
    for w in eng_words:
        if w in text:
            text = "".join(text.split(w))
        if len(text) == 0:
            break
    return (t - float(len(text))) / t * 100

# ANALYSE
# ---------------------------------------------------------
# IC of given keylength
def IC_analyses( datastr, keylength=1 ):
    datastr = clean_datastr( datastr )
    blocks = [''] * keylength
    ics = []
    for i in range(keylength):
        blocks[i] = "".join([datastr[k] 
            for k in range(i,len(datastr),keylength)])
    for b in blocks:
        ics.append( IC(b) )
    return (np.mean(ics),np.std(ics))

# Return indices of each unique block of characters from given size
# Sorted by occurence
def block_freq_analyses( datastr, blksize=1, shift=True ):
    datastr = clean_datastr( datastr )
    diction = {}
    if shift:
        blocks = shift_group( datastr, blksize )
    else:
        blocks = block_group( datastr, blksize )

    for sub in blocks:
        if sub not in diction:
            diction[sub] = find_indc( datastr, sub, [] )

    dictlist = sorted(diction.items(),key=lambda kv: len(kv[1]),reverse=True)
    return dictlist

# Calculate the gap (and fractors) between substrings of a datastring
# You may also give it the block_freq_analyses list
def keylength_analyses( datastr, substrs ):
    diffs = []
    factors = []
    result = []
    for substr in substrs:
        if type(substr[1]) == list:
            f = substr[1]
        else:
            f = find_indc( clean_datastr( datastr ), substr )
        diffs += [f[i+1] - f[i] - 1 for i in range(0,len(f)-1,2)]
    for d in diffs:
        factors += calc_factors( d )

    result = sorted( set(factors), 
                     key=lambda k: factors.count(k),
                     reverse=True )
    return result



def compare_english( datastr ):
    ENG_ALPH = 'ETAOINSRHLDCUMFPGWYBVKXJQZ'
    datastr = clean_datastr( datastr )
    orderd = sorted( set( datastr ),
                     key=lambda k: datastr.count(k),
                     reverse=True )
    print orderd
    score = 0
    for i in range(len(orderd)):
        if orderd[i] == ENG_ALPH[i]:
            score += 1
    return score

def block_analyses( datastr, blksize ):
    blocks = group( datastr, blksize )
    letters = {}
    for i in range(blksize):
        letters[i] = []
    for block in blocks:
        for i in range(len(block)):
            letters[i].append(block[i])
    return letters

def vineger_decipher( datastr, key):
    datastr = clean_datastr( datastr )
    result = ''
    for i in range( len(datastr) ):
        k = key[i % len(key)]
        if k == '-':
            result += '-'
        else:
            result += rot( datastr[i], 26 - (ord(k) - 65) )
    return result

# lettrs = block_analyses( found1, 4 )
# for n in lettrs:
#     chars = lettrs[n]
#     analyses = freq_analyses( "".join(chars) )
#     print "letter" + str(int(n) + 1) + " in block"
#     print column_print( analyses, ["letter","occur","indice"], 5 )

# head = [ "subdatastr", "occurence", "indices" ]
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

def score_english( datastr ):
    # f = open("dictionary.txt")
    # words = f.read()
    # words = words.split('\n')
    # f.close()
    words = ['THE','AND','THA','ENT','ION','TIO','FOR','NDE','HAS','NCE','EDT','TIS','OFT','STH','MEN']
    score = 0
    # multiple = len(datastr) / (len(datastr) - datastr.count('-')) 
    for word in words:
        if word in datastr:
            score+=datastr.count(word)
    return score
    # return score * multiple

def convert_to_key( data, ii, oo, length ):
    blocks = []
    keys = []
    for datastr in data:
        blocks += group( datastr, length )
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

# p = ''
# for c in vineger_decipher( found1, "KEYLENGTH" ):
#     p += rot(c,13)
# print p
# IC( p )
# print vineger_decipher( found1, "KEYLENGTH" )
# IC( vineger_decipher( found1, "KEYLENGTH" ) )
# freq_an = freq_analyses( [found1], 3 )
# common_encr = [e[0] for e in freq_an[:15]]
# keylengths = calc_poss_keylength( [found1], [t[0] for t in freq_an])
# calc_keylengths( found1 )
# print "".join(found2.split())
# IC( found2 )

def calc_keylengths( datastr ):
    datastr = clean_datastr( datastr )
    blocks = []
    diffs = []
    result = {}
    for b in [datastr[i:i+3] for i in range(0,len(datastr)-3,1)]:
        if b not in blocks:
            blocks.append( b )
            frq = find_indc( datastr, b, [] )
            if len(frq) > 2:
                frq.sort()
                for i in range(len(frq)-1):
                    for j in range(i+1,len(frq[i:])):
                        diffs.append( frq[j] - frq[i] )
    fact = []
    for d in diffs:
        fact += calc_factors( d )
    uniq = set( fact )
    for u in uniq:
        result[u] = fact.count( u )
    result = sorted(result.items(),
                    key=lambda kv: (kv[1],kv[0]),
                    reverse=True) 
    print result

print vineger_decipher( found1,'KEYLENGTH' )
print vineger_decipher( found2,'KEYLENGTH' )
print vineger_decipher( found3,'KEYLENGTH' )
# for i in range(1,26):
#     print IC_analyses( found2, i )
