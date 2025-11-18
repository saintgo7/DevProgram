import 'dart:io';

class FileAnalyzer {
  String filePath;

  FileAnalyzer(this.filePath);

  Future<void> analyze() async {
    try {
      File file = File(filePath);

      if (!await file.exists()) {
        print('File not found: $filePath');
        return;
      }

      String content = await file.readAsString();
      List<String> lines = await file.readAsLines();

      int charCount = content.length;
      int lineCount = lines.length;
      int wordCount = content.split(RegExp(r'\s+')).where((w) => w.isNotEmpty).length;

      print('=== File Analysis ===');
      print('File: $filePath');
      print('Characters: $charCount');
      print('Words: $wordCount');
      print('Lines: $lineCount');

    } catch (e) {
      print('Error reading file: $e');
    }
  }
}

void main(List<String> args) async {
  if (args.isEmpty) {
    print('Usage: dart file_reader.dart <filename>');
    return;
  }

  FileAnalyzer analyzer = FileAnalyzer(args[0]);
  await analyzer.analyze();
}
