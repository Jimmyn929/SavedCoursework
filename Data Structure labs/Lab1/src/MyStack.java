/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author jimmy
 */
public class MyStack {
    private MyList front;
    private int size;

    public MyStack() {
        this.front = new MyList(null, null, 0);
        size = 0;
    }
    
    public void push(MyList node) 
    {
        if(size == 0) {
                front.setNext(node);
                size++;
        }
        else
        {
            node.setNext(front.getNext());
            
            front.setNext(node);
            size++;
        }  
    }
    
    public MyList pop()
    {
        if(size > 0)
        {
            MyList temp = front.getNext();
            front.setNext(temp.getNext());
            size--;
            
            return temp;
        }
        else
        {
            return null;
        }  
    }
    
    public int getSize()
    {
        return size;
    }
    
    public String toString()
    {
        String s = "";
        MyList temp = front.getNext();
        
        for(int x = 0; x < size; x++ )
        {
            s += temp;
            
            if(temp.getNext() != null)
            {
                temp = temp.getNext();
            }
            
        }
        return s;
    }
    
    
}


