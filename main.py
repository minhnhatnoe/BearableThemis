code = '''
// Judges with GCC >= 12 only needs Ofast
// #pragma GCC optimize("O3,no-stack-protector,fast-math,unroll-loops,tree-vectorize")
// MLE optimization
// #pragma GCC optimize("conserve-stack")
// Old judges
// #pragma GCC target("sse,sse2,sse3,ssse3,sse4,sse4.1,sse4.2,popcnt,lzcnt,abm,mmx,avx,fma,bmi,bmi2")
// New judges. Test with assert(__builtin_cpu_supports("avx2"));
// #pragma GCC target("avx2,popcnt,lzcnt,abm,bmi,bmi2,fma,tune=native")
// Atcoder
// #pragma GCC target("avx2,popcnt,lzcnt,abm,bmi,bmi2,fma")
// #pragma GCC optimize("O2")
#ifndef NHAT
    #define NDEBUG
#endif
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
#define endl "\n"
const long MOD = 1000000007;
#ifdef NHAT
    #define dump(x) cerr << __LINE__ << ": " << #x << " " << (x) << endl
#else
    #define dump(x) void(0)
#endif
vector<vector<int>> g;
struct testcase{
    int a, b, k;
    vector<int> cnt;
    queue<int> q;
    void print(){
        int c = 0;
        for (int i=a; i<=b; i++){
            if (cnt[i]){
                c++;
            }
        }
        cout << c << endl;
    }
    void remove(int v){
        cnt[v] = 0;
        for (int e: g[v]){
            if (cnt[e]){
                cnt[e]--;
                if (cnt[e] == k-1) q.push(e);
            }
        }
    }
    testcase(int a, int b, int k): a(a), b(b), k(k){
        cnt.assign(g.size(), 0);
        for (int i=a; i<=b; i++){
            for (int e: g[i]){
                if (a <= e && e <= b){
                    cnt[i]++;
                }
            }
        }
        for (int i=a; i<=b; i++){
            if (cnt[i] < k) q.push(i);
        }
        while (q.size()){
            int tp = q.front();
            q.pop();
            remove(tp);
        }
        print();
    }
};
int main(){
    cin.tie(0)->sync_with_stdio(0);
    #ifdef NHAT
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
        freopen("log.txt", "w", stderr);
        auto start_time = chrono::high_resolution_clock::now();
    #else
        freopen("GROUP.inp","r", stdin);
        freopen("GROUP.out","w", stdout);
    #endif
    
    int n, m; cin >> n >> m;
    g.resize(n);
    for (int i=0; i<m; i++){
        int u, v; cin >> u >> v;
        u--, v--;
        g[u].push_back(v);
        g[v].push_back(u);
    }
    int t; cin >> t;
    for (int i=0; i<t; i++){
        int start, end, k; cin >> start >> end >> k;
        testcase(start-1, end-1, k);
    }

    #ifdef NHAT
        auto end_time = chrono:: high_resolution_clock::now();
        double time_delta = chrono::duration_cast<chrono::milliseconds> (end_time-start_time).count();
        cout << "\n[" << time_delta << "ms]\n";
    #endif
}'''
import datetime
from src.api.themis import ThemisInstance
from src.api.submission import Submission
from src.validators.sequential import Sequential
import asyncio

async def testing():
    inst = ThemisInstance("E:\\themistesting\\osd", ["B05"], Sequential())
    result = await inst.submit(Submission("B05", "GROUP", "cpp", code, "abc", datetime.datetime.now()))
    print(result)

asyncio.run(testing())