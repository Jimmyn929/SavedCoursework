/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package lab3;

import java.io.*;
import java.util.*;

/**
 * 
 * @author jimmy
 */
public class Lab3 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) throws IOException
    {    
        int[] tree = new int[31];
        
        for(int x = 0; x < tree.length; x++)
        {
            tree[x] = -1;
        }
        
        Scanner file = new Scanner(new File("Lab3InputFile1.txt"));
        
        
        do
        {
            int parent = file.nextInt();
            int child = file.nextInt();
            int index = 0;
            boolean found = false;
            do
            {
                if(parent < 0)  //Determines Root
                {
                    found = true;
                    tree[0] = child;
                }
                else    //If not the root
                {
                     if(tree[index] == parent)  //If the parent is found
                     {
                        found = true;
                        
                        if(child < parent)
                            tree[2 * index + 1] = child;
                        else
                            tree[2*(index + 1)] = child; 
                     }
                     else   //If parent is not found
                     {
                        if(parent < tree[index])
                            index = 2 * index + 1;
                        else
                            index = 2 *(index + 1);
                     }
                }    
            }
            while(found == false);
        }
        while(file.hasNext());
        
        
        file = new Scanner(new File("Lab3InputFile2.txt"));
        do
        {
            int find = file.nextInt();
            int index = 0;
            int level = 0;
            boolean found = false;
            
            do
            {
                if(find != tree[index])
                {
                    level++;
                
                    if(find < tree[index])
                        index = 2 * index + 1;
                    else
                        index = 2 * (index + 1);
                
                    if(level == 5)
                    {
                        found = true;
                        System.out.println(find + " cannot be found.");
                    }
                }
                else
                {
                    System.out.println(find + " can be found at index " + index + ", level " + level);
                    found = true;
                }
            }
            while(found == false);
        }
        while(file.hasNext());
        /*
        for(int x = 0; x < tree.length; x++)
            System.out.println(tree[x]);
        */
    }
}
    

