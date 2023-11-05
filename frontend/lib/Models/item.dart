class Item {
  String type;
  String brand;
  List<String> color;
  String image; // Represented as a URL or image path
  List<String> occasions;

  Item({
    required this.type,
    required this.brand,
    required this.color,
    required this.image,
    required this.occasions,
  });

  factory Item.fromJson(Map<String, dynamic> json) {
    return Item(
      type: json['type'],
      brand: json['brand'],
      color: List<String>.from(json['color']),
      image: json['image'], // Store as a URL or image path
      occasions: List<String>.from(json['occasions']),
    );
  }
}
