sets 
t time  /1*24/
i DGs  /1*5/
s senarios /1*5/
;
 
table PV(s,t)  'PV forecast power'
   1   2   3   4   5   6   7   8   9   10      11      12      13      14      15      16      17      18      19      20     21  22  23  24
1  0   0   0   0   0   0   0   0   0   0.23    1.111   1.835   2.287   2.555   2.673   2.57    1.815   1.353   0.944   0.116   0   0   0   0
2  0   0   0   0   0   0   0   0   0   0.92    1.754   2.509   3.704   4.516   4.703   4.541   3.96    3.063   2.138   0.645   0   0   0   0
3  0   0   0   0   0   0   0   0   0   0.82    1.659   2.401   3.632   4.152   4.351   4.212   3.908   3       1.985   0.564   0   0   0   0
4  0   0   0   0   0   0   0   0   0   0.71    1.534   2.266   3.567   3.926   4.126   3.988   3.711   2.805   1.832   0.479   0   0   0   0
5  0   0   0   0   0   0   0   0   0   0.27    1.239   2.071   2.825   3.457   3.631   3.477   2.913   2.103   1.254   0.15    0   0   0   0
;

table WT(s,t)  'WT forecast power'
     1        2      3        4       5       6      7       8       9       10      11       12     13      14      15      16      17       18      19      20      21      22     23      24
1   14.445   10.027  9.598   7.939   11.111  8.211   4.726   4.806   9.932   9.878   15.356  6.959   4.331   4.461   4.037   3.462   6.239   1.935   2.505   2.924   4.247   4.772   7.914   9.55
2   8.861    5.566   5.087   4.173   4.586   3.261   4.91    3.214   7.693   6.794   11.843  6.393   3.132   3.245   3.116   3.16    4.576   1.899   2.221   2.87    3.262   4.904   9.766   11.99
3   11.349   5.949   4.713   3.244   2.148   2.728   3.256   1.83    5.128   3.63    5.842   4.17    1.365   2.01    2.311   1.751   0.679   1.373   0.87    1.199   1.136   1.561   4.094   2.415
4   15.859   9.474   8.635   6.944   8.346   4.644   4.24    3.544   7.602   7.68    12.59   5.895   3.263   3.548   3.252   2.768   4.372   1.473   1.688   2.204   3.35    3.406   5.534   7.942
5   9.283    5.143   4.416   3.516   0.184   1.783   3.857   2.105   4.047   1.106   0.249   1.864   0.027   0.866   0.555   0.819   0.294   1.104   1.062   1.061   1.314   2.959   3.879   2.027
;
table  prob(s,t)
     1       2       3       4        5      6       7        8      9        10      11     12      13      14       15     16      17      18      19      20      21      22      23      24
1   0.138   0.156   0.169   0.178   0.234   0.236   0.134   0.178   0.163   0.167   0.156   0.128   0.118   0.111   0.108   0.100   0.125   0.078   0.100   0.113   0.153   0.119   0.111   0.123
2   0.085   0.087   0.090   0.093   0.097   0.094   0.140   0.119   0.126   0.128   0.129   0.129   0.121   0.122   0.126   0.128   0.132   0.117   0.126   0.131   0.118   0.122   0.136   0.154
3   0.108   0.093   0.083   0.073   0.045   0.079   0.093   0.068   0.084   0.074   0.071   0.095   0.089   0.097   0.108   0.099   0.071   0.103   0.083   0.066   0.041   0.039   0.057   0.031
4   0.151   0.147   0.152   0.155   0.176   0.134   0.121   0.131   0.125   0.139   0.134   0.119   0.121   0.118   0.119   0.112   0.125   0.101   0.102   0.100   0.121   0.085   0.077   0.102
5   0.089   0.080   0.078   0.079   0.004   0.051   0.110   0.078   0.066   0.023   0.014   0.057   0.051   0.068   0.068   0.071   0.050   0.076   0.067   0.045   0.047   0.074   0.054   0.026
;

