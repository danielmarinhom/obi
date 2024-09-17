//4/9, fase 2 2006

#include <bits/stdc++.h>

using namespace std;

int main(){
  //bfs que vai multiplicando o atual pelo valor matriz[i][j]
  int n;
  cin >> n;

  int matriz[n][n];
  bool visited[n][n] = {false};
  for(int i = 0; i < n; i++){
    for(int j = 0; j < n; j++)
      cin >> matriz[i][j];
  
  int value;
  queue<pair<int,int>> q;
  int dy[] = {0, 1};
  int dx[] = {1, 0}; //nslo (0,1)(1,0)
  q.push({0,0});
  visited[0][0] = true;
  while(!q.empty()){
    int x = q.front().first;
    int y = q.front().second;
    if(x == n and y == n){
      break;
    }
    q.pop();
    for(int i = 0; i < 2; i++){
      int nx = x + dx[i];
      int ny = y + dy[i];
      if(nx >= 0 and nx < n and )
      value *= matriz[nx][ny];
    }
  }
}