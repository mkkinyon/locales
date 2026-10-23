# Rank-two fitted approximation via rather-below disjointness
23 October 2026

For frame L, write d=join(a box b : a meet b=0), and c rather-below a when c* join a=1. Set
 d_sep=join(c box f : c rather-below a, f rather-below b, a meet b=0).

THEOREM. For every indicated pair, the strip v=(c* box 1) join (1 box f*) is a bar of height at most 2. Root H split 1=c* join a, using v-leaf (c*,1). Under (a,1), root V split 1=f* join b, using v-leaf (a,f*) and D-leaf (a,b). Moreover v meet(c box f)=0. Hence c box f<=v->w for every bar w. With P2(w)=join(v->w : v bar rank<=2), this proves
  w join d_sep <= P2(w).
So if d_sep=d, then P2(w)=1 for every bar, and V2=V on L. No spatiality or approximation hypotheses on L are needed.

EXAMPLE. Let Y be an uncountable set with cocountable topology and X=Y disjoint-union Y. The component opens e,f are complemented and hyperconnected. Disjointness d=(e box f) join(f box e), and e rather-below e, f rather-below f, so d_sep=d. The frame has no nonzero compact or way-below approximants: for any nonzero c<=U choose infinitely many distinct x_k in c and increasing opens U_n=U minus {x_k:k>=n}; join U_n=U, but no U_n contains c. Hence it is noncompact, noncontinuous, not regular or completely distributive, yet V2=V. Actually every bar admits a direct H-V depth2 tree, since the diagonal component squares are forced into the bar and cross blocks lie in D.

RATIONAL-BRIDGE CONTRAST. For the earlier rational graph g(t)=(ell_t,r_t), g*(d)=1 since left and right sheets are disjoint, but g*(d_sep)=0. If g*(c box f) contained a rational interval J, both sheet traces would contain J; a bridge attaching to both sheets inside J belongs to closures of c and f. Yet c rather-below a and f rather-below b force those closures into disjoint opens a and b, impossible. Thus d_sep<d and d_sep join q<1 for the graph-null rank3 bar q. The criterion detects exactly the kind of separated-apartness deficit exhibited by V2 strictly containing V3.

This is a sufficient but not necessary condition for V2=V, and does not settle Question A, V_fin=V, on arbitrary frames.
