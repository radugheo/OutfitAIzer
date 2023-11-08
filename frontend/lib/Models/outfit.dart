import 'package:frontend/Models/item.dart';

class Outfit {
  List<Item> items;
  int rating;
  String date; // Represented as a string for simplicity

  Outfit({
    required this.items,
    required this.rating,
    required this.date,
  });

  factory Outfit.fromJson(Map<String, dynamic> json) {
    return Outfit(
      items: List<Item>.from(json['items']),
      rating: json['rating'],
      date: json['date'],
    );
  }
}
