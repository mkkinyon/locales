# Symmetric meets as rank-amplification test

Let T=L coproduct L, tau the factor-flip, d the disjointness open, and w any bar neighborhood with w join d=1. Then w_sym=w meet tau(w) is still a bar neighborhood, since d join w_sym=(d join w) meet (d join tau(w))=1. Moreover tau(w_sym)=w_sym. For its canonical rectangle bar B_sym={(a,b):a box b<=w_sym}, transposition gives B_sym^tau=B_sym. Thus an H-V-H tree for B_sym transposes to a V-H-V tree, and conversely. Any orientation-specific rank disparity is IMPOSSIBLE for these symmetric canonical bars.

There is an exact symmetric indexing of V: V=meet_{w join d=1} O(w meet tau(w)). One inclusion holds because w_sym also joins d to 1; the other because O(w meet tau(w))<=O(w) for each w, since finite meets of opens correspond to meet of open sublocales.

Unlike union symmetrization w join tau(w), which weakens a bar, meet symmetrization can increase minimal proof depth. Natural test: original rational graph null q and w_sym=q meet tau(q). Its barhood is immediate; rank≥3 because canonical leaf bar for w_sym is contained in that for q, whose minimal depth is 3. Whether this symmetric bar requires depth 4, or still has an H-V-H proof, is NOT established here. Notice symmetric canonical bars cannot witness an H-first vs V-first orientation asymmetry.

This shifts a possible rank-four search to an explicit familiar frame and avoids extra localic boundary proofs, but the lower-bound problem remains.
