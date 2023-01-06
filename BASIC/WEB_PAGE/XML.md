```toc
```

## XML
用于传输和存储数据与HTML配合使用
![xml实例结构](https://www.runoob.com/wp-content/uploads/2013/09/nodetree.gif)
EXAMPLE:
```xml
<?xml version="1.0" encoding="utf-8">
<note>
	<to>Tove</to>
	<from>Jani</from>
	<heading>Reminder</heading>
	<body>Don't forget</body>
</note>
```
- 第一行xml声明，定义编码和版本号
- `<note></note>` 为信息体标签，内容为信息体
- `<to></to>` 目的标签，内容为目的地名称
- `<from></from>` 源标签，内容为源名称

### 实体引用
在xml内容和值中直接使用”<,&,',",>,“是非法的。
| xml引用 | 替代符号 | 符号语义 |
| --- | --- | ---|
| \&lt; | < | less than |
| \&amp; | & | ampersand |
| \&gt; | > | greater than |
| \&apos; | ' | apostrophe |
| \&quot; | " | quotation mark |

### 显示方法
- CSS：添加标签`<?xml-stylesheet type="text/css" href="css_name.css"?>`
- XSLT(recommend): 显示以前将xml转为html

### XMLHttpRequest
Exchange data with Server in background.
```js
/ create a xmlhttprequest object
xmlhttp = new XMLHttpRequest();
```
### XML DOM & HTML DOM
DOM define a serise of standard mothed to access and operate doc.
XML and HTML regarded as a tags' tree in DOM.

### XPATH 导航

[XPATH参考手册]([XPath、XQuery 以及 XSLT 函数 | 菜鸟教程 (runoob.com)](https://www.runoob.com/xpath/xpath-functions.html))
XML文件被描述成树的结构，XPATH表达式就是在XML文档树中遍历节点的路径表示。
XPATH包含一个标准库，式XSLT主要元素，是W3C的一个标准
(PS:XSLT将xml文档转换为其他格式的文档，如：html)
#### xpath node
- element node:
- attribute node:
- text node:
- namespace node:
- deal instruct node:
- doc root node:
- annotation node: 
#### XPATH Expression grammar
**Grammar**
| grammar elem | describe |
| --- | --- |
| nodename | select all of node which parents is nodename.|
| \/ | select start at root |
| \/\/ | select doc's node start at present node |
| . | select present node |
| .. | select parents of present node |
| @ | select node's attribution |
**Predicates**
| predicates | result |
| --- | --- |
| nodename[k] | select kth node which name is node name |
| nodename[last()-k] | select k+1 from the bottom node |
| nodename[position()<k] | select frist k-1 node |
| nodename[@attr='value'] | select all of attr='value' is node |
| nodename[elem>k] |select all of elem>k is node |
| \* | select any node |
| @\* | select any node with attribution |
| node/elem1 \| node/elem2 | select node with elem1 and elem2 |