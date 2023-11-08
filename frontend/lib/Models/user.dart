import 'package:frontend/Models/item.dart';
import 'package:frontend/Models/outfit.dart';

class User {
  String username;
  String email;
  String picture; // URL or image path for the user's picture
  List<Item> items; // List of item IDs associated with the user
  List<Outfit> outfits; // List of outfit IDs associated with the user

  User({
    required this.username,
    required this.email,
    required this.picture,
    required this.items,
    required this.outfits,
  });

  factory User.fromJson(Map<String, dynamic> json) {
    return User(
      username: json['username'],
      email: json['email'],
      picture: json['picture'],
      items: List<Item>.from(json['items']),
      outfits: List<Outfit>.from(json['outfits']),
    );
  }
}
