import java.io.*;
import java.util.ArrayList;
import java.util.List;

/**
 * Pıllan - Java proqramından Python kodunu icra edən class
 */
public class Pıllan {
    
    private String pythonPath;
    
    /**
     * Constructor - Python interpreter yolunu təyin edir
     * @param pythonPath Python interpreter-in yolu (məsələn: "python" və ya "python3")
     */
    public Pıllan(String pythonPath) {
        this.pythonPath = pythonPath;
    }
    
    /**
     * Default constructor - "python" istifadə edir
     */
    public Pıllan() {
        this.pythonPath = "python";
    }
    
    /**
     * Python kodunu birbaşa icra edir
     * @param pythonCode İcra ediləcək Python kodu
     * @return Python kodunun nəticəsi
     * @throws IOException
     * @throws InterruptedException
     */
    public String executePythonCode(String pythonCode) throws IOException, InterruptedException {
        List<String> command = new ArrayList<>();
        command.add(pythonPath);
        command.add("-c");
        command.add(pythonCode);
        
        return executeCommand(command);
    }
    
    /**
     * Python faylını icra edir
     * @param scriptPath Python faylının yolu
     * @return Python skriptinin nəticəsi
     * @throws IOException
     * @throws InterruptedException
     */
    public String executePythonFile(String scriptPath) throws IOException, InterruptedException {
        List<String> command = new ArrayList<>();
        command.add(pythonPath);
        command.add(scriptPath);
        
        return executeCommand(command);
    }
    
    /**
     * Python faylını arqumentlərlə icra edir
     * @param scriptPath Python faylının yolu
     * @param args Arqumentlər
     * @return Python skriptinin nəticəsi
     * @throws IOException
     * @throws InterruptedException
     */
    public String executePythonFile(String scriptPath, String[] args) throws IOException, InterruptedException {
        List<String> command = new ArrayList<>();
        command.add(pythonPath);
        command.add(scriptPath);
        
        for (String arg : args) {
            command.add(arg);
        }
        
        return executeCommand(command);
    }
    
    /**
     * Əmri icra edib nəticəni qaytarır
     */
    private String executeCommand(List<String> command) throws IOException, InterruptedException {
        ProcessBuilder processBuilder = new ProcessBuilder(command);
        processBuilder.redirectErrorStream(true);
        
        Process process = processBuilder.start();
        
        StringBuilder output = new StringBuilder();
        try (BufferedReader reader = new BufferedReader(
                new InputStreamReader(process.getInputStream()))) {
            String line;
            while ((line = reader.readLine()) != null) {
                output.append(line).append("\n");
            }
        }
        
        int exitCode = process.waitFor();
        
        if (exitCode != 0) {
            throw new RuntimeException("Python kodu səhv ilə başa çatdı. Exit code: " + exitCode);
        }
        
        return output.toString().trim();
    }
    
    /**
     * Python versiyasını yoxlayır
     */
    public String getPythonVersion() throws IOException, InterruptedException {
        List<String> command = new ArrayList<>();
        command.add(pythonPath);
        command.add("--version");
        
        ProcessBuilder processBuilder = new ProcessBuilder(command);
        processBuilder.redirectErrorStream(true);
        Process process = processBuilder.start();
        
        StringBuilder output = new StringBuilder();
        try (BufferedReader reader = new BufferedReader(
                new InputStreamReader(process.getInputStream()))) {
            String line;
            while ((line = reader.readLine()) != null) {
                output.append(line).append("\n");
            }
        }
        
        process.waitFor();
        return output.toString().trim();
    }
    
    /**
     * Test üçün main metodu
     */
    public static void main(String[] args) {
        try {
            Pıllan pıllan = new Pıllan();
            
            // Python versiyasını yoxla
            System.out.println("=== Python Versiyası ===");
            System.out.println(pıllan.getPythonVersion());
            System.out.println();
            
            // Sadə Python kodu icra et
            System.out.println("=== Sadə kod icra ===");
            String result1 = pıllan.executePythonCode("print('Salam Dünya!')");
            System.out.println(result1);
            System.out.println();
            
            // Hesablama icra et
            System.out.println("=== Hesablama ===");
            String result2 = pıllan.executePythonCode("print(2 + 2)");
            System.out.println("2 + 2 = " + result2);
            System.out.println();
            
            // Daha mürəkkəb kod
            System.out.println("=== Mürəkkəb kod ===");
            String complexCode = "for i in range(5):\n    print(f'Nömrə: {i}')";
            String result3 = pıllan.executePythonCode(complexCode);
            System.out.println(result3);
            System.out.println();
            
            // List comprehension
            System.out.println("=== List Comprehension ===");
            String result4 = pıllan.executePythonCode("print([x**2 for x in range(10)])");
            System.out.println(result4);
            
        } catch (Exception e) {
            System.err.println("Xəta baş verdi: " + e.getMessage());
            e.printStackTrace();
        }
    }
}
