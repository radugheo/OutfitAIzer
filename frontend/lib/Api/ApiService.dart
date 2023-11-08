import 'package:flutter_dotenv/flutter_dotenv.dart';
import 'package:frontend/Models/item.dart';
import 'package:frontend/Models/user.dart';
import 'package:http/http.dart' as http;

class ApiService {
  late String baseUrl;
     
  Future<void> getBaseUrl() async { // future is like a promise object in js
    await dotenv.load(fileName: ".env");
    baseUrl = dotenv.env['BACKEND_URL']!; 
  } 

  //user
  Future<void> registerUser(User user, String password) async{
    await getBaseUrl();
    final Uri url = Uri.parse('$baseUrl/user/register'); 

    if(user.picture == null)
    {
      user.picture = 'https://www.pngitem.com/pimgs/m/146-1468479_my-profile-icon-blank-profile-picture-circle-hd.png';
    }

    final Map<String, dynamic> userData ={
      'username': user.username,
      'email': user.email,
      'password': password,
      'picture': user.picture
    };
    
    final response = await http.post(url, body: userData);

    if(response.statusCode == 200){
      print('User registered');
    }else{
      throw Exception('Failed to register user');
  
    }

  }
}

