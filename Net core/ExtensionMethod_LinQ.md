##  Từ khóa “var” và Anonymous Object

- Ngày trước, khi khai báo 1 biến, chúng ta phải khai báo type của biến đó (Ở đây là stream).
        Stream stream = new FileStream("C:\\abc.txt", FileMode.CreateNew);
- Tuy nhiên, với từ khóa var, chúng ta có thể khai báo biến mà không cần quan tâm đến type. Các chức năng nhắc lệnh vẫn được thực hiện bình thường.
        var stream = new FileStream("C:\\abc.txt", FileMode.CreateNew);
- Kết hợp với anonymous object, ta có thể khai báo 1 object với các properties định sẵn, không cần phải khai báo class:
        var sampleObj = new { FirstProp = "A", SecondProp = "B"};
        Console.WriteLine(sampleObj.FirstProp + sampleObj.SecondProp ); //AB
- Anonymous object này có thể được serialize thành XML, JSON. Có thể nói từ khóa “var” là 1 cứu cánh cho những developer “lười” như mình. (Nói nhỏ các bạn nghe, trong Java không có anonymous object cũng như từ khóa “var” này đâu).

## Tự động tạo Properties
- Khi được học về tính bao đóng (Encapsulation) trong trường đại học, chúng ta đều được dạy là không nên access trực tiếp field của object, mà phải thông qua các method như sau.
        public class Student
        {
            private string _name;
            public string Name
            {
                get { return _name; }
                set { _name = value; }
            }
        }
- Với C#, khi ta khai báo 1 auto-property, ngôn ngữ sẽ tự tạo 1 field private, gettter và setter cho field đó. Ta còn có thể set private cho getter và setter đó. Code mới như sau:
        public string Name { get; set; }       
        public string Name { get; private set; } //Field is read only, private setter

## using blocks

Ngày xửa ngày xưa,khi chưa có using, mỗi khi muốn đóng 1 stream, connection, ta thường cho vào block try/finally.
        try
        {
            stream = new FileStream("C:\\abc.txt", FileMode.CreateNew);
            stream2 = new FileStream("C:\\abc2.txt", FileMode.CreateNew);
        //Do some readding
        }
        finally
        {
            if (stream != null) stream.Close();
            if (stream2 != null) stream2.Close();
        }
- Sau 1 thời gian, đống code này sẽ khá rối. Với using, ta không cần phải lo chuyện đóng connection bằng tay, code ngắn và dễ hiểu hơn nhiều
        using(var stream = new FileStream("C:\\abc.txt", FileMode.CreateNew))
        using(var stream2 = new FileStream("C:\\abc.txt", FileMode.CreateNew))
        {
        //Do some readding
        }
## Đo thời gian với class Stopwatch

- Đo thời gian 1 method chạy chỉ với 2 dòng code, StartNew và Stop, vô cùng đơn giản.
        var sw = Stopwatch.StartNew();
        DoSomething();
        sw.Stop();
        Console.WriteLine("Time elapsed: " + sw.ElapsedMilliseconds);
## Toán tử 3 ngôi, toán tử null
- Thông thường, khi gán giá trị default cho 1 biến null, ta thường set bằng 1 trong 2 cách sau
        if (input == null)
        {
        input = "default";
        }
        
        // Toán tử 3 ngôi
        input = input != null ? input : "default";

- Với C#, ta có toán tử null, giúp code ngắn hơn và dễ đọc hơn
        input = input ?? "default"; //Nếu index là null thì set bằng default
- Việc implement một toán tử nhỏ nhặt thế này trong ngôn ngữ cho thấy các bạn developer của Microsoft rất biết suy nghĩ cho giới developer chúng ta.

## Khởi tạo object và collection
- Thông thường, khi khởi tạo object và property, ta thường làm như sau
        Student student = new Student();
        student.Name = "Hoang";
        student.Age = 10;
