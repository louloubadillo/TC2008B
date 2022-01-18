//Script to create multiple instances of a prefab

using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class InstanceCar : MonoBehaviour
{
    public GameObject CarPrefab; //this is the prefab we will instantiate
    int numberOfPrefabs = 10; //this is the number of instances we will create
    // Start is called before the first frame update
    void Start()
    {
        for(int i = 0; i < numberOfPrefabs; i++)
        {
            Instantiate(CarPrefab, new Vector3(Random.Range(-20, 20), 0, Random.Range(-20, 20)), Quaternion.Euler(0,Random.Range(0, 360),0));
        }
    }

    // Update is called once per frame
    void Update()
    {
        /* Draw x,y,z axis in the scene view
        Debug.DrawLine(Vector3.zero, new Vector3(30,0,0),Color.red);
        Debug.DrawLine(Vector3.zero, new Vector3(0,30,0),Color.green);
        Debug.DrawLine(Vector3.zero, new Vector3(0,0,30),Color.blue); */

    }
}
