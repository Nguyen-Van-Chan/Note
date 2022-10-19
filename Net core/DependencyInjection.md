## Quản lý vòng đời (lifetime) Service
- Bất cứ khi nào chúng ta yêu cầu service, DI Container sẽ quyết định xem có tạo mới một thể hiện (instance) hay sử dụng lại thể hiện đã tạo từ trước đó. Vòng đời của Service phụ thuộc vào khi khởi tạo thể hiện và nó tồn tại bao lâu. Chúng ta định nghĩa vòng đời khi đăng ký service.

- Có 3 mức độ vòng đời, bằng cách này chúng ta có thể quyết định mỗi service có vòng đời ra sao.
    - Transient: Một thể hiện mới luôn được tạo, mỗi khi được yêu cầu.
    - Scoped: Tạo một thể hiện mới cho tất cả các scope (Mỗi request là một scope). Trong scope thì service  - được dùng lại
    - Singleton: Service được tạo chỉ một lần duy nhất.

## Project ví dụ
 - Hãy tạo một project ví dụ để demo vòng đời của Service. Tạo một ứng dụng ASP.NET Core sử dụng Empty Template và gọi nó là DependencyInjection. Thêm HomeController với Index method. Bạn có thể theo bài viết trước.

- Tạo mới service tên là SomeService trong thư mục Services. Thêm mới 3 interface. Mỗi interface tương ứng với một vòng đời trong ASP.NET Core. Interface thật đơn giản chúng chứa mỗi phương thức GetID trả về một Guid.

        public interface ITransientService
        {
            Guid GetID();
        }

        public interface IScopedService
        {
            Guid GetID();
        }

        public interface ISingletonService
        {
            Guid GetID();
        }

- Tạo một Service: Giờ chúng ta sẽ tạo một service đơn lẻ, triển khai cả 3 interface kia:

        public class SomeService : ITransientService, IScopedService, ISingletonService
        {
            Guid id;
            public SomeService()
            {
                id = Guid.NewGuid();
            }

            public Guid GetID()
            {
                return id;
            }
        }

- Service tạo ra một ID duy nhất và nó sẽ được khởi tạo và trả về id trong phương thức GetID. Giờ hãy xem chi tiết

## Transient
- Transient Service luôn tạo mới mỗi lần service được yêu cầu

- Đăng ký Transient Service
Giờ bên trong phương thức ConfigureServices của Startup sẽ đăng ký SomeService thông qua ITransientService interface.

        services.AddTransient<ITransientService, SomeService>();

- Inject vào Controller
Mở HomeController ra và inject 2 thể hiện của SomeService như dưới đây:

        public class HomeController : Controller
        {
            ITransientService _transientService1;
            ITransientService _transientService2;

            public HomeController(ITransientService transientService1,
                                ITransientService transientService2)
            {
                _transientService1 = transientService1;
                _transientService2 = transientService2;
            }

            public IActionResult Index()
            {

                ViewBag.message1 ="First Instance " + _transientService1.GetID().ToString();
                ViewBag.message2 ="Second Instance "+ _transientService2.GetID().ToString();

                return View();
            }
        }

- Đầu tiên, chúng ta inject 2 thể hiện của service thông qua interface ITransientService trong constructor của HomeController.

        public HomeController(ITransientService transientService1,ITransientService transientService2)

- Tiếp theo, chúng ta gọi phương thức GetID trong mỗi thể hiện và gán nó vào view sử dụng ViewBag.

        ViewBag.message1 ="First Instance " + _transientService1.GetID().ToString();
        ViewBag.message2 ="Second Instance "+ _transientService2.GetID().ToString();

- View: Mở view và thêm code:

        <h3>Transient Service</h3>
        @ViewBag.message1
        </br>
        @ViewBag.message2

- Chạy ứng dụng và bạn sẽ nhìn thấy 2 Guid khác nhau hiển thị trên màn hình. Bằng chứng là chúng ta đã nhận 2 thể hiện của Transient service.

 
## Scoped: 
- Các service với vòng đời Scoped được tạo chỉ một lần cho mỗi request (scope). Một thể hiện mới được tạo cho mỗi request và thể hiện được dùng lại trong request.

- Đăng ký Scoped Service
Trong phương thức ConfigureServices đăng ký SomeService sử dụng phương thức AddScoped sử dụng IScopedService interface.

        services.AddScoped<IScopedService, SomeService>();

- Inject scoped service vào Controller: Tiếp theo inject service này vào Controller. Chúng ta đã có transient service được inject vào controller. Giờ không thay đổi gì nhưng thêm mới:

        public class HomeController : Controller
        {

            ITransientService _transientService1;
            ITransientService _transientService2;

            IScopedService _scopedService1;
            IScopedService _scopedService2;


            public HomeController(ITransientService transientService1,
                                ITransientService transientService2, 
                                IScopedService scopedService1,
                                IScopedService scopedService2)
            {
                _transientService1 = transientService1;
                _transientService2 = transientService2;

                _scopedService1 = scopedService1;
                _scopedService2 = scopedService2;
            }

            public IActionResult Index()
            {

                ViewBag.message1 ="First Instance " + _transientService1.GetID().ToString();
                ViewBag.message2 ="Second Instance "+ _transientService2.GetID().ToString();

                ViewBag.message3 = "First Instance " + _scopedService1.GetID().ToString();
                ViewBag.message4 = "Second Instance " + _scopedService2.GetID().ToString();

                return View();
            }
        }

