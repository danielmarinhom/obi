#include <bits/stdc++.h>
//#include <queue>

using namespace std;

const int MAX = 100;
int n,m;
int grid[MAX*MAX]; //matriz linear
bool visited[MAX*MAX];
int dist[MAX*MAX];

int dx[] = {0, 0, 1, -1}; //nsloe, (0,-1),(0,1),(1,0),(-1,0)
int dy[] = {-1, 1, 0, 0};

bool isValid(int pos){
  int x = pos / m; //formula para converter x linearizado em x da matriz
  int y = pos % m; //formula para converter y linearizado em y da matriz
  return x >= 0 and x < n and y >= 0 and y < m; 
}

void bfs(int start){
  queue<int> q;
  q.push(start);
  visited[start] = true;
  dist[start] = 0;
  while(!q.empty()){
    int cur = q.front();
    q.pop();
    int x = cur / m;
    int y = cur % m;
    cout << "(" << x << y << ")" << " dist: " << dist[cur];
    for(int i = 0; i < 4; i++){
      int newX = x + dx[i];
      int newY = y + dy[i];
      int newpos = newX * m + newY;
      if(isValid(newpos) and !visited[newpos]){
        visited[newpos] = true;
        dist[newpos] = dist[cur] + 1;
        q.push(newpos);
      }
    }
  }
}

int main(){
  cin >> n >> m;
  for(int i = 0; i < n*m; i++){
    cin >> grid[i];
    visited[i] = false;
  }

}