****************************************************
Parameters
C_AGDG1    'AG DG marginal generation cost' /22.5/
C_AGDG2                          /20/
C_AGDG3                          /20/
C_AGDG4                          /20/
C_AGDG5                          /22.5/
P_AGDG1max   'AG DGs maximum generation'  /1.2/
P_AGDG1min   'AG DGs minimum generation'  /0/
P_AGDG2max   'AG DGs maximum generation' /1.0/  
P_AGDG2min   'AG DGs minimum generation' /0/
P_AGDG3max   'AG DGs maximum generation'  /1.0/
P_AGDG3min   'AG DGs minimum generation' /0/
P_AGDG4max   'AG DGs maximum generation'  /1.0/
P_AGDG4min   'AG DGs minimum generation' /0/
P_AGDG5max   'AG DGs maximum generation'  /1.2/
P_AGDG5min   'AG DGs minimum generation' /0/
E_AGBS1ini                      /0.02/
E_AGBS1min    Min amount of energy stored in AGBS  / 0.4/
E_AGBS1max    Max amount of energy stored in AGBS  / 8/
P_AGBS1chmin   Min charge power of AGBS / 0/
P_AGBS1chmax   Max charge power of AGBS / 6.5/
P_AGBS1dchmin   Min discharge power of AGBS / 0/
P_AGBS1dchmax   Max discharge power of AGBS /2.5/
Neeta_AGBS1ch   / 0.98/
Neeta_AGBS1dch / 0.98/
P_AGDGini   Initial Gen power of AGs DG
P_exchLEMmax Max_exchange power in DA LEM   / 20/
Lambda_LEMmax                               /30/                                                
RD_AGDG1       Ramp down rate of AGs DG  /0.5/      
RU_AGDG1      Ramp up rate of AGs DG     /0.5/
RD_AGDG2       Ramp down rate of AGs DG  /0.6/ 
RU_AGDG2      Ramp up rate of AGs DG    /0.6/
RD_AGDG3       Ramp down rate of AGs DG /0.6/  
RU_AGDG3      Ramp up rate of AGs DG   /0.6/
RD_AGDG4       Ramp down rate of AGs DG /0.6/  
RU_AGDG4      Ramp up rate of AGs DG   /0.6/
RD_AGDG5       Ramp down rate of AGs DG /0.5/  
RU_AGDG5      Ramp up rate of AGs DG   /0.5/
CI            Confidence interval      /0.95/
beta          Risk aversion factor    /0.4/
Lambda_PV      Cost of PV             /36/
Lambda_WT      Cost of WT             /29/;
*************************************************************
Variables
P_exchWEMDA(t)  Exchange power in DA WEM
P_exchLEMDA(s,t)   Exchange power in DA LEM
P_AGDG1(s,t)
P_AGDG2(s,t)
P_AGDG3(s,t)
P_AGDG4(s,t)
P_AGDG5(s,t)
P_AGBS1ch
P_AGBS1dch
E_AGBS1
P_SLEM(t)    Surplus power
Rev(s,t)
Cos(s,t)
OF
Lambda_LEMDA(t)
E_Prof(s,t)
CVaR
VaR
OF1
neeta;
********************************************
Equations
const1(s,t)
const2(s,t)
const3(s,t)
const4(s,t)
const5(s,t)
const6(s,t)
const7(s,t)
const8(s,t)
const9(s,t)
const10(s,t)
const11(s,t)
const12(s,t)
const13(s,t)
const14(s,t)
const15(s,t)
const16(s,t)
const17(s,t)
const18(s,t)
const19(s,t)
const20(s,t)
const21(s,t)
const22(s,t)
const23(s,t)
const24(s,t)
const25(s,t)
const26(s,t)
const27(s,t)
const28(s,t)
const29(s,t)
const30(s,t)
const31(t)
const32(t)
const33(s,t)
const34(s,t)
const35(s,t)
const36(s,t)
const37(s,t)
;
****************************************************
const1(s,t)..  PV(s,t)+WT(s,t)+P_AGDG1(s,t)+P_AGDG2(s,t)+P_AGDG3(s,t)+P_AGDG4(s,t)+P_AGDG5(s,t)+(P_AGBS1ch(s,t)-P_AGBS1dch(s,t)) =e= P_exchLEMDA(s,t);

const2(s,t)..  P_exchLEMDA(s,t) =g= 0;

const3(s,t)..  P_exchLEMDA(s,t) =l= P_exchLEMmax;

const4(s,t)..  P_AGDG1(s,t) =g= P_AGDG1min;

const5(s,t)..  P_AGDG1(s,t) =l= P_AGDG1max;

const6(s,t)..  P_AGDG2(s,t) =g= P_AGDG2min;

