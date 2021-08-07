/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author jimmy
 */
public class MyList
{
    private String courseName;
    private String courseID;
    private int creditHours;
    private MyList next;

    public MyList(String courseName, String courseID, int creditHours)
    {
        this.courseName = courseName;
        this.courseID = courseID;
        this.creditHours = creditHours;
        this.next = null;
    }
    
    public String getCourseName()
    {
        return courseName;
    }

    public String getCourseID()
    {
        return courseID;
    }

    public int getCreditHours()
    {
        return creditHours;
    }

    public MyList getNext() 
    {
        return next;
    }
    
    

    public void setCourseName(String courseName)
    {
        this.courseName = courseName;
    }

    public void setCourseID(String courseID) 
    {
        this.courseID = courseID;
    }

    public void setCreditHours(int creditHours) 
    {
        this.creditHours = creditHours;
    }
    
    public void setNext(MyList next)
    {
        this.next = next;
    }
    
    public String toString()
    {
        return "Course Name: " + courseName +
                "\n Course ID: " + courseID +
                "\n Credit Hours: " + creditHours;
    }
}


