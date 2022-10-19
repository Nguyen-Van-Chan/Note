## Delegate trong C#
Trong javascript, function cũng xem như là 1 object, nên ta có thể truyền function vào như 1 param.
 Khi ta thử viết lại chương trình trên trong C#, ta phải khai báo kiểu dữ liệu cho parameter truyền vào, 
 vậy kiểu dữ liệu của function “tangqua” là gì?

		public void tangQua(string qua) {
		   Console.Write("Da tang " + qua);
		}
		 
		 //Kiểu dữ liệu cho params "vo" là Person, kiểu dữ liệu cho tangQua là gì???
		public void oNha(Person vo, tangQua){
		   var qua = "Quà đã nhận";
		   tangQua(qua);
		}
## Action, Predicate, Func trong C#

Ở phần này, mình xin giới thiệu về Action, Predicate, Func (Viết tắt là APF là cho nhanh) trong C#. Như các bạn đã đọc trong series C# hay ho, các lão developer trong Microsoft rất lười. Do đó họ luôn thêm thắt nhiều thứ trong C# để các developer chúng ta cũng lười như họ. APF thật ra là 1 cách lười hơn để chúng ta khai báo delegate.

Dưới đây là khái niệm cũng như cách dùng APF :
	- Action: Action<T in1, T in2, …>. Action tương đương 1 delegate với kiểu trả về là void, với in1, in2 là các params nhận vào.
	- Predicate: Predicate<T in>. Predicate tương đương 1 delegate với kiểu trả về là bool, với in là các param nhận vào. Predicate chỉ có thể nhận vào 1 param duy nhất.
	- Func: Func<T in1, T in2, … , T result>. Function tương đương 1 delegate với kiểu trả về do ta khai báo (result), in1, in2 là các params nhận vào. Func bắt buộc phải trả ra giá trị, không thể trả void.
	Để dễ hiểu, các bạn hãy tham khảo bảng sau. Đây là bảng so sánh các khai báo bằng delegate, cùng với cách khai báo tương ứng bằng Action, Predicate, Func:


		public void tangQua(string qua) {
		Console.Write("Da tang " + qua);
		}
		
		public void oNha(Person vo, Action tangQua)
		{
		var qua = "Quà đã nhận";
		tangQua(qua);
		}

- Có thể bạn sẽ thắc mắc: Ủa, mình có thấy người khác dùng Action, Predicate, … mấy đâu, biết làm gì?
Bạn sẽ ngạc nhiên khi biết AFP, kết hợp với lambda expression và vài thứ khác nữa ….,
 đã tạo nên sự “bá đạo” của LINQ, thứ mà Java thèm đỏ mắt mà không có, phải thêm vào ở Java SDK