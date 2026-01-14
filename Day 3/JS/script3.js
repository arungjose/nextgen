var num1=Number(prompt("Enter a number1"))
var num2=Number(prompt("Enter a number2"))
var num3=Number(prompt("Enter a number3"))
if(num1>num2 && num1>num3)
{
    document.writeln("<h1>largest is",num1)
    
}
else if(num2>num1&& num2>num3)
{
     document.writeln("largest is ",num2)
}
else{
    document.writeln("largest is ",num3)
}
