import os, sys, base64, zlib
code = b'c%0Q*QFGfi41U+IVBMQfN>ne)?Ws<(%ThPXtxbK2+lTdfJlUdct+J>|RBA8Fe)|BDmS~BNy?9%_JUB84fcQWV1SmVtqhu5pAtNXKg_!cBGd*)E+8rASo}D>B8i#C5D80OXe?h6i!sg=JbV$Se+aS;Rh>mz7f+%5GXPTyGRz{IAMpGU~qlIEB@+g^*B$%;04MvRQBJ4JZlunX@ro%ArIxtBtfGrTwhy;b;WW;AFO&5IlD>)?}Ke_$IyWy{3{Q*(DZ4ys&pESwYH23bEjEN#kh&$vw_LfZaCK^pIKyi?<A7Q|iDl(;qz8QF3;yf%31!y@FFgc<-amtB&Cn@5XibcwNCuE}-pWMn^&v&vRl`av%#CPNq&q9__i7y9;IZb%TXpx42V9r_BdCuaT8NP*?*LZPXJY{hde4bQpA~xShs7V-&o#zmK5LKjqeskNS=Qo$PE;7ReoleIi(b#>~Uz}$X+7Ggv4T>~oZjeo2T(eR7;atj5>Ul(?xPJfUO{w~_H=zA@SJ#8yjhl;$AkB-IdBnYC;``E0fUHO8B@=xfC4yxYyH8psdtYQN&%wW3WW`7jbMW5LuE<4KKfZh!fw}<p9EpHva=RXR37jjD157Y=XUHZ|;sUDshgA`^eJdxQwF!{4B6wO#`bh48qw(?YOrS!;B((_&su|#^lM9O$XUsE8+@(^?!;rbUzPRbVc2f)-=g(C?Y$5)tXNY5@k{}EXkvS+)Vz?zBv@sk-CrWab33m=+5k_d%8Alne4un_M$r*@*AX(XmoH~?XeHqM#8?)Rb;{d*)2@h31fY6)qJ61DBP6rl1AckuGv5PcGlnYbFY=6<qG72uy{($fE5&fAVnP)zz^GT)M!w~N}l}`>Lv4n@Jvmj@#B0VxAz2*rkp&nptnvil9WTPpaMw2O|E%sXx#B1=y{0ndld9ek|4U^6=nC?*n$mY@S%=J!Bk36UDrdyFg+R<*hN<uc*j%tAhGS2vn1PNiYR4gzhwQTNNny*9n5u<|ne`{2lu{*bP-g?7Qp3>btrnNlPYvv}%VN6<S2}NxXFj+wC>|w2C7cV~z2wF=8i5WOUXRR_-lwej7<8eR}D4jIsO`8Q+4iBHYqvT`~YHhMIbFb6%;zeDT;53HX#Q<83;Q+X*zjy-=^qPICmJ(A!B1i<oN8QKsyqSknxh7KGEu7+4gWg*gXMv;V@X#mf9MHxhebv?pGws|VC8?FSuarG7tF+yc!UVXjVYqF??O;8)0U}_g5A~QQlQxM$%-;Bnk5IJZ-0(!sV1dXF^6{noJR~l%c}5_kEn4X8w2E-@#~-D#6H?#0uX#2LgzGdmuG1Q&DV9sxP7>i5;e{Z4OtK)EFyi72r{9D=P5}SCmS4>)iH^;=_3p+zjp=Zq%JC%@Z&`jf(i?`WjNa3uE{RSwe-~pADpYZJSXQ%-Wa+(kKiK$xcKy>*w^{;3y;9heNuv&<%Id0><74`nEo8}~5J-i}f+K77e_TWOWg5k3+A(=nZEn(T8}&NYcE?x%BIILCd@un*H?e3pJYYlS-0>(}Dc|WB+RqXqIlyB6ex>GL=HV3V+om-F4YsDJ3%zj61S9F{4p=cp&V+rF;q;uvW3xNOCa+<lJYN#_g{*cC-740Xmg4E-q8ko8JT4lB`c3zE+gMDox==^pM%#^(5sxOL#cjO<1KL2<=OXMTxv%wEcQIw7&n^yoID{(#T%I1qe)jh2m!7NSG3<zxmEG}rVKr=%wx3}GXt0-u*n|u4dnBL_P{(`%!7NZAE_tIL#l900M{@@wQn`EYQR-v#sVW#M!yyA2Sk<X74}EMvO(5n_*QgtmYPq1>1Q0gQ|9%XuwyGOqh8!4o4+ryF^vLir7}}VCEJ*EFA6?Ztt1Oj^7iVbM-1Gqbv54aELl75C#VYdRqR;`f!*UVmYixoa!`o<xzbfSV`GB~!g&UzihVt<qdG8?G%-sn;HlI(yYsrVE?K{Gpt+ew`Ko!jQ5f%2xJD^%#7VICg@)~2Ms39Am?Bybrml@ka!Fz+R3qxOER2bw{#=1a@VJ6j-YzQ}bzp;M{WZb>%vX}5aWlzDWyPh4uEpK`D4_|rzwC(P~OQ8LOA+M%(SRmEV?jJ6FQ?>)L5l<Ii8Cae5*w!-~<igw3GaT>UG%PRgp5~F|4O7iGalNp_`>1~+rlqM$*)B!O{{bzUxq@^<9;#n5ebvsuxTTVZhO}+{s>Q~t>7N|*7jK!E^6(WKBTn@t|A_7Uy>s6x?@Q|OUJm%=ZEx@s{cwJRm|&w^WGoO2-`C))X5ei-_@<`n=4GwUie<BQ^_obklk-3iT-OVvhMw~<#P=yPC8Qe2x}2gmL~kV7khb(<byXIYhTdDrW9WrKx~>OE4Y^D31<<2eF*AjOc|$mu+l7O9O<0%lbp@K-P}1kA#R6SGTa{QWkxCktKm}V@03<66tbUac7KL>wq*=vqfZX8*(Pl%@)vy_8R$&~7c#)e5bZJx9p~($3Z-dWF-NngB#`m034W!|^3Lsgnkgr?BG>}jFf;uND-tgitdIGIc9_n?SlGxDNlP|lr)Qd-bb1$ch=H><B3P8EeO^`@l4|KRtH~nRlSt86DT~$;mdEb)R?bE8)DdS25z8vw1`aDt(5Aw%m%e<<8PXy_ehmfl=y#nx={33I!F+zXpoxh@2*H?q`Ee_b`DDBRR@8F|K&Ayxkq~E<l3Hti|^#x3Gl|<llDJ#pC>X%^4iKt4QZo9NYo&$dYClOdp'
code_setup = '\nfrom distutils.core import setup, Extension\nmodule = Extension(\n    "cppset",\n    sources=["set_wrapper.cpp"],\n    extra_compile_args=["-O3", "-march=native"]\n)\nsetup(\n    name="SetMethod",\n    version="0.1.0",\n    description="wrapper for C++ set",\n    ext_modules=[module]\n)\n'
if sys.argv[-1] == "ONLINE_JUDGE" or os.name == "nt":
    with open("set_wrapper.cpp", "w") as f:
        f.write(zlib.decompress(base64.b85decode(code)).decode("utf-8"))
    with open("setup.py", "w") as f:
        f.write(code_setup)
    os.system(f"{sys.executable} setup.py build_ext --inplace")

