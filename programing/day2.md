## Bài 1 in các số hoàn hảo trong khoảng a -> b 
1. Python code (mình không sử dụng những cú pháp viết tắt trong python nhé)
```python 
a = int(input("nhap vao so a: "))
b = int(input("nhap vao so b: "))

if a > b:
    c = a
    a = b
    b = c

def is_perfect_number(number):
    total = 0
    for i in range(1, number):
        if number%i==0:
            total += i
    if total == number:
        return True
    else:
        return False

for i in range(a, b+1):
    if is_perfect_number(i):
        print(i)
        
```
2. C++ code 
```cpp                                                                                               

#include <iostream>

using namespace std;

bool is_perfect_number(int number) {
    int total =  0;
    for(int i=1; i<number; i++) {
        if(number%i==0) {
            total += i;
        }
    }
    if(total == number) {
        return true;
    }
    else {
        return false;
    }
}

int main() {
    int a, b;
    cout<<"nhap vao a=";
    cin>>a;
    cout<<"nhap vao b=";
    cin>>b;
    if(a > b) {
        int temp = a;
        a = b;
        b = temp;
    }

    for(int i = a; i <= b; i++) {
        if(is_perfect_number(i) == true) {
            cout<<i<<endl;
        }
    }

}

```
