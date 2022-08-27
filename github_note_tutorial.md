# Get started with github
halo chào các bạn mình là sơn v

## step 1
Cài đặt GITHUB tại  https://git-scm.com/download/win
## bước 2 quy trình làm việc với git:

Manager
-  có 1 ông project manager có quyền review code  của mọi người
-  merge code (hợp đống code mà mọi người mới code vào cái đống đã tồn tại, )

Member
- Pull về (tải cái code mới nhất về)(có 1 ông A và một ông B 2 ông này làm việc trên một kho code C, và 1 ông manager D, ông A viết đc 100 dòng code
và được ông D review ông D comment bảo với ông A rằng ``Dòng số 90 chú code lởm k đc code lại đi ``
Ông A sau khi đọc comment của ông D và sửa code của mình, Sau khi sửa xong ông A gửi yêu cầu merge lại tới ông D. ông D thấy OK
Ông d merge code của ông A vào kho chính, ông B code cần tải code mới nhất mà ông A vừa code về (lệnh pull)
)
- sao chép code từ nhánh chính
- tạo nhánh phụ
- yêu cầu merge vào nhánh chính

## bước 3 Tải project về như thế nào
``git clone <link project >``

Ví dụ: ``git clone https://github.com/nguyenthihangtn1996/Note.git ``

## bước 4 tạo nhánh mới 
``git checkout -b ten_nhanh``

Ví dụ: ``git checkout -b dangphattrien``
sửa code bình thường, 


## bước 5 check code 

kiểm tra xem mình vừa sửa cái gì, sửa những file nào
sử dụng lệnh: ``git status`` sẽ hiển thị ra các file vừa sửa
sau đó dùng lệnh ``git add <tenfile> `` <- add 1 file, theo dõi 1 file
``git add <tenfile_so1> <tenfile_so2> <tenthumuc>`` sẽ add cái file có tến hoặc tất cả các file có trong thư mục

``git add .`` add hết những file có trong thư mục đó

## Bước 6 commit dể chuẩn bị up load lên server

Bước này cần ghi tóm tắt commit này thêm chức năng gì

ví dụ vừa làm xong chức năng đặt hàng 
sử dụng lệnh ``git commit -m 'mô tả ngắn của commit'``

## Bước 6.5 bước đẩy code lên server
 ``git push``

## bước 7 cách pull code về update

Khi có một người khác trong team thêm code về master, thì mình cần update code mới nhất của master về
sử dụng lệnh

``git pull origin master`` 
