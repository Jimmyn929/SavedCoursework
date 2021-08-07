/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author jimmy
 */
public class ArrayItem implements Comparable <ArrayItem>
{
    private String color;
    private int ID;
    
    public ArrayItem()
    {
        color = null;
        ID = 0;
    }
    
    public ArrayItem(String c, int i)
    {
        color = c;
        ID = i;
    }
    
    @Override
    public int compareTo(ArrayItem other)
    {
        if( this.ID - other.ID == 0)
            return this.color.compareTo(other.color);
        else
        {
            return this.ID - other.ID;
        }
    }
    @Override
    public String toString()
    {
        return "Color: " + color +
                "\nID: " + ID +
                "\n";
    }
}
