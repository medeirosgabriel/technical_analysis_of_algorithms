#include <bits/stdc++.h>
#define ll long long

using namespace std;

int main () {
    ll quant_n, i;
    //scanf("%ld", &quant_n);
    cin >> quant_n;

    ll numbers[200000];
    for (i = 0; i < quant_n; i++) {
        //scanf("%ld", &numbers[i]);
        cin >> numbers[i];
    }

    if (quant_n == 1) {
        cout << 1 << endl;
        cout << 1 << endl;
    } else {
        map<ll, ll> dp;
        ll maxdp = 0, indexn = 0, n = 0;
        for (i = 0; i < quant_n; i++) {
            ll ant_key = numbers[i] - 1;
            dp[numbers[i]] = dp[ant_key] + 1;
            if (dp[numbers[i]] > maxdp) {
                maxdp = dp[numbers[i]];
                indexn = i;
                n = numbers[i];
            }
        }

        cout << maxdp << endl;

        ll pos = indexn - 1, x = n - 1;
        vector<ll> out;
        while (pos >= 0) {
            if (numbers[pos] == x) {
                out.push_back(pos + 1);
                x --;
                pos --;
            } else {
                pos--;
            }
        }

        for (auto index = out.rbegin(); index != out.rend(); ++index) {
            cout << *index << " ";
        }

        cout << indexn + 1 << endl;
    }
}