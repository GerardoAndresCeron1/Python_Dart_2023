import 'dart:math';

void main() {
  List<List<int>> listas = [];

  //aqui generamos las 3 listas aleatorias utilizando la clase random

  for (int i = 0; i < 3; i++) {
    List<int> lista = [];
    for (int j = 0; j < 7; j++) {
      int elemento = Random().nextInt(71) + 30;
      lista.add(elemento);
    }
    listas.add(lista);
  }
  // aqui calculamos los promedios y los guardamos en una nueva lista
  List<double> promedios = [];
  for (int i = 0; i < 3; i++) {
    List<int> lista = listas[i];
    double promedio = lista.reduce((a, b) => a + b) / lista.length;
    promedios.add(promedio);
  }
//imprimimos los promedios
  for (int i = 0; i < 3; i++) {
    print('Promedio ${i + 1}: ${promedios[i]}');
  }
}
