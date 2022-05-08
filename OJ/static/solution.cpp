#include <bits/stdc++.h>

using namespace std;





int main() {

    int n,target;cin>>n;

     int a[n];

	for(int i=0;i<n;i++)cin>>a[i];

	cin>>target;

	

    

        vector<int> gatcha;

        

        for(int i = 0; i < n - 1; ++i){

            for(int j = i + 1; j < n; ++j){

                if(a[i] + a[j] == target){

                    gatcha = {i, j};

                }

            }

        }

        cout<<gatcha[0]<<" "<<gatcha[1];

    

	return 0;

}

           
                