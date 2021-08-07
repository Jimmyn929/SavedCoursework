/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package lab4;

import java.io.*;
import java.util.*;

/**
 *
 * @author jimmy
 */
public class Lab4 {

    /**
     * @param args the command line arguments
     * @throws java.io.IOException
     */
    public static void main(String[] args) throws IOException
    {
        //integer and string
        int first;
        String second;
        
        //create hashmap with 100 capacity
        HashMap<Integer, HashObject> map = new HashMap(100);
        
        //read file
        Scanner file = new Scanner(new File("Lab4InputFile1.txt"));
        int count = 0;
        do
        {
            
            
            first = file.nextInt();
            second = file.next();
            
            HashObject object = new HashObject(first, second);
            
            String tempFirst = "" + first;
            
            int a = (int)tempFirst.charAt(0);
            int b = (int)tempFirst.charAt(1);
            int c = (int)tempFirst.charAt(2);
            
            int x = (int)Math.pow(a,2) + (int)Math.pow(b,2) + (int)Math.pow(c,2);
            int y = Integer.parseInt(second) % 99;
            int key = (x + y) % 100;
            map.put(key, object);
            count++;
        }
        while(file.hasNext());
        
        //Print report 
        System.out.println("Report 1");
        for(Map.Entry<Integer, HashObject> entry : map.entrySet())
        {
            //System.out.println(entry.getValue() + " " + entry.getKey());
            System.out.println("\t[Value][String]:" + entry.getValue());
            System.out.println("\tHash Key: " + entry.getKey() + "\n");
        }
        
        System.out.println("Number of objects in file: " + count + "\n--------------------------------");
        
        //Read second file
        file = new Scanner(new File("Lab4InputFile2.txt"));
        
        //Search for keys to see if present
        System.out.println("Report 2");
        do
        {
            first = file.nextInt();
            second = file.next();
            
            HashObject search = new HashObject(first, second);
            String tempFirst = "" + first;
            
            int a = (int)tempFirst.charAt(0);
            int b = (int)tempFirst.charAt(1);
            int c = (int)tempFirst.charAt(2);
            
            int x = (int)Math.pow(a,2) + (int)Math.pow(b,2) + (int)Math.pow(c,2);
            int y = Integer.parseInt(second) % 99;
            int key = (x + y) % 100;
            
            //print report 2
            if(map.containsKey(key))
            {
                System.out.println("\tGenerated key: " + key);
                System.out.println("\tSearching for: " + first + " " + second);
                System.out.println("\tFound\n");
            }
            else
            {
                System.out.println("\tGenerated key: " + key);
                System.out.println("\tSearching for: " + first + " " + second);
                System.out.println("\tNot Found\n");
            }
            
        }
        while(file.hasNext());
    }
    
}
