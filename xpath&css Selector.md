# Xpath

- 浏览器console中使用 `$x('')`来检查选取结果

- 常用语法

  | syntax      | desc                              | e.g.                               | Remark |
  | ----------- | --------------------------------- | ---------------------------------- | ------ |
  | /           | Start from root                   | `/html/body`                       |        |
  | //          | parse from any where and list all | `//div`                            |        |
  | [1]         | index of element                  | `//div/p[1]`                       |        |
  | @           | get the attr                      | `//a/@href `                       |        |
  | @           | 包含herf属性链接                  | `//a[@href] `                      |        |
  | @           | get the attr equal to             | `//a[@class="123"]`                |        |
  | contains    |                                   | `//a[contains(@href,"abc")]`       |        |
  | not         |                                   | `//a[not(contains(@href,"abc"))]`  |        |
  | starts-with |                                   | `//a[starts-with(@href,"https:")]` |        |
  | text()      | 获取文本                          | `//div/text()`                     |        |
  | *           | All                               | `//div/*`                          |        |
  |             |                                   |                                    |        |

  

- http://www.w3school.com.cn/xpath/index.asp

- 建议

  - 不要使用带数字的xpath表达式
  - 尽量少用@class ,因为网站可能经常修改样式
  - 

测试网站：http://quotes.toscrape.com/

# CSS Selector

http://www.w3school.com.cn/cssref/css_selectors.asp

- 浏览器console中使用 `$('')或 $$('')`来检查选取结果

```javascript
$$('')// 简单理解就是 document.querySelectorAll 而已。
$('')// 简单理解就是 document.querySelector 而已。
```



# chrome consloe

https://blog.csdn.net/qq_34986769/article/details/52161794

1. console

   `console.log()`

   `console.info()`

   `console.error()`

   `console.warn()`

2. Group,end

   ```javascript
   console.group('group1');
   console.info('1.')
   console.info('2.')
   console.log('3.')
   console.groupEnd();
   ```

   

3. assert

   ```javascript
   var isDebug = false;
   console.assert(isDebug,'为false输出log信息')
   ```

4. count

   ```javascript
   function myfunction(){
       //balabala
       console.count("myfunction被执行的次数：")
   }
   ```

   

5. dir `console.dir(console)`

6. console.time,console.timeEnd

7. ...

