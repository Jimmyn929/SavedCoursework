import java.io.*;
import java.util.*;
/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author jimmy
 */
public class Driver 
{
    public static void main(String[] args) throws IOException 
    {
        ArrayItem[] mainItems;
        ArrayItem[] searchItems;
        ArrayItem[] temp = new ArrayItem[30];
        
        Scanner file = new Scanner(new File("Lab2InputFile1.txt"));
        
        //Reads file1
        int count = 0;
        do
        {
            String color = file.next();
            int ID = file.nextInt();
            
            ArrayItem item = new ArrayItem(color, ID);
            
            temp[count] = item;
            count++;
        }
        while(file.hasNext());
        
        
        //puts file1 onto array
        mainItems = new ArrayItem[count];
        for(int x = 0; x < count; x++)
        {
            mainItems[x] = temp[x];
        }
        
        
        
        file = new Scanner(new File("Lab2InputFile2.txt"));
        
        //reads file2
        count = 0;
        do
        {
            String color = file.next();
            int ID = file.nextInt();
            
            ArrayItem item = new ArrayItem(color, ID);
            
            temp[count] = item;
            count++;
        }
        while(file.hasNext());
        
        //puts file2 on search
        searchItems = new ArrayItem[count];
        for(int x = 0; x < count; x++)
        {
            searchItems[x] = temp[x];
        }
        
        Arrays.sort(mainItems); //sorted based on order of ID then color
        
        //print sorted array 
        for(int x = 0; x < mainItems.length; x++)
        {
            System.out.print(mainItems[x]);
            
        }
        
        
        //searches item, says if found or not
        for(int x = 0; x < searchItems.length; x++)
        {
            System.out.print("Searching for \n" + searchItems[x]);
            
            if(binarySearch(mainItems, 0, mainItems.length, searchItems[x]) != -1)
            {
                System.out.print("Found at " + binarySearch(mainItems, 0, mainItems.length, searchItems[x]));
                
            }
            else
            {
                System.out.print("Not Found");
            }
            System.out.println("\n");
        }
        
        
    }
    
    public static int binarySearch(ArrayItem[] i, int lower, int upper, ArrayItem target)
    {
        if(lower < upper)
        {
            int mid = lower + (upper - lower) / 2;
            
            if(i[mid].compareTo(target) == 0)
            {
                return mid;
            }
            
            if(i[mid].compareTo(target) > 0)
                return binarySearch(i, lower, mid, target);
            
            if(i[mid].compareTo(target) < 0)
                return binarySearch(i, mid + 1, upper, target);
        }
        
        return -1;
        
        
    }
}