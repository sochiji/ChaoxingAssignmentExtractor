# ChaoxingAssignmentExtractor
> 一个Python 3脚本，用于清除从超星学习通下载的学生作业存档中的成绩单，并解除压缩包的嵌套。

使用学习通“导出作业附件”功能获得的压缩包结构如下所示：
```
assignment.zip
|-- 学号1-学生1.zip
|   |-- 学生1的成绩单.doc
|   |-- 学生1的附件1
|   |-- 学生1的附件2
|   |-- ...
|-- 学号2-学生2.zip
|   |-- 学生2的成绩单.doc
|   |-- 学生2的附件1
|   |-- 学生2的附件2
|   |-- ...
|-- ...
```

可以看出，它内嵌套了每个学生的作业压缩包，且每个学生的作业压缩包内含了一份成绩单文件。

有时，解压逐个学生的压缩包是麻烦的事情……

> 当然，你可以先解压一层批量解压。但如果有很多这种压缩包呢？

有时，不想使用学习通来登记与统计成绩，因此成绩单文件显得很多余……

### 本项目的脚本可以将每个学生的压缩包替换为文件夹，并清除成绩单文件。

# 使用方法
1. 确保计算机上有 Python 3 环境；
2. 下载并保存本项目的`extract.py`文件，将学习通导出的压缩包（暂且称为`assignment.zip`）和它放在同一目录下；
3. 使用 Python 3 在当前目录运行`extract.py`脚本；
    >命令行为 `python extract.py`，此脚本会搜索当前目录下的所有`.zip`文件并列出来
4. 根据屏幕提示，从列出的`.zip`文件中找到`assignment.zip`（暂且假设你下载的文件叫这个名字），输入它的序号，按`Enter`键；
    >脚本会在当前目录下生成`已修改-assignment.zip`文件，不会就地修改原文件

# 应用场景1：老师批阅作业

有一个开设在学习通的课程，老师布置了作业。

>如果作业的答案形式是传统的、仅包含简单图文信息的，就可以让学生将答案直接填写在正文中。这种情况下，老师可以直接在学习通的Web页面上直接批阅学生的图文答案并打分。

>若作业的答案并非简单图文信息，而是诸如排版过的文档、代码、有目录层次关系的多个文件等形式，则不适合将答案内容直接粘贴在正文区域，因为学习通的Web页面不能向批阅作业的老师很好地呈现（单个Office文档除外，能凑合着看）。以附件形式上传答案文件则是更好的方法。老师应该要求学生回答问题时，上传一个或多个文件作为附件。老师可以将附件下载下来批阅。

## 痛点：逐个解压学生的作业很麻烦

老师每批阅一个学生的作业时，都要进行一次或多次下载并另存文件的操作。当然，这取决于该学生所上传的附件文件的数量，学生可以将多个文件打包，这给老师增加了解包操作的工作，临时文件也会产生不必要的磁盘容量占用与读写开销。

查看并审阅作业，是与课程内容高度相关的脑力劳动。如果要连续批阅多个学生的作业，工作流中掺入下载文件、另存文件等无关操作，对工作本身来说是一种打扰，会降低工作流的效率。

# 应用场景2：课代表收作业
## 痛点：命名难以统一、网盘下载慢、FTP服务器不好实践

- 命名难以统一：收作业的时候强调过的命名格式，总有人理解不了，不统一的命名格式不利于后续工作的自动化；
- 网盘下载慢：有网盘提供了文件收集功能，看起来很方便，但是下载文件时不充钱太慢了。
- FTP服务器不好实践：如果在学校内网架设FTP服务器来收作业，从作业布置下来到作业截止的这段时间，FTP服务器得一直开着。自己的电脑长时间开着显然不现实，也不好因为这事儿让校园网部门给自己开一台虚拟机。用云服务器吧，下载小水管速率不忍直视，境外服务器的网络连接不稳定……