//https://www.codingninjas.com/studio/problems/data-type_8357232?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf


import java.util.Scanner;
public class Solution {
    public static int dataTypes(String type) 
    {
        // Write your code here
        //System.out.print(a);
        if(type.equals("Double")||type.equals("Long"))
            return 8;
        else if(type.equals("Float")||type.equals("Integer"))
            return 4;
        else
            return 1;
    }
}