const7(s,t)..  P_AGDG2(s,t) =l= P_AGDG2max;

const8(s,t)..  P_AGDG3(s,t) =g= P_AGDG3min;

const9(s,t)..  P_AGDG3(s,t) =l= P_AGDG3max;

const10(s,t).. P_AGDG4(s,t) =g= P_AGDG4min;

const11(s,t).. P_AGDG4(s,t) =l= P_AGDG4max;

const12(s,t).. P_AGDG5(s,t) =g= P_AGDG5min;

const13(s,t).. P_AGDG5(s,t) =l= P_AGDG5max;

const14(s,t).. P_AGDG1(s,t)-P_AGDG1(s,t-1) =l= RU_AGDG1;

const15(s,t).. P_AGDG1(s,t-1)-P_AGDG1(s,t) =l= RD_AGDG1;

const16(s,t).. P_AGDG2(s,t)-P_AGDG2(s,t-1) =l= RU_AGDG2;

const17(s,t).. P_AGDG2(s,t-1)-P_AGDG2(s,t) =l= RD_AGDG2;

const18(s,t).. P_AGDG3(s,t)-P_AGDG3(s,t-1) =l= RU_AGDG3;

const19(s,t).. P_AGDG3(s,t-1)-P_AGDG3(s,t) =l= RD_AGDG3;

const20(s,t).. P_AGDG4(s,t)-P_AGDG4(s,t-1) =l= RU_AGDG4;

const21(s,t).. P_AGDG4(s,t-1)-P_AGDG4(s,t) =l= RD_AGDG4;

const22(s,t).. P_AGDG5(s,t)-P_AGDG5(s,t-1) =l= RU_AGDG5;

const23(s,t).. P_AGDG5(s,t-1)-P_AGDG5(s,t) =l= RD_AGDG5;

const24(s,t).. P_AGBS1dch(s,t) =g= P_AGBS1dchmin;

const25(s,t).. P_AGBS1dch(s,t) =l= P_AGBS1dchmax;

const26(s,t).. P_AGBS1ch(s,t) =g= P_AGBS1chmin;

const27(s,t).. P_AGBS1ch(s,t) =l= P_AGBS1chmax;

const28(s,t).. E_AGBS1(s,t) =e= E_AGBS1(s,t-1)+(P_AGBS1ch(s,t)*Neeta_AGBS1ch)-(P_AGBS1dch(s,t)/Neeta_AGBS1dch);

const29(s,t).. E_AGBS1(s,t) =g= E_AGBS1min;

const30(s,t).. E_AGBS1(s,t) =l= E_AGBS1max;

const31(t)..  Lambda_LEMDA(t) =g= 0;

const32(t)..  Lambda_LEMDA(t) =l= Lambda_LEMmax;

const33(s,t)..  E_Prof(s,t) =e= ((P_exchLEMDA(s,t)*Lambda_LEMDA(t))-((P_AGDG1(s,t)*C_AGDG1)+(P_AGDG2(s,t)*C_AGDG2)+(P_AGDG3(s,t))*C_AGDG3)+(P_AGDG4(s,t)*C_AGDG4)+(P_AGDG5(s,t)*C_AGDG5));

const34(s,t)..  CVaR =e= (VaR) -(1*(prob(s,t)*neeta)/(1-0.95));

const35(s,t).. VaR-E_Prof(s,t)-neeta  =l= 0;

const36(s,t)..  neeta=g= 0;

const37(s,t)..  OF1 =e= (1-beta)*prob(s,t)*E_Prof(s,t)+(beta*CVaR);

*const19(t)..  P_SLEM(t) =e= P_LEMload(t,'P')-P_exchLEMDA(t);
 
model NewVaR/ const1, const2,const3,const4,const5,const6,const7,const8,const9,const10,const11,const12,const13,const14,const15,const16, const17, const18,const19,const20,const21,const22,const23,const24,const25,const26, const27,const28, const29,
const30,const31,const32,const33,const34,const35,const36,const37/;
option nlp = conopt;
solve NewVaR maximizing OF1 using nlp;
Display  P_exchLEMDA.l, P_AGDG1.l, P_AGDG2.l, P_AGDG3.l,P_AGDG4.l,P_AGDG5.l,neeta.l,Lambda_LEMDA.l,E_Prof.l, OF1.l,CVaR.l,VaR.l;
