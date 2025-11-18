import 'dart:io';

void main() {
  print('=== Dart Calculator ===');
  stdout.write('Enter first number: ');
  double num1 = double.parse(stdin.readLineSync()!);

  stdout.write('Enter operator (+, -, *, /): ');
  String op = stdin.readLineSync()!;

  stdout.write('Enter second number: ');
  double num2 = double.parse(stdin.readLineSync()!);

  double result;
  switch (op) {
    case '+':
      result = num1 + num2;
      break;
    case '-':
      result = num1 - num2;
      break;
    case '*':
      result = num1 * num2;
      break;
    case '/':
      result = num2 != 0 ? num1 / num2 : double.nan;
      break;
    default:
      print('Invalid operator');
      return;
  }

  print('Result: $num1 $op $num2 = $result');
}
