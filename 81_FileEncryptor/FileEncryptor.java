import java.util.*;
/** FileEncryptor - Simple Caesar cipher encryption */
public class FileEncryptor {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("=== File Encryptor (Caesar Cipher) ===");
        System.out.print("Enter text to encrypt: ");
        String text = sc.nextLine();
        System.out.print("Enter shift (1-25): ");
        int shift = sc.nextInt();
        String encrypted = encrypt(text, shift);
        System.out.println("Encrypted: " + encrypted);
        System.out.println("Decrypted: " + encrypt(encrypted, 26 - shift));
        sc.close();
    }
    private static String encrypt(String text, int shift) {
        StringBuilder result = new StringBuilder();
        for(char c : text.toCharArray()) {
            if(Character.isLetter(c)) {
                char base = Character.isUpperCase(c) ? 'A' : 'a';
                result.append((char)((c - base + shift) % 26 + base));
            } else {
                result.append(c);
            }
        }
        return result.toString();
    }
}
