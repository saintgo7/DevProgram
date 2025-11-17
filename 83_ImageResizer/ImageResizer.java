import java.util.*;
/** ImageResizer - Calculate new image dimensions */
public class ImageResizer {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("=== Image Dimension Calculator ===");
        System.out.print("Original width: ");
        int width = sc.nextInt();
        System.out.print("Original height: ");
        int height = sc.nextInt();
        System.out.print("New width (or 0 to specify height): ");
        int newWidth = sc.nextInt();
        
        if(newWidth == 0) {
            System.out.print("New height: ");
            int newHeight = sc.nextInt();
            newWidth = (int)((double)newHeight / height * width);
            System.out.printf("New dimensions: %dx%d%n", newWidth, newHeight);
        } else {
            int newHeight = (int)((double)newWidth / width * height);
            System.out.printf("New dimensions: %dx%d%n", newWidth, newHeight);
        }
        sc.close();
    }
}
