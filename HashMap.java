import java.util.HashMap;

public class YourClassNameHere {
    public static void main(String[] args) {
      //Creating the HashMap
      HashMap<String, Integer> firstHashMap = new HashMap<String, Integer>();
      // Inserting into the HashMap
      firstHashMap.put("a", 10);
      firstHashMap.put("b", 3);
      firstHashMap.put("c", 88);
      
      //To print out HashMap
      System.out.println(firstHashMap);
      
      //To print out specific element
      System.out.println(firstHashMap.get("b"));
      
      //Creating another hashmap;
      HashMap<String, String> secondHashMap = new HashMap<String, String>();
      secondHashMap.put("Trent", "66");
      secondHashMap.put("Joe", "12");
      secondHashMap.put("Virgil", "4");
      secondHashMap.put("Ramos", "4");
      secondHashMap.put("Robbo", "26");
      
      System.out.println(secondHashMap);
      
      //To remove from HashMap;
      secondHashMap.remove("Ramos");
      
      System.out.println(secondHashMap);
      
      //To check if a hashmap contains a certain value
      System.out.println(secondHashMap.containsKey("Virgil"));
      
      //To find size of hashmap
      System.out.println(secondHashMap.size());
      
      //To replace value of element in hashmap
      System.out.println(secondHash
      Map.replace("Virgil", "7"));
      
      System.out.println(secondHashMap);
      
      //To get all of the value in a HashMap
      System.out.println(secondHashMap.values());
      
      //To get all the keys in a HashMap
      System.out.println(secondHashMap.keySet());
      
      // To sort array//
      // Arrays.sort(name of array)
      
    }
}
