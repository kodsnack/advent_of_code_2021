#include <stdio.h>
#include <string.h>

struct Node { int l, r, v, f; } t[100005];
int cnt;

int stk[10005], match[10005], head, root;
char str[10005];

int new_node(int l, int r, int v) { t[++cnt] = (Node) { l, r, v, 0 }; return cnt; }
int parse(int l, int r) {
    if (r == l + 1) return new_node(0, 0, str[l] & 15);
    ++l; --r;
    if (str[l] == '[') {
        int L = parse(l, match[l] + 1), R = parse(match[l] + 2, r), v = new_node(L, R, 0);
        t[L].f = v; t[R].f = v;
        return v;
    } else {
        int L = parse(l, l + 1), R = parse(l + 2, r), v = new_node(L, R, 0);
        t[L].f = v; t[R].f = v;
        return v;
    }
}

int nxt(int u) {
    while (u != root && u == t[t[u].f].r) u = t[u].f;
    if (u == root) return 0;
    u = t[t[u].f].r;
    while (t[u].l) u = t[u].l;
    return u;
}
int prv(int u) {
    while (u != root && u == t[t[u].f].l) u = t[u].f;
    if (u == root) return 0;
    u = t[t[u].f].l;
    while (t[u].r) u = t[u].r;
    return u;
}

bool explode(int u, int d) {
    if (!t[u].l && !t[u].r) return false;
    if (explode(t[u].l, d + 1)) return true;
    if (d == 4) {
        int L = prv(u), R = nxt(u);
        if (L) t[L].v += t[t[u].l].v;
        if (R) t[R].v += t[t[u].r].v;
        t[u].l = t[u].r = 0;
        return true;
    }
    return explode(t[u].r, d + 1);
}
bool split(int u) {
    if (!t[u].l && !t[u].r) {
        if (t[u].v > 9) {
            t[u].l = new_node(0, 0, t[u].v >> 1);
            t[u].r = new_node(0, 0, t[u].v - (t[u].v >> 1));
            t[t[u].l].f = u; t[t[u].r].f = u;
            t[u].v = 0;
            return true;
        }
        return false;
    }
    return split(t[u].l) || split(t[u].r);
}
long long magnitude(int u) {
    if (!t[u].l && !t[u].r) return t[u].v;
    return magnitude(t[u].l) * 3 + magnitude(t[u].r) * 2;
}

int main() {
    while (~scanf(" %s", str)) {
        int len = strlen(str);
        for (int i = 0; i < len; ++i) {
            if (str[i] == '[') stk[++head] = i;
            else if (str[i] == ']') {
                match[i] = stk[head];
                match[stk[head]] = i;
                --head;
            }
        }
        if (root) root = new_node(root, parse(0, len), 0);
        else root = parse(0, len);
        t[t[root].l].f = root; t[t[root].r].f = root;
        while (1) {
            if (explode(root, 0)) continue;
            if (!split(root)) break;
        }
    }
    printf("%lld\n", magnitude(root));
    return 0;
}