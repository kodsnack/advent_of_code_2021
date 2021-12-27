#include <stdio.h>

#include <map>
#include <set>
#include <vector>
#include <string>

std::map< std::string, std::vector<std::string> > M;
char str1[1005], str2[1005];
int ans;

void add_edge(std::string f, std::string t) {
	if (t != "start")
		if (M.count(f)) M[f].push_back(t);
		else M[f] = (std::vector<std::string>) { t };
}

void dfs(std::string node, std::set<std::string> passed, bool twice) {
	if (node == "end") {
		++ans;
		return;
	}
	for (std::string p : M[node]) {
		if (!passed.count(p)) {
			std::set<std::string> S = passed;
			if (p[0] >= 'a') S.insert(p);
			dfs(p, S, twice);
		} else if (!twice) {
			dfs(p, passed, true);
		}
	}
}

int main() {
	while (~scanf(" %[^-]-%s", str1, str2)) {
		add_edge(str1, str2);
		add_edge(str2, str1);
	}
	dfs("start", std::set<std::string>(), false);
	printf("%d\n", ans);
	return 0;
}