import cppset
class CppSet:
    def __init__(self, lst=None, capsule=None):
        if lst:
            self.st = cppset.construct_from_list(lst)
        elif capsule:
            self.st = capsule
        else:
            self.st = cppset.construct()
 
    def add(self, val):
        return cppset.add(self.st, val)
 
    def remove(self, val):
        return cppset.remove(self.st, val)
 
    def search_higher_equal(self, val):
        return cppset.search_higher_equal(self.st, val)
 
    def min(self):
        return cppset.min(self.st)
 
    def max(self):
        return cppset.max(self.st)
 
    def pop_min(self):
        return cppset.pop_min(self.st)
 
    def pop_max(self):
        return cppset.pop_max(self.st)
 
    def __len__(self):
        return cppset.len(self.st)
 
    def __getitem__(self, idx):
        # g++ 拡張
        return cppset.getitem(self.st, idx)
 
    def pop(self, idx):
        # g++ 拡張
        return cppset.pop(self.st, idx)
 
    def index(self, val):
        # g++ 拡張  # イテレータは変化しない
        return cppset.index(self.st, val)
 
    def __contains__(self, val):
        return self.search_higher_equal(val) == val
 
    def next(self):
        return cppset.next(self.st)
 
    def prev(self):
        return cppset.prev(self.st)
 
    def to_list(self):
        return cppset.to_list(self.st)
 
    def get(self):
        return cppset.get(self.st)
 
    def erase(self):
        return cppset.erase(self.st)
 
    def copy(self):
        return CppSet(capsule=cppset.copy(self.st))
 
    def __repr__(self):
        return f"CppSet({self.to_list().__repr__()})"
 
 

n,q = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
#
st = CppSet(a)

#「最大の区間」を取り出すために
from heapq import heapify,heappush,heappop
que = []
heapify(que)
for i in range(1,n):#でかい方から取り出したいから-
    heappush(que,[-a[i]+a[i-1],a[i],a[i-1]])

#「存在」
dic = {}
for i in range(n):
    dic[a[i]]=0

ret = []
ans = st.max()-st.min()+que[0][0]
ret.append(ans)

for query in range(q):
    x,y = map(int,input().split())

    if x == 0:
        dic.pop(y)
        st.remove(y)
        r = st.search_higher_equal(y)
        l = st.prev()
        if r!=None and l!=None:
            heappush(que,[-r+l,l,r])
    else:
        dic[y]=0
        st.add(y)
        r = st.search_higher_equal(y)
        l = st.prev()
        r = st.search_higher_equal(y+1)
        if r!=None:
            heappush(que,[-r+y,y,r])
        if l!=None:
            heappush(que,[-y+l,l,y])

    length,L,R = heappop(que)
    while len(que)>0 and not((L in dic)and(R in dic)and(st.search_higher_equal(L+1)==R)):
        length,L,R = heappop(que)
        
    heappush(que,[length,L,R])
    
    if st.__len__()<=2:
        ret.append(0)
        continue

    length = -length

    r = st.max()
    l = st.min()

    ans = r-l-length
    ret.append(ans)

for i in range(q+1):
    print(ret[i])

