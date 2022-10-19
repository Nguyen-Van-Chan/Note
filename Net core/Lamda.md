## Lambda expression
- Ta có thể hiểu lambda expression là 1 cách viết anonymous function ngắn gọn hơn:

		//Cách cũ
		TangQuaDelegate dlg = delegate(string qua) { Console.WriteLine("Tặng quà" + qua); };
		 
		//Dùng lambda expression
		TangQuaDelegate lamdaDlg = (qua) => { Console.WriteLine("Tặng quà: " + qua); }
		 
		//Câu lệnh đầy đủ của lambda expression.
		//Dấu "=>" gọi là go-to
		(parameters) => { statement }

- Dưới đây là một số qui tắc viết lambda expression:

		//1. Có thể bỏ qua kiểu dữ liệu của parameter truyền vào
		(string qua) => {Console.WriteLine("Tặng quà: " + qua);}
		(qua) => {Console.WriteLine("Tặng quà: " + qua);}
		 
		//2. Nếu không có parameter, bỏ dấu () trống
		() => {Console.WriteLine("Hello");}
		 
		//3. Nếu chỉ có 1 parameter, có thể bỏ luôn dấu ()
		(x) => {Console.WriteLine("Hello " + x);}
		x => {Console.WriteLine("Hello " + x);}
		 
		//4. Nếu có nhiều parameter, ngăn cách bằng dấu phẩy
		(x, y) => {Console.WriteLine("Hello " + x + y);}
		 
		//5. Nếu anonymous function chỉ có 1 câu lệnh, có thể bỏ dấu {}
		x => { Console.WriteLine("Hello " + x); }
		x => Console.WriteLine("Hello " + x)
		 
		//6. Nếu chỉ return 1 giá trị, có thể bỏ chữ return.
		//4 lambda expression sau tương đương nhau
		(x) => { return x > 4; }
		x => { return x > 4; }
		x => return x > 4
		x => x > 4
		
- Tới đây, có bạn sẽ ồ lên kinh ngạc: “À, ra vậy”. Đây là cách ta áp dụng các bước trên để rút gọn 1 lambda expression.

////image

- Cũng có bạn sẽ thắc mắc: Ớ, tưởng lambda expression là gì ghê gớm chứ, hóa ra đơn giản thế thôi à.
 Vâng, vì nó đơn giản thế nên nhiều bạn sử dụng nó mà không biết tên gọi cũng như chính xác nó là gì.

## Lambda Expression và LINQ

- Đã có bao giờ bạn xem thử param truyền vào cho 1 hàm của LINQ như Where, First là gì chưa?. Vâng, nó chính là 1 delegate cho một function có kiểu trả về là bool 

- Do đó, ta sử dụng lambda expression để truyền 1 anonymous function vào hàm Where hoặc First. Ví dụ, khi dùng hàm Where của LINQ để tìm những phần tử trong 1 mảng:

var studentList = new List<Student>();
 
		//Thứ đẹp đẽ ngắn gọn này là lambda expression
		var students = studentList.Where(stu => stu.Age > 20);
		
		//Nếu không có nó, ta phải viết cái thứ vừa dài dòng vừa gớm ghiếc như sau
		var student = studentList.Where(new delegate(Student stu) { return stu.Age > 20; });
		
		//Hoặc tệ hơn
		public bool FindStudentWithAge(Student stu) { return stu.Age > 20; }
		var student = studentList.Where(FindStudentWithAge);
