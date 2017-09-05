/**
 * Created by liu on 2017/9/4.
 */
var a=$("img");
var b= new Array(9);
var t
for (var i=0;i<a.length;i++)
{
b[i] = a[i].src;
}
function randomsort(a, b) {
    return Math.random()>.5 ? -1 : 1;
    //用Math.random()函数生成0~1之间的随机数与0.5比较，返回-1或1
}
function time(){
    b.sort(randomsort);
    for (var i=0;i<a.length;i++)
{
a[i].src = b[i];
}
t=setTimeout("time()",3000)
}
time()


