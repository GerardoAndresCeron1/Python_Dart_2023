import 'dart:math';

void main() {
  // creamos la primera lista con los elementos que se entregaron
  List<int> lista = [3, 4, 7, 9, 8, 5, 1, 2, 5, 7];

  // creamos la segunda lista con elementos randoms entre -1 y -5
  List<int> lista2 = List.generate(10, (index) => Random().nextInt(5) - 5);
  //
  List<int> lista3 = [];
  for (int i = 0; i < lista.length; i++) {
    lista3.add(lista[i] + lista2[i]);
  }
  print(lista3);

  lista3.removeAt(7);
  lista3.removeAt(7);
  print(lista3);
}
