/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package lab4;

/**
 *
 * @author jimmy
 */
public class HashObject
{
    private int integer;
    private String string;
    
    public HashObject(int i, String s)
    {
        integer = i;
        string = s;
    }
    
    public String toString()
    {
        return integer + " " + string;
    }
    
    
}
