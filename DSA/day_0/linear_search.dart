import 'dart:io';

main() {
  List numbers = List.generate(10, (index) => index + 1);
  print(numbers);

  // for (var i = 0; i < numbers.length; i++) {
  //   if (num == numbers[i]) {
  //     print(i);
  //     break;
  //   } else if (numbers[i] == 10 && numbers[i] != num) {
  //     print('$num not found in  list');
  //   }
  // }
}
