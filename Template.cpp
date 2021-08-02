#include <bits/stdc++.h>

using namespace std;
using namespace std::chrono;

using ll = long long;
using ld = long double;

#define TESTING

#ifdef TESTING
#define DEBUG                  fprintf(stderr, "====TESTING====\n") 
#define VALUE(x)               cerr << "The value of " << #x << " is " << x << endl 
#define debug(...)             fprintf(stderr, __VA_ARGS__) 
#else 
#define DEBUG 
#define VALUE(x) 
#define debug(...) 
#endif

#define rep(i,a,b)              for(int i = (a); i < (b); i++)
#define per(i,a,b)              for(int i = (a); i > (b); i--)
#define repl(i,a,b)             for(ll i = (a); i < (b); i++)
#define perl(i,a,b)             for(ll i = (a); i > (b); i--)
#define tr(ii,c)                for(__typeof((c).begin()) ii=(c).begin();ii!=(c).end();ii++)
#define maX(a,b)                ((a) > (b) ? (a) : (b))
#define miN(a,b)                ((a) < (b) ? (a) : (b))
#define max3(A,B,C)             max(max((A),(B)),(C))
#define max4(A,B,C,D)           max(max((A),(B)),max((C),(D)))
#define min3(A,B,C)             min(min((A),(B)),(C))
#define min4(A,B,C,D)           min(min((A),(B)),min((C),(D)))

typedef pair<int, int>           pii;
typedef pair<ll, ll>             pll;
typedef pair<string, string>     pss;
typedef vector<int>              vi;
typedef vector<vi>               vvi;
typedef vector<pii>              vii;
typedef vector<ll>               vl;
typedef vector<vl>               vvl;

const ll MOD                    = 1e9+7;
const ll MAXN                   = 1e6; 
const ll INF                    = 1e15-1;
const ld EPS                    = 1e-8;

ll gcd(ll A,ll B) {if(B==0) return A; return gcd(B,A%B);}


void solve(){
    
}


int main(){
    #ifndef ONLINE_JUDGE
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    auto start = high_resolution_clock::now();
    #endif
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    int t = 1;
    //ll t = 1;
    cin >> t;  
    // Comment out above if only 1 test case
    //t = 1;
    while(t--)solve();

    #ifndef ONLINE_JUDGE
        auto stop = high_resolution_clock::now();auto duration = duration_cast<milliseconds>(stop - start);cerr << "Time taken: "<< duration.count() << " ms" << endl;
    #endif
    return 0;
}