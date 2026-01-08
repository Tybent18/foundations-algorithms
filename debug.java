public class Program
{
    public static void main(String[] args) {
        
// Print Statements

int x = 42;
System.out.println("DEBUG: x = " + x);

// Try/Catch

try {
    int z = x / y;
} catch (ArithmeticException e) {
    e.printStackTrace();  // shows where it went wrong
}

// Assertions

int a = -1;
assert a >= 0 : "a cannot be negative!";
        
    }
}