- Với C#, mọi chuyện trở nên đơn giản ngắn gọn hơn
        Student student = new Student { Name = "Hoang", Age = 10};
- Có thể bạn sẽ hỏi: Tại sao không tạo constructor cho object, cũng vậy thôi mà. Mình xin trả lời: Khi tạo constructor, ta phải khai báo toàn tham số truyền vào. Với cách này, ta có thể truyền vào số lượng tham số ta muốn (Ví dụ object student có 10 fields, ta chỉ muốn set 2 fields).
- Tiếp theo là khởi tạo 1 collection, cách thông thường và cách C#. Cách nào ngắn gọn, dễ hiểu hơn các bạn tự thấy nhỉ.
        //Cách cũ
        List<string> list = new List<string>();
        list.Add("string 1");
        list.Add("string 2");
        list.Add("string 3");
        
        //Cách mới
        List<string> list = new List<string> { "string 1" , "string 2", "string 3" };
        Kết hợp cả class và collection

        1
        2
        3
        4
        5
        List<Student> list = new List<Student>
        {
            new Student { Name = "Student 2", Age = 2},
            new Student { Name = "Student 3", Age = 4}
        };
## Extension method
- Có 1 số trường hợp, ta muốn thêm method cho một số class sealed, hoặc class từ các library khác. Với một số ngôn ngữ, điều này là ko thể được, nhưng với C#, chúng ta có thể dùng extension method.
VD ở đây, chúng ta có class Student từ library khác, không thể sửa code. Ta muốn thêm method Print.
        public class Student
        {
            public string Name { get; set; }
            public int Age { get; set; }
        }
- Chúng ta tạo 1 extenstion class, class này phải là static class, method cũng phải static, params đầu tiên truyền vào là class cần extention, với từ khóa this.
        public static class StudentExtension
        {
        public static void Print(this Student student)
        {
            Console.WriteLine(student.ToString());
        }
        }
        //Sử dụng
        var student = new Student();
        student.Print();
- Trong quá trình tìm hiểu, bạn sẽ thấy extension method rất hữu dụng. (Nói nhỏ nữa là trong Java không có cái extension method này đâu hen).

## LINQ
- Linq khá dễ sử dụng, nhưng để hiểu nó cần biết về Predicate, Func, lambda v…v, mình sẽ dành 1 bài viết để nói rõ hơn. Ở đây mình chỉ giới thiệu sợ, vì sao nó hay.
- Ngày xưa, khi chưa có linq, giả sử ta muốn tìm những học sinh có tuổi <20 trong list, ta cần viết code dài như sau:
        var studentsUnder20 = new List<Student>();
        foreach (var student in students)
        {
            if (student.Age < 20) studentsUnder20.Add(student);
        }
- Ngày nay, với linq, ta chỉ cần đúng 1 dòng code:
        var studentsUnder20 = students.Where(student => student.Age < 20);

- Dấu “=>” là dấu gì. Toàn bộ cụm “stu => stu.Age < 20” được gọi là gì? Dấu “=>” là dấu “go-to”, toàn bộ cụm đi kèm là 1 lambda expression. Bản chất của lambda expression là 1 anonymous method.
-Hàm Where được viết như thế nào, nhận parameter gì vào, trả ra giá trị gì? Hàm Where là 1 extension method của class IEnumerable, nhận vào 1 delegate với kiểu trả về là bool, trả ra 1 IEnumerable đã filter.
- Tại sao IDE tại biết stu là 1 Student để có thể nhắc lệnh? Ở đây ta sử dụng lambda expression, stu là 1 param của hàm. Do Linq sử dụng generic, list students là 1 list với kiểu dữ liệu Student. do đó C# tự hiểu stu là 1 param với kiểu dữ liệu Student.
- Có thể viết 1 thứ tương tự như LINQ trong javascript không? Có thể. Bạn có thể tìm hiểu thêm về underscore và lodash, 2 thư viện hỗ trợ linq cho javascript.   