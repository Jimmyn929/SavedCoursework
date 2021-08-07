/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author jimmy
 */
import java.util.*;
import java.io.*;
public class Driver {
    public static void main(String[] args) throws IOException 
    {
        Scanner file = new Scanner(new File("Lab1InputFile.txt"));
        
        MyStack stack = new MyStack();
        do
        {
            String courseName = file.nextLine();
            String courseID = file.nextLine();
            int credithours = Integer.parseInt(file.nextLine());
            
            MyList course = new MyList(courseName, courseID, credithours);
            
            stack.push(course);
            
            
        }
        while(file.hasNext());
        
        System.out.println("Number of items: " + stack.getSize());
        System.out.println(stack);
        
        System.out.println();
        
        stack.pop();
        stack.pop();
        stack.pop();
        
        System.out.println("Number of items: " + stack.getSize());
        System.out.println(stack);
    }
}
