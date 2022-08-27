## Cấu trúc project 

Khi bạn sử dụng CLI command để tạo project bằng lệnh
```shell 
    ng new <ten project>

```

- Một dự án với thư mục gốc có tên là ```<ten project>``` mà bạn tạo
- Một test project end to end (e2e)
- Tập tin cấu hình liên quan 

## Những tập tin trong thư mục làm việc 

1. Tệp tin cấu hình cho các trình soạn thảo
```
    .editorconfig
```
2. Tệp chỉ định bỏ qua một số file khi upload mã nguồn của bạn nên github 

```
    .gitignore 
```
3. Tệp tin cấu hình CLI mặc định cho tất cả dự án trong working dir 

```
    angular.json 
```
4. cung cấp các npm package cho working dir 
```
    node_modeles 
```
5. Cấu hình npm package cho working space 
```
    package.json
```
6. Cung cấp thông tin version cho tất cả các package install trong node_modules 
```
    package-lock.json 
```
7. cấu hình typescript mặc định 
```
tsconfig.json 
```
8. Cấu hình TSLint mặc định
```
tslint.json
```
9. intro của document 
```
    README.md
```

## Những tập tin trong project 

1. Chưa các tệp thành phần trong đó có app logic và dữ liệu mà bạn định nghĩa.
```
    app/
```
2. Chứa ảnh và  các tệp khác khi bạn build app 
```
    assets/
```
3. Thư mục chứa file cấu hình tùy chọn cho các môi trường cụ thể. (môi trường phát triển, môi trường product chạy thật)
```
    environments/ 
```
4. Cấu hình trình duyệt và nodejs cũng như front end tool 
```
    browserslist 
```
5. Icon để sử dụng cho app trong bookmark bar 

```
favicon.ico 
``` 
6. Trang HTML chính được hiển thị khi ai đó truy cập trang web của bạn 

```
index.html
```
7. File code typescript đầu tiên sẽ chạy 
```
main.ts 
```
8. Cung cấp các kịch bản polyfill để hỗ trợ trình duyệt 

```
    polyfills.ts 
```
9. CSS hoặc SASS, LESS file 
```
styles.css
```
10. Kế thừa từ tệp tsconfig.json trên workspace 
```
    tsconfig.app.json 
```
11. kế  thừa từ tệp tsconfig.json 
```
    tsconfig.spec.json
```
12. kế thừa từ tslint.json file 
```
tslint.json
```

## Default app project e2e files 

thư mục e2e/ chứa các tệp cấu hình và mã nguồn cho các bài test end-to-end cấu trúc thư mục như sau
```
my-app/                     
    e2e/
        src/
        protrctor.conf.js
        tsconfig.e2e.json 
```


## App source folder 
Định nghĩa logic cho root component 

```
app/app.component.ts 
```

định nghĩa HTML template cho app component 
```
app/app.component.html
```
định nghĩa base CSS cho app component 

```
app/app.component.css 
```
định nghĩa một unit test cho root appcomponent 
```
app/app.component.spec.ts
```
