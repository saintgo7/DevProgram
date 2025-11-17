import java.util.*;
/** FileCompressor - Simple run-length encoding */
public class FileCompressor {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("=== File Compressor (RLE) ===");
        System.out.print("Enter text to compress: ");
        String text = sc.nextLine();
        String compressed = compress(text);
        System.out.println("Compressed: " + compressed);
        System.out.println("Original size: " + text.length());
        System.out.println("Compressed size: " + compressed.length());
        sc.close();
    }
    private static String compress(String text) {
        StringBuilder result = new StringBuilder();
        int count = 1;
        for(int i = 0; i < text.length(); i++) {
            if(i + 1 < text.length() && text.charAt(i) == text.charAt(i+1)) {
                count++;
            } else {
                result.append(text.charAt(i)).append(count);
                count = 1;
            }
        }
        return result.toString();
    }
}
