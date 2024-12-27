// JAVA TERMS
autoboxing
inner class vs static nested class
javadoc
// CONSOLE
$javac basics/com/HelloWorld.java // compiles the code
$java basics.com.HelloWorld       // launchs jvm to run it
#!/path/to/jdk/bin/java --source 17 // add this line to create exe chmod +x program
$jshell //repl
// STD LIB
io
time
math
net
nio.file
util
util.concurrent
util.function
util.prefs
util.regex
util.stream
util.Scanner

// CONSTANTS
Integer.MIN_VALUE / Integer.MAX_VALUE 
Double.POSITIVE_INIFINITY / Double.NaN
// DATA TYPES
byte, short, int, long
float, double
char, boolean
BigInteger, BigDecimal
BigInteger n = BigInteger.valueOf(8329348293491234) // or from "321423423"
BigInteger.ZERO, BigInteger.ONE
Integer.toString(n)
Integer.parseInt(str)

// BASIC PROGRAM
package basics.com;

public class HelloWorld {
	public static void main(String[] args){
		System.out.println("Hello world");	
		final int PI = 3.14f; // CONSTANT
		var input = new Scanner(System.in); // TYPE INFERENCE
		var name = in.nextLine(); // vs in.next() for single word
		enum Weekday { MONDAY, TUESDAY, WEDNESSDAY,...} // ENUM
		Weekday day = Weekday.MONDAY;

		Console terminal = System.console();
		char[] passwd = terminal.readPassword("Password: ");
	}}

// JOIN
String foods = "Coconuts" + "Chorizos"
String names = String.join(", ", "Max", "Otto",)

var builder = new StringBuilder();
while (more strings){ builder.append(next string); }
String result = builder.toString();

String location = locations.substring(5, 9);
String[] namesArray = names.split(",");

name.equals("Max"); // compare strings, == does memory comparation
String multiline = """
Hey hey hey
People!
It's zerg here!
"

// SWITCH
//switch(seasonCode){
//  case 0 -> seasonName = "Spring";
//  case 1 -> seasonName = "Summer";
//  default -> {
//    seasonName = "";
//  }
//}

//int numLetters = switch(seasonName){
//  case "Spring", "Summer" -> 5;
//  case "Fall" -> 4;
//  default -> throw new IllegalArgumentException();
//}

// ARRAY vs ARRAYLIST
int[] primes = {2, 3, 5, 8};
ArrayList<String> friends = new ArrayList<String>();
friends.add("Max")
friends.remove(1)
friends.get(0)
friends.set(1, "Otto")

for (int n: numbers){ sum += n; }

String[] names = ...;
var friends = new ArrayList<>(List.of(names));
names = friends.toArray(new String[0])
int[] copiedPrimes = Array.copyOf(primes, primes.length) // COPY

public static double average(double... values){} // VARARGS or MULTI ARGS
double[] scores = {3, 4, 5.5}
average(scores)
average(3, 4, 5.5)

// CLASSES & RECORDS
public class Employee{
	private final int salary;
	public Employee(){}
	static{} // static initializer, when first class loaded sets salary
}

record Point(double x, double y){}

public interface IntSequence{
	boolean hasNext();
	int next();
}

public class SquareSequence implements IntSequence {
	private int i;

	public boolean hasNext(){
		return true;
	}

	public int next(){
		i++;
		return i * i;
	}
}

// INSTANCEOF and CAST

if (sequence instanceof DigitSequence digits){ ... use digits here ... }
/*
String description = switch(sequence){
	case DigitSequence digits ->
		"A digit sequence with rest " + digits.rest();
	case SquareSequence squares -> "A square sequence";
	
}
*/


