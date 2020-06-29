package backpack_problems

/*
	有N件物品和一个容量为V的背包。
	第i件物品的费用是c[i]，价值是w[i]。
	求解将哪些物品装入背包可使价值总和最大。

	01背包问题的特点是：每种物品只有一件，并且可以选择放或者不放
	用子问题定义状态：即f[i][v]表示前i件物品恰放入一个容量为v的背包可以获得的最大价值。

				f[i][v]=max{f[i-1][v], f[i-1][v-c[i]]+w[i]}

	“将前i件物品放入容量为v的背包中”这个子问题，若只考虑第i件物品的策略（放或不放），那么就可以转化为一个只牵扯前i-1件物品的问题。
	1. 	如果不放第i件物品，那么问题就转化为“前i-1件物品放入容量为v的背包中”，价值为f[i-1][v]。
	2. 	如果放第i件物品，那么问题就转化为“前i-1件物品放入剩下的容量为v-c[i]的背包中”，此时能获得的最大价值就是f[i-1][v-c[i]]，
		   再加上通过放入第i件物品获得的价值w[i]。

	以上方法的时间和空间复杂度均为O(VN)，其中时间复杂度应该已经不能再优化了，但空间复杂度却可以优化到O(V)。
*/

// 测试代码地址： https://www.acwing.com/problem/content/2/

#include <bits/stdc++.h>
using namespace std;

// 使用二维数组的01背包解法
int solve_01_backpack(vector<int>& v, vector<int>& w, int N, int V) {
    vector<vector<int>> f(N + 1, vector<int>(V + 1, 0));

    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= V; j++) {
            if (j >= v[i]) {
                f[i][j] = max(f[i-1][j], f[i-1][j-v[i]] + w[i]);
            } else {
                f[i][j] = f[i-1][j];
            }
        }
    }
    return f[N][V];
}

// 使用一维数组的01背包解法
int solve_01_backpack_1d(vector<int>& v, vector<int>& w, int N, int V) {
    vector<int> f(V + 1);
    for (int i = 1; i <= N; i++) {
        for (int j = V; j >= v[i]; j--) {
            f[j] = max(f[j], f[j-v[i]] + w[i]);
        }
    }
    return f[V];
}


// f 里面的虽然是 0 ~ 之前的item所能够产生的最优结果，
// 这里我们却可以把它看成一个固有的值，即在不同容量下的增益，从而只关注当前的item
// 这个函数在后面的背包问题中还会被用到
void ZeroOnePack(vector<int>& f, int v, int w) {
    int V = f.size() - 1;
    for (int j = V; j >= v; j--) {
        f[j] = max(f[j], f[j-v]+w);
    }
}

// 对于每个item来说，其前面的items对f数组造成的在不同容量下的增益偏置与当前的item无关
// 因为我们将其抽象为一个单独的求解函数，用来针对某一个item进行求解。
int solve_01_backpack_simple(vector<int>& v, vector<int>& w, int N, int V) {
    vector<int> f(V + 1);
    for (int i = 1; i <= N; i++) {
        ZeroOnePack(f, v[i], w[i]);
    }
    return f[V];
}

int main() {
    int N, V;
    cin >> N >> V;
    vector<int> v(N+1), w(N+1);
    for (int i = 1; i <= N; i++) {
        cin >> v[i] >> w[i];
    }
    
    cout << solve_01_backpack_simple(v, w, N, V) << endl;
    return 0;
}
