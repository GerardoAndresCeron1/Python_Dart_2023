import "dart:io";

void main() {
  // Crear una lista vacia para almacenar los números
  List<int> lista = [];

  // Pedir al usurio que ingrese el tamaño de la lista
  print("ingrese el tamaño de la lista: ");
  int tamano = int.parse(stdin.readLineSync()!);

  // Pedir al usurio que ingrese los elementos de la lista
  print("ingrese los elemntos de la lista(solo enteros postivos): ");
  for (int i = 0; i < tamano; i++) {
    int elemento = int.parse(stdin.readLineSync()!);

    // Verificar que los elemntos sean positivos
    if (elemento >= 0) {
      lista.add(elemento);
    } else {
      // Mostrar un mensaje de error y terminar el programa
      print('Error: el elemento debe ser positivo.');
      return;
    }
  }
  // Ordenar la lista de forma ascendente
  lista.sort();

  // Mostrar la lista ordenada de forma ascendente
  print('La lista ordenada de forma ascendente es:');
  print(lista);

  // Ordenar la lista de forma descendente
  print('La lista ordenada de forma descendente es:');
  print(lista);

  // obtener el valor máximo y mínimo de la lista
  int maximo = lista[0];
  int minimo = lista[lista.length - 1];

  // Mostrar el valor máximo y mínimo de la lista
  print('El valor máximo de la lista es: $maximo');
  print('El valor mínimo de la lista es: $minimo');
}
