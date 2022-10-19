## 1 Single responsibility principle
- Nguyên lý đầu tiên, tương ứng với chữ S trong SOLID. Nội dung nguyên lý:Một class chỉ nên giữ 1 trách nhiệm duy nhất (Chỉ có thể sửa đổi class với 1 lý do duy nhất)
Để hiểu nguyên lý này, ta hãy lấy ví dụ với 1 class vi phạm nguyên lý. Ta có 1 class như sau

        public class ReportManager()
        {
        public void ReadDataFromDB();
        public void ProcessData();
        public void PrintReport();
        }

-- Class này giữ tới 3 trách nhiệm: Đọc dữ liệu từ DB, xử lý dữ liệu, in kết quả. Do đó, chỉ cần ta thay đổi DB, thay đổi cách xuất kết quả, … ta sẽ phải sửa đổi class này. Càng về sau class sẽ càng phình to ra. Theo đúng nguyên lý, ta phải tách class này ra làm 3 class riêng. Tuy số lượng class nhiều hơn những việc sửa chữa sẽ đơn giản hơn, class ngắn hơn nên cũng ít bug hơn.

## 2. Open/closed principle
- Nguyên lý thứ hai, tương ứng với chữ O trong SOLID. Nội dung nguyên lý:
Có thể thoải mái mở rộng 1 class, nhưng không được sửa đổi bên trong class đó 
(open for extension but closed for modification).
Theo nguyên lý này, mỗi khi ta muốn thêm chức năng,.. cho chương trình, chúng ta nên viết class mới mở rộng class cũ ( bằng cách kế thừa hoặc sở hữu class cũ) không nên sửa đổi class cũ.

## 3. Liskov Substitution Principle
- Nguyên lý thứ ba, tương ứng với chữ L trong SOLID. Nội dung nguyên lý:
Trong một chương trình, các object của class con có thể thay thế class cha mà không làm thay đổi tính đúng đắn của chương trình
- Hơi khó hiểu? Không sao, lúc mới đọc mình cũng vậy. Hãy tưởng tượng bạn có 1 class cha tên Vịt. Các class VịtBầu, VịtXiêm có thể kế thừa class này, chương trình chạy bình thường. Tuy nhiên nếu ta viết class VịtChạyPin, cần pin mới chạy được. Khi class này kế thừa class Vịt, vì không có pin không chạy được, sẽ gây lỗi. Đó là 1 trường hợp vi phạm nguyên lý này.

## 4. Interface Segregation Principle
- Nguyên lý thứ tư, tương ứng với chữ I trong SOLID. Nội dung nguyên lý:
Thay vì dùng 1 interface lớn, ta nên tách thành nhiều interface nhỏ, với nhiều mục đích cụ thể
Nguyên lý này khá dễ hiểu. Hãy tưởng tượng chúng ta có 1 interface lớn, khoảng 100 methods. Việc implements sẽ khá cực khổ, ngoài ra còn có thể dư thừa vì 1 class không cần dùng hết 100 method. Khi tách interface ra thành nhiều interface nhỏ, gồm các method liên quan tới nhau, việc implement và quản lý sẽ dễ hơn.

## 5. Dependency inversion principle

- guyên lý cuối cùng, tương ứng với chữ D trong SOLID. Nội dung nguyên lý:

1. Các module cấp cao không nên phụ thuộc vào các modules cấp thấp. 
   Cả 2 nên phụ thuộc vào abstraction.
2. Interface (abstraction) không nên phụ thuộc vào chi tiết, mà ngược lại.
( Các class giao tiếp với nhau thông qua interface, 
không phải thông qua implementation.)
Nguyên lý này khá lắt léo, mình sẽ lấy ví dụ thực tế. Chúng ta đều biết 2 loại đèn: đèn tròn và đèn huỳnh quang. Chúng cùng có đuôi tròn, do đó ta có thể thay thế đèn tròn bằng đèn huỳnh quanh cho nhau 1 cách dễ dàng.

- Ở đây, interface chính là đuôi tròn, implementation là bóng đèn tròn và bóng đèn huỳnh quang. Ta có thể swap dễ dàng giữa 2 loại bóng vì ổ điện chỉ quan tâm tới interface (đuôi tròn), không quan tâm tới implementation.

- Trong code cũng vậy, khi áp dụng Dependency Inverse, ta chỉ cần quan tâm tới interface. Để kết nối tới database, ta chỉ cần gọi hàm Get, Save … của Interface IDataAccess. Khi thay database, ta chỉ cần thay implementation của interface này.