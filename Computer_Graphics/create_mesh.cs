using System.Collections;
using System.Collections.Generic;
using UnityEngine;

//Script to create a mesh from a list of points and a list of triangles

[RequireComponent(typeof(MeshFilter))]
public class create_mesh : MonoBehaviour
{
    Mesh mesh; 
    Vector3[] vertices; 
    int[] triangles;

    // Start is called before the first frame update
    void Start()
    {
        mesh = new Mesh(); //Create a new mesh
        GetComponent<MeshFilter>().mesh = mesh; //Assign the mesh to the mesh filter
        Create(); 
        UpdateMesh(); 
    }

    void Create()
    {
        //Create a list of vertices and triangles
        vertices = new Vector3[]{
            new Vector3(0,0,0),
            new Vector3(0,0,1),
            new Vector3(1,0,0),
            new Vector3(1,0,1),
            new Vector3(0,1,0),
            new Vector3(0,1,1),
            new Vector3(1,1,0),
            new Vector3(1,1,1),

        };

        triangles = new int[] {
            //base
            0,1,2,
            1,3,2,
            //top
            4,5,6,
            5,7,6,
            //right
            1,5,3,
            5,7,3,
            //left
            0,4,2,
            4,6,2,
            //front 
            2,6,3,
            6,7,3, 
            //back
            0,4,1,
            4,5,1
            

            }; //clockwise order
    }

    void UpdateMesh()
    {
        mesh.Clear(); //Clear the mesh
        mesh.vertices = vertices; //Assign the vertices
        mesh.triangles = triangles; //Assign the triangles
    }
}