- Thêm vào action method 2 biến message3 và message4 cho scoped service.

- View: Trong view thêm 3 dòng

        <h3>Scoped Service</h3>
        @ViewBag.message3
        </br>
        @ViewBag.message4


- Thể hiện được tạo chỉ một lần cho mỗi request, đó là lý do chúng ta tạo ra 2 ID giống nhau. Giờ hãy refresh trình duyệt. ID đã thay đổi bởi vì một thể hiện mới được tạo ra cho mỗi request.

## Singleton
- Một thể hiện duy nhất của service được tạo khi nó được yêu cầu lần đầu. Sau đó mỗi một request sau này sẽ chỉ sử dụng cùng instance đó thôi. Request mới không tạo thể hiện mới mà nó được dùng lại.

- Đăng ký Singleton Service: Singleton service được đăng ký sử dụng phương thức AddSingleton

        services.AddSingleton<ISomeServiceService, SomeService>();

- Inject Singleton service vào Controller

        public class HomeController : Controller
        {
            ITransientService _transientService1;
            ITransientService _transientService2;

            IScopedService _scopedService1;
            IScopedService _scopedService2;

            ISingletonService _singletonService1;
            ISingletonService _singletonService2;

            public HomeController(ITransientService transientService1,
                            ITransientService transientService2, 
                            IScopedService scopedService1,
                            IScopedService scopedService2,
                            ISingletonService singletonService1,
                            ISingletonService singletonService2)
            {

                _transientService1 = transientService1;
                _transientService2 = transientService2;

                _scopedService1 = scopedService1;
                _scopedService2 = scopedService2;

                _singletonService1 = singletonService1;
                _singletonService2 = singletonService2;

            }

            public IActionResult Index()
            {

                ViewBag.message1 ="First Instance " + _transientService1.GetID().ToString();
                ViewBag.message2 ="Second Instance "+ _transientService2.GetID().ToString();


                ViewBag.message3 = "First Instance " + _scopedService1.GetID().ToString();
                ViewBag.message4 = "Second Instance " + _scopedService2.GetID().ToString();

                ViewBag.message5 = "First Instance " + _singletonService1.GetID().ToString();
                ViewBag.message6 = "Second Instance " + _singletonService2.GetID().ToString();

                return View();
            }
        }

- Đầu tiên chúng ta inject 6 thể hiện của SomeService. Hai thể hiện cho mỗi interface. 

        View
        @{
            ViewData["Title"] = "Index";
        }

        <h2>Index</h2>

        <h3>Transient Service</h3>
        @ViewBag.message1
        </br>
        @ViewBag.message2

        <h3>Scoped Service</h3>
        @ViewBag.message3
        </br>
        @ViewBag.message4

        <h3>Singleton Service</h3>
        @ViewBag.message5
        </br>
        @ViewBag.message6

- Chạy ứng dụng và bạn thấy rằng các ID tạo ra từ Singleton service luôn giống nhau và sẽ không thay đổi ngay cả khi bạn refresh ứng dụng. Bạn có thể thấy trong hình dưới đây

- Vậy nên sử dụng cái nào?
- Transient service là cách an toàn nhất để tạo, vì bạn luôn tạo mới một thể hiện. Nhưng vì thế mà nó sẽ tạo mỗi lần bạn yêu cầu như vậy sẽ dùng nhiều bộ nhớ và tài nguyên hơn. Điều này có thể ảnh hưởng không tốt đến hiệu năng nếu quá nhiều thể hiện được tạo.
- Sử dụng Transient Service phù hợp khi bạn muốn dùng cho các service nhẹ và nhỏ cũng như không có trạng thái.
- Scoped service thì tốt hơn khi bạn muốn duy trì trạng thái trong một request.
- Singleton được tạo chỉ một lần, nó không bị huỷ cho đến khi ứng dụng tắt. Bất cứ việc chiếm bộ nhớ nào với các service này đều tích lại theo thời gian và nó đầy lên. Nhưng cũng giúp chúng ta tiết kiệm bộ nhớ nếu xử lý tốt vì chúng được tạo chỉ 1 lần và sử dụng mọi nơi.
- Sử dụng Singleton khi bạn cần duy trì trạng thái trong toàn hệ thống. Cấu hình, tham số của ứng dụng, các service logging, caching dữ liệu...là các ví dụ thường dùng Singleton.
- Inject service với các vòng đời khác nhau vào service khác
Hãy cẩn thân, khi inject service vào service khác với các vòng đời khác nhau. Hãy xem ví dụ Singleton Service phụ thuộc vào một service khác được đăng ký với vòng đời là Transient.

-Khi request đến lần đầu thì một instance của Singleton được tạo.
-nKhi request thứ 2 đến thì thể hiện này của Singleton được dùng lại. Và singleton này đã chứa một thể hiện của transient service. Vì thế nó không được tạo lại. Điều này vô hình chung đã chuyển transient service thành singleton service.

- Các service với mức độ vòng đời thấp hơn được inject vào service có vòng đời cao hơn sẽ thay đổi service vòng đời thấp hơn thành vòng đời cao hơn. Điều này sẽ làm việc debug khó hơn và nó nên tránh. Từ thấp đến cao là Transient, Scoped và Singleton.

- Vì thế hãy nhớ quy tắc:

    Không bao giờ inject Scoped & Transient service vào Singleton service
    Không bao giờ inject Transient Service vào Scope Service