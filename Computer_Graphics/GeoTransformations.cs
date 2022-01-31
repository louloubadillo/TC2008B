using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Transformations : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }
    //3D transformations

    //Translate
     public static Matrix4x4 Translate(float x, float y, float z)
    {
        Matrix4x4 tm = Matrix4x4.identity;
        tm[0, 3] = tx;
        tm[1, 3] = ty;
        tm[2, 3] = tz;
        return tm;
    }

    //Scale
    public static Matrix4x4 Scale(float x, float y, float z)
    {
        Matrix4x4 scale = Matrix4x4.identity;
        scale[0, 0] = x;
        scale[1, 1] = y;
        scale[2, 2]  = z;
        return scale;
    }

    //Rotate
    //X axis
    public static Matrix4x4 RotateX(float angle)
    {
        //convert angle to rad
        float rad = angle * Mathf.Deg2Rad;
        Matrix4x4 rotate = Matrix4x4.identity;
        rotate[1, 1] = Mathf.Cos(rad);
        rotate[1, 2] = Mathf.Sin(rad);
        rotate[2, 1] = -Mathf.Sin(rad);
        rotate[2, 2] = Mathf.Cos(rad);
        return rotate;
    }
    //Y axis
    public static Matrix4x4 RotateY(float angle)
    {
        //convert angle to rad
        float rad = angle * Mathf.Deg2Rad;
        Matrix4x4 rotate = Matrix4x4.identity;
        rotate[0, 0] = Mathf.Cos(rad);
        rotate[0, 2] = -Mathf.Sin(rad);
        rotate[2, 0] = Mathf.Sin(rad);
        rotate[2, 2] = Mathf.Cos(rad);
        return rotate;
    }

    //Z axis
    public static Matrix4x4 RotateZ(float angle)
    {
        //convert angle to rad
        float rad = angle * Mathf.Deg2Rad;
        Matrix4x4 rotate = Matrix4x4.identity; 
        rotate[0, 0] = Mathf.Cos(rad);
        rotate[0, 1] = Mathf.Sin(rad);
        rotate[1, 0] = -Mathf.Sin(rad);
        rotate[1, 1] = Mathf.Cos(rad);
        return rotate;
    }

}
