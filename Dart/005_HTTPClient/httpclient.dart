import 'dart:io';
import 'dart:convert';

class HTTPClient {
  Future<void> get(String url) async {
    try {
      HttpClient client = HttpClient();
      Uri uri = Uri.parse(url);

      HttpClientRequest request = await client.getUrl(uri);
      HttpClientResponse response = await request.close();

      print('Status: ${response.statusCode}');
      print('Headers:');
      response.headers.forEach((name, values) {
        print('  $name: ${values.join(', ')}');
      });

      String responseBody = await response.transform(utf8.decoder).join();
      print('\nBody:');
      print(responseBody.substring(0, responseBody.length > 500 ? 500 : responseBody.length));

      client.close();
    } catch (e) {
      print('Error: $e');
    }
  }
}

void main(List<String> args) async {
  if (args.isEmpty) {
    print('Usage: dart http_client.dart <url>');
    return;
  }

  HTTPClient client = HTTPClient();
  await client.get(args[0]);
}
