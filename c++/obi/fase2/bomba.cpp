#include <bits/stdc++.h>

using namespace std;

//toda rua liga duas rotatorias
//possui uma faixa de pedestres com dois semaforos
//abrem nos minutos multiplos de 3 e fecham nos demais, outros fecham no multiplo de 3 e abrem nos demais
//toda rua leva exatamente 1 minuto para ser percorrida
//

int bel(vector<tuple<int,int,int>> &adj, int start, int end, int n){
    vector<int> dist(n, INT_MAX);
    dist[start] = 0;
    for(int i = 0; i < n-1; ++i){
        for(auto [u,v,t] : adj){
            int tempo = dist[u];
            int espera = 0;
            if(t == 1){
                if(tempo % 3 != 0){
                    espera = 3-(tempo%3);
                }
            }
            else{
                if(tempo%3 == 0){
                    espera = 1;
                }
            }
            int novo = tempo+espera+1;
            if(novo < dist[v]) dist[v] = novo;
        }
    }
    //cout << dist[end] << endl;
    if(dist[end] == INT_MAX){
        return -1;
    }else{
        return dist[end];
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n,e,s,m; // rotatorias(0 index), rotatoria entrada, rotatoria saida, numero de ruas
    cin >> n >> e >> s >> m;
    vector< tuple<int,int,int> > rot(m);
    for(int i = 0; i < m; ++i){
        int a,b,t; // origem da rua, destino, t=0 ou 1
        cin >> a >> b >> t;
        rot[i] = {a,b,t};
    }
    int dis = bel(rot, e, s, n);
    if(dis == -1) cout << '*';
    else cout << dis;

}