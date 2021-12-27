#include <stdio.h>

#define MIN -64
#define MAX 63

struct Node {
    int tag;
    long long sum;
    int son[8];
} seg[20000005];

int root, cnt;

char op[15];
int x1, x2, y1, y2, z1, z2;

inline int new_node() { seg[++cnt].tag = -1; return cnt; }

inline void push_down(int k, int Xl, int Xr, int Yl, int Yr, int Zl, int Zr) {
    if (seg[k].tag == -1) return;
    int Xm = (Xl + Xr) >> 1, Ym = (Yl + Yr) >> 1, Zm = (Zl + Zr) >> 1;
    Node& K = seg[k];
    Node &LDF = seg[K.son[0]], &LDB = seg[K.son[1]], &LUF = seg[K.son[2]], &LUB = seg[K.son[3]],
         &RDF = seg[K.son[4]], &RDB = seg[K.son[5]], &RUF = seg[K.son[6]], &RUB = seg[K.son[7]];
    LDF.tag = K.tag; LDB.tag = K.tag; LUF.tag = K.tag; LUB.tag = K.tag;
    RDF.tag = K.tag; RDB.tag = K.tag; RUF.tag = K.tag; RUB.tag = K.tag;
    LDF.sum = (long long) K.tag * (Xm - Xl + 1) * (Ym - Yl + 1) * (Zm - Zl + 1);
    LDB.sum = (long long) K.tag * (Xm - Xl + 1) * (Ym - Yl + 1) * (Zr - Zm);
    LUF.sum = (long long) K.tag * (Xm - Xl + 1) * (Yr - Ym) * (Zm - Zl + 1);
    LUB.sum = (long long) K.tag * (Xm - Xl + 1) * (Yr - Ym) * (Zr - Zm);
    RDF.sum = (long long) K.tag * (Xr - Xm) * (Ym - Yl + 1) * (Zm - Zl + 1);
    RDB.sum = (long long) K.tag * (Xr - Xm) * (Ym - Yl + 1) * (Zr - Zm);
    RUF.sum = (long long) K.tag * (Xr - Xm) * (Yr - Ym) * (Zm - Zl + 1);
    RUB.sum = (long long) K.tag * (Xr - Xm) * (Yr - Ym) * (Zr - Zm);
    K.tag = -1;
}

void update(int xl, int xr, int yl, int yr, int zl, int zr, int v, int &k, int Xl, int Xr, int Yl, int Yr, int Zl, int Zr) {
    if (!k) k = new_node();
    if (xl <= Xl && Xr <= xr && yl <= Yl && Yr <= yr && zl <= Zl && Zr <= zr) {
        seg[k].tag = v;
        seg[k].sum = (long long) v * (Xr - Xl + 1) * (Yr - Yl + 1) * (Zr - Zl + 1);
        return;
    }
    for (int i = 0; i < 8; ++i) if (!seg[k].son[i]) seg[k].son[i] = new_node();
    push_down(k, Xl, Xr, Yl, Yr, Zl, Zr);
    int Xm = (Xl + Xr) >> 1, Ym = (Yl + Yr) >> 1, Zm = (Zl + Zr) >> 1;
    if (xl <= Xm) {
        if (yl <= Ym) {
            if (zl <= Zm) update(xl, xr, yl, yr, zl, zr, v, seg[k].son[0], Xl, Xm, Yl, Ym, Zl, Zm);
            if (Zm < zr) update(xl, xr, yl, yr, zl, zr, v, seg[k].son[1], Xl, Xm, Yl, Ym, Zm + 1, Zr);
        }
        if (Ym < yr) {
            if (zl <= Zm) update(xl, xr, yl, yr, zl, zr, v, seg[k].son[2], Xl, Xm, Ym + 1, Yr, Zl, Zm);
            if (Zm < zr) update(xl, xr, yl, yr, zl, zr, v, seg[k].son[3], Xl, Xm, Ym + 1, Yr, Zm + 1, Zr);
        }
    }
    if (Xm < xr) {
        if (yl <= Ym) {
            if (zl <= Zm) update(xl, xr, yl, yr, zl, zr, v, seg[k].son[4], Xm + 1, Xr, Yl, Ym, Zl, Zm);
            if (Zm < zr) update(xl, xr, yl, yr, zl, zr, v, seg[k].son[5], Xm + 1, Xr, Yl, Ym, Zm + 1, Zr);
        }
        if (Ym < yr) {
            if (zl <= Zm) update(xl, xr, yl, yr, zl, zr, v, seg[k].son[6], Xm + 1, Xr, Ym + 1, Yr, Zl, Zm);
            if (Zm < zr) update(xl, xr, yl, yr, zl, zr, v, seg[k].son[7], Xm + 1, Xr, Ym + 1, Yr, Zm + 1, Zr);
        }
    }
    seg[k].sum = 0;
    for (int i = 0; i < 8; ++i)
        seg[k].sum += seg[seg[k].son[i]].sum;
}

int main() {
    while (~scanf("%s x=%d..%d,y=%d..%d,z=%d..%d", op, &x1, &x2, &y1, &y2, &z1, &z2)) {
        if (x1 < -50 || x2 > 50 || y1 < -50 || y2 > 50 || z1 < -50 || z2 > 50) break;
        update(x1, x2, y1, y2, z1, z2, *(op + 1) == 'n', root, MIN, MAX, MIN, MAX, MIN, MAX);
    }
    printf("%lld\n", seg[root].sum);
    return 0;
}