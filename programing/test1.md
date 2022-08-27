## Bài 1
In ra các số nguyên tố trong khoảng từ 5 đến 100

## Bài 2

Khai báo danh sách gồm 4 các user biết mỗi user gồm các thuộc tính 
```python
    ID
    Tên
    Tuổi
    Giới tính 
```

- Hiển thị những user có giới tính là nam
- Sắp sếp danh sách các user theo tuổi giảm dần


## Lời giải bài 1

### cách 1
```python

for i in range(5, 101):
    couter = 0
    for j in range(1, i+1):
        if i%j==0:
            couter += 1
    if couter == 2:
        print(i)


```
### cách 2
- tự nghĩ thêm nha còn nhiều cách lắm, ví dụ thay vì duyệt từ 2-i có thể duyệt từ 2- sqrt(i)

## bài 2

Tạm ổn, nhưng mà thấy có vẻ vẫn phức tạm hóa vấn đề :3 

```python
#trong mấy quyển sách bọn nó hay khai báo thế này cho nhanh =))) và rõ ràng chuẩn theo kiểu xml, json 
users = [
    {'id': 1, 'name': 'son 1', 'age': 16, 'gender': True},
    {'id': 2, 'name': 'son 1', 'age': 56, 'gender': True},
    {'id': 3, 'name': 'son 1', 'age': 26, 'gender': False},
    {'id': 4, 'name': 'son 1', 'age': 96, 'gender': False},
]
# cách 1
print([user for user in users if user['gender']==True])

# cách 2

for user in users:
    if user['gender'] == True:
        print(user)


# sắp sếp 
print('chua sap sep')
print(users)
#cài đặt chay cái thuật toán sắp sếp đơn giản nhất -_- 
#cái này khi học offline mình sẽ giai thích nó chạy như thế nào
for i in range(len(users)):
    for j in range(i+1, len(users)):
        if users[i]['age'] < users[j]['age']:
            # thuật toán đổi chỗ 2 phần tử của mảng
            user1 = users[i]
            users[i] = users[j]
            users[j] = user1

#in sau khi sắp sếp
print(users)


```
