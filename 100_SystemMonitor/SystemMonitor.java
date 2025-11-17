import java.util.*;
/** SystemMonitor - System resource monitor */
public class SystemMonitor {
    public static void main(String[] args) {
        Runtime runtime = Runtime.getRuntime();
        
        System.out.println("=== System Monitor ===");
        System.out.println("\n--- Java Runtime Info ---");
        System.out.println("Available Processors: " + runtime.availableProcessors());
        
        long maxMemory = runtime.maxMemory();
        long totalMemory = runtime.totalMemory();
        long freeMemory = runtime.freeMemory();
        long usedMemory = totalMemory - freeMemory;
        
        System.out.println("\n--- Memory Info (MB) ---");
        System.out.println("Max Memory: " + (maxMemory / 1024 / 1024) + " MB");
        System.out.println("Total Memory: " + (totalMemory / 1024 / 1024) + " MB");
        System.out.println("Free Memory: " + (freeMemory / 1024 / 1024) + " MB");
        System.out.println("Used Memory: " + (usedMemory / 1024 / 1024) + " MB");
        
        System.out.println("\n--- System Properties ---");
        System.out.println("OS: " + System.getProperty("os.name"));
        System.out.println("OS Version: " + System.getProperty("os.version"));
        System.out.println("Java Version: " + System.getProperty("java.version"));
        System.out.println("User: " + System.getProperty("user.name"));
        System.out.println("Home: " + System.getProperty("user.home"));
    }
}
