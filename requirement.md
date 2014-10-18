####日志分析的重要元素

#####FEP
* 请求-响应报文各域
* 交易代码
* ATMP流水号
* MQ队列  FEP2TXE / TXE2FEP XML报文解析


######BEP
* 请求-响应报文各域
* 交易代码
* ATMP流水号(注意序列号，和FEP最大的区别)
* MQ队列  BEP2TXE / TXE2BEP XML报文解析

######TXE
* Error message
* workflow of the transation
* ESR service ERROR message


###### memo
1. data display using web application
2. Which web framework to choose
Django vs Flask vs Pyramid
3. Full Text Search Engine
Need No-SQL components?
4. static code analysis within Eclipse plugin mapping the workflow xml file?

###### ATMP自动化测试系统设计
作用：比较ATMP系统单个组件代码修改后，持续集成测试
意义：ATMP开发目前没有真正意义上的自测，一旦要修改涉及多支交易的主流程公共主键，一般只能通过全局的的Code Review来观察代码的重构是否影响了交易
两种实现：
1. 如何在现有框架下引入Unit Test
2. 系统末端的输入/输出在一次更新后的对比（报文对比监控）
模式：
Note: CI（Continuous Integration）Jenkins / Husdon