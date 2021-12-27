#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <vector>

int bin[10005], n;
char str[2005];

int get_value(int* &bin, int len) {
    int value = 0;
    for (int i = 0; i < len; ++i)
        value = (value << 1) | bin[i];
    bin += len; return value;
}

struct Packet {
    std::vector<Packet> sub_packets;
    int version, type;
    long long value;
    int* parse(int *s) {
        version = get_value(s, 3);
        type = get_value(s, 3);
        value = 0; sub_packets = std::vector<Packet>();
        if (type == 4) {
            int last = 1;
            while (last) {
                last = s[0]; ++s;
                value = value << 4 | get_value(s, 4);
            }
            return s;
        } else {
            int ltype = s[0]; ++s;
            int len;
            if (ltype == 0) {
                len = get_value(s, 15);
                int *start = s;
                while (s - start < len) {
                    Packet packet;
                    s = packet.parse(s);
                    sub_packets.push_back(packet);
                }
                return s;
            } else {
                len = get_value(s, 11);
                for (int i = 0; i < len; ++i) {
                    Packet packet;
                    s = packet.parse(s);
                    sub_packets.push_back(packet);
                }
                return s;
            }
        }
    }
} P;

long long traverse(const Packet &p) {
    long long ans, T;
    switch (p.type) {
        case 0:
        ans = 0;
        for (const Packet &u : p.sub_packets)
            ans += traverse(u);
        break;

        case 1:
        ans = 1;
        for (const Packet &u : p.sub_packets)
            ans *= traverse(u);
        break;

        case 2:
        ans = 0x3fffffffffffffffll;
        for (const Packet &u : p.sub_packets)
            if ((T = traverse(u)) < ans)
                ans = T;
        break;

        case 3:
        ans = 0;
        for (const Packet &u : p.sub_packets)
            if ((T = traverse(u)) > ans)
                ans = T;
        break;

        case 4:
        ans = p.value;
        break;

        case 5:
        ans = traverse(p.sub_packets[0]) > traverse(p.sub_packets[1]);
        break;

        case 6:
        ans = traverse(p.sub_packets[0]) < traverse(p.sub_packets[1]);
        break;

        case 7:
        ans = traverse(p.sub_packets[0]) == traverse(p.sub_packets[1]);
        break;

        default:
        exit(-1);
    }
    return ans;
}

int main() {
    scanf("%s", str);
    n = strlen(str);
    for (int i = 0; i < n; ++i) {
        int v = (str[i] > 64) ? (str[i] - 55) : (str[i] - 48);
        bin[(i << 2)] = (v >> 3) & 1; bin[(i << 2) | 1] = (v >> 2) & 1;
        bin[(i << 2) | 2] = (v >> 1) & 1; bin[(i << 2) | 3] = v & 1;
    }
    P.parse(bin);
    printf("%lld\n", traverse(P));
    return 0;
}