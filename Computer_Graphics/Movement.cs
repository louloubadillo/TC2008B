using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Movement : MonoBehaviour
{

    Vector3 tempPos;
    // Start is called before the first frame update
    void Start()
    {
        tempPos = transform.position;
    }

    // Update is called once per frame
    void Update()
    {
        
        tempPos.x += 0.5f;

        tempPos.z += 0.5f;

        transform.position = tempPos;

        if (tempPos.x > 20){
            enabled = false;
        }
    }
}

