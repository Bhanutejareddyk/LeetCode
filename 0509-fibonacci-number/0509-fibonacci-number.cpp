class Solution {
public:
    int fib(int n) {
        if(n <= 1){
            return n;
        }
         int num1 = 0;
        int num2 = 1;
        int nxt_num;
        for(int i=2;i<=n;i++){
           nxt_num = num1+num2;
           num1=num2;
           num2=nxt_num;
        }
        return num2;

       
    